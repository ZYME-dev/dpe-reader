"""
Script pour télécharger et indexer les cas tests
"""

import json
from collections import OrderedDict

import loguru
import xmltodict

import dpe.ademe as ademe

if __name__ == "__main__":

    # file = "_list_open3CL.txt"
    file = "_list.txt"
    
    DOWNLOAD = True
    PERSIST = True

    with open(f"./assets/samples/{file}") as f:
        ids = [line.rstrip() for line in f]

    index = OrderedDict()
    for id in ids:
        
        if DOWNLOAD:
            file_path = f"assets/samples/{id}.xml" if PERSIST else None
            xmlstring = ademe.download_xmlstring(id, file_path)
        else:
            file_path = f"assets/samples/{id}.xml"
            xmlstring = ademe.load_xmlstring(file_path)

        numero_dpe, statut, enum_version_id, xmltree = ademe.get_xmltree(xmlstring)

        root = xmltree.getroot()

        enum_modele_dpe_id = xmltree.xpath("administratif/date_etablissement_dpe")[
            0
        ].text

        date_visite_diagnostiqueur = xmltree.xpath(
            "administratif/date_visite_diagnostiqueur"
        )[0].text

        date_etablissement_dpe = xmltree.xpath("administratif/date_etablissement_dpe")[
            0
        ].text

        enum_methode_application_dpe_log_id = int(
            xmltree.xpath(
                "logement/caracteristique_generale/enum_methode_application_dpe_log_id"
            )[0].text
        )

        surface_habitable_logement = float(
            xmltree.xpath(
                "logement/caracteristique_generale/surface_habitable_logement"
            )[0].text
        )

        nombre_niveau_logement = int(
            xmltree.xpath("logement/caracteristique_generale/nombre_niveau_logement")[
                0
            ].text
        )

        date_format = "%Y-%m-%d"

        index[id] = {
            "numero_dpe": numero_dpe,
            "statut": statut,
            "enum_version_id": enum_version_id,
            "enum_modele_dpe_id": enum_modele_dpe_id,
            "date_visite_diagnostiqueur": date_visite_diagnostiqueur,
            "date_etablissement_dpe": date_etablissement_dpe,
            "enum_methode_application_dpe_log_id": enum_methode_application_dpe_log_id,
            "surface_habitable_logement": surface_habitable_logement,
            "nombre_niveau_logement": nombre_niveau_logement,
        }
        print(id)

    with open("./assets/samples/index.json", "w+") as f:
        json.dump(index, f, indent=4)
