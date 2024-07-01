"""
    Model de DPE écrit à la main
"""

from pydantic import BaseModel, Field
from typing import List, Tuple, Literal, Optional

class Mur(BaseModel):

    class DonneeEntree:
        description: Optional[str]
        reference: Optional[str]
        reference_lnc: Optional[str]
        tv_coef_reduction_deperdition_id: Optional[int]
        surface_aiu: Optional[float]
        surface_aue: Optional[float]
        enum_cfg_isolation_lnc_id: Optional[int]
        enum_type_adjacence_id: Optional[int]
        enum_orientation_id: Optional[int]
        surface_paroi_totale: Optional[float]
        surface_paroi_opaque: Optional[float]
        umur0_saisi: Optional[float]
        tv_umur0_id: Optional[int]
        epaisseur_structure: Optional[float]
        enum_materiaux_structure_mur_id: Optional[int]
        enum_methode_saisie_u0_id: Optional[int]
        enduit_isolant_paroi_ancienne: Optional[bool]
        umur_saisi: Optional[float]
        enum_type_doublage_id: Optional[int]
        enum_type_isolation_id: Optional[int]
        enum_periode_isolation_id: Optional[int]
        resistance_isolation: Optional[float]
        epaisseur_isolation: Optional[float]
        tv_umur_id: Optional[int]
        enum_methode_saisie_u_id: Optional[int]

    class DonneeIntermediaire:

        b: Optional[float]
        umur: Optional[float]
        umur0: Optional[float]


class PlancherBas(BaseModel):
    pass

class PlancherHaut(BaseModel):
    pass

class BaieVitree(BaseModel):
    pass

class Enveloppe(BaseModel):
    mur_collection:List[Mur]
    plancher_bas_collection:List[PlancherBas]
    plancher_haut_collection:List[PlancherHaut]
    baie_vitree_collection:List[BaieVitree]

class Logement(BaseModel):
    enveloppe:Enveloppe



