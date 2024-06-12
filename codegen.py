"""
    Génération auto d'un model de données à partir du xsd
"""

if __name__ == "__main__" :

    # Uncomment to work on models_pydantic version
    # from models_pydantic import Dpe
    # from xsdata_pydantic.bindings import XmlParser

    # Uncomment to work on models_dataclass version
    from models_dataclass import Dpe
    from xsdata.formats.dataclass.parsers import XmlParser

    parser = XmlParser()
    result = parser.parse("2344E0308327N.xml", Dpe)

    murs = result.logement.enveloppe.mur_collection.mur
    for mur in murs:
        print(mur.donnee_entree.surface_paroi_totale)



