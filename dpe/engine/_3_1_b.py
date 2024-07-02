"""
    3.1 Détermination du coefficient de réduction des déperditions b

    Données d’entrée :

        - Surface des parois séparant le local non chauffé des locaux chauffés : Aiu (m2)
        - Surface des parois séparant le local non chauffé de l’extérieur ou du sol : Aue (m2)
        - Type de local non chauffé (garage, comble, circulation…)
        - Etat d’isolation des parois du local non chauffé (isolées, non isolées)


    <mur>
    <donnee_entree>
        <description>Mur  1 Sud - Inconnu (à structure lourde) avec un doublage rapporté avec isolation intérieure (6 cm) donnant sur des circulations avec ouverture directe sur l&apos;extérieur</description>
        <reference>2023_01_31_12_13_08_05242480060202</reference>
        <reference_lnc>LNC2023_01_31_12_13_08_05242480060202</reference_lnc>
        <tv_coef_reduction_deperdition_id>100</tv_coef_reduction_deperdition_id>
        <surface_aiu>20</surface_aiu>
        <surface_aue>2.5</surface_aue>
        <enum_cfg_isolation_lnc_id>2</enum_cfg_isolation_lnc_id>
        <enum_type_adjacence_id>15</enum_type_adjacence_id>
        <enum_orientation_id>1</enum_orientation_id>
        <surface_paroi_totale>6.94</surface_paroi_totale>
        <surface_paroi_opaque>6.94</surface_paroi_opaque>
        <tv_umur0_id>1</tv_umur0_id>
        <enum_materiaux_structure_mur_id>1</enum_materiaux_structure_mur_id>
        <enum_methode_saisie_u0_id>2</enum_methode_saisie_u0_id>
        <paroi_ancienne>0</paroi_ancienne>
        <enum_type_doublage_id>3</enum_type_doublage_id>
        <enum_type_isolation_id>3</enum_type_isolation_id>
        <epaisseur_isolation>6</epaisseur_isolation>
        <enum_methode_saisie_u_id>3</enum_methode_saisie_u_id>
    </donnee_entree>
    <donnee_intermediaire>
        <b>0.15</b>
        <umur>0.5</umur>
        <umur0>2</umur0>
    </donnee_intermediaire>
    </mur>    

"""


