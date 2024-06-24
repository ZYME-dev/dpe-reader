import dpe.ademe as ademe

if __name__ == "__main__":


    # dpe_id = '2344E0308327N' # v2.2
    dpe_id = '2369E3640698P' # v2.3  

    xmlstring = ademe.download_xmlstring(dpe_id)
    numero_dpe, statut, enum_version_id, xmltree = ademe.get_xmltree(xmlstring)
    
    model = ademe.load_model(xmltree, enum_version_id)

    for child in xmltree.getroot():
            print(child)

    print(f"N°      : {numero_dpe}")
    print(f"Version : {enum_version_id}")
    print(f"Statut  : {statut}")

    murs = model.logement.enveloppe.mur_collection.mur
    for mur in murs:
        print(mur.donnee_entree.surface_paroi_totale)