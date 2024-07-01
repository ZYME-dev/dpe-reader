import streamlit as st
import requests
import _models as mg
from collections import OrderedDict 
import json
import dpe.ademe as ademe
import pandas as pd
from datetime import datetime
import dpe.models as models
import typing

date_format = "%Y-%m-%d"

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

@st.experimental_dialog("Importer un DPE")
def load_sample():
    st.caption("Importer un DPE à partir d'un numéro ADEME ou sélectionner un DPE dans la liste de cas tests.")

    samples = get_samples()
    event = st.dataframe(
            samples,
            use_container_width=True,
            hide_index=True,
            on_select="rerun",
            selection_mode="single-row",
        )
    if st.button("valider"):
        if len(event.selection.rows) > 0:
            index = event.selection.rows[0]
            dpe_id = samples.iat[index,0]
            st.session_state["dpe_id"] = dpe_id
        else:
            st.session_state["dpe_id"] = None
        st.rerun()

with st.sidebar:
    if "dpe_id" not in st.session_state:
        st.session_state["dpe_id"] = "2369E3640698P"

    st.header("Importer un DPE")
    st.caption("Pour obtenir les informations d'un DPE, saisissez son numéro d'identification ou bien sélectionnez un cas test dans la liste.")

    if st.button("Choisir un cas test"):
        load_sample()
    st.text_input("Numéro ADEME :", value=st.session_state["dpe_id"])
    button_load = st.button("Importer")
    
    st.divider()
    
    if button_load:
        xmlstring = ademe.download_xmlstring(st.session_state.dpe_id)
        numero_dpe, statut, enum_version_id, xmltree = ademe.get_xmltree(xmlstring)
        model = ademe.load_model(xmltree, enum_version_id)
        st.text_input("N°", value=numero_dpe, disabled=True)
        st.text_input("Statut", value=statut, disabled=True)
        st.text_input("Version", value=model.administratif.enum_version_id.value, disabled=True)
        st.text_input("Methode", value=model.logement.caracteristique_generale.enum_methode_application_dpe_log_id, disabled=True)
        st.date_input("Date DPE", value=model.administratif.date_etablissement_dpe.to_date(), format="DD/MM/YYYY", disabled=True)
        st.date_input("Date Visite", value=model.administratif.date_visite_diagnostiqueur.to_date(), format="DD/MM/YYYY", disabled=True)
        st.divider()
        st.text_input("SHAB (m2)", value=model.logement.caracteristique_generale.surface_habitable_logement, disabled=True)
        st.text_input("Niveaux", value=model.logement.caracteristique_generale.nombre_niveau_logement, disabled=True)


if model != None:
    for mur in model.logement.enveloppe.mur_collection.mur:
        st.write(mur)  

st.title("DPE")

st.header("Choisir un DPE")

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
    

