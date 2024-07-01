from enum import Enum

class Version(Enum):
    """_summary_

    Args:
        Enum (_type_): _description_
    """
    v_1     = ("1", "version du 1er juillet 2021"),
    v_1_1   = ("1.1", "version corrective du 1er novembre"),
    v_2     = "2", "version avec modèle complet sans contrôle de cohérence",
    
    # "1" = "version du 1er juillet 2021",
    # "1.1": "version corrective du 1er novembre",
    # "2": "version avec modèle complet sans contrôle de cohérence",
    # "2.1": "version de fin de validation incluant les contrôles de cohérences",
    # "2.2": "version de préparation de compatibilité audit/dpe",
    # "2.3": "version corrective de janvier 2023",
    # "2.4": "version correspondant à l'arrêté des seuils pour les petites surfaces"

Version.v_1