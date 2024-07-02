from typing import List, Tuple, Callable
from enums import Enum
from dataclasses import dataclass

@dataclass(order=True)
class Mur:

    description:str
    reference:str
    reference_lnc:str
    tv_coef_reduction_deperdition_id:int

    surface_aiu:float
    surface_aue:float
    enum_cfg_isolation_lnc_id:int
    enum_type_adjacence_id:int
    enum_orientation_id:int
    surface_paroi_totale:float
    surface_paroi_opaque:float
    umur0_saisi:float
    tv_umur0_id:int

    epaisseur_structure:float
    enum_materiaux_structure_mur_id:int
    enum_methode_saisie_u0_id:int
    paroi_ancienne:BlockingIOError
    enduit_isolant_paroi_ancienne:bool
    umur_saisi:float
    enum_type_isolation_id:int
    enum_type_doublage_id:int
    enum_periode_isolation_id:int
    resistance_isolation:float
    epaisseur_isolation:float
    tv_umur_id:int

    enum_methode_saisie_u_id:int
    b:float
    umur:float
    umur0:float


    def calc_U(self):
        pass

m = Mur()
m.calc_U()