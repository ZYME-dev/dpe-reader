import streamlit as st
import requests
import _models as mg
from collections import OrderedDict 
import json
import dpe.ademe as ademe
import pandas as pd
from datetime import datetime

@st.cache_data
def get_samples():

    with open('assets/samples/_index.json', 'r') as f:
        data = json.loads(f.read())

        date_format = "%Y-%m-%d"
        rows = []
        for id, info in data.items():
            rows.append([
                info["numero_dpe"],
                info["statut"],
                info["enum_version_id"],
                datetime.strptime(info["date_visite_diagnostiqueur"], date_format).date(),   
                datetime.strptime(info["date_etablissement_dpe"], date_format).date(),
                info["surface_habitable_logement"]])
        df = pd.DataFrame(rows, columns=["Id","Statut", "Version", "Date Visite", "Date DPE", "SHAB"])
        return df
    
st.title("DPE")

st.caption("pour obtenir les informations d'un DPE, saisissez son numéro d'identification")

st.header("Choisir un DPE")

dpe_id = '2369E3640698P' # v2.3
dpe_id = st.text_input("Numéro de DPE", value=dpe_id)


samples = get_samples()
event = st.dataframe(
        samples,
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row",
    )

if len(event.selection.rows) > 0:
    index = event.selection.rows[0]
    dpe_id = samples.iat[index,0]
else:
    index = None
    dpe_id = None

st.write("Numéro de DPE : ", dpe_id)


b = st.button("Obtenir")

if b:

    xmlstring = ademe.download_xmlstring(dpe_id)
    numero_dpe, statut, enum_version_id, xmltree = ademe.get_xmltree(xmlstring)
    model = ademe.load_model(xmltree, enum_version_id)

    st.text_input("Version", value=enum_version_id)
    st.text_input("Statut", value=statut)

    st.subheader("Murs")
    murs = model.logement.enveloppe.mur_collection.mur
    st.write(murs)
    # for mur in murs:
    #     print(mur.donnee_entree.surface_paroi_totale)

    st.subheader("Plancher Bas")
    pb = model.logement.enveloppe.plancher_bas_collection.plancher_bas
    st.write(pb)
    

