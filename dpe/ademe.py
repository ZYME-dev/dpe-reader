from urllib.request import urlopen
import pyrfc6266
from settings import DPE_VERSION
from lxml import etree
import xml.dom.minidom


def download_xmlstring(dpe_id: str, file_path: str = None) -> str:
    """Télécharge le xml d'un DPE à partir de son ID depuis la plateforme
    observatoire-dpe-audit.ademe.fr
    """

    # https://stackoverflow.com/questions/2795331/python-download-without-supplying-a-filename

    url = f"https://observatoire-dpe-audit.ademe.fr/pub/dpe/{dpe_id}/xml"

    data = urlopen(url)
    # info = data.info()
    # filename = pyrfc6266.parse_filename(info["Content-Disposition"])
    xmlstring = data.read()

    if file_path is not None:
        with open(file_path, "w+") as f:
            dom = xml.dom.minidom.parseString(xmlstring)
            f.write(dom.toprettyxml(indent=' '*2))

    return xmlstring


def open_xmlstring(file_path:str=None) -> str:

    with open(file_path, 'rb') as f:
        return f.read()


def load_xmlstring(file_path: str = None) -> str:
    with open(file_path, "wb+") as f:
        xmlstring = f.read()
    return xmlstring


def get_xmltree(xmlstring: str):
    """Obtient les identifiants du DPE et le numéro de version et retourne
    le xml sous forme de xmltree (lxml).

    Le numéro de version est nécessaire pour savoir quelle schéma/modèle
    utiliser.

    Un cleaning est pratiqué pour enlever :
        - les nodes 'status' et 'numero_dpe' qui ne sont pas conforme au model
        - les nodes 'data_complementaires' qui provoquent une erreur lors du parse
    """

    xmltree = etree.ElementTree(etree.fromstring(xmlstring))
    numero_dpe = xmltree.xpath("numero_dpe")[0]
    statut = xmltree.xpath("statut")[0]
    enum_version_id = xmltree.xpath("administratif/enum_version_id")[0]

    return (numero_dpe.text, statut.text, enum_version_id.text, xmltree)


def load_model(xmltree, enum_version_id):
    """Sérialize le xml dans un modèle python (dataclass).
    Principe du dispatch selon la méthode utilisée.
    """

    from xsdata.formats.dataclass.parsers import XmlParser
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
                Seuls les versions suivantes sont prise en charge : {','.join(DPE_VERSION)}"
        )

    # do some cleaning ...
    # sinon erreur lors de la déserialization xml > dataclass

    root = xmltree.getroot()

    numero_dpe = xmltree.xpath("numero_dpe")[0]
    root.remove(numero_dpe)

    statut = xmltree.xpath("statut")[0]
    root.remove(statut)

    for c in xmltree.xpath("//data_complementaires"):
        c.getparent().remove(c)

    # parse xmltree to model
    parser = XmlParser()
    model = parser.parse(xmltree, Dpe)

    return model
