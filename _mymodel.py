import dpe.ademe as ademe
import dpe.models.dpe
from lxml import etree
import xmltodict

id = "2307E3075089A"
file_path = f"assets/samples/{id}.xml"
# xmlstring = ademe.download_xmlstring(id, None)
xmlstring = ademe.open_xmlstring(file_path)
numero_dpe, statut, enum_version_id, xmltree = ademe.get_xmltree(xmlstring)

    # xmltree = etree.ElementTree(etree.fromstring(xmlstring))
    # root = xmltree.getroot()
    # numero_dpe = xmltree.xpath('numero_dpe')[0]
    # statut = xmltree.xpath('statut')[0]
    # enum_version_id = xmltree.xpath('administratif/enum_version_id')[0]


print(numero_dpe)


    
