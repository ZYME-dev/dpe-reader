import streamlit as st
import requests
import model_generator as mg
from streamlit_datalist import stDatalist
from collections import OrderedDict 
import yaml
import modules.ademe as ademe

def get_samples():

    with open('assets/samples/_index.yaml', 'r') as f:
        samples = yaml.load(f, Loader=yaml.SafeLoader)
    st.write(samples)
    return samples
    

st.title("DPE")

st.caption("pour obtenir les informations d'un DPE, saisissez son numéro d'identification")

dpe_ids = '2369E3640698P' # v2.3
dpe_id = '2344E0308327N' # v2.2
dpe_id = st.text_input("Numéro de DPE", value=dpe_id)
get_samples()

selection = stDatalist("This datalist is...", ["great", "cool", "neat"])
st.write(selection)

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
    

