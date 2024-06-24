import sys
for p in sys.path:
    print(p)

from urllib.request import urlopen
import pyrfc6266
import requests
from streamlit_datalist import stDatalist
from collections import OrderedDict 
import yaml
import models
from settings import DPE_VERSION

def download_xmlstring(dpe_id:str, file_path:str=None) -> str:
    """Télécharge le xml d'un DPE à partir de son ID depuis la plateforme 
    observatoire-dpe-audit.ademe.fr
    """

    # https://stackoverflow.com/questions/2795331/python-download-without-supplying-a-filename

    url = f"https://observatoire-dpe-audit.ademe.fr/pub/dpe/{dpe_id}/xml"
    headers = {
        'Accept': 'text/xml',
    }
    
    data = urlopen(url)
    info = data.info()
    filename = pyrfc6266.parse_filename(info['Content-Disposition'])
    xmlstring = data.read()

    if file_path != None:
        with open(file_path) as f:
            f.write(xmlstring)

    return xmlstring


def get_xmltree(xmlstring:str):
    """Obtient les identifiants du DPE et le numéro de version et retourne 
    le xml sous forme de xmltree (lxml).

    Le numéro de version est nécessaire pour savoir quelle schéma/modèle 
    utiliser.

    Un cleaning est pratiqué pour enlever :
        - les nodes 'status' et 'numero_dpe' qui ne sont pas conforme au model
        - les nodes 'data_complementaires' qui provoquent une erreur lors du parse
    """

    from lxml import etree

    xmltree = etree.ElementTree(etree.fromstring(xmlstring))
    root = xmltree.getroot()
    numero_dpe = xmltree.xpath('numero_dpe')[0]
    statut = xmltree.xpath('statut')[0]
    enum_version_id = xmltree.xpath('administratif/enum_version_id')[0]
    
    return (numero_dpe.text, statut.text, enum_version_id.text, xmltree)


def load_model(xmltree, enum_version_id):
    """Sérialize le xml dans un modèle python (dataclass). 
    Principe du dispatch selon la méthode utilisée.
    """
    
    from xsdata.formats.dataclass.parsers import XmlParser 
    import models.dpe_v2
    import models.dpe_v2
    import models.dpe_v2_2
    import models.dpe_v2_3
    import models.dpe_v2_4
    
    if enum_version_id == "2":
        Dpe = models.dpe_v2.Dpe
    elif enum_version_id == "2.2":
        Dpe = models.dpe_v2_2.Dpe
    elif enum_version_id == "2.3":
        Dpe = models.dpe_v2_3.Dpe
    elif enum_version_id == "2.4":
        Dpe = models.dpe_v2_4.Dpe
    else:
        raise Exception(
            f"La version {enum_version_id} du DPE n'est pas prise en charge. \
                Seuls les versions suivantes sont prise en charge : {','.join(DPE_VERSION)}")
    
    # do some cleaning ...
    # sinon erreur lors de la déserialization xml > dataclass

    root = xmltree.getroot()

    numero_dpe = xmltree.xpath('numero_dpe')[0]
    root.remove(numero_dpe)

    statut = xmltree.xpath('statut')[0]
    root.remove(statut)

    for c in xmltree.xpath('//data_complementaires'): 
        c.getparent().remove(c)
    
    # parse xmltree to model
    parser = XmlParser()
    file_path = f"assets/{dpe_id}.xml"
    model = parser.parse(xmltree, Dpe)

    return model


if __name__ == "__main__":

    for p in sys.path:
        print(p)

    # dpe_id = '2344E0308327N' # v2.2
    dpe_id = '2369E3640698P' # v2.3  

    xmlstring = download_xmlstring(dpe_id)
    numero_dpe, statut, enum_version_id, xmltree = get_xmltree(xmlstring)
    
    model = load_model(xmltree, enum_version_id)

    for child in xmltree.getroot():
            print(child)

    print(f"N°      : {numero_dpe}")
    print(f"Version : {enum_version_id}")
    print(f"Statut  : {statut}")

    murs = model.logement.enveloppe.mur_collection.mur
    for mur in murs:
        print(mur.donnee_entree.surface_paroi_totale)


