from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDate


class AdministratifEnumVersionId(Enum):
    VALUE_1 = "1"
    VALUE_1_1 = "1.1"
    VALUE_2 = "2"
    VALUE_2_1 = "2.1"
    VALUE_2_2 = "2.2"


class CaracteristiqueGeneraleEnumUsageFonctionnelBatimentId(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_31 = 31
    VALUE_32 = 32


class DonneeEntreeEnumMethodeSaisieCaracSysId(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8


class DonneeEntreeEnumTypeGenerateurChId(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33
    VALUE_34 = 34
    VALUE_35 = 35
    VALUE_36 = 36
    VALUE_37 = 37
    VALUE_38 = 38
    VALUE_39 = 39
    VALUE_40 = 40
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_55 = 55
    VALUE_56 = 56
    VALUE_57 = 57
    VALUE_58 = 58
    VALUE_59 = 59
    VALUE_60 = 60
    VALUE_61 = 61
    VALUE_62 = 62
    VALUE_63 = 63
    VALUE_64 = 64
    VALUE_65 = 65
    VALUE_66 = 66
    VALUE_67 = 67
    VALUE_68 = 68
    VALUE_69 = 69
    VALUE_70 = 70
    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_73 = 73
    VALUE_74 = 74
    VALUE_75 = 75
    VALUE_76 = 76
    VALUE_77 = 77
    VALUE_78 = 78
    VALUE_79 = 79
    VALUE_80 = 80
    VALUE_81 = 81
    VALUE_82 = 82
    VALUE_83 = 83
    VALUE_84 = 84
    VALUE_85 = 85
    VALUE_86 = 86
    VALUE_87 = 87
    VALUE_88 = 88
    VALUE_89 = 89
    VALUE_90 = 90
    VALUE_91 = 91
    VALUE_92 = 92
    VALUE_93 = 93
    VALUE_94 = 94
    VALUE_95 = 95
    VALUE_96 = 96
    VALUE_97 = 97
    VALUE_98 = 98
    VALUE_99 = 99
    VALUE_100 = 100
    VALUE_101 = 101
    VALUE_102 = 102
    VALUE_103 = 103
    VALUE_104 = 104
    VALUE_105 = 105
    VALUE_106 = 106
    VALUE_107 = 107
    VALUE_108 = 108
    VALUE_109 = 109
    VALUE_110 = 110
    VALUE_111 = 111
    VALUE_112 = 112
    VALUE_113 = 113
    VALUE_114 = 114
    VALUE_115 = 115
    VALUE_116 = 116
    VALUE_117 = 117
    VALUE_118 = 118
    VALUE_119 = 119
    VALUE_120 = 120
    VALUE_121 = 121
    VALUE_122 = 122
    VALUE_123 = 123
    VALUE_124 = 124
    VALUE_125 = 125
    VALUE_126 = 126
    VALUE_127 = 127
    VALUE_128 = 128
    VALUE_129 = 129
    VALUE_130 = 130
    VALUE_131 = 131
    VALUE_132 = 132
    VALUE_133 = 133
    VALUE_134 = 134
    VALUE_135 = 135
    VALUE_136 = 136
    VALUE_137 = 137
    VALUE_138 = 138
    VALUE_139 = 139
    VALUE_140 = 140
    VALUE_141 = 141
    VALUE_142 = 142
    VALUE_145 = 145
    VALUE_146 = 146
    VALUE_147 = 147
    VALUE_148 = 148
    VALUE_149 = 149
    VALUE_150 = 150
    VALUE_151 = 151
    VALUE_152 = 152
    VALUE_153 = 153
    VALUE_154 = 154
    VALUE_155 = 155
    VALUE_156 = 156
    VALUE_157 = 157
    VALUE_158 = 158
    VALUE_159 = 159
    VALUE_160 = 160
    VALUE_161 = 161
    VALUE_162 = 162
    VALUE_163 = 163
    VALUE_164 = 164
    VALUE_165 = 165
    VALUE_166 = 166
    VALUE_167 = 167
    VALUE_168 = 168
    VALUE_169 = 169
    VALUE_170 = 170
    VALUE_171 = 171


class SOuiNon(Enum):
    """
    oui/non.
    """

    VALUE_0 = 0
    VALUE_1 = 1


class SQualite(Enum):
    """
    qualité.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class TAdresseBanType(Enum):
    HOUSENUMBER = "housenumber"
    STREET = "street"
    MUNICIPALITY = "municipality"
    LOCALITY = "locality"


@dataclass
class TAdresse:
    """
    Attributes:
        adresse_brut: champs texte brute de l'adresse saisi par le
            diagnostiqueur
        code_postal_brut: code postal de l'adresse brute saisie par le
            diagnostiqueur
        nom_commune_brut: nom de commune brute saisie par le
            diagnostiqueur
        label_brut: label complet de l'adresse saisie par le
            diagnostiqueur (adresse + code postal + nom commune)
        enum_statut_geocodage_ban_id: statut de l'appareillement à la
            BAN de l'adresse
        ban_date_appel: date d'appel à la ban
        ban_id: identifiant de la BAN referençant l'adresse
        ban_label: label de l'adresse au format ban
        ban_housenumber: Numéro éventuel de l’adresse dans la voie
            (champ BAN)
        ban_street: Nom de la voie en minuscules accentuées avec les
            noms alternatifs éventuels (champ BAN)
        ban_citycode: code insee de la commune de l'adresse géocodée ban
        ban_postcode: code postal de la commune de l'adresse géocodée
            ban
        ban_city: nom de la commune de l'adresse géocodée ban
        ban_type: type de résultat ban :
            housenumber/street/locality/municipality
        ban_score: score de match entre le label brut et le résultat de
            géocodage de la BAN
        ban_x: coordonnée x du géolocalisant ban dans le referentiel
            epsg 2154 lambert 93
        ban_y: coordonnée y du géolocalisant ban dans le referentiel
            epsg 2154 lambert 93
        compl_nom_residence: complement d'adresses : nom de la residence
        compl_ref_batiment: complement d'adresse : référence du bâtiment
            ( ex. A,B ,1,2,3,4)
        compl_etage_appartement: complement d'adresses : etage du
            logement (cas de l'appartement) sous format entier 0 =RDC
        compl_ref_cage_escalier: complement d'adresses : reference de
            cage d'escalire&gt;
        compl_ref_logement: complement d'adresses : reference du
            logement dans le bâtiment (appartement ex. 10, A13, 3eme
            gauche)
    """

    class Meta:
        name = "t_adresse"

    adresse_brut: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    code_postal_brut: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{1}[A-Za-z0-9]{1}[0-9]{3}",
        },
    )
    nom_commune_brut: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    label_brut: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 255,
        },
    )
    enum_statut_geocodage_ban_id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
        },
    )
    ban_date_appel: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": XmlDate(2021, 1, 1),
        },
    )
    ban_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )
    ban_label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )
    ban_housenumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )
    ban_street: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )
    ban_citycode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )
    ban_postcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )
    ban_city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )
    ban_type: Optional[TAdresseBanType] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    ban_score: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
            "nillable": True,
        },
    )
    ban_x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": 0.0,
            "nillable": True,
        },
    )
    ban_y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": 0.0,
            "nillable": True,
        },
    )
    compl_nom_residence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )
    compl_ref_batiment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )
    compl_etage_appartement: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    compl_ref_cage_escalier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )
    compl_ref_logement: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )


@dataclass
class Administratif:
    """
    Attributes:
        dpe_a_remplacer: numéro du DPE à remplacer dans le cas d'une
            opération de remplacement du DPE
        motif_remplacement: motif du remplacement du DPE : texte libre
        dpe_immeuble_associe: numéro du DPE immeuble associé au DPE
            logement utilisant la méthode de génération des DPE à
            l'appartement à partir du DPE immeuble
        enum_version_id: version du DPE. Cenuméro de version permet de
            tracer les évolutions de modèle de données, de contexte
            réglementaire et de contrôle mis en place sur les DPE.
            Chaque nouvelle version induit un certain nombre de
            changements substantiels. Certaines données ne sont
            disponible ou obligatoires qu'à partir d'une certaine
            version
        date_visite_diagnostiqueur: date de visite du diagnostiqueur
        nom_proprietaire: denomination ou raison sociale du propriétaire
        siren_proprietaire: siren du propriétaire lorsque celui-ci est
            une personne morale.
        nom_proprietaire_installation_commune: dénomination ou raison
            sociale du propriétaire des installations communes
        date_etablissement_dpe: date de l'établissement du dpe
        enum_modele_dpe_id: modèle de dpe (3CL logement / tertiaire ou
            neuf)
        diagnostiqueur:
        geolocalisation:
    """

    class Meta:
        name = "administratif"

    dpe_a_remplacer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[2-3][0-9]{2}[0-9A-B][ETN][0-9]{7}[A-Z]",
            "nillable": True,
        },
    )
    motif_remplacement: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    dpe_immeuble_associe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "pattern": r"[2-3][0-9]{2}[0-9A-B][ETN][0-9]{7}[A-Z]",
            "nillable": True,
        },
    )
    enum_version_id: Optional[AdministratifEnumVersionId] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    date_visite_diagnostiqueur: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": XmlDate(2021, 7, 1),
        },
    )
    nom_proprietaire: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 255,
        },
    )
    siren_proprietaire: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "length": 9,
            "pattern": r"[0-9]{9}",
            "nillable": True,
        },
    )
    nom_proprietaire_installation_commune: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 255,
            "nillable": True,
        },
    )
    date_etablissement_dpe: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": XmlDate(2021, 7, 1),
        },
    )
    enum_modele_dpe_id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 4,
        },
    )
    diagnostiqueur: Optional["Administratif.Diagnostiqueur"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    geolocalisation: Optional["Administratif.Geolocalisation"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Diagnostiqueur:
        """
        Attributes:
            usr_logiciel_id: identifiant de logiciel dpe unique
            version_logiciel: version du logiciel utilisé
            version_moteur_calcul: version du moteur de calcul utilisé
                par le logiciel
            nom_diagnostiqueur: nom du diagnostiqueur
            prenom_diagnostiqueur: prénom du diagnostiqueur
            mail_diagnostiqueur: mail du diagnostiqueur
            telephone_diagnostiqueur: numéro de téléphone du
                diagnostiqueur
            adresse_diagnostiqueur: adresse postale du diagnostiqueur
            entreprise_diagnostiqueur: entreprise du diagnostiqueur
            numero_certification_diagnostiqueur: numero de certification
                du diagnostiqueur
            organisme_certificateur: nom de l'organisme certificateur
        """

        usr_logiciel_id: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_exclusive": 0,
            },
        )
        version_logiciel: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 255,
            },
        )
        version_moteur_calcul: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "max_length": 32,
                "nillable": True,
            },
        )
        nom_diagnostiqueur: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 255,
            },
        )
        prenom_diagnostiqueur: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 255,
            },
        )
        mail_diagnostiqueur: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 255,
            },
        )
        telephone_diagnostiqueur: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 255,
            },
        )
        adresse_diagnostiqueur: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 255,
            },
        )
        entreprise_diagnostiqueur: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 255,
            },
        )
        numero_certification_diagnostiqueur: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 255,
            },
        )
        organisme_certificateur: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 255,
            },
        )

    @dataclass
    class Geolocalisation:
        """
        Attributes:
            invar_logement: invariant fiscal du logement (10 caractères)
            rpls_log_id: identifiant Repertoire Logement Social (RPLS)
                du logement (dans le cas d'un propriétaire bailleur
                social)
            rpls_org_id: identifiant Repertoire Logement Social (RPLS)
                de l'organisation de bailleur social propriétaire du
                logement (dans le cas d'un propriétaire bailleur social)
            idpar: identifiant de parcelle cadastrale (14 caractères)
            immatriculation_copropriete: numéro d'immatriculation de la
                copropriété au registre des copropriétés (9 caractères
                XX0000000)
            adresses: Adresses bien, propriétaire, installations
        """

        invar_logement: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
        rpls_log_id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "length": 8,
                "pattern": r"[0-9]{8}",
                "nillable": True,
            },
        )
        rpls_org_id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "length": 5,
                "pattern": r"[0-9]{5}",
                "nillable": True,
            },
        )
        idpar: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
        immatriculation_copropriete: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "length": 9,
                "pattern": r"[A-Z][A-Z][0-9]{7}",
                "nillable": True,
            },
        )
        adresses: Optional["Administratif.Geolocalisation.Adresses"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

        @dataclass
        class Adresses:
            adresse_bien: Optional[TAdresse] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            adresse_proprietaire: Optional[TAdresse] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            adresse_proprietaire_installation_commune: Optional[TAdresse] = (
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
            )


@dataclass
class Dpe:
    """Version V7.1.0 - 2022-09-28 : version compatible audit énergétique

    Attributes:
        administratif:
        logement: Modele 3cl logement
        tertiaire: Tertiaire
        logement_neuf: Logement neuf
        dpe_immeuble:
        descriptif_enr_collection:
        descriptif_simplifie_collection:
        fiche_technique_collection:
        justificatif_collection:
        descriptif_geste_entretien_collection:
        descriptif_travaux:
        hashkey: clé de hachage
        id: id
        version: Version schéma
    """

    class Meta:
        name = "dpe"

    administratif: Optional[Administratif] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    logement: Optional["Dpe.Logement"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tertiaire: Optional["Dpe.Tertiaire"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    logement_neuf: Optional["Dpe.LogementNeuf"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    dpe_immeuble: Optional["Dpe.DpeImmeuble"] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    descriptif_enr_collection: Optional["Dpe.DescriptifEnrCollection"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    descriptif_simplifie_collection: Optional[
        "Dpe.DescriptifSimplifieCollection"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    fiche_technique_collection: Optional["Dpe.FicheTechniqueCollection"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
    )
    justificatif_collection: Optional["Dpe.JustificatifCollection"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    descriptif_geste_entretien_collection: Optional[
        "Dpe.DescriptifGesteEntretienCollection"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    descriptif_travaux: Optional["Dpe.DescriptifTravaux"] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    hashkey: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class DpeImmeuble:
        logement_visite_collection: Optional[
            "Dpe.DpeImmeuble.LogementVisiteCollection"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

        @dataclass
        class LogementVisiteCollection:
            logement_visite: List[
                "Dpe.DpeImmeuble.LogementVisiteCollection.LogementVisite"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass
            class LogementVisite:
                """
                Attributes:
                    description: description du logement visité
                    enum_position_etage_logement_id: position du
                        logement dans l'immeuble en terme d'étage
                    enum_typologie_logement_id: typologie de logement
                        (T1… T6)
                """

                description: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                enum_position_etage_logement_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 3,
                    },
                )
                enum_typologie_logement_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 7,
                    },
                )

    @dataclass
    class DescriptifEnrCollection:
        descriptif_enr: List["Dpe.DescriptifEnrCollection.DescriptifEnr"] = (
            field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
        )

        @dataclass
        class DescriptifEnr:
            """
            Attributes:
                description: description du système d'ENR
                enum_categorie_enr_descriptif_id: catégorie de système
                    ENR
            """

            description: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            enum_categorie_enr_descriptif_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 9,
                },
            )

    @dataclass
    class DescriptifSimplifieCollection:
        descriptif_simplifie: List[
            "Dpe.DescriptifSimplifieCollection.DescriptifSimplifie"
        ] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass
        class DescriptifSimplifie:
            """
            Attributes:
                description: description du composant
                enum_categorie_descriptif_simplifie_id: catégorie de
                    composant
            """

            description: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            enum_categorie_descriptif_simplifie_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 9,
                },
            )

    @dataclass
    class FicheTechniqueCollection:
        fiche_technique: List[
            "Dpe.FicheTechniqueCollection.FicheTechnique"
        ] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )

        @dataclass
        class FicheTechnique:
            """
            Attributes:
                enum_categorie_fiche_technique_id: catégorie de
                    composant
                sous_fiche_technique_collection:
            """

            enum_categorie_fiche_technique_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 12,
                },
            )
            sous_fiche_technique_collection: Optional[
                "Dpe.FicheTechniqueCollection.FicheTechnique.SousFicheTechniqueCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )

            @dataclass
            class SousFicheTechniqueCollection:
                sous_fiche_technique: List[
                    "Dpe.FicheTechniqueCollection.FicheTechnique.SousFicheTechniqueCollection.SousFicheTechnique"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                    },
                )

                @dataclass
                class SousFicheTechnique:
                    """
                    Attributes:
                        description: description de la sous catégorie
                        valeur: valeur de la sous catégorie
                        detail_origine_donnee: description détail de
                            l'origne de la donnée ( type de
                            document,type de mesure etc..)
                        enum_origine_donnee_id: origine de la donnée
                    """

                    description: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    valeur: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    detail_origine_donnee: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )
                    enum_origine_donnee_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 6,
                        },
                    )

    @dataclass
    class JustificatifCollection:
        justificatif: List["Dpe.JustificatifCollection.Justificatif"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )

        @dataclass
        class Justificatif:
            """
            Attributes:
                description: description du justificatif adjoint au DPE
                enum_type_justificatif_id: type de justificatif
            """

            description: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            enum_type_justificatif_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 20,
                },
            )

    @dataclass
    class DescriptifGesteEntretienCollection:
        descriptif_geste_entretien: List[
            "Dpe.DescriptifGesteEntretienCollection.DescriptifGesteEntretien"
        ] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )

        @dataclass
        class DescriptifGesteEntretien:
            """
            Attributes:
                description: description du geste d'entretien
                enum_picto_geste_entretien_id: catégorie de composant
                    concerné
                categorie_geste_entretien: catégorie de composant
                    concerné
            """

            description: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            enum_picto_geste_entretien_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 17,
                },
            )
            categorie_geste_entretien: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "max_length": 255,
                },
            )

    @dataclass
    class DescriptifTravaux:
        """
        Attributes:
            pack_travaux_collection:
            commentaire_travaux: commentaires généraux sur les travaux à
                réaliser
        """

        pack_travaux_collection: Optional[
            "Dpe.DescriptifTravaux.PackTravauxCollection"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        commentaire_travaux: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

        @dataclass
        class PackTravauxCollection:
            pack_travaux: List[
                "Dpe.DescriptifTravaux.PackTravauxCollection.PackTravaux"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

            @dataclass
            class PackTravaux:
                """
                Attributes:
                    enum_num_pack_travaux_id: numéro du pack travaux
                        (1,2,1+2)
                    conso_5_usages_apres_travaux: consommation 5 usages
                        après travaux en energie primaire (kWhEP/m²/an)
                    emission_ges_5_usages_apres_travaux: emissions C02 5
                        usages après travaux (kgCO2/m²/an)
                    cout_pack_travaux_min: fourchette basse de
                        l'estimation des coûts du pack travaux(€)
                    cout_pack_travaux_max: fourchette haute de
                        l'estimation des coûts du pack travaux(€)
                    travaux_collection:
                """

                enum_num_pack_travaux_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 3,
                    },
                )
                conso_5_usages_apres_travaux: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_exclusive": 0.0,
                        "nillable": True,
                    },
                )
                emission_ges_5_usages_apres_travaux: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                cout_pack_travaux_min: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_exclusive": 0.0,
                        "nillable": True,
                    },
                )
                cout_pack_travaux_max: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_exclusive": 0.0,
                        "nillable": True,
                    },
                )
                travaux_collection: Optional[
                    "Dpe.DescriptifTravaux.PackTravauxCollection.PackTravaux.TravauxCollection"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )

                @dataclass
                class TravauxCollection:
                    travaux: List[
                        "Dpe.DescriptifTravaux.PackTravauxCollection.PackTravaux.TravauxCollection.Travaux"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                    @dataclass
                    class Travaux:
                        """
                        Attributes:
                            description_travaux: description textuelle
                                des travaux envisagés sur le lot
                            enum_lot_travaux_id: lot concerné par les
                                travaux
                            avertissement_travaux: avertissement
                                concernant les travaux à réaliser
                            performance_recommande: performance
                                recommandé des composants rénovés
                        """

                        description_travaux: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )
                        enum_lot_travaux_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 9,
                            },
                        )
                        avertissement_travaux: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        performance_recommande: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "max_length": 255,
                            },
                        )

    @dataclass
    class Logement:
        caracteristique_generale: Optional[
            "Dpe.Logement.CaracteristiqueGenerale"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        meteo: Optional["Dpe.Logement.Meteo"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        enveloppe: Optional["Dpe.Logement.Enveloppe"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        ventilation_collection: Optional[
            "Dpe.Logement.VentilationCollection"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        climatisation_collection: Optional[
            "Dpe.Logement.ClimatisationCollection"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        production_elec_enr: Optional["Dpe.Logement.ProductionElecEnr"] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
        )
        installation_ecs_collection: Optional[
            "Dpe.Logement.InstallationEcsCollection"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        installation_chauffage_collection: Optional[
            "Dpe.Logement.InstallationChauffageCollection"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        sortie: Optional["Dpe.Logement.Sortie"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

        @dataclass
        class CaracteristiqueGenerale:
            """
            Attributes:
                annee_construction: annee de construction
                enum_periode_construction_id: période de construction
                enum_methode_application_dpe_log_id: méthode
                    d'application du DPE logement
                surface_habitable_logement: surface habitable du
                    logement renseignée sauf dans le cas du dpe à
                    l'immeuble
                nombre_niveau_immeuble: nombre de niveaux total de
                    l'immeuble
                nombre_niveau_logement: nombre de niveaux du logement
                    (maison ou appartement)
                hsp: hauteur sous plafond moyenne du logement/de
                    l'immeuble
                surface_habitable_immeuble: surface habitable totale de
                    l'immeuble dans le cas d'un DPE appartement avec
                    usage collectif ou d'un DPE immeuble.
                surface_tertiaire_immeuble: surface tertiaire totale de
                    l'immeuble dans le cas d'un DPE immeuble. La surface
                    tertiaire est prise en compte pour le calcul des
                    besoins dans le cas d'une installation collective
                    mixte tertiaire/residentiel
                nombre_appartement: nombre d'appartements de l'immeuble
                    dans le cas d'un DPE appartement avec usage
                    collectif ou d'un DPE immeuble.
                appartement_non_visite: est ce que l'appartement est un
                    appartement non visité dans le cas d'un DPE
                    appartement généré à partir d'un immeuble.
                    (application de système individuel les moins
                    performants de l'immeuble)
            """

            annee_construction: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_inclusive": "1200",
                    "max_inclusive": "2100",
                    "pattern": r"[0-9]{4}",
                    "nillable": True,
                },
            )
            enum_periode_construction_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                },
            )
            enum_methode_application_dpe_log_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 40,
                },
            )
            surface_habitable_logement: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0.0,
                    "nillable": True,
                },
            )
            nombre_niveau_immeuble: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0,
                    "nillable": True,
                },
            )
            nombre_niveau_logement: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0,
                    "nillable": True,
                },
            )
            hsp: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_exclusive": 0.0,
                },
            )
            surface_habitable_immeuble: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0.0,
                    "nillable": True,
                },
            )
            surface_tertiaire_immeuble: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0.0,
                    "nillable": True,
                },
            )
            nombre_appartement: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0,
                    "nillable": True,
                },
            )
            appartement_non_visite: Optional[SOuiNon] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

        @dataclass
        class Meteo:
            """
            Attributes:
                enum_zone_climatique_id: zone climatique du logement
                enum_classe_altitude_id: classe d'altitude du logement
                batiment_materiaux_anciens: est ce que le bâtiment est
                    principalement composé de matériaux anciens pour ses
                    murs 0 : non 1 : oui
            """

            enum_zone_climatique_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 8,
                },
            )
            enum_classe_altitude_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 3,
                },
            )
            batiment_materiaux_anciens: Optional[SOuiNon] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )

        @dataclass
        class Enveloppe:
            inertie: Optional["Dpe.Logement.Enveloppe.Inertie"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            mur_collection: Optional[
                "Dpe.Logement.Enveloppe.MurCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            plancher_bas_collection: Optional[
                "Dpe.Logement.Enveloppe.PlancherBasCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            plancher_haut_collection: Optional[
                "Dpe.Logement.Enveloppe.PlancherHautCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            baie_vitree_collection: Optional[
                "Dpe.Logement.Enveloppe.BaieVitreeCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            porte_collection: Optional[
                "Dpe.Logement.Enveloppe.PorteCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            ets_collection: Optional[
                "Dpe.Logement.Enveloppe.EtsCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            pont_thermique_collection: Optional[
                "Dpe.Logement.Enveloppe.PontThermiqueCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )

            @dataclass
            class Inertie:
                """
                Attributes:
                    inertie_plancher_bas_lourd: est ce que le plancher
                        bas est considéré comme lourd 0 : non 1 : oui
                    inertie_plancher_haut_lourd: est ce que le plancher
                        haud est considéré comme lourd 0 : non 1 : oui
                    inertie_paroi_verticale_lourd: est ce que les parois
                        verticales sont considérées comme lourdes 0 :
                        non 1 : oui
                    enum_classe_inertie_id: classe d'inertie globale du
                        bâtiment
                """

                inertie_plancher_bas_lourd: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                inertie_plancher_haut_lourd: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                inertie_paroi_verticale_lourd: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                enum_classe_inertie_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 4,
                    },
                )

            @dataclass
            class MurCollection:
                mur: List["Dpe.Logement.Enveloppe.MurCollection.Mur"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class Mur:
                    donnee_entree: Optional[
                        "Dpe.Logement.Enveloppe.MurCollection.Mur.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.Logement.Enveloppe.MurCollection.Mur.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            reference_lnc: reference projet de l'objet
                                local non chauffé qui peut être associé
                                à la paroi . Dans le cas d'un espace
                                tampon solarisé cette référence est
                                celle de l'espace tampon.
                            tv_coef_reduction_deperdition_id: id de la
                                ligne de la table utilisée pour le
                                calcul du coefficient de reduction des
                                deperditions
                            surface_aiu: surface aiu : surface des
                                parois du local non chauffé qui donnent
                                sur des locaux chauffés.
                            surface_aue: surface aue : surface des
                                parois du local non chauffé en contact
                                avec l'extérieur ou le sol
                            enum_cfg_isolation_lnc_id: configuration de
                                l'adjacence avec local non chauffé :
                                local chauffé (non) isolé/local non
                                chauffé (non) isolé/orientation véranda
                                qui permet de calculer le b
                            enum_type_adjacence_id: type d'adjacence de
                                la paroi
                            enum_orientation_id: orientation du mur
                            surface_paroi_totale: Surface de paroi
                                opaque + paroi vitrée de la paroi +
                                surface des portes
                            surface_paroi_opaque: Surface de paroi
                                opaque (sans baies vitrées sans portes)
                            umur0_saisi: Coefficient de transmission
                                thermique du mur non isolé Saisi en
                                direct par l'utilisateur (à justifier).
                                Coefficient de transmission thermique du
                                mur non isolé (avec pris en compte de
                                l'enduit et du doublage). C'est bien le
                                U du mur "nu" avec l'ensemble des
                                éléments hors isolations rapportée
                            tv_umur0_id: id de la ligne de la table
                                utilisée pour le calcul du Umur0
                            epaisseur_structure: epaisseur de la partie
                                structure de la paroi (sans l'isolation
                                intérieure ou extérieure) (cm)
                            enum_materiaux_structure_mur_id: matériaux
                                de structure de la paroi
                            enum_methode_saisie_u0_id: methode de saisie
                                de U0 (inclus les justifications à
                                produire en cas de saisie directe)
                            paroi_ancienne: la paroi est une paroi
                                ancienne sur laquelle a été appliquée un
                                enduit isolant (Renduit=0,7m².K.W-1) 0 :
                                non 1 : oui. (Attention ! nom de
                                propriété pas tout à fait explicite)
                            umur_saisi: Coefficient de transmission
                                thermique du mur saisi en direct par le
                                diagnostiqueur(à justifier)
                            enum_type_doublage_id: type de doublage
                                intérieur du mur.(précision de la nature
                                du doublage ou de l'epaisseur de la lame
                                d'air en cas de doublage indéterminé.)
                            enum_type_isolation_id: type d'isolation du
                                mur (ITI/ITE…..)
                            enum_periode_isolation_id: periode
                                d'isolation à saisir si différent de la
                                période de construction (cas d'une
                                rénovation de la paroi)
                            resistance_isolation: resistance isolation
                            epaisseur_isolation: epaisseur de
                                l'isolation (si plusieurs isolant
                                différents sommer leurs épaisseurs) (cm)
                            tv_umur_id: id de la ligne de la table
                                utilisée pour le calcul du coefficient
                                de transmission thermique umur
                            enum_methode_saisie_u_id: methode de saisie
                                du U (inclus les justifications à
                                produire en cas de saisie directe)
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_lnc: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        tv_coef_reduction_deperdition_id: Optional[int] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 283,
                                    "nillable": True,
                                },
                            )
                        )
                        surface_aiu: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_aue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_cfg_isolation_lnc_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                            },
                        )
                        enum_type_adjacence_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 22,
                            },
                        )
                        enum_orientation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 5,
                            },
                        )
                        surface_paroi_totale: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_paroi_opaque: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        umur0_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        tv_umur0_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 157,
                                "nillable": True,
                            },
                        )
                        epaisseur_structure: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_materiaux_structure_mur_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 27,
                            },
                        )
                        enum_methode_saisie_u0_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 5,
                            },
                        )
                        paroi_ancienne: Optional[SOuiNon] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )
                        umur_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_type_doublage_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 5,
                            },
                        )
                        enum_type_isolation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 9,
                            },
                        )
                        enum_periode_isolation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 10,
                            },
                        )
                        resistance_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        epaisseur_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        tv_umur_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 48,
                                "nillable": True,
                            },
                        )
                        enum_methode_saisie_u_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 10,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            b: coefficient de réduction des déperditions
                                du mur
                            umur: Coefficient de transmission thermique
                                du mur
                            umur0: Coefficient de transmission thermique
                                du mur non isolé final (avec pris en
                                compte de l'enduit et du doublage).
                                C'est bien le U du mur "nu" avec
                                l'ensemble des éléments hors isolations
                                rapportée
                        """

                        b: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 0.0,
                                "max_inclusive": 1.0,
                            },
                        )
                        umur: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        umur0: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )

            @dataclass
            class PlancherBasCollection:
                plancher_bas: List[
                    "Dpe.Logement.Enveloppe.PlancherBasCollection.PlancherBas"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class PlancherBas:
                    donnee_entree: Optional[
                        "Dpe.Logement.Enveloppe.PlancherBasCollection.PlancherBas.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.Logement.Enveloppe.PlancherBasCollection.PlancherBas.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            reference_lnc: reference projet de l'objet
                                local non chauffé qui peut être associé
                                à la paroi . Dans le cas d'un espace
                                tampon solarisé cette référence est
                                celle de l'espace tampon.
                            tv_coef_reduction_deperdition_id: id de la
                                ligne de la table utilisée pour le
                                calcul de coefficient de reduction des
                                déperditions
                            surface_aiu: surface aiu : surface des
                                parois du local non chauffé qui donnent
                                sur des locaux chauffés.
                            surface_aue: surface aue : surface des
                                parois du local non chauffé en contact
                                avec l'extérieur ou le sol
                            enum_cfg_isolation_lnc_id: configuration de
                                l'adjacence avec local non chauffé :
                                local chauffé (non) isolé/local non
                                chauffé (non) isolé/orientation véranda
                                qui permet de calculer le b
                            enum_type_adjacence_id: type d'adjacence de
                                la paroi
                            surface_paroi_opaque: Surface de paroi
                                opaque
                            upb0_saisi: Coefficient de transmission
                                thermique du planchers bas non isolé
                                Saisi en direct par l'utilisateur (à
                                justifier)
                            tv_upb0_id: id de la ligne de la table
                                utilisée pour le calcul du coefficient
                                de transmission thermique upb0
                            enum_type_plancher_bas_id: type de plancher
                                bas
                            enum_methode_saisie_u0_id: methode de saisie
                                de U0 (inclus les justifications à
                                produire en cas de saisie directe)
                            upb_saisi: Coefficient de transmission
                                thermique du planchers_bas saisi en
                                direct par le diagnostiqueur(à
                                justifier)
                            enum_type_isolation_id: type d'isolation du
                                plancher bas (ITI/ITE…..)
                            enum_periode_isolation_id: periode
                                d'isolation à saisir si différent de la
                                période de construction (cas d'une
                                rénovation de la paroi)
                            resistance_isolation: resistance isolation
                            epaisseur_isolation: epaisseur de
                                l'isolation (si plusieurs isolant
                                différents sommer leurs épaisseurs)
                            tv_upb_id: id de la ligne de la table
                                utilisée pour le calcul du coefficient
                                de transmission thermique upb
                            enum_methode_saisie_u_id: methode de saisie
                                du U (inclus les justifications à
                                produire en cas de saisie directe)
                            calcul_ue: est ce que le plancher bas est
                                passé par le calcul du Ue 0 : non 1 :
                                oui
                            perimetre_ue: périmètredu plancher lorsqu'il
                                est en contact avec un terre plein/sous
                                sol non chauffé ou vide sanitaire (à
                                renseigner lorsque calcul du Ue)
                            surface_ue: surface de plancher qui est en
                                contact avec un terre plein/sous sol non
                                chauffé ou vide sanitaire (à renseigner
                                lorsque calcul du Ue)
                            ue: Ue coefficient remplaçant Upb dans le
                                cas sur terre plein
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_lnc: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        tv_coef_reduction_deperdition_id: Optional[int] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 283,
                                    "nillable": True,
                                },
                            )
                        )
                        surface_aiu: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_aue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_cfg_isolation_lnc_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                            },
                        )
                        enum_type_adjacence_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 22,
                            },
                        )
                        surface_paroi_opaque: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        upb0_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        tv_upb0_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 12,
                                "nillable": True,
                            },
                        )
                        enum_type_plancher_bas_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 13,
                            },
                        )
                        enum_methode_saisie_u0_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 5,
                            },
                        )
                        upb_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_type_isolation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 9,
                            },
                        )
                        enum_periode_isolation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 10,
                            },
                        )
                        resistance_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        epaisseur_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        tv_upb_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 48,
                                "nillable": True,
                            },
                        )
                        enum_methode_saisie_u_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 10,
                            },
                        )
                        calcul_ue: Optional[SOuiNon] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )
                        perimetre_ue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_ue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        ue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            b: coefficient de réduction des déperditions
                                du planchers_bas
                            upb: Coefficient de transmission thermique
                                du planchers_bas Upb
                            upb_final: Coefficient de transmission
                                thermique du planchers_bas (Ue ou Upb en
                                fonction du type d'adjacence)
                            upb0: Coefficient de transmission thermique
                                du planchers bas non isolé final
                        """

                        b: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 0.0,
                                "max_inclusive": 1.0,
                            },
                        )
                        upb: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        upb_final: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        upb0: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )

            @dataclass
            class PlancherHautCollection:
                plancher_haut: List[
                    "Dpe.Logement.Enveloppe.PlancherHautCollection.PlancherHaut"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class PlancherHaut:
                    donnee_entree: Optional[
                        "Dpe.Logement.Enveloppe.PlancherHautCollection.PlancherHaut.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.Logement.Enveloppe.PlancherHautCollection.PlancherHaut.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            reference_lnc: reference projet de l'objet
                                local non chauffé qui peut être associé
                                à la paroi . Dans le cas d'un espace
                                tampon solarisé cette référence est
                                celle de l'espace tampon.
                            tv_coef_reduction_deperdition_id: id de la
                                ligne de la table utilisée pour le
                                calcul du coefficient de reduction des
                                deperditions
                            surface_aiu: surface aiu : surface des
                                parois du local non chauffé qui donnent
                                sur des locaux chauffés.
                            surface_aue: surface aue : surface des
                                parois du local non chauffé en contact
                                avec l'extérieur ou le sol
                            enum_cfg_isolation_lnc_id: configuration de
                                l'adjacence avec local non chauffé :
                                local chauffé (non) isolé/local non
                                chauffé (non) isolé/orientation véranda
                                qui permet de calculer le b
                            enum_type_adjacence_id: type d'adjacence de
                                la paroi
                            surface_paroi_opaque: Surface de paroi
                                opaque
                            uph0_saisi: Coefficient de transmission
                                thermique du planchers hauts non isolé
                                Saisi en direct par l'utilisateur (à
                                justifier)
                            tv_uph0_id: id de la ligne de la table
                                utilisée pour le calcul du coefficient
                                de transmission thermique uph0
                            enum_type_plancher_haut_id: type de plancher
                                haut
                            enum_methode_saisie_u0_id: methode de saisie
                                de U0 (inclus les justifications à
                                produire en cas de saisie directe)
                            uph_saisi: Coefficient de transmission
                                thermique du planchers_hauts saisi en
                                direct par le diagnostiqueur(à
                                justifier)
                            enum_type_isolation_id: type d'isolation du
                                plancher haut (ITI/ITE…..)
                            enum_periode_isolation_id: periode
                                d'isolation à saisir si différent de la
                                période de construction (cas d'une
                                rénovation de la paroi)
                            resistance_isolation: resistance isolation
                            epaisseur_isolation: epaisseur de
                                l'isolation (si plusieurs isolant
                                différents sommer leurs épaisseurs)
                            tv_uph_id: id de la ligne de la table
                                utilisée pour le calcul du coefficient
                                de transmission thermique uph
                            enum_methode_saisie_u_id: methode de saisie
                                du U (inclus les justifications à
                                produire en cas de saisie directe)
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_lnc: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        tv_coef_reduction_deperdition_id: Optional[int] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 283,
                                    "nillable": True,
                                },
                            )
                        )
                        surface_aiu: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_aue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_cfg_isolation_lnc_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                            },
                        )
                        enum_type_adjacence_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 22,
                            },
                        )
                        surface_paroi_opaque: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        uph0_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        tv_uph0_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 14,
                                "nillable": True,
                            },
                        )
                        enum_type_plancher_haut_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 16,
                            },
                        )
                        enum_methode_saisie_u0_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 5,
                            },
                        )
                        uph_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_type_isolation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 9,
                            },
                        )
                        enum_periode_isolation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 10,
                            },
                        )
                        resistance_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        epaisseur_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        tv_uph_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 96,
                                "nillable": True,
                            },
                        )
                        enum_methode_saisie_u_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 10,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            b: coefficient de réduction des déperditions
                                du planchers_hauts
                            uph: Coefficient de transmission thermique
                                du planchers_hauts uph
                            uph0: Coefficient de transmission thermique
                                du planchers hauts non isolé final
                        """

                        b: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 0.0,
                                "max_inclusive": 1.0,
                            },
                        )
                        uph: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        uph0: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )

            @dataclass
            class BaieVitreeCollection:
                baie_vitree: List[
                    "Dpe.Logement.Enveloppe.BaieVitreeCollection.BaieVitree"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class BaieVitree:
                    donnee_entree: Optional[
                        "Dpe.Logement.Enveloppe.BaieVitreeCollection.BaieVitree.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.Logement.Enveloppe.BaieVitreeCollection.BaieVitree.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            reference_paroi: reference projet de l'objet
                                paroi qui est associé à l'objet baie
                                vitrée. La codification et utilisation
                                des références peut différer entre
                                logiciels mais il devrait être attendu
                                que reference_paroi est la référence
                                d'une paroi de type mur,plancher_haut ou
                                plancher_bas
                            reference_lnc: reference projet de l'objet
                                local non chauffé qui peut être associé
                                à la paroi . Dans le cas d'un espace
                                tampon solarisé cette référence est
                                celle de l'espace tampon.
                            tv_coef_reduction_deperdition_id: id de la
                                ligne de la table utilisée pour le
                                calcul du coefficient de reduction des
                                deperditions
                            surface_aiu: surface aiu : surface des
                                parois du local non chauffé qui donnent
                                sur des locaux chauffés.
                            surface_aue: surface aue : surface des
                                parois du local non chauffé en contact
                                avec l'extérieur ou le sol
                            enum_cfg_isolation_lnc_id: configuration de
                                l'adjacence avec local non chauffé :
                                local chauffé (non) isolé/local non
                                chauffé (non) isolé/orientation véranda
                                qui permet de calculer le b
                            enum_type_adjacence_id: type d'adjacence de
                                la paroi
                            surface_totale_baie: surface totale de paroi
                                vitrée pour ce type de vitrage et sur
                                cette orientation (nombre de baies x
                                surface unitaire). La surface est la
                                surface de la baie dans son ensemble.
                                (vitrage + menuiserie inclus)
                            nb_baie: nombre de baies
                            tv_ug_id: id de la ligne de la table
                                utilisée pour le calcul du coefficent de
                                transmission thermique du vitrage ug
                            enum_type_vitrage_id: type de vitrage
                            enum_inclinaison_vitrage_id: inclinaison du
                                vitrage
                            enum_type_gaz_lame_id: type de gaz présent
                                dans la lame
                            epaisseur_lame: epaisseur de la lame
                            vitrage_vir: est ce que le vitrage est à
                                isolation renforcée 0 : non 1 : oui
                            enum_methode_saisie_perf_vitrage_id: methode
                                de saisie des caractéristiques
                                thermiques des vitrage (valeurs
                                forfaitaires ou saisies en direct
                                lorsque issu d'un justificatif)
                            ug_saisi: coefficient de transmission
                                thermique du vitrage saisi directement
                                (nécessite une justification)
                            tv_uw_id: id de la ligne de la table
                                utilisée pour le calcul du coefficent de
                                transmission thermique de la baie uw.
                                Dans le cas d'une
                                interpolation/extrapolation prendre la
                                valeur tabulée la plus proche
                            enum_type_materiaux_menuiserie_id: type de
                                matériaux des menuiseries
                            enum_type_baie_id: type de baie
                            uw_saisi: coefficient de transmission
                                thermique de la baie saisi directement
                                (nécessite une justification)
                            double_fenetre: est ce qu'il s'agit d'une
                                double fenetre. DANS LE CAS D'UNE DOUBLE
                                FENETRE LES DONNEES DU MODELE SONT
                                FOURNIES POUR LE VITRAGE LE PLUS
                                PERFORMANT OU POUR LA BAIE DANS SON
                                ENSEMBLE A L'EXCEPTION DE Uw2 ET Sw2 QUI
                                SONT LES CARACTERISTIQUES DU DEUXIEME
                                VITRAGE (le moins performant) 0 : non 1
                                : oui
                            uw_1: Uw de la première fenêtre dans le cas
                                d'une double fenêtre (par défaut la
                                première fenêtre est toujours celle avec
                                le Uw le plus élevé -&gt; plus
                                performante)
                            sw_1: Sw de la première fenêtre dans le cas
                                d'une double fenêtre (par défaut la
                                première fenêtre est toujours celle avec
                                le Uw le plus élevé -&gt; plus
                                performante)
                            uw_2: Uw de la deuxième fenêtre dans le cas
                                d'une double fenêtre (par défaut la
                                deuxième fenêtre est toujours celle avec
                                le Uw le plus faible -&gt; moins
                                performante)
                            sw_2: Sw de la deuxième fenêtre dans le cas
                                d'une double fenêtre (par défaut la
                                deuxième fenêtre est toujours celle avec
                                le Uw le plus faible -&gt; moins
                                performante)
                            tv_deltar_id: id de la ligne de la table
                                utilisée pour le calcul du delta de
                                resistance de la protection mobile.
                                (volets persienne etc..)
                            tv_ujn_id: id de la ligne de la table
                                utilisée pour le calcul du coefficient
                                de transmissiion de la baie jour/nuit
                                Ujn. Dans le cas d'une
                                interpolation/extrapolation prendre la
                                valeur tabulée la plus proche
                            enum_type_fermeture_id: type de fermeture
                                associé à la baie (volets/persiennes
                                etc..)
                            ujn_saisi: coefficient de transmission
                                thermique de la baie avec ses protection
                                solaires saisi directement (nécessite
                                une justification)
                            presence_retour_isolation: y a-t-il un
                                retour d'isolant de la paroi opaque sur
                                la baie 0 : non 1 : oui
                            largeur_dormant: largeur du dormant de la
                                baie (cm)
                            tv_sw_id: id de la ligne de la table
                                utilisée pour le calcul du facteur
                                solaire de la baie sw
                            sw_saisi: facteur solaire de la baie saisi
                                directement (nécessite une
                                justification)
                            enum_type_pose_id: type de pose de la baie
                            enum_orientation_id: orientation de la baie
                            tv_coef_masque_proche_id: id de la ligne de
                                la table utilisée pour le calcul du
                                coefficent de masque proche
                            tv_coef_masque_lointain_homogene_id: id de
                                la ligne de la table utilisée pour le
                                calcul du coefficient de masque homogène
                                lointain
                            masque_lointain_non_homogene_collection:
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_paroi: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_lnc: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        tv_coef_reduction_deperdition_id: Optional[int] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 283,
                                    "nillable": True,
                                },
                            )
                        )
                        surface_aiu: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_aue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_cfg_isolation_lnc_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                            },
                        )
                        enum_type_adjacence_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 22,
                            },
                        )
                        surface_totale_baie: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        nb_baie: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        tv_ug_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 181,
                                "nillable": True,
                            },
                        )
                        enum_type_vitrage_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 6,
                            },
                        )
                        enum_inclinaison_vitrage_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 4,
                            },
                        )
                        enum_type_gaz_lame_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 3,
                                "nillable": True,
                            },
                        )
                        epaisseur_lame: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        vitrage_vir: Optional[SOuiNon] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        enum_methode_saisie_perf_vitrage_id: Optional[int] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 15,
                                },
                            )
                        )
                        ug_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        tv_uw_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 723,
                                "nillable": True,
                            },
                        )
                        enum_type_materiaux_menuiserie_id: Optional[int] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 7,
                                },
                            )
                        )
                        enum_type_baie_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 8,
                            },
                        )
                        uw_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        double_fenetre: Optional[SOuiNon] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )
                        uw_1: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        sw_1: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        uw_2: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        sw_2: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        tv_deltar_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 7,
                                "nillable": True,
                            },
                        )
                        tv_ujn_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 236,
                                "nillable": True,
                            },
                        )
                        enum_type_fermeture_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 8,
                            },
                        )
                        ujn_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        presence_retour_isolation: Optional[SOuiNon] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )
                        largeur_dormant: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        tv_sw_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 173,
                                "nillable": True,
                            },
                        )
                        sw_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_type_pose_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 4,
                            },
                        )
                        enum_orientation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 5,
                            },
                        )
                        tv_coef_masque_proche_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 19,
                            },
                        )
                        tv_coef_masque_lointain_homogene_id: Optional[int] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 12,
                                    "nillable": True,
                                },
                            )
                        )
                        masque_lointain_non_homogene_collection: Optional[
                            "Dpe.Logement.Enveloppe.BaieVitreeCollection.BaieVitree.DonneeEntree.MasqueLointainNonHomogeneCollection"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )

                        @dataclass
                        class MasqueLointainNonHomogeneCollection:
                            masque_lointain_non_homogene: List[
                                "Dpe.Logement.Enveloppe.BaieVitreeCollection.BaieVitree.DonneeEntree.MasqueLointainNonHomogeneCollection.MasqueLointainNonHomogene"
                            ] = field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "min_occurs": 1,
                                },
                            )

                            @dataclass
                            class MasqueLointainNonHomogene:
                                """
                                Attributes:
                                    tv_coef_masque_lointain_non_homogene_id:
                                        id de la ligne de la table
                                        utilisée pour le calcul du
                                        coefficient de masque non
                                        homogène lointain
                                """

                                tv_coef_masque_lointain_non_homogene_id: Optional[
                                    int
                                ] = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "required": True,
                                        "min_inclusive": 1,
                                        "max_inclusive": 20,
                                    },
                                )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            b: coefficient de réduction des déperditions
                                de la baie vitrée
                            ug: Ug final de la baie : soit saisi
                                directement soit issu des tables
                                forfaitaires
                            uw: Uw final de la baie : soit saisi
                                directement soit issu des tables
                                forfaitaires
                            ujn: Ujn final de la baie : soit saisi
                                directement soit issu des tables
                                forfaitaires
                            u_menuiserie: U final de la menuiserie
                                utilisé dans le calcul : soit Ujn dans
                                le cas d'une baie avec protection
                                solaire soit Uw dans le cas d'une baie
                                sans protection solaire
                            sw: sw final de la baie: soit saisi
                                directement soit issu des tables
                                forfaitaires
                            fe1: fe1 facteur d'ensoleillement calculé à
                                partir de la table sur les masques
                                proches
                            fe2: fe2 facteur d'ensoleillement calculé
                                soit à l'aide de la méthode masque
                                lointain homogène ou méthode des masques
                                lointains proches
                        """

                        b: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 0.0,
                                "max_inclusive": 1.0,
                            },
                        )
                        ug: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        uw: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        ujn: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        u_menuiserie: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        sw: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        fe1: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        fe2: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 0.0,
                            },
                        )

            @dataclass
            class PorteCollection:
                porte: List["Dpe.Logement.Enveloppe.PorteCollection.Porte"] = (
                    field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                )

                @dataclass
                class Porte:
                    donnee_entree: Optional[
                        "Dpe.Logement.Enveloppe.PorteCollection.Porte.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.Logement.Enveloppe.PorteCollection.Porte.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            reference_paroi: reference projet de l'objet
                                paroi qui est associé à l'objet porte.
                                La codification et utilisation des
                                références peut différer entre logiciels
                                mais il devrait être attendu que
                                reference_paroi est la référence d'une
                                paroi de type mur,plancher_haut ou
                                plancher_bas
                            reference_lnc: reference projet de l'objet
                                local non chauffé qui peut être associé
                                à la paroi . Dans le cas d'un espace
                                tampon solarisé cette référence est
                                celle de l'espace tampon.
                            enum_cfg_isolation_lnc_id: configuration de
                                l'adjacence avec local non chauffé :
                                local chauffé (non) isolé/local non
                                chauffé (non) isolé/orientation véranda
                                qui permet de calculer le b
                            enum_type_adjacence_id: type d'adjacence de
                                la paroi
                            tv_coef_reduction_deperdition_id: id de la
                                ligne de la table utilisée pour le
                                calcul du coefficient de reduction des
                                deperditions
                            surface_aiu: surface aiu : surface des
                                parois du local non chauffé qui donnent
                                sur des locaux chauffés.
                            surface_aue: surface aue : surface des
                                parois du local non chauffé en contact
                                avec l'extérieur ou le sol
                            surface_porte: surface totale de portes
                                déclaré (nb_porte x surface unitaire de
                                porte dans le cas de plusieurs portes)
                            tv_uporte_id: id de la ligne de la table
                                utilisée pour le calcul du coefficient
                                de transfert thermique de la porte
                            enum_methode_saisie_uporte_id: méthode de
                                saisie du U de la porte
                            enum_type_porte_id: type de porte
                            uporte_saisi: coefficient de transmission
                                thermique de la porte saisi directement
                                (nécessite une justification)
                            nb_porte: nombre de portes
                            largeur_dormant: largeur du dormant de la
                                porte (cm)
                            presence_retour_isolation: y a-t-il un
                                retour d'isolant de la paroi opaque sur
                                la porte 0 : non 1 : oui
                            enum_type_pose_id: type de pose de la porte
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_paroi: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_lnc: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        enum_cfg_isolation_lnc_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                            },
                        )
                        enum_type_adjacence_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 22,
                            },
                        )
                        tv_coef_reduction_deperdition_id: Optional[int] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 283,
                                    "nillable": True,
                                },
                            )
                        )
                        surface_aiu: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_aue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_porte: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        tv_uporte_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                                "nillable": True,
                            },
                        )
                        enum_methode_saisie_uporte_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 3,
                            },
                        )
                        enum_type_porte_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 16,
                            },
                        )
                        uporte_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        nb_porte: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        largeur_dormant: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        presence_retour_isolation: Optional[SOuiNon] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        enum_type_pose_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 4,
                                "nillable": True,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            uporte: coefficient de transmission
                                thermique de la porte final : soit saisi
                                directement soit issu des tables de
                                valeurs forfaitaires
                            b: coefficient de transmission thermique de
                                la porte final : soit saisi directement
                                soit issu des tables de valeurs
                                forfaitaires
                        """

                        uporte: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        b: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 0.0,
                                "max_inclusive": 1.0,
                            },
                        )

            @dataclass
            class EtsCollection:
                ets: List["Dpe.Logement.Enveloppe.EtsCollection.Ets"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class Ets:
                    baie_ets_collection: Optional[
                        "Dpe.Logement.Enveloppe.EtsCollection.Ets.BaieEtsCollection"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    donnee_entree: Optional[
                        "Dpe.Logement.Enveloppe.EtsCollection.Ets.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.Logement.Enveloppe.EtsCollection.Ets.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )

                    @dataclass
                    class BaieEtsCollection:
                        baie_ets: List[
                            "Dpe.Logement.Enveloppe.EtsCollection.Ets.BaieEtsCollection.BaieEts"
                        ] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "min_occurs": 1,
                            },
                        )

                        @dataclass
                        class BaieEts:
                            donnee_entree: Optional[
                                "Dpe.Logement.Enveloppe.EtsCollection.Ets.BaieEtsCollection.BaieEts.DonneeEntree"
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                },
                            )

                            @dataclass
                            class DonneeEntree:
                                """
                                Attributes:
                                    description: description textuelle
                                        de l'objet
                                    reference: reference projet de
                                        l'objet (cette référence permet
                                        de faire d'éventuels liens entre
                                        objets). La codification et
                                        utilisation des références peut
                                        différer entre logiciels
                                    enum_orientation_id: orientation de
                                        la baie
                                    enum_inclinaison_vitrage_id:
                                        inclinaison du vitrage
                                    surface_totale_baie: surface totale
                                        de paroi vitrée pour ce type de
                                        vitrage et sur cette orientation
                                        (nombre de baies x surface
                                        unitaire). La surface est la
                                        surface de la baie dans son
                                        ensemble. (vitrage + menuiserie
                                        inclus)
                                    nb_baie: nombre de baies
                                """

                                description: Optional[str] = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "nillable": True,
                                    },
                                )
                                reference: Optional[str] = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "max_length": 255,
                                        "nillable": True,
                                    },
                                )
                                enum_orientation_id: Optional[int] = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "required": True,
                                        "min_inclusive": 1,
                                        "max_inclusive": 5,
                                    },
                                )
                                enum_inclinaison_vitrage_id: Optional[int] = (
                                    field(
                                        default=None,
                                        metadata={
                                            "type": "Element",
                                            "required": True,
                                            "min_inclusive": 1,
                                            "max_inclusive": 4,
                                        },
                                    )
                                )
                                surface_totale_baie: Optional[float] = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "required": True,
                                        "min_exclusive": 0.0,
                                    },
                                )
                                nb_baie: Optional[float] = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "required": True,
                                        "min_exclusive": 0.0,
                                    },
                                )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            tv_coef_reduction_deperdition_id: id de la
                                ligne de la table utilisée pour le
                                calcul du coefficient de reduction des
                                deperditions
                            enum_cfg_isolation_lnc_id: configuration de
                                l'adjacence avec local non chauffé :
                                local chauffé (non) isolé/local non
                                chauffé (non) isolé/orientation véranda
                                qui permet de calculer le b
                            tv_coef_transparence_ets_id: id de la ligne
                                de la table utilisée pour le calcul du
                                coefficient de transparence de l'espace
                                tampon solarisé
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        tv_coef_reduction_deperdition_id: Optional[int] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 283,
                                    "nillable": True,
                                },
                            )
                        )
                        enum_cfg_isolation_lnc_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                            },
                        )
                        tv_coef_transparence_ets_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 21,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            coef_transparence_ets: coefficient de
                                transparence de l'espace tampon solarisé
                                T (déterminé à partir des parois vitrées
                                de l'espace tampon solarisé)
                            bver: coefficient de reduction des
                                déperditions de l'espace tampon solarisé
                        """

                        coef_transparence_ets: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        bver: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )

            @dataclass
            class PontThermiqueCollection:
                pont_thermique: List[
                    "Dpe.Logement.Enveloppe.PontThermiqueCollection.PontThermique"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class PontThermique:
                    donnee_entree: Optional[
                        "Dpe.Logement.Enveloppe.PontThermiqueCollection.PontThermique.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.Logement.Enveloppe.PontThermiqueCollection.PontThermique.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            reference_1: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre
                                logiciels. Pour les ponts thermique il
                                est laissé la possibilité d'avoir 2
                                références complémentaires correspondant
                                aux référence de chacun des deux objets
                                concernés par le pont thermique
                            reference_2: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre
                                logiciels. Pour les ponts thermique il
                                est laissé la possibilité d'avoir 2
                                références complémentaires correspondant
                                aux référence de chacun des deux objets
                                concernés par le pont thermique
                            tv_pont_thermique_id: id de la ligne de la
                                table utilisée pour le calcul de la
                                valeur du pont thermique k
                            pourcentage_valeur_pont_thermique:
                                pourcentage de prise en compte de la
                                valeur du pont thermique (dans le cas
                                des pont thermiques refend/mur et
                                plancher intermediaire/mur cette valeur
                                est à 0,5 au lieu de 1)
                            l: longueur du pont thermique(m)
                            enum_methode_saisie_pont_thermique_id:
                                methode de saisie des ponts thermiques
                            enum_type_liaison_id: type de liaison de
                                pont thermique
                            k_saisi: valeur du pont thermique saisie
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_1: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_2: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        tv_pont_thermique_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 137,
                                "nillable": True,
                            },
                        )
                        pourcentage_valeur_pont_thermique: Optional[float] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 0.5,
                                    "max_inclusive": 1.0,
                                    "nillable": True,
                                },
                            )
                        )
                        l: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_exclusive": 0.0,
                            },
                        )
                        enum_methode_saisie_pont_thermique_id: Optional[
                            int
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 3,
                            },
                        )
                        enum_type_liaison_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_inclusive": 1,
                                "max_inclusive": 5,
                            },
                        )
                        k_saisi: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            k: valeur du pont thermique
                        """

                        k: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )

        @dataclass
        class VentilationCollection:
            ventilation: List[
                "Dpe.Logement.VentilationCollection.Ventilation"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass
            class Ventilation:
                donnee_entree: Optional[
                    "Dpe.Logement.VentilationCollection.Ventilation.DonneeEntree"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                donnee_intermediaire: Optional[
                    "Dpe.Logement.VentilationCollection.Ventilation.DonneeIntermediaire"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )

                @dataclass
                class DonneeEntree:
                    """
                    Attributes:
                        surface_ventile: surface ventilée. Dans le cas
                            d'une seule ventilation c'est la surface
                            habitable totale. Dans le cas d'un DPE
                            immeuble ou d'un DPE appartement à partir de
                            l'immeuble c'est la surface de
                            l'installation à l'immeuble qu'il faut
                            renseigner
                        description: description textuelle de l'objet
                        reference: reference projet de l'objet (cette
                            référence permet de faire d'éventuels liens
                            entre objets). La codification et
                            utilisation des références peut différer
                            entre logiciels
                        plusieurs_facade_exposee: est ce qu'il y a
                            plusieurs facades exposées au vent 0 : non 1
                            : oui
                        tv_q4pa_conv_id: id de la ligne de la table
                            utilisée pour le calcul du q4pa
                            conventionnel. valeur conventionnelle de la
                            perméabilité sous 4Pa (m3/(h.m2))
                        q4pa_conv_saisi: q4paconv saisi directement
                            quand la valeur est donnée par une mesure
                            d'étanchéité à l'air. valeur conventionnelle
                            de la perméabilité sous 4Pa (m3/(h.m2))
                        enum_methode_saisie_q4pa_conv_id: code de la
                            methode de saisie du q4paconv
                        tv_debits_ventilation_id: id de la ligne de la
                            table utilisée pour le calcul des débits de
                            ventilations
                        enum_type_ventilation_id: code du type de
                            ventilation
                        ventilation_post_2012: est ce que le système de
                            ventilation est postérieur à 2012 0 : non 1
                            : oui
                        ref_produit_ventilation: référence produit et
                            marque du système de ventilation
                        cle_repartition_ventilation: clé de répartition
                            pour passer des consommations bâtiments au
                            consommation logement dans le cas DPE
                            appartement calculé à partir du DPE immeuble
                            UNIQUEMENT. Voir section 8.5.4 du document
                            guide pour plus de détail. Pour la
                            ventilation il s'agit du rapport surface
                            habitable logement / surface habitable
                            immeuble
                    """

                    surface_ventile: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    description: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    reference: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )
                    plusieurs_facade_exposee: Optional[SOuiNon] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    tv_q4pa_conv_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 12,
                            "nillable": True,
                        },
                    )
                    q4pa_conv_saisi: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    enum_methode_saisie_q4pa_conv_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 3,
                        },
                    )
                    tv_debits_ventilation_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 38,
                        },
                    )
                    enum_type_ventilation_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 38,
                        },
                    )
                    ventilation_post_2012: Optional[SOuiNon] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    ref_produit_ventilation: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )
                    cle_repartition_ventilation: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "max_inclusive": 1.0,
                            "nillable": True,
                        },
                    )

                @dataclass
                class DonneeIntermediaire:
                    """
                    Attributes:
                        pvent_moy: puissance de la ventilation moyenne
                            soit saisie soit calculée avec la méthode
                            proposée
                        q4pa_conv: q4pa conv final soit issue d'une
                            saisie de mesure à l'étanchéité à l'air soit
                            d'une valeur forfaitaire. valeur
                            conventionnelle de la perméabilité sous 4Pa
                            (m3/(h.m2))
                        conso_auxiliaire_ventilation: Consommation des
                            auxilliaires de ventilation. Dans le cas
                            d'un DPE immeuble ou d'un DPE appartement à
                            partir de l'immeuble c'est la consommation
                            de l'installation à l'immeuble qu'il faut
                            saisir.
                        hperm: déperdition thermique par renouvellement
                            d'air due au vent
                        hvent: déperdition thermique par renouvellement
                            d'air due au système de ventilation
                    """

                    pvent_moy: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    q4pa_conv: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    conso_auxiliaire_ventilation: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    hperm: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    hvent: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )

        @dataclass
        class ClimatisationCollection:
            climatisation: List[
                "Dpe.Logement.ClimatisationCollection.Climatisation"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

            @dataclass
            class Climatisation:
                donnee_entree: Optional[
                    "Dpe.Logement.ClimatisationCollection.Climatisation.DonneeEntree"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                donnee_intermediaire: Optional[
                    "Dpe.Logement.ClimatisationCollection.Climatisation.DonneeIntermediaire"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )

                @dataclass
                class DonneeEntree:
                    """
                    Attributes:
                        description: description textuelle de l'objet
                        reference: reference projet de l'objet (cette
                            référence permet de faire d'éventuels liens
                            entre objets). La codification et
                            utilisation des références peut différer
                            entre logiciels
                        surface_clim: surface climatisée : si le
                            logement n'est pas climatisé dans son
                            ensemble la surface climatisée peut être
                            inférieure à la surface totale du
                            logement.Dans le cas spécifique d'un DPE
                            immeuble avec installation individuelle
                            échantillonée :saisir la surface climatisée
                            par la totalité des logements représentés
                            par le logement moyen surface_clim =
                            Shmoy*Nblgt. Dans le cas d'un DPE immeuble
                            ou d'un DPE appartement à partir de
                            l'immeuble c'est la surface de
                            l'installation à l'immeuble qu'il faut
                            renseigner
                        tv_seer_id: id de la ligne de la table utilisée
                            pour le calcul du coefficient d'efficience
                            énergétique du système de climatisation seer
                        nombre_logement_echantillon: nombre de logements
                            représentés par le logement échantillon dans
                            le cas d'un DPE immeuble avec installation
                            de climatisation individuelle. (à ne
                            renseigner que dans ce cas précis)
                        enum_methode_calcul_conso_id: méthode de calcul
                            de consommation de froid : simple, ou cas
                            particuliers installation collective
                            virtualisée ou installation individuelle
                            échantilonnée (dpe immeuble)
                        enum_periode_installation_fr_id: période
                            d'installation du système de refroidissement
                        cle_repartition_clim: clé de répartition pour
                            passer des consommations bâtiments au
                            consommation logement dans le cas DPE
                            appartement calculé à partir du DPE immeuble
                            UNIQUEMENT. Voir section 8.5.4 du document
                            guide pour plus de détail.
                        enum_type_generateur_fr_id: type de générateur
                            de froid
                        enum_type_energie_id: type d'énergie consommée
                            par le générateur de froid
                        enum_methode_saisie_carac_sys_id: methode de
                            saisie du seer : lecture de table
                            forfaitaire ou saisie justifiée
                        ref_produit_fr: référence produit et marque du
                            générateur de froid
                    """

                    description: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    reference: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )
                    surface_clim: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    tv_seer_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 6,
                            "nillable": True,
                        },
                    )
                    nombre_logement_echantillon: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    enum_methode_calcul_conso_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 6,
                        },
                    )
                    enum_periode_installation_fr_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 3,
                        },
                    )
                    cle_repartition_clim: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "max_inclusive": 1.0,
                            "nillable": True,
                        },
                    )
                    enum_type_generateur_fr_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 23,
                        },
                    )
                    enum_type_energie_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 15,
                            "nillable": True,
                        },
                    )
                    enum_methode_saisie_carac_sys_id: Optional[
                        DonneeEntreeEnumMethodeSaisieCaracSysId
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    ref_produit_fr: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )

                @dataclass
                class DonneeIntermediaire:
                    """
                    Attributes:
                        eer: coefficient d'efficience energétique du
                            système de climatisation final (SEER *0,95)
                        besoin_fr: besoin de refroidissement annuel.
                            Dans le cas d'un DPE immeuble ou d'un DPE
                            appartement à partir de l'immeuble c'est le
                            besoin de l'installation à l'immeuble qu'il
                            faut saisir.
                        conso_fr: consommation de refroidissement annuel
                            (kWh). Dans le cas d'un DPE immeuble ou d'un
                            DPE appartement à partir de l'immeuble c'est
                            la consommation de l'installation à
                            l'immeuble qu'il faut saisir.
                        conso_fr_depensier: consommation de
                            refroidissement annuel pour le scénario
                            dépensier (kWh) . Dans le cas d'un DPE
                            immeuble ou d'un DPE appartement à partir de
                            l'immeuble c'est la consommation de
                            l'installation à l'immeuble qu'il faut
                            saisir.
                    """

                    eer: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                            "max_inclusive": 15.0,
                        },
                    )
                    besoin_fr: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    conso_fr: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    conso_fr_depensier: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )

        @dataclass
        class ProductionElecEnr:
            donnee_entree: Optional[
                "Dpe.Logement.ProductionElecEnr.DonneeEntree"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            donnee_intermediaire: Optional[
                "Dpe.Logement.ProductionElecEnr.DonneeIntermediaire"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
            panneaux_pv_collection: Optional[
                "Dpe.Logement.ProductionElecEnr.PanneauxPvCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )

            @dataclass
            class DonneeEntree:
                """
                Attributes:
                    description: description textuelle de l'objet
                    reference: reference projet de l'objet (cette
                        référence permet de faire d'éventuels liens
                        entre objets). La codification et utilisation
                        des références peut différer entre logiciels
                    presence_production_pv: est ce qu'il y a de la
                        production de photovoltaique renouvelable 0 :
                        non 1 : oui
                    enum_type_enr_id: enumérateur listant les systèmes
                        de production d'éléctricité d'origine
                        renouvelables présents dans le bâtiment
                """

                description: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                reference: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "max_length": 255,
                        "nillable": True,
                    },
                )
                presence_production_pv: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                enum_type_enr_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 7,
                    },
                )

            @dataclass
            class DonneeIntermediaire:
                """
                Attributes:
                    taux_autoproduction: taux d'autoproduction Tap de la
                        production d'éléctricité d'origne renouvelable
                    production_pv: production d'éléctricité
                        photovoltaique (kWh)
                    conso_elec_ac: éléctricité photovoltaique
                        autoconsommée (kWh)
                """

                taux_autoproduction: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                production_pv: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_elec_ac: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )

            @dataclass
            class PanneauxPvCollection:
                panneaux_pv: List[
                    "Dpe.Logement.ProductionElecEnr.PanneauxPvCollection.PanneauxPv"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class PanneauxPv:
                    """
                    Attributes:
                        surface_totale_capteurs: surface totale de
                            capteurs photovoltaïque. Dans le cas d'une
                            installation collective de PV pour un DPE
                            appartement, la surface est celle proratisé
                        ratio_virtualisation: ratio de virtualisation de
                            l'installation PV collective lorsque l'on
                            rapporte des usages collectifs à un
                            appartement (a = Shabappartement/Shabtotale)
                        nombre_module: nombre de modules photovoltaïque
                            standards posés.
                        tv_coef_orientation_pv_id: id de la ligne de la
                            table utilisée pour le calcul du coefficient
                            d'orientation des panneaux photovoltaïques
                        enum_orientation_pv_id: orientation des panneaux
                            photovoltaïques
                        enum_inclinaison_pv_id: inclinaison des panneaux
                            photovoltaïques
                    """

                    surface_totale_capteurs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    ratio_virtualisation: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    nombre_module: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0,
                            "nillable": True,
                        },
                    )
                    tv_coef_orientation_pv_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 20,
                            "nillable": True,
                        },
                    )
                    enum_orientation_pv_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 5,
                            "nillable": True,
                        },
                    )
                    enum_inclinaison_pv_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 4,
                            "nillable": True,
                        },
                    )

        @dataclass
        class InstallationEcsCollection:
            installation_ecs: List[
                "Dpe.Logement.InstallationEcsCollection.InstallationEcs"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

            @dataclass
            class InstallationEcs:
                donnee_entree: Optional[
                    "Dpe.Logement.InstallationEcsCollection.InstallationEcs.DonneeEntree"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                donnee_intermediaire: Optional[
                    "Dpe.Logement.InstallationEcsCollection.InstallationEcs.DonneeIntermediaire"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                generateur_ecs_collection: Optional[
                    "Dpe.Logement.InstallationEcsCollection.InstallationEcs.GenerateurEcsCollection"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )

                @dataclass
                class DonneeEntree:
                    """
                    Attributes:
                        description: description textuelle de l'objet
                        reference: reference projet de l'objet (cette
                            référence permet de faire d'éventuels liens
                            entre objets). La codification et
                            utilisation des références peut différer
                            entre logiciels
                        enum_cfg_installation_ecs_id: code de
                            configuration de l'installation d'ECS
                            (installation simple, avec solaire ou avec
                            plusieurs systèmes d'ECS)
                        enum_type_installation_id: code du type
                            d'installation d'ECS (collective ou
                            individuelle)
                        enum_methode_calcul_conso_id: méthode de calcul
                            de consommation d'ECS : simple, ou cas
                            particuliers installation collective
                            virtualisée ou installation individuelle
                            échantilonnée (dpe immeuble)
                        ratio_virtualisation: ratio de virtualisation de
                            l'installation collective lorsque l'on
                            rapporte des usages collectifs à un
                            appartement (a = Shabappartement/Shabtotale)
                        cle_repartition_ecs: clé de répartition pour
                            passer des consommations bâtiments au
                            consommation logement dans le cas DPE
                            appartement calculé à partir du DPE immeuble
                            UNIQUEMENT. Voir section 8.5.4 du document
                            guide pour plus de détail
                        surface_habitable: surface habitable
                            correspondant au(x) logement(x) desservi(s)
                            par l'installation d'ECS.(surface habitable
                            du logement ou de la totalité des logements
                            de l'immeuble) Dans le cas spécifique d'un
                            DPE immeuble avec installation individuelle
                            échantillonée :saisir la surface de la
                            totalité des logements représentés par le
                            logement moyen surface_habitable=
                            Shmoy*Nblgt. Dans le cas d'un DPE immeuble
                            ou d'un DPE appartement à partir de
                            l'immeuble c'est la surface de
                            l'installation à l'immeuble qu'il faut
                            renseigner
                        nombre_logement: nombre de logements desservis
                            par l'installation d'ECS. Dans le cas d'un
                            DPE immeuble avec installation individuelle
                            échantillonée : saisir le nombre de
                            logements qui sont équipés de ce type
                            d'installation d'ECS.
                        nombre_niveau_installation_ecs: nombre de
                            niveaux desservis par l'installation d'ECS
                            (très souvent égal au nombre de niveaux du
                            bâtiment)
                        fecs_saisi: facteur de couverture solaire pour
                            l'ECS saisi directement lorsque celui-ci
                            peut être justifié
                        tv_facteur_couverture_solaire_id: id de la ligne
                            de la table utilisée pour le calcul du
                            facteur de couverture solaire
                        enum_methode_saisie_fact_couv_sol_id: méthode de
                            saisie du facteur de couverture solaire pour
                            l'ECS (saisi en direct justifié ou calculé à
                            partir de la table)
                        enum_type_installation_solaire_id: type
                            d'installation solaire (ECS+Chauffage , ECS
                            solaire seule etc…)
                        tv_rendement_distribution_ecs_id: id de la ligne
                            de la table utilisée pour le calcul du
                            rendement de distribution de l'installation
                            d'ECS
                        enum_bouclage_reseau_ecs_id: type de bouclage du
                            réseau d'ECS pour la prise en compte des
                            consommations d'auxiliaires de distribution
                        reseau_distribution_isole: est ce que le réseau
                            de distribution est isolé 0 : non 1 : oui
                    """

                    description: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    reference: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )
                    enum_cfg_installation_ecs_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 3,
                        },
                    )
                    enum_type_installation_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 4,
                        },
                    )
                    enum_methode_calcul_conso_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 6,
                        },
                    )
                    ratio_virtualisation: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    cle_repartition_ecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "max_inclusive": 1.0,
                            "nillable": True,
                        },
                    )
                    surface_habitable: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    nombre_logement: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    nombre_niveau_installation_ecs: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0,
                        },
                    )
                    fecs_saisi: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    tv_facteur_couverture_solaire_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 48,
                            "nillable": True,
                        },
                    )
                    enum_methode_saisie_fact_couv_sol_id: Optional[int] = (
                        field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 2,
                                "nillable": True,
                            },
                        )
                    )
                    enum_type_installation_solaire_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 4,
                            "nillable": True,
                        },
                    )
                    tv_rendement_distribution_ecs_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 8,
                        },
                    )
                    enum_bouclage_reseau_ecs_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 3,
                        },
                    )
                    reseau_distribution_isole: Optional[SOuiNon] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                @dataclass
                class DonneeIntermediaire:
                    """
                    Attributes:
                        rendement_distribution: rendement de
                            distribution de l'installation d'ECS (0-1)
                        besoin_ecs: besoin d'ECS annuel pour l'ensemble
                            de l'installation (kWh). Dans le cas d'un
                            DPE immeuble ou d'un DPE appartement à
                            partir de l'immeuble c'est la consommation
                            de l'installation à l'immeuble qu'il faut
                            saisir.
                        besoin_ecs_depensier: besoin d'ECS annuel pour
                            l'ensemble de l'installation dans le cas du
                            scénario dépensier (kWh). Dans le cas d'un
                            DPE immeuble ou d'un DPE appartement à
                            partir de l'immeuble c'est la consommation
                            de l'installation à l'immeuble qu'il faut
                            saisir.
                        fecs: facteur de couverture solaire de l'ECS
                        production_ecs_solaire: production d'ecs solaire
                            annuelle (kWh). Dans le cas d'un DPE
                            immeuble ou d'un DPE appartement à partir de
                            l'immeuble c'est la consommation de
                            l'installation à l'immeuble qu'il faut
                            saisir.
                        conso_ecs: consommation d'energie annuelle de
                            l'installation d'ECS en energie finale kWh.
                            Dans le cas d'un DPE immeuble ou d'un DPE
                            appartement à partir de l'immeuble c'est la
                            consommation de l'installation à l'immeuble
                            qu'il faut saisir.
                        conso_ecs_depensier: consommation d'energie
                            annuelle de l'installation d'ECS pour le
                            scénario dépensier en energie finale kWh.
                            Dans le cas d'un DPE immeuble ou d'un DPE
                            appartement à partir de l'immeuble c'est la
                            consommation de l'installation à l'immeuble
                            qu'il faut saisir.
                    """

                    rendement_distribution: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                            "max_inclusive": 1.0,
                        },
                    )
                    besoin_ecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    besoin_ecs_depensier: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    fecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    production_ecs_solaire: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    conso_ecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    conso_ecs_depensier: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )

                @dataclass
                class GenerateurEcsCollection:
                    generateur_ecs: List[
                        "Dpe.Logement.InstallationEcsCollection.InstallationEcs.GenerateurEcsCollection.GenerateurEcs"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                        },
                    )

                    @dataclass
                    class GenerateurEcs:
                        donnee_entree: Optional[
                            "Dpe.Logement.InstallationEcsCollection.InstallationEcs.GenerateurEcsCollection.GenerateurEcs.DonneeEntree"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )
                        donnee_intermediaire: Optional[
                            "Dpe.Logement.InstallationEcsCollection.InstallationEcs.GenerateurEcsCollection.GenerateurEcs.DonneeIntermediaire"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )

                        @dataclass
                        class DonneeEntree:
                            """
                            Attributes:
                                description: description textuelle de
                                    l'objet
                                reference: reference projet de l'objet
                                    (cette référence permet de faire
                                    d'éventuels liens entre objets). La
                                    codification et utilisation des
                                    références peut différer entre
                                    logiciels
                                reference_generateur_mixte: référence
                                    commune pour un générateur mixte
                                    chauffage ECS. Cette référence est
                                    identique pour les deux parties du
                                    générateur (chauffage et ECS) et est
                                    utilisé pour faire le lien entre les
                                    deux
                                enum_type_generateur_ecs_id: type de
                                    generateur d'ecs
                                ref_produit_generateur_ecs: référence
                                    produit et marque du générateur
                                    d'ECS
                                enum_usage_generateur_id: usages assurés
                                    par le générateur
                                    (chauffage/ecs/chauffage+ecs)
                                enum_type_energie_id: type d'énergie
                                    consommée par le générateur d'ECS
                                tv_generateur_combustion_id: id de la
                                    ligne de la table utilisée pour le
                                    calcul des paramètres du générateur
                                    à combustion Rpn,Rpint,Qp0,Pveil
                                enum_methode_saisie_carac_sys_id:
                                    méthode de saisie des performances
                                    du système d'ECS
                                tv_pertes_stockage_id: id de la ligne de
                                    la table utilisée pour le calcul des
                                    pertes de stockage pour les ballons
                                    éléctriques
                                tv_scop_id: id de la ligne de la table
                                    utilisée pour le calcul du
                                    coefficient de performance du
                                    système thermodynamique (SCOP)
                                enum_periode_installation_ecs_thermo_id:
                                    periode installation du système
                                    thermodynamique
                                identifiant_reseau_chaleur: identifiant
                                    réseau de chaleur ou de froid
                                    utilisé (utilisé à partir du 18
                                    janvier 2022)
                                tv_reseau_chaleur_id: id de la ligne de
                                    la table utilisée pour le calcul du
                                    contenu CO2 des réseaux de chaleurs
                                    (OBSOLETE et remplacé par
                                    identifiant_reseau_chaleur à partir
                                    du 18 janvier 2022 et la prise en
                                    compte du nouvel arrêté réseau de
                                    chaleur).
                                enum_type_stockage_ecs_id: Type de
                                    stockage d'ECS (intégré à la
                                    production ou indépendant)
                                position_volume_chauffe: est ce que le
                                    générateur est positionné dans le
                                    volume chauffé. (pour le calcul des
                                    pertes de génération récupérables)
                                position_volume_chauffe_stockage: est ce
                                    que le ballon de stockage est
                                    positionné dans le volume chauffé.
                                    (pour le calcul des pertes de
                                    stockage récupérables)
                                volume_stockage: volume de stockage
                                    associé au générateur d'ECS
                                presence_ventouse: présence d'un système
                                    de ventouse ou avec un ventilateur
                                    pour l'évacuation des fumées d'un
                                    système à combustion 0 : non 1 : oui
                            """

                            description: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            reference: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            reference_generateur_mixte: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            enum_type_generateur_ecs_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 134,
                                },
                            )
                            ref_produit_generateur_ecs: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            enum_usage_generateur_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 3,
                                },
                            )
                            enum_type_energie_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 15,
                                },
                            )
                            tv_generateur_combustion_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 93,
                                    "nillable": True,
                                },
                            )
                            enum_methode_saisie_carac_sys_id: Optional[
                                DonneeEntreeEnumMethodeSaisieCaracSysId
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                },
                            )
                            tv_pertes_stockage_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 16,
                                    "nillable": True,
                                },
                            )
                            tv_scop_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 88,
                                    "nillable": True,
                                },
                            )
                            enum_periode_installation_ecs_thermo_id: Optional[
                                int
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 3,
                                    "nillable": True,
                                },
                            )
                            identifiant_reseau_chaleur: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "pattern": r"[0-9]{4}[C-F]",
                                    "nillable": True,
                                },
                            )
                            tv_reseau_chaleur_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 797,
                                    "nillable": True,
                                },
                            )
                            enum_type_stockage_ecs_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 3,
                                },
                            )
                            position_volume_chauffe: Optional[SOuiNon] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                },
                            )
                            position_volume_chauffe_stockage: Optional[
                                SOuiNon
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            volume_stockage: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 0.0,
                                },
                            )
                            presence_ventouse: Optional[SOuiNon] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )

                        @dataclass
                        class DonneeIntermediaire:
                            """
                            Attributes:
                                pn: puissance nominale du générateur à
                                    combustion. Dans le cas d'un
                                    générateur virtualisé pour DPE
                                    appartement avec ECS collective
                                    saisir Pe = a*Pn(collectif) (W)
                                qp0: pertes à l'arret du générateur à
                                    combustion. Dans le cas d'un
                                    générateur virtualisé pour DPE
                                    appartement avec ECS collective
                                    saisir Qp0 correspondant à Pe =
                                    a*Pn(collectif)
                                pveilleuse: puissance de la veilleuse du
                                    générateur à combustion (W)
                                rpn: rendement de génération à pleine
                                    charge du générateur à combustion
                                    (0-1,5)
                                cop: COP du chauffe-eau thermodynamique
                                    (inclus le rendement de stockage)
                                    (0-20)
                                ratio_besoin_ecs: ratio du besoin ecs de
                                    l'installation affecté au
                                    générateur. Ce ratio est de 1 pour
                                    les installations classiques et de
                                    0,5 pour les installations d'ECS
                                    avec deux générateurs
                                rendement_generation: Rg : rendement de
                                    génération dans le cas où le
                                    rendement de stockage est séparé du
                                    rendement de génération (ballon
                                    éléctrique ou ballon séparé de la
                                    production) (0-1,5)
                                rendement_generation_stockage: RgxRs :
                                    rendement de génération x rendement
                                    de stockage pour les systèmes pour
                                    lesquels le ballon est intégré au
                                    système de production ou réseau de
                                    chaleur (0-1,5)
                                conso_ecs: consommation d'energie
                                    annuelle du générateur d'ECS (kWh)
                                    (Exprimé en kWh PCI pour les
                                    combustibles ). Dans le cas d'un DPE
                                    immeuble ou d'un DPE appartement à
                                    partir de l'immeuble c'est la
                                    consommation du générateur à
                                    l'immeuble qu'il faut saisir.
                                conso_ecs_depensier: consommation
                                    d'énergie annuelle du générateur
                                    d'ECS pour le scénario dépensier en
                                    énergie finale (kWh) (Exprimé en kWh
                                    PCI pour les combustibles ). Dans le
                                    cas d'un DPE immeuble ou d'un DPE
                                    appartement à partir de l'immeuble
                                    c'est la consommation du générateur
                                    à l'immeuble qu'il faut saisir.
                                rendement_stockage: Rs : rendement de
                                    stockage dans le cas où le rendement
                                    de stockage est séparé du rendement
                                    de génération (ballon éléctrique ou
                                    ballon séparé de la production)
                                    sinon égal à 1 (0-1)
                            """

                            pn: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 100.0,
                                    "nillable": True,
                                },
                            )
                            qp0: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            pveilleuse: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            rpn: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.5,
                                    "nillable": True,
                                },
                            )
                            cop: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 1.0,
                                    "max_inclusive": 8.0,
                                    "nillable": True,
                                },
                            )
                            ratio_besoin_ecs: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.0,
                                },
                            )
                            rendement_generation: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.5,
                                    "nillable": True,
                                },
                            )
                            rendement_generation_stockage: Optional[float] = (
                                field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "min_exclusive": 0.0,
                                        "max_inclusive": 1.5,
                                        "nillable": True,
                                    },
                                )
                            )
                            conso_ecs: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 0.0,
                                },
                            )
                            conso_ecs_depensier: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 0.0,
                                },
                            )
                            rendement_stockage: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.08,
                                    "nillable": True,
                                },
                            )

        @dataclass
        class InstallationChauffageCollection:
            installation_chauffage: List[
                "Dpe.Logement.InstallationChauffageCollection.InstallationChauffage"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

            @dataclass
            class InstallationChauffage:
                donnee_entree: Optional[
                    "Dpe.Logement.InstallationChauffageCollection.InstallationChauffage.DonneeEntree"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                donnee_intermediaire: Optional[
                    "Dpe.Logement.InstallationChauffageCollection.InstallationChauffage.DonneeIntermediaire"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                emetteur_chauffage_collection: Optional[
                    "Dpe.Logement.InstallationChauffageCollection.InstallationChauffage.EmetteurChauffageCollection"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                generateur_chauffage_collection: Optional[
                    "Dpe.Logement.InstallationChauffageCollection.InstallationChauffage.GenerateurChauffageCollection"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )

                @dataclass
                class DonneeEntree:
                    """
                    Attributes:
                        description: description textuelle de l'objet
                        reference: reference projet de l'objet (cette
                            référence permet de faire d'éventuels liens
                            entre objets). La codification et
                            utilisation des références peut différer
                            entre logiciels
                        surface_chauffee: surface chauffée par
                            l'installation de chauffage(surface du
                            logement ou de l'immeuble). Dans le cas
                            spécifique d'un DPE immeuble avec
                            installation individuelle échantillonée
                            :saisir la surface chauffée de la totalité
                            des logements représentés par le logement
                            moyen surface_habitable= Shmoy*Nblgt. Dans
                            le cas d'un DPE immeuble ou d'un DPE
                            appartement à partir de l'immeuble c'est la
                            surface de l'installation à l'immeuble qu'il
                            faut renseigner
                        nombre_logement_echantillon: nombre de logements
                            représentés par le logement échantillon dans
                            le cas d'un DPE immeuble avec installation
                            de chauffage individuelle. (à ne renseigner
                            que dans ce cas précis)
                        nombre_niveau_installation_ch: nombre de niveaux
                            desservis par l'installation de chauffage
                            (très souvent égal au nombre de niveaux du
                            bâtiment)
                        enum_cfg_installation_ch_id: configuration de
                            l'installation de chauffage
                        ratio_virtualisation: ratio de virtualisation de
                            l'installation collective lorsque l'on
                            rapporte des usages collectifs à un
                            appartement (a = Shabappartement/Shabtotale)
                        coef_ifc: coefficient d'individualisation des
                            frais de chauffage dans le cas d'un DPE
                            appartement calculé à partir d'un DPE
                            immeuble
                        cle_repartition_ch: clé de répartition pour
                            passer des consommations bâtiments au
                            consommation logement dans le cas DPE
                            appartement calculé à partir du DPE immeuble
                            UNIQUEMENT. Voir section 8.5.4 du document
                            guide pour plus de détail
                        enum_type_installation_id: type d'installation
                            de chauffage (collective ou individuelle ou
                            collective multi batiment
                        enum_methode_calcul_conso_id: méthode de calcul
                            de consommation de chauffage : simple, ou
                            cas particuliers installation collective
                            virtualisée ou installation individuelle
                            échantilonnée (dpe immeuble)
                        enum_methode_saisie_fact_couv_sol_id: méthode de
                            saisie du facteur de couverture solaire pour
                            le chauffage (saisi en direct justifié ou
                            calculé à partir de la table)
                        tv_facteur_couverture_solaire_id: id de la ligne
                            de la table utilisée pour le calcul du
                            facteur de couverture solaire
                        fch_saisi: Facteur de couverture solaire pour
                            l'installation de chauffage(saisi)
                    """

                    description: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    reference: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )
                    surface_chauffee: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    nombre_logement_echantillon: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    nombre_niveau_installation_ch: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0,
                        },
                    )
                    enum_cfg_installation_ch_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 11,
                        },
                    )
                    ratio_virtualisation: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "max_inclusive": 1.0,
                            "nillable": True,
                        },
                    )
                    coef_ifc: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    cle_repartition_ch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "max_inclusive": 1.0,
                            "nillable": True,
                        },
                    )
                    enum_type_installation_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 4,
                        },
                    )
                    enum_methode_calcul_conso_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 6,
                        },
                    )
                    enum_methode_saisie_fact_couv_sol_id: Optional[int] = (
                        field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 2,
                                "nillable": True,
                            },
                        )
                    )
                    tv_facteur_couverture_solaire_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 48,
                            "nillable": True,
                        },
                    )
                    fch_saisi: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "max_inclusive": 1.0,
                            "nillable": True,
                        },
                    )

                @dataclass
                class DonneeIntermediaire:
                    """
                    Attributes:
                        besoin_ch: Besoin de chauffage total de
                            l'installation (kWh)
                        besoin_ch_depensier: Besoin de chauffage total
                            de l'installation pour le scénario dépensier
                            (DH21) (kWh)
                        production_ch_solaire: Production de chauffage
                            solaire (kWh)
                        fch: Facteur de couverture solaire pour
                            l'installation de chauffage
                        conso_ch: consommation d'energie annuelle de
                            l'installation de chauffage en energie
                            finale kWh. Dans le cas d'un DPE immeuble ou
                            d'un DPE appartement à partir de l'immeuble
                            c'est la consommation de l'installation à
                            l'immeuble qu'il faut saisir.
                        conso_ch_depensier: consommation d'energie
                            annuelle de l'installation de chauffage pour
                            le scénario dépensier (scénario DH21) en
                            energie finale kWh. Dans le cas d'un DPE
                            immeuble ou d'un DPE appartement à partir de
                            l'immeuble c'est la consommation de
                            l'installation à l'immeuble qu'il faut
                            saisir.
                    """

                    besoin_ch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    besoin_ch_depensier: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    production_ch_solaire: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    fch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "max_inclusive": 1.0,
                            "nillable": True,
                        },
                    )
                    conso_ch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    conso_ch_depensier: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )

                @dataclass
                class EmetteurChauffageCollection:
                    emetteur_chauffage: List[
                        "Dpe.Logement.InstallationChauffageCollection.InstallationChauffage.EmetteurChauffageCollection.EmetteurChauffage"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                        },
                    )

                    @dataclass
                    class EmetteurChauffage:
                        donnee_entree: Optional[
                            "Dpe.Logement.InstallationChauffageCollection.InstallationChauffage.EmetteurChauffageCollection.EmetteurChauffage.DonneeEntree"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )
                        donnee_intermediaire: Optional[
                            "Dpe.Logement.InstallationChauffageCollection.InstallationChauffage.EmetteurChauffageCollection.EmetteurChauffage.DonneeIntermediaire"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )

                        @dataclass
                        class DonneeEntree:
                            """
                            Attributes:
                                description: description textuelle de
                                    l'objet
                                reference: reference projet de l'objet
                                    (cette référence permet de faire
                                    d'éventuels liens entre objets). La
                                    codification et utilisation des
                                    références peut différer entre
                                    logiciels
                                surface_chauffee: surface chauffée par
                                    l'emetteur (sous ensemble de la
                                    surface chauffée par
                                    l'installation). Dans le cas d'un
                                    DPE immeuble ou d'un DPE appartement
                                    à partir de l'immeuble c'est la
                                    surface de l'installation à
                                    l'immeuble qu'il faut renseigner
                                tv_rendement_emission_id: id de la ligne
                                    de la table utilisée pour le calcul
                                    du rendement d'emission de
                                    l'émetteur de chauffage
                                tv_rendement_distribution_ch_id: id de
                                    la ligne de la table utilisée pour
                                    le calcul du rendement de
                                    distribution de la distribution
                                    associée à l'émission
                                tv_rendement_regulation_id: id de la
                                    ligne de la table utilisée pour le
                                    calcul du rendement de régulation
                                    associé à l'émission
                                enum_type_emission_distribution_id:
                                    enumérateur qui couple les notions
                                    d'emission et de distribution pour
                                    produire une description complète
                                    des emetteurs de chauffage
                                tv_intermittence_id: id de la ligne de
                                    la table utilisée pour le calcul du
                                    coefficient d'intermittence de
                                    l'installation I0
                                reseau_distribution_isole: est ce que le
                                    réseau de distribution est isolé 0 :
                                    non 1 : oui
                                enum_equipement_intermittence_id: type
                                    d'équipement d'intermittence associé
                                    à la génération
                                enum_type_regulation_id: type de
                                    régulation associée au générateur
                                enum_periode_installation_emetteur_id:
                                    période d'installation des émetteurs
                                    de chauffage (utilisé pour le calcul
                                    des températures de fonctionnement
                                    des systèmes à combustion de type
                                    chaudière gaz ou fioul)
                                enum_type_chauffage_id: type de
                                    chauffage : Central ou Divisé
                                enum_temp_distribution_ch_id:
                                    température de distribution de
                                    l'installation de chauffage (pour le
                                    calcul des auxiliaires de
                                    distribution)
                                enum_lien_generateur_emetteur_id: lien
                                    entre le générateur et l'émetteur
                                    associé
                            """

                            description: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            reference: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            surface_chauffee: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_exclusive": 0.0,
                                },
                            )
                            tv_rendement_emission_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 7,
                                },
                            )
                            tv_rendement_distribution_ch_id: Optional[int] = (
                                field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "required": True,
                                        "min_inclusive": 1,
                                        "max_inclusive": 12,
                                    },
                                )
                            )
                            tv_rendement_regulation_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 15,
                                },
                            )
                            enum_type_emission_distribution_id: Optional[
                                int
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 50,
                                },
                            )
                            tv_intermittence_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 188,
                                },
                            )
                            reseau_distribution_isole: Optional[SOuiNon] = (
                                field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "nillable": True,
                                    },
                                )
                            )
                            enum_equipement_intermittence_id: Optional[int] = (
                                field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "required": True,
                                        "min_inclusive": 1,
                                        "max_inclusive": 7,
                                    },
                                )
                            )
                            enum_type_regulation_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 2,
                                },
                            )
                            enum_periode_installation_emetteur_id: Optional[
                                int
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 3,
                                    "nillable": True,
                                },
                            )
                            enum_type_chauffage_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 2,
                                },
                            )
                            enum_temp_distribution_ch_id: Optional[int] = (
                                field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "required": True,
                                        "min_inclusive": 1,
                                        "max_inclusive": 4,
                                    },
                                )
                            )
                            enum_lien_generateur_emetteur_id: Optional[int] = (
                                field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "required": True,
                                        "min_inclusive": 1,
                                        "max_inclusive": 3,
                                    },
                                )
                            )

                        @dataclass
                        class DonneeIntermediaire:
                            """
                            Attributes:
                                i0: coefficient d'intermittence de
                                    l'installation
                                rendement_emission: Re : rendement
                                    d'émission du système de chauffage
                                    (0-1)
                                rendement_distribution: Rd : rendement
                                    de distribution du système de
                                    chauffage (0-1)
                                rendement_regulation: Rr : rendement de
                                    régulation du système de chauffage
                                    (0-1)
                            """

                            i0: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.2,
                                },
                            )
                            rendement_emission: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.0,
                                },
                            )
                            rendement_distribution: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.0,
                                },
                            )
                            rendement_regulation: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.0,
                                },
                            )

                @dataclass
                class GenerateurChauffageCollection:
                    generateur_chauffage: List[
                        "Dpe.Logement.InstallationChauffageCollection.InstallationChauffage.GenerateurChauffageCollection.GenerateurChauffage"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                        },
                    )

                    @dataclass
                    class GenerateurChauffage:
                        donnee_entree: Optional[
                            "Dpe.Logement.InstallationChauffageCollection.InstallationChauffage.GenerateurChauffageCollection.GenerateurChauffage.DonneeEntree"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )
                        donnee_intermediaire: Optional[
                            "Dpe.Logement.InstallationChauffageCollection.InstallationChauffage.GenerateurChauffageCollection.GenerateurChauffage.DonneeIntermediaire"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            },
                        )

                        @dataclass
                        class DonneeEntree:
                            """
                            Attributes:
                                description: description textuelle de
                                    l'objet
                                reference: reference projet de l'objet
                                    (cette référence permet de faire
                                    d'éventuels liens entre objets). La
                                    codification et utilisation des
                                    références peut différer entre
                                    logiciels
                                reference_generateur_mixte: référence
                                    commune pour un générateur mixte
                                    chauffage ECS. Cette référence est
                                    identique pour les deux parties du
                                    générateur (chauffage et ECS) et est
                                    utilisé pour faire le lien entre les
                                    deux
                                ref_produit_generateur_ch: référence
                                    produit et marque du générateur de
                                    chauffage
                                enum_type_generateur_ch_id: type de
                                    generateur de chauffage
                                enum_usage_generateur_id: usages assurés
                                    par le générateur
                                    (chauffage/ecs/chauffage+ecs)
                                enum_type_energie_id: type d'énergie
                                    consommée par le générateur de
                                    chauffage
                                position_volume_chauffe: est ce que le
                                    générateur est positionné dans le
                                    volume chauffé. (pour le calcul des
                                    pertes de génération récupérables)
                                tv_rendement_generation_id: id de la
                                    ligne de la table utilisée pour le
                                    calcul des rendements de générations
                                    forfaitaires des générateurs autres
                                    qu'à combustion
                                tv_scop_id: id de la ligne de la table
                                    utilisée pour le calcul du
                                    coefficient de performance du
                                    système thermodynamique (SCOP)
                                tv_temp_fonc_100_id: id de la ligne de
                                    la table utilisée pour le calcul de
                                    la température à 100% de charge du
                                    système à combustion(SUPPRIME)
                                tv_temp_fonc_30_id: id de la ligne de la
                                    table utilisée pour le calcul de la
                                    température à 30% de charge du
                                    système à combustion(SUPPRIME)
                                tv_generateur_combustion_id: id de la
                                    ligne de la table utilisée pour le
                                    calcul des paramètres du générateur
                                    à combustion Rpn,Rpint,Qp0,Pveil
                                tv_reseau_chaleur_id: id de la ligne de
                                    la table utilisée pour le calcul du
                                    contenu CO2 des réseaux de chaleurs
                                    (OBSOLETE et remplacé par
                                    identifiant_reseau_chaleur à partir
                                    du 18 janvier 2022 et la prise en
                                    compte du nouvel arrêté réseau de
                                    chaleur).
                                identifiant_reseau_chaleur: identifiant
                                    réseau de chaleur ou de froid
                                    utilisé (utilisé à partir du 18
                                    janvier 2022)
                                n_radiateurs_gaz: nombre de radiateurs
                                    gaz
                                priorite_generateur_cascade: ordre de
                                    priorité du générateur en cascade
                                    (ordonné de manière croissante 1 :
                                    générateur principal , 2: genérateur
                                    secondaire etc…). Dans le cas de
                                    deux générateurs en cascade sans
                                    priorité, les deux générateurs sont
                                    déclarés comme principal
                                presence_ventouse: présence d'un système
                                    de ventouse ou avec un ventilateur
                                    pour l'évacuation des fumées d'un
                                    système à combustion 0 : non 1 : oui
                                presence_regulation_combustion: présence
                                    d'un organe de régulation pour le
                                    système de chauffage à combustion 0
                                    : non 1 : oui
                                enum_methode_saisie_carac_sys_id:
                                    méthode de saisie des performances
                                    du système de chauffage
                                enum_lien_generateur_emetteur_id: lien
                                    entre le générateur et l'émetteur
                                    associé
                            """

                            description: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            reference: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            reference_generateur_mixte: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            ref_produit_generateur_ch: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            enum_type_generateur_ch_id: Optional[
                                DonneeEntreeEnumTypeGenerateurChId
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                },
                            )
                            enum_usage_generateur_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 3,
                                },
                            )
                            enum_type_energie_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 1,
                                    "max_inclusive": 15,
                                },
                            )
                            position_volume_chauffe: Optional[SOuiNon] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                },
                            )
                            tv_rendement_generation_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 31,
                                    "nillable": True,
                                },
                            )
                            tv_scop_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 88,
                                    "nillable": True,
                                },
                            )
                            tv_temp_fonc_100_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 9,
                                    "nillable": True,
                                },
                            )
                            tv_temp_fonc_30_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 36,
                                    "nillable": True,
                                },
                            )
                            tv_generateur_combustion_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 93,
                                    "nillable": True,
                                },
                            )
                            tv_reseau_chaleur_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 797,
                                    "nillable": True,
                                },
                            )
                            identifiant_reseau_chaleur: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "pattern": r"[0-9]{4}[C-F]",
                                    "nillable": True,
                                },
                            )
                            n_radiateurs_gaz: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0,
                                    "nillable": True,
                                },
                            )
                            priorite_generateur_cascade: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0,
                                    "nillable": True,
                                },
                            )
                            presence_ventouse: Optional[SOuiNon] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            presence_regulation_combustion: Optional[
                                SOuiNon
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            enum_methode_saisie_carac_sys_id: Optional[
                                DonneeEntreeEnumMethodeSaisieCaracSysId
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                },
                            )
                            enum_lien_generateur_emetteur_id: Optional[int] = (
                                field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "required": True,
                                        "min_inclusive": 1,
                                        "max_inclusive": 3,
                                    },
                                )
                            )

                        @dataclass
                        class DonneeIntermediaire:
                            """
                            Attributes:
                                scop: scop du générateur thermodynamique
                                    (en remplacement du Rg pour les
                                    générateurs thermodynamique) (0-20)
                                pn: puissance nominale du générateur à
                                    combustion (W)
                                qp0: pertes à l'arret du générateur à
                                    combustion. Dans le cas d'un
                                    générateur virtualisé pour DPE
                                    appartement avec chauffage collectif
                                    saisir Qp0 correspondant à Pe =
                                    a*Pn(collectif) (W)
                                pveilleuse: puissance de la veilleuse du
                                    générateur à combustion (W)
                                temp_fonc_30: température de
                                    fonctionnement à 30% de charge (°C)
                                temp_fonc_100: température de
                                    fonctionnement à 100% de charge (°C)
                                rpn: rendement de génération à pleine
                                    charge du générateur à combustion
                                    (0-1,5)
                                rpint: rendement de génération à charge
                                    intermédiaire du générateur à
                                    combustion (0-1,5)
                                rendement_generation: Rg : rendement de
                                    génération du système de chauffage
                                    pour tous les générateurs sauf
                                    thermodynamique. Pour les
                                    générateurs à combustion il faut
                                    saisir le rendement sur PCI (0-1,5)
                                conso_ch: consommation d'energie
                                    annuelle du générateur de chauffage
                                    en energie finale kWh (exprimée en
                                    kWh PCI pour les combustibles). Dans
                                    le cas d'un DPE immeuble ou d'un DPE
                                    appartement à partir de l'immeuble
                                    c'est la consommation du générateur
                                    à l'immeuble qu'il faut saisir.
                                conso_ch_depensier: consommation
                                    d'énergie annuelle du générateur de
                                    chauffage pour le scénario dépensier
                                    (scénario DH21) en energie finale
                                    kWh (exprimée en kWh PCI pour les
                                    combustibles). Dans le cas d'un DPE
                                    immeuble ou d'un DPE appartement à
                                    partir de l'immeuble c'est la
                                    consommation du générateur à
                                    l'immeuble qu'il faut saisir.
                            """

                            scop: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 1.0,
                                    "max_inclusive": 8.0,
                                    "nillable": True,
                                },
                            )
                            pn: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 100.0,
                                    "nillable": True,
                                },
                            )
                            qp0: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            pveilleuse: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            temp_fonc_30: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            temp_fonc_100: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            rpn: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.5,
                                    "nillable": True,
                                },
                            )
                            rpint: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.5,
                                    "nillable": True,
                                },
                            )
                            rendement_generation: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 0.0,
                                    "max_inclusive": 1.5,
                                    "nillable": True,
                                },
                            )
                            conso_ch: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 0.0,
                                },
                            )
                            conso_ch_depensier: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "required": True,
                                    "min_inclusive": 0.0,
                                },
                            )

        @dataclass
        class Sortie:
            deperdition: Optional["Dpe.Logement.Sortie.Deperdition"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            apport_et_besoin: Optional[
                "Dpe.Logement.Sortie.ApportEtBesoin"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            ef_conso: Optional["Dpe.Logement.Sortie.EfConso"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            ep_conso: Optional["Dpe.Logement.Sortie.EpConso"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            emission_ges: Optional["Dpe.Logement.Sortie.EmissionGes"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            cout: Optional["Dpe.Logement.Sortie.Cout"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            production_electricite: Optional[
                "Dpe.Logement.Sortie.ProductionElectricite"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            sortie_par_energie_collection: Optional[
                "Dpe.Logement.Sortie.SortieParEnergieCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            confort_ete: Optional["Dpe.Logement.Sortie.ConfortEte"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
            qualite_isolation: Optional[
                "Dpe.Logement.Sortie.QualiteIsolation"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )

            @dataclass
            class Deperdition:
                """
                Attributes:
                    hvent: part des deperditions de renouvellement d'air
                        liées au système de(W/K) ventilation. Pour les
                        DPE immeubles et appartement à partir de
                        l'immeuble ces données sont à l'immeuble.
                    hperm: part des deperditions de renouvellement d'air
                        liées à la perméabilité à l'air du
                        bâtiment(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_renouvellement_air: deperditions par
                        renouvellement d'air totale (hvent +
                        hperm)(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_mur: deperditions par les murs(W/K).
                        Pour les DPE immeubles et appartement à partir
                        de l'immeuble ces données sont à l'immeuble.
                    deperdition_plancher_bas: deperditions par les
                        planchers bas(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_plancher_haut: deperditions par les
                        planchers hauts(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_baie_vitree: deperditions par les baies
                        vitrées (W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_porte: deperditions par les ponts
                        thermiques(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_pont_thermique: deperditions par les
                        ponts thermiques(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_enveloppe: deperditions par l'enveloppe
                        (GV). Pour les DPE immeubles et appartement à
                        partir de l'immeuble ces données sont à
                        l'immeuble.
                """

                hvent: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                hperm: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                deperdition_renouvellement_air: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                deperdition_mur: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                deperdition_plancher_bas: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                deperdition_plancher_haut: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                deperdition_baie_vitree: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                deperdition_porte: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                deperdition_pont_thermique: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                deperdition_enveloppe: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )

            @dataclass
            class ApportEtBesoin:
                """
                Attributes:
                    surface_sud_equivalente: surface sud équivalente.
                        Pour les DPE immeubles et appartement à partir
                        de l'immeuble ces données sont à l'immeuble.
                    apport_solaire_fr: apports solaires totaux durant la
                        saison de froid As (kWh). Pour les DPE immeubles
                        et appartement à partir de l'immeuble ces
                        données sont à l'immeuble.
                    apport_interne_fr: apports internes totaux durant la
                        saison de froid Ai (kWh). Pour les DPE immeubles
                        et appartement à partir de l'immeuble ces
                        données sont à l'immeuble.
                    apport_solaire_ch: apports solaires totaux durant la
                        saison de chauffe As (kWh). Pour les DPE
                        immeubles et appartement à partir de l'immeuble
                        ces données sont à l'immeuble.
                    apport_interne_ch: apports internes totaux durant la
                        saison de chauffe Ai (kWh). Pour les DPE
                        immeubles et appartement à partir de l'immeuble
                        ces données sont à l'immeuble.
                    fraction_apport_gratuit_ch: fraction des apports
                        gratuits sur la saison de chauffe F. Pour les
                        DPE immeubles et appartement à partir de
                        l'immeuble ces données sont à l'immeuble.
                    fraction_apport_gratuit_depensier_ch: fraction des
                        apports gratuits sur la saison de chauffe F pour
                        le scénario dépensier (DH21). Pour les DPE
                        immeubles et appartement à partir de l'immeuble
                        ces données sont à l'immeuble.
                    pertes_distribution_ecs_recup: pertes de
                        distribution d'ECS récupérées(kWh). Pour les DPE
                        immeubles et appartement à partir de l'immeuble
                        ces données sont à l'immeuble.
                    pertes_distribution_ecs_recup_depensier: pertes de
                        distribution d'ECS récupérées(kWh) pour le
                        scénario dépensier. Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    pertes_stockage_ecs_recup: pertes de stockage d'ECS
                        récupérées(kWh). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    pertes_generateur_ch_recup: pertes des générateurs
                        de chauffage récupérées(kWh). Pour les DPE
                        immeubles et appartement à partir de l'immeuble
                        ces données sont à l'immeuble.
                    pertes_generateur_ch_recup_depensier: pertes des
                        générateurs de chauffage récupérées(kWh) pour le
                        scénario dépensier. Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    nadeq: nombre d'adulte équivalent calculés pour le
                        besoin d'ECS. Pour les DPE immeubles ces données
                        sont à l'immeuble. Pour les dpe appartements à
                        partir de l'immeuble ces données sont à
                        l'appartement
                    v40_ecs_journalier: consommation en l d'ecs à 40°C
                        sur une journée. Pour les DPE immeubles ces
                        données sont à l'immeuble. Pour les dpe
                        appartements à partir de l'immeuble ces données
                        sont à l'appartement
                    v40_ecs_journalier_depensier: consommation en l
                        d'ecs à 40°C sur une journée scénario dépensier.
                        Pour les DPE immeubles ces données sont à
                        l'immeuble. Pour les dpe appartements à partir
                        de l'immeuble ces données sont à l'appartement
                    besoin_ch: besoin de chauffage annuel total du
                        logement ou immeuble (kWh) . Pour les DPE
                        immeubles ces données sont à l'immeuble. Pour
                        les dpe appartements à partir de l'immeuble ces
                        données sont à l'appartement
                    besoin_ch_depensier: besoin de chauffage total du
                        bâtiment pour le scénario dépensier (kWh)
                        (DH21). Pour les DPE immeubles ces données sont
                        à l'immeuble. Pour les dpe appartements à partir
                        de l'immeuble ces données sont à l'appartement
                    besoin_ecs: besoin d'ecs annuel total du bâtiment
                        (kWh). Pour les DPE immeubles ces données sont à
                        l'immeuble. Pour les dpe appartements à partir
                        de l'immeuble ces données sont à l'appartement
                    besoin_ecs_depensier: besoin d'ecs total du bâtiment
                        pour le scénario dépensier (kWh). Pour les DPE
                        immeubles ces données sont à l'immeuble. Pour
                        les dpe appartements à partir de l'immeuble ces
                        données sont à l'appartement
                    besoin_fr: besoin de refroidissement annuel
                        (kWh).Pour les DPE immeubles ces données sont à
                        l'immeuble. Pour les dpe appartements à partir
                        de l'immeuble ces données sont à l'appartement
                    besoin_fr_depensier: besoin de refroidissement
                        annuel pour le scénario dépensier (kWh). Pour
                        les DPE immeubles ces données sont à l'immeuble.
                        Pour les dpe appartements à partir de l'immeuble
                        ces données sont à l'appartement
                """

                surface_sud_equivalente: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                apport_solaire_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                apport_interne_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                apport_solaire_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                apport_interne_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                fraction_apport_gratuit_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                fraction_apport_gratuit_depensier_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                pertes_distribution_ecs_recup: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                pertes_distribution_ecs_recup_depensier: Optional[float] = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                )
                pertes_stockage_ecs_recup: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                pertes_generateur_ch_recup: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                pertes_generateur_ch_recup_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                nadeq: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                v40_ecs_journalier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                v40_ecs_journalier_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                besoin_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                besoin_ch_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                besoin_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                besoin_ecs_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                besoin_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                besoin_fr_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )

            @dataclass
            class EfConso:
                """
                Attributes:
                    conso_ch: consommation annuelle de chauffage en
                        energie finale (déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_ch_depensier: consommation annuelle de
                        chauffage en energie finale pour le scénario
                        dépensier(déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_ecs: consommation annuelle d'ECS en energie
                        finale (déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_ecs_depensier: consommation annuelle d'ECS en
                        energie finale pour le scénario dépensier
                        (déduit de la production pv autoconsommée)
                        (kWhef/an)
                    conso_eclairage: consommation annuelle d'eclairage
                        en energie finale (déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_auxiliaire_generation_ch: consommation
                        annuelle d'auxilliaires de génération de
                        chauffage en energie finale (kWhef/an)
                    conso_auxiliaire_generation_ch_depensier:
                        consommation annuelle d'auxilliaires de
                        génération de chauffage en energie finale pour
                        le scénario dépensier (kWhef/an)
                    conso_auxiliaire_distribution_ch: consommation
                        annuelle d'auxilliaires de distribution de
                        chauffage en energie finale (kWhef/an)
                    conso_auxiliaire_generation_ecs: consommation
                        annuelle d'auxillaires de generation d'ECS en
                        energie finale (kWhef/an)
                    conso_auxiliaire_generation_ecs_depensier:
                        consommation annuelle d'auxillaires de
                        generation d'ECS en energie finale pour le
                        scénario dépensier (kWhef/an)
                    conso_auxiliaire_distribution_ecs: consommation
                        annuelle d'auxilliaires de distribution d'ECS en
                        energie finale (kWhef/an)
                    conso_auxiliaire_distribution_fr: consommation
                        annuelle d'auxilliaires de distribution de froid
                        en energie finale (kWhef/an)
                    conso_auxiliaire_ventilation: consommation annuelle
                        d'auxilliaires de ventilation en energie finale
                        (kWhef/an)
                    conso_totale_auxiliaire: consommation annuelle de
                        l'ensemble des auxiliaires en énergie
                        finale(déduit de la production pv autoconsommée)
                        (kWhef/an)
                    conso_fr: consommation de refroidissement annuel en
                        energie finale (déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_fr_depensier: consommation de refroidissement
                        annuel en energie finale pour le scénario
                        dépensier (déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_5_usages: consommation annuelle 5 usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)en
                        energie finale(déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_5_usages_m2: consommation annuelle 5 usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)en
                        energie finale(déduit de la production pv
                        autoconsommée) (kWhef/m²/an)
                """

                conso_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_ch_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_ecs_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_eclairage: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                conso_auxiliaire_generation_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_auxiliaire_generation_ch_depensier: Optional[float] = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                )
                conso_auxiliaire_distribution_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_auxiliaire_generation_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_auxiliaire_generation_ecs_depensier: Optional[float] = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                )
                conso_auxiliaire_distribution_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_auxiliaire_distribution_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                conso_auxiliaire_ventilation: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_totale_auxiliaire: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_fr_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_5_usages: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                conso_5_usages_m2: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )

            @dataclass
            class EpConso:
                """
                Attributes:
                    ep_conso_ch: consommation annuelle de chauffage en
                        energie primaire(déduit de la production pv
                        autoconsommée) (kWhep/an)
                    ep_conso_ch_depensier: consommation annuelle de
                        chauffage en energie primaire pour le scénario
                        dépensier (déduit de la production pv
                        autoconsommée) (kWhep/an)
                    ep_conso_ecs: consommation annuelle d'ECS en energie
                        primaire (déduit de la production pv
                        autoconsommée) (kWhep/an)
                    ep_conso_ecs_depensier: consommation annuelle d'ECS
                        en energie primaire pour le scénario dépensier
                        (déduit de la production pv autoconsommée)
                        (kWhep/an)
                    ep_conso_eclairage: consommation annuelle
                        d'eclairage en energie primaire (déduit de la
                        production pv autoconsommée) (kWhep/an)
                    ep_conso_auxiliaire_generation_ch: consommation
                        annuelle d'auxilliaires de génération de
                        chauffage en energie primaire (kWhep/an)
                    ep_conso_auxiliaire_generation_ch_depensier:
                        consommation annuelle d'auxilliaires de
                        génération de chauffage en energie primaire pour
                        le scénario dépensier (kWhep/an)
                    ep_conso_auxiliaire_distribution_ch: consommation
                        annuelle d'auxilliaires de distribution de
                        chauffage en energie primaire (kWhep/an)
                    ep_conso_auxiliaire_generation_ecs: consommation
                        annuelle d'auxillaires de generation d'ECS en
                        energie primaire (kWhep/an)
                    ep_conso_auxiliaire_generation_ecs_depensier:
                        consommation annuelle d'auxillaires de
                        generation d'ECS en energie primaire pour le
                        scénario dépensier (kWhep/an)
                    ep_conso_auxiliaire_distribution_ecs: consommation
                        annuelle d'auxilliaires de distribution d'ECS en
                        energie primaire (kWhep/an)
                    ep_conso_auxiliaire_distribution_fr: consommation
                        annuelle d'auxilliaires de distribution de froid
                        en energie primaire (kWhep/an) SUPPRIME
                    ep_conso_auxiliaire_ventilation: consommation
                        annuelle d'auxilliaires de ventilation en
                        energie primaire (kWhep/an)
                    ep_conso_totale_auxiliaire: consommation annuelle de
                        l'ensemble des auxiliaires en energie primaire
                        (déduit de la production pv autoconsommée)
                        (kWhep/an)
                    ep_conso_fr: consommation de refroidissement annuel
                        en énergie primaire (déduit de la production pv
                        autoconsommée) (kWhep/an)
                    ep_conso_fr_depensier: consommation de
                        refroidissement annuel en énergie primaire pour
                        le scénario dépensier (déduit de la production
                        pv autoconsommée) (kWhep/an)
                    ep_conso_5_usages: consommation annuelle 5 usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)en
                        energie primaire (déduit de la production pv
                        autoconsommée) (kWhep/an)
                    ep_conso_5_usages_m2: consommation annuelle 5 usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)en
                        energie primaire (déduit de la production pv
                        autoconsommée) (kWhep/m²/an)
                    classe_bilan_dpe: Classe du DPE issu de la synthèse
                        du double seuil sur les consommations énergie
                        primaire et les émissions de CO2 sur les 5
                        usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)
                """

                ep_conso_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_ch_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_ecs_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_eclairage: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                ep_conso_auxiliaire_generation_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_auxiliaire_generation_ch_depensier: Optional[
                    float
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_auxiliaire_distribution_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_auxiliaire_generation_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_auxiliaire_generation_ecs_depensier: Optional[
                    float
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_auxiliaire_distribution_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_auxiliaire_distribution_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                ep_conso_auxiliaire_ventilation: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_totale_auxiliaire: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_fr_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_5_usages: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                ep_conso_5_usages_m2: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                classe_bilan_dpe: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"[A-G]",
                    },
                )

            @dataclass
            class EmissionGes:
                """
                Attributes:
                    emission_ges_ch: estimation GES de chauffage (déduit
                        de la production pv autoconsommée) (kgCO2/an)
                    emission_ges_ch_depensier: estimation GES de
                        chauffage pour le scénario dépensier(déduit de
                        la production pv autoconsommée) (kgCO2/an)
                    emission_ges_ecs: estimation GES d'ECS (déduit de la
                        production pv autoconsommée) (kgCO2/an)
                    emission_ges_ecs_depensier: estimation GES d'ECS
                        pour le scénario dépensier (déduit de la
                        production pv autoconsommée) (kgCO2/an)
                    emission_ges_eclairage: estimation GES d'eclairage
                        (déduit de la production pv autoconsommée)
                        (kgCO2/an)
                    emission_ges_auxiliaire_generation_ch: estimation
                        GES d'auxilliaires de génération de chauffage
                        (kgCO2/an)
                    emission_ges_auxiliaire_generation_ch_depensier:
                        estimation GES d'auxilliaires de génération de
                        chauffage pour le scénario dépensier (kgCO2/an)
                    emission_ges_auxiliaire_distribution_ch: estimation
                        GES d'auxilliaires de distribution de chauffage
                        (kgCO2/an)
                    emission_ges_auxiliaire_generation_ecs: estimation
                        GES d'auxillaires de generation d'ECS (kgCO2/an)
                    emission_ges_auxiliaire_generation_ecs_depensier:
                        estimation GES d'auxillaires de generation d'ECS
                        pour le scénario dépensier (kgCO2/an)
                    emission_ges_auxiliaire_distribution_ecs: estimation
                        GES d'auxilliaires de distribution d'ECS
                        (kgCO2/an)
                    emission_ges_auxiliaire_distribution_fr: estimation
                        GES d'auxilliaires de distribution de froid
                        (kgCO2/an) SUPPRIME
                    emission_ges_auxiliaire_ventilation: estimation GES
                        d'auxilliaires de ventilation (kgCO2/an)
                    emission_ges_totale_auxiliaire: estimation GES de
                        l'ensemble des auxiliaires (déduit de la
                        production pv autoconsommée) (kgCO2/an)
                    emission_ges_fr: estimation GES de refroidissement
                        annuel (déduit de la production pv
                        autoconsommée) (kgCO2/an)
                    emission_ges_fr_depensier: estimation GES de
                        refroidissement pour le scénario dépensier
                        (déduit de la production pv autoconsommée)
                        (kgCO2/an)
                    emission_ges_5_usages: estimation GES totale 5
                        usages (déduit de la production pv
                        autoconsommée)
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/an)
                    emission_ges_5_usages_m2: estimation GES totale 5
                        usages rapportée au m² (déduit de la production
                        pv autoconsommée)
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an)
                    classe_emission_ges: classe d'estimation ges du DPE
                        5 usages
                """

                emission_ges_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_ch_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_ecs_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_eclairage: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                emission_ges_auxiliaire_generation_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_auxiliaire_generation_ch_depensier: Optional[
                    float
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_auxiliaire_distribution_ch: Optional[float] = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                )
                emission_ges_auxiliaire_generation_ecs: Optional[float] = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                )
                emission_ges_auxiliaire_generation_ecs_depensier: Optional[
                    float
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_auxiliaire_distribution_ecs: Optional[float] = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                )
                emission_ges_auxiliaire_distribution_fr: Optional[float] = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 0.0,
                            "nillable": True,
                        },
                    )
                )
                emission_ges_auxiliaire_ventilation: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_totale_auxiliaire: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_fr_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_5_usages: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_5_usages_m2: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                classe_emission_ges: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"[A-G]",
                    },
                )

            @dataclass
            class Cout:
                """
                Attributes:
                    cout_ch: coût de chauffage(déduit de la production
                        pv autoconsommée) (€)
                    cout_ch_depensier: coût de chauffage pour le
                        scénario dépensier (déduit de la production pv
                        autoconsommée) (€)
                    cout_ecs: coût de l'ECS (déduit de la production pv
                        autoconsommée) (€)
                    cout_ecs_depensier: coût de l'ECS pour le scénario
                        dépensier (déduit de la production pv
                        autoconsommée) (€)
                    cout_eclairage: coût des eclairage (déduit de la
                        production pv autoconsommée) (€)
                    cout_auxiliaire_generation_ch: coût des auxilliaires
                        de génération de chauffage (€)
                    cout_auxiliaire_generation_ch_depensier: coût des
                        auxilliaires de génération de chauffage pour le
                        scénario dépensier (€)
                    cout_auxiliaire_distribution_ch: coût des
                        auxilliaires de distribution de chauffage (€)
                    cout_auxiliaire_generation_ecs: coût des auxillaires
                        de generation de l'ECS (€)
                    cout_auxiliaire_generation_ecs_depensier: coût des
                        auxillaires de generation de l'ECS pour le
                        scénario dépensier (€)
                    cout_auxiliaire_distribution_ecs: coût des
                        auxilliaires de distribution de l'ECS (€)
                    cout_auxiliaire_distribution_fr: coût des
                        auxilliaires de distribution de froid (€)
                        SUPPRIME
                    cout_auxiliaire_ventilation: coût des auxilliaires
                        de ventilation (€)
                    cout_total_auxiliaire: coût des auxilliaires de
                        l'ensemble des auxiliaires (déduit de la
                        production pv autoconsommée) (€)
                    cout_fr: coût de refroidissement annuel (déduit de
                        la production pv autoconsommée) (€)
                    cout_fr_depensier: coût de refroidissement pour le
                        scénario dépensier (déduit de la production pv
                        autoconsommée) (€)
                    cout_5_usages: coût totale 5 usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)
                        (déduit de la production pv autoconsommée) (€)
                """

                cout_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_ch_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_ecs_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_eclairage: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                cout_auxiliaire_generation_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_auxiliaire_generation_ch_depensier: Optional[float] = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                )
                cout_auxiliaire_distribution_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_auxiliaire_generation_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_auxiliaire_generation_ecs_depensier: Optional[float] = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                )
                cout_auxiliaire_distribution_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_auxiliaire_distribution_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                cout_auxiliaire_ventilation: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_total_auxiliaire: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_fr_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_5_usages: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )

            @dataclass
            class ProductionElectricite:
                """
                Attributes:
                    production_pv: production d'éléctricité
                        photovoltaique(kWhep/an)
                    conso_elec_ac: éléctricité photovoltaique
                        autoconsommée(kWhep/an)
                    conso_elec_ac_ch: éléctricité photovoltaique
                        autoconsommée pour l'usage chauffage (les
                        consommations finales sont déduites de cette
                        valeur) (kWhep/an)
                    conso_elec_ac_ecs: éléctricité photovoltaique
                        autoconsommée pour l'usage ecs (les
                        consommations finales sont déduites de cette
                        valeur) (kWhep/an)
                    conso_elec_ac_fr: éléctricité photovoltaique
                        autoconsommée pour l'usage climatisation (les
                        consommations finales sont déduites de cette
                        valeur) (kWhep/an)
                    conso_elec_ac_eclairage: éléctricité photovoltaique
                        autoconsommée pour l'usage eclairage (les
                        consommations finales sont déduites de cette
                        valeur) (kWhep/an)
                    conso_elec_ac_auxiliaire: éléctricité photovoltaique
                        autoconsommée pour l'usage auxiliaire (les
                        consommations finales sont déduites de cette
                        valeur) (kWhep/an)
                    conso_elec_ac_autre_usage: éléctricité
                        photovoltaique autoconsommée pour les autres
                        usages de l'éléctricité (kWhep/an)
                """

                production_pv: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_elec_ac: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_elec_ac_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_elec_ac_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_elec_ac_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_elec_ac_eclairage: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_elec_ac_auxiliaire: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_elec_ac_autre_usage: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )

            @dataclass
            class SortieParEnergieCollection:
                sortie_par_energie: List[
                    "Dpe.Logement.Sortie.SortieParEnergieCollection.SortieParEnergie"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                    },
                )

                @dataclass
                class SortieParEnergie:
                    """
                    Attributes:
                        enum_type_energie_id: type d'énergie
                        conso_ch: consommation de chauffage en énergie
                            finale pour l'énergie considérée (kWhef/an)
                        conso_ecs: consommation d'ECS en énergie finale
                            pour l'énergie considérée (kWhef/an)
                        conso_5_usages: consommation totale en énergie
                            finale pour l'énergie considérée (kWhef/an)
                        emission_ges_ch: estimation GES de chauffage
                            pour l'énergie considérée (kgCO2/an)
                        emission_ges_ecs: estimation GES d'ECS pour
                            l'énergie considérée (kgCO2/an)
                        emission_ges_5_usages: estimation GES totale
                            pour l'énergie considérée (kgCO2/an)
                        cout_ch: coût lié au chauffage pour l'énergie
                            considérée (€)
                        cout_ecs: coût lié à l'ECS pour l'énergie
                            considérée (€)
                        cout_5_usages: coût totale pour l'énergie
                            considérée (€)
                    """

                    enum_type_energie_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 15,
                        },
                    )
                    conso_ch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    conso_ecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    conso_5_usages: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_exclusive": 0.0,
                        },
                    )
                    emission_ges_ch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    emission_ges_ecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    emission_ges_5_usages: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    cout_ch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    cout_ecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    cout_5_usages: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )

            @dataclass
            class ConfortEte:
                """
                Attributes:
                    isolation_toiture: as-t-on une isolation de toiture
                        0 : non 1 : oui
                    protection_solaire_exterieure: as-t-on une
                        protection solair exteriaire sur les facades
                        vitrées (exception nord) 0 : non 1 : oui
                    aspect_traversant: est ce que le logement est
                        traversant 0 : non 1 : oui
                    brasseur_air: est ce que le logement est équipé de
                        brasseurs d'air 0 : non 1 : oui
                    inertie_lourde: est ce que le logement possède une
                        inerte lourde ou très lourde 0 : non 1 : oui
                    enum_indicateur_confort_ete_id: indicateur confort
                        été (bon moyen ou mauvais)
                """

                isolation_toiture: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                protection_solaire_exterieure: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                aspect_traversant: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                brasseur_air: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                inertie_lourde: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                enum_indicateur_confort_ete_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 3,
                    },
                )

            @dataclass
            class QualiteIsolation:
                """
                Attributes:
                    ubat: Ubat(W/m²K)
                    qualite_isol_enveloppe: qualité d'isolation de
                        l'enveloppe
                    qualite_isol_mur: qualité d'isolation des murs
                    qualite_isol_plancher_haut_toit_terrasse: qualité
                        d'isolation de la toiture/planchers hauts partie
                        toit terrasse
                    qualite_isol_plancher_haut_comble_perdu: qualité
                        d'isolation de la toiture/planchers hauts partie
                        comble perdue
                    qualite_isol_plancher_haut_comble_amenage: qualité
                        d'isolation de la toiture/planchers hauts partie
                        comble aménagé
                    qualite_isol_plancher_bas: qualité de l'isolation
                        des planchers
                    qualite_isol_menuiserie: qualité d'isolation des
                        menuiseries
                """

                ubat: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                qualite_isol_enveloppe: Optional[SQualite] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                qualite_isol_mur: Optional[SQualite] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                qualite_isol_plancher_haut_toit_terrasse: Optional[
                    SQualite
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                qualite_isol_plancher_haut_comble_perdu: Optional[SQualite] = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                )
                qualite_isol_plancher_haut_comble_amenage: Optional[
                    SQualite
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                qualite_isol_plancher_bas: Optional[SQualite] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                qualite_isol_menuiserie: Optional[SQualite] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )

    @dataclass
    class Tertiaire:
        """
        Attributes:
            caracteristique_generale: Caractéristiques Générales du DPE
                Tertiaire
            bilan_consommation: bilan consommation
            consommation_collection: consommations par usage et energie
        """

        caracteristique_generale: Optional[
            "Dpe.Tertiaire.CaracteristiqueGenerale"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        bilan_consommation: Optional["Dpe.Tertiaire.BilanConsommation"] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
        )
        consommation_collection: Optional[
            "Dpe.Tertiaire.ConsommationCollection"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

        @dataclass
        class CaracteristiqueGenerale:
            """
            Attributes:
                enum_usage_fonctionnel_batiment_id: type d'usage
                    fonctionnel du batiment tertiaire ou batiment
                    recevant du public
                enum_categorie_erp_id: categorie d'ERP
                enum_methode_application_dpe_ter_id: methode
                    d'application du DPE tertiaire (facture, vierge ou
                    neuf)
                surface_utile: surface de référence utile du bâtiment
                    auquelle la consommation est rapportée
                shon: surface hors œuvre nette du bâtiment
                nombre_occupant: nombre d'occupants du bâtiment
                    tertiaire
                enum_periode_construction_id: période de construction
                annee_construction: annee de construction
            """

            enum_usage_fonctionnel_batiment_id: Optional[
                CaracteristiqueGeneraleEnumUsageFonctionnelBatimentId
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            enum_categorie_erp_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_inclusive": 1,
                    "max_inclusive": 5,
                    "nillable": True,
                },
            )
            enum_methode_application_dpe_ter_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 8,
                },
            )
            surface_utile: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_exclusive": 0.0,
                },
            )
            shon: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0.0,
                    "nillable": True,
                },
            )
            nombre_occupant: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_inclusive": 0,
                    "nillable": True,
                },
            )
            enum_periode_construction_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                },
            )
            annee_construction: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_inclusive": "700",
                    "max_inclusive": "2100",
                    "pattern": r"[0-9]{4}",
                    "nillable": True,
                },
            )

        @dataclass
        class BilanConsommation:
            """
            Attributes:
                classe_conso_energie: classe de consommation d'energie
                    suivant le referentiel DPE 2006 (energie primaire)
                classe_emission_ges: classe d'estimation ges suivant le
                    referentiel DPE 2006
                conso_energie_primaire: consommation d'énergie primaire
                    totale rapportée à la surface (kWhep/m²/an)
                emission_ges: estimation ges totale rapportée à la
                    surface (kgCO2/m²/an)
            """

            classe_conso_energie: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "pattern": r"[A-I]",
                },
            )
            classe_emission_ges: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "pattern": r"[A-I]",
                },
            )
            conso_energie_primaire: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            emission_ges: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )

        @dataclass
        class ConsommationCollection:
            consommation: List[
                "Dpe.Tertiaire.ConsommationCollection.Consommation"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

            @dataclass
            class Consommation:
                """
                Attributes:
                    conso_energie_finale: consommation d'energie finale
                        du poste de consommation en kWh
                    conso_energie_primaire: consommation d'energie
                        primaire du poste de consommation en kWhep
                    enum_type_usage_id: type d'usage associé à la
                        consommation
                    enum_type_energie_id: type d'énergie associée à la
                        consommaton
                    frais_annuels_energie: frais d'energies associés à
                        la consommation (en euros)
                    annee_consommation: année de relève de la
                        consommation/production electricité
                """

                conso_energie_finale: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                conso_energie_primaire: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                enum_type_usage_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 16,
                    },
                )
                enum_type_energie_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 15,
                    },
                )
                frais_annuels_energie: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                annee_consommation: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_exclusive": 2000,
                        "nillable": True,
                    },
                )

    @dataclass
    class LogementNeuf:
        repartition_chauffage: Optional[
            "Dpe.LogementNeuf.RepartitionChauffage"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
        repartition_ecs: Optional["Dpe.LogementNeuf.RepartitionEcs"] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
        caracteristique_generale: Optional[
            "Dpe.LogementNeuf.CaracteristiqueGenerale"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        meteo: Optional["Dpe.LogementNeuf.Meteo"] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
        enveloppe: Optional["Dpe.LogementNeuf.Enveloppe"] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
        ventilation_collection: Optional[
            "Dpe.LogementNeuf.VentilationCollection"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
        climatisation_collection: Optional[
            "Dpe.LogementNeuf.ClimatisationCollection"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
        production_elec_enr: Optional["Dpe.LogementNeuf.ProductionElecEnr"] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
        )
        installation_ecs_collection: Optional[
            "Dpe.LogementNeuf.InstallationEcsCollection"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
        installation_chauffage_collection: Optional[
            "Dpe.LogementNeuf.InstallationChauffageCollection"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
        sortie: Optional["Dpe.LogementNeuf.Sortie"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        rset: Optional["Dpe.LogementNeuf.Rset"] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )
        rsee: Optional["Dpe.LogementNeuf.Rsee"] = field(
            default=None,
            metadata={
                "type": "Element",
                "nillable": True,
            },
        )

        @dataclass
        class RepartitionChauffage:
            """
            Attributes:
                surface_baie_nord: surface des baies du logement
                    orientées nord
                surface_baie_sud: surface des baies du logement
                    orientées sud
                surface_baie_est_ouest: surface des baies du logement
                    orientées est ou ouest
                surface_paroi_verticale_ext: surface des parois
                    verticales donnant sur l'extérieur
                surface_plancher_haut: surface des planchers hauts du
                    logement
                surface_plancher_bas: surface des planchers bas du
                    logement
                coef_ifc: coefficient d'individualisation des frais de
                    chauffage dans le cas d'un DPE appartement calculé à
                    partir d'un DPE immeuble
                deperdition_totale_logement: calcul de deperdition
                    logement pour de la clé de répartition de chauffage
                deperdition_totale_batiment: calcul de deperdition
                    batiment pour de la clé de répartition de chauffage
                cle_repartition_ch: clé de répartition de chauffage à
                    appliquer au logement
            """

            surface_baie_nord: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 0.0,
                },
            )
            surface_baie_sud: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 0.0,
                },
            )
            surface_baie_est_ouest: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 0.0,
                },
            )
            surface_paroi_verticale_ext: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 0.0,
                },
            )
            surface_plancher_haut: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 0.0,
                },
            )
            surface_plancher_bas: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 0.0,
                },
            )
            coef_ifc: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 0.0,
                },
            )
            deperdition_totale_logement: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 0.0,
                },
            )
            deperdition_totale_batiment: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 0.0,
                },
            )
            cle_repartition_ch: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_exclusive": 0.0,
                },
            )

        @dataclass
        class RepartitionEcs:
            """
            Attributes:
                besoin_ecs_batiment: besoin d'ECS du bâtiment calculé
                    pour la clé de répartition d'ECS
                besoin_ecs_logement: besoin d'ECS du logement calculé
                    pour la clé de répartition d'ECS
                cle_repartition_ecs: clé de répartition de l'ECS
            """

            besoin_ecs_batiment: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_exclusive": 0.0,
                },
            )
            besoin_ecs_logement: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_exclusive": 0.0,
                },
            )
            cle_repartition_ecs: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_exclusive": 0.0,
                },
            )

        @dataclass
        class CaracteristiqueGenerale:
            """
            Attributes:
                annee_construction: annee de construction
                enum_periode_construction_id: période de construction
                enum_methode_application_dpe_log_id: méthode
                    d'application du DPE logement
                surface_habitable_logement: surface habitable du
                    logement renseignée sauf dans le cas du dpe à
                    l'immeuble
                nombre_niveau_immeuble: nombre de niveaux total de
                    l'immeuble
                nombre_niveau_logement: nombre de niveaux du logement
                    (maison ou appartement)
                hsp: hauteur sous plafond moyenne du logement/de
                    l'immeuble
                surface_habitable_immeuble: surface habitable totale de
                    l'immeuble dans le cas d'un DPE appartement avec
                    usage collectif ou d'un DPE immeuble.
                surface_tertiaire_immeuble: surface tertiaire totale de
                    l'immeuble dans le cas d'un DPE immeuble. La surface
                    tertiaire est prise en compte pour le calcul des
                    besoins dans le cas d'une installation collective
                    mixte tertiaire/residentiel
                nombre_appartement: nombre d'appartements de l'immeuble
                    dans le cas d'un DPE appartement avec usage
                    collectif ou d'un DPE immeuble.
                appartement_non_visite: est ce que l'appartement est un
                    appartement non visité dans le cas d'un DPE
                    appartement généré à partir d'un immeuble.
                    (application de système individuel les moins
                    performants de l'immeuble)
            """

            annee_construction: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": "2011",
                    "max_inclusive": "2100",
                    "pattern": r"[0-9]{4}",
                },
            )
            enum_periode_construction_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 10,
                },
            )
            enum_methode_application_dpe_log_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 1,
                    "max_inclusive": 40,
                },
            )
            surface_habitable_logement: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0.0,
                    "nillable": True,
                },
            )
            nombre_niveau_immeuble: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0,
                    "nillable": True,
                },
            )
            nombre_niveau_logement: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0,
                    "nillable": True,
                },
            )
            hsp: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_exclusive": 0.0,
                },
            )
            surface_habitable_immeuble: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0.0,
                    "nillable": True,
                },
            )
            surface_tertiaire_immeuble: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0.0,
                    "nillable": True,
                },
            )
            nombre_appartement: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_exclusive": 0,
                    "nillable": True,
                },
            )
            appartement_non_visite: Optional[SOuiNon] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

        @dataclass
        class Meteo:
            """
            Attributes:
                enum_zone_climatique_id: zone climatique du logement
                enum_classe_altitude_id: classe d'altitude du logement
                batiment_materiaux_anciens: est ce que le bâtiment est
                    principalement composé de matériaux anciens pour ses
                    murs 0 : non 1 : oui
            """

            enum_zone_climatique_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_inclusive": 1,
                    "max_inclusive": 8,
                    "nillable": True,
                },
            )
            enum_classe_altitude_id: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_inclusive": 1,
                    "max_inclusive": 3,
                    "nillable": True,
                },
            )
            batiment_materiaux_anciens: Optional[SOuiNon] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

        @dataclass
        class Enveloppe:
            inertie: Optional["Dpe.LogementNeuf.Enveloppe.Inertie"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
            mur_collection: Optional[
                "Dpe.LogementNeuf.Enveloppe.MurCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
            plancher_bas_collection: Optional[
                "Dpe.LogementNeuf.Enveloppe.PlancherBasCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
            plancher_haut_collection: Optional[
                "Dpe.LogementNeuf.Enveloppe.PlancherHautCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
            baie_vitree_collection: Optional[
                "Dpe.LogementNeuf.Enveloppe.BaieVitreeCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
            porte_collection: Optional[
                "Dpe.LogementNeuf.Enveloppe.PorteCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
            pont_thermique_collection: Optional[
                "Dpe.LogementNeuf.Enveloppe.PontThermiqueCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

            @dataclass
            class Inertie:
                """
                Attributes:
                    enum_classe_inertie_id: classe d'inertie globale du
                        bâtiment
                """

                enum_classe_inertie_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 1,
                        "max_inclusive": 4,
                        "nillable": True,
                    },
                )

            @dataclass
            class MurCollection:
                mur: List["Dpe.LogementNeuf.Enveloppe.MurCollection.Mur"] = (
                    field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                )

                @dataclass
                class Mur:
                    donnee_entree: Optional[
                        "Dpe.LogementNeuf.Enveloppe.MurCollection.Mur.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.LogementNeuf.Enveloppe.MurCollection.Mur.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            surface_aiu: surface aiu : surface des
                                parois du local non chauffé qui donnent
                                sur des locaux chauffés.
                            surface_aue: surface aue : surface des
                                parois du local non chauffé en contact
                                avec l'extérieur ou le sol
                            enum_cfg_isolation_lnc_id: configuration de
                                l'adjacence avec local non chauffé :
                                local chauffé (non) isolé/local non
                                chauffé (non) isolé/orientation véranda
                                qui permet de calculer le b
                            enum_type_adjacence_id: type d'adjacence de
                                la paroi
                            enum_orientation_id: orientation du mur
                            surface_paroi_totale: Surface de paroi
                                opaque + paroi vitrée de la paroi +
                                surface des portes
                            surface_paroi_opaque: Surface de paroi
                                opaque (sans baies vitrées sans portes)
                            epaisseur_structure: epaisseur de la partie
                                structure de la paroi (sans l'isolation
                                intérieure ou extérieure) (cm)
                            enum_materiaux_structure_mur_id: matériaux
                                de structure de la paroi
                            paroi_ancienne: la paroi est une paroi
                                ancienne sur laquelle a été appliquée un
                                enduit isolant (Renduit=0,7m².K.W-1) 0 :
                                non 1 : oui. (Attention ! nom de
                                propriété pas tout à fait explicite)
                            enum_type_doublage_id: type de doublage
                                intérieur du mur.(précision de la nature
                                du doublage ou de l'epaisseur de la lame
                                d'air en cas de doublage indéterminé.)
                            enum_type_isolation_id: type d'isolation du
                                mur (ITI/ITE…..)
                            resistance_isolation: resistance isolation
                            epaisseur_isolation: epaisseur de
                                l'isolation (si plusieurs isolant
                                différents sommer leurs épaisseurs) (cm)
                            enum_methode_saisie_u_id: methode de saisie
                                du U (inclus les justifications à
                                produire en cas de saisie directe)
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        surface_aiu: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_aue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_cfg_isolation_lnc_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                            },
                        )
                        enum_type_adjacence_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 22,
                            },
                        )
                        enum_orientation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 5,
                            },
                        )
                        surface_paroi_totale: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_paroi_opaque: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        epaisseur_structure: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_materiaux_structure_mur_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 27,
                                "nillable": True,
                            },
                        )
                        paroi_ancienne: Optional[SOuiNon] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        enum_type_doublage_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 5,
                                "nillable": True,
                            },
                        )
                        enum_type_isolation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 9,
                                "nillable": True,
                            },
                        )
                        resistance_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        epaisseur_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_methode_saisie_u_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 10,
                                "nillable": True,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            b: coefficient de réduction des déperditions
                                du mur
                            umur: Coefficient de transmission thermique
                                du mur
                            umur0: Coefficient de transmission thermique
                                du mur non isolé final (avec pris en
                                compte de l'enduit et du doublage).
                                C'est bien le U du mur "nu" avec
                                l'ensemble des éléments hors isolations
                                rapportée
                        """

                        b: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "max_inclusive": 1.0,
                                "nillable": True,
                            },
                        )
                        umur: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        umur0: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )

            @dataclass
            class PlancherBasCollection:
                plancher_bas: List[
                    "Dpe.LogementNeuf.Enveloppe.PlancherBasCollection.PlancherBas"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class PlancherBas:
                    donnee_entree: Optional[
                        "Dpe.LogementNeuf.Enveloppe.PlancherBasCollection.PlancherBas.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.LogementNeuf.Enveloppe.PlancherBasCollection.PlancherBas.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            surface_aiu: surface aiu : surface des
                                parois du local non chauffé qui donnent
                                sur des locaux chauffés.
                            surface_aue: surface aue : surface des
                                parois du local non chauffé en contact
                                avec l'extérieur ou le sol
                            enum_cfg_isolation_lnc_id: configuration de
                                l'adjacence avec local non chauffé :
                                local chauffé (non) isolé/local non
                                chauffé (non) isolé/orientation véranda
                                qui permet de calculer le b
                            enum_type_adjacence_id: type d'adjacence de
                                la paroi
                            surface_paroi_opaque: Surface de paroi
                                opaque
                            enum_type_plancher_bas_id: type de plancher
                                bas
                            enum_type_isolation_id: type d'isolation du
                                plancher bas (ITI/ITE…..)
                            resistance_isolation: resistance isolation
                            epaisseur_isolation: epaisseur de
                                l'isolation (si plusieurs isolant
                                différents sommer leurs épaisseurs)
                            enum_methode_saisie_u_id: methode de saisie
                                du U (inclus les justifications à
                                produire en cas de saisie directe)
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        surface_aiu: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_aue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_cfg_isolation_lnc_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                            },
                        )
                        enum_type_adjacence_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 22,
                            },
                        )
                        surface_paroi_opaque: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_type_plancher_bas_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 13,
                                "nillable": True,
                            },
                        )
                        enum_type_isolation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 9,
                                "nillable": True,
                            },
                        )
                        resistance_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        epaisseur_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_methode_saisie_u_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 10,
                                "nillable": True,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            b: coefficient de réduction des déperditions
                                du planchers_bas
                            upb_final: Coefficient de transmission
                                thermique du planchers_bas (Ue ou Upb en
                                fonction du type d'adjacence)
                            upb0: Coefficient de transmission thermique
                                du planchers bas non isolé final
                        """

                        b: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "max_inclusive": 1.0,
                                "nillable": True,
                            },
                        )
                        upb_final: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        upb0: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )

            @dataclass
            class PlancherHautCollection:
                plancher_haut: List[
                    "Dpe.LogementNeuf.Enveloppe.PlancherHautCollection.PlancherHaut"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class PlancherHaut:
                    donnee_entree: Optional[
                        "Dpe.LogementNeuf.Enveloppe.PlancherHautCollection.PlancherHaut.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.LogementNeuf.Enveloppe.PlancherHautCollection.PlancherHaut.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            surface_aiu: surface aiu : surface des
                                parois du local non chauffé qui donnent
                                sur des locaux chauffés.
                            surface_aue: surface aue : surface des
                                parois du local non chauffé en contact
                                avec l'extérieur ou le sol
                            enum_cfg_isolation_lnc_id: configuration de
                                l'adjacence avec local non chauffé :
                                local chauffé (non) isolé/local non
                                chauffé (non) isolé/orientation véranda
                                qui permet de calculer le b
                            enum_type_adjacence_id: type d'adjacence de
                                la paroi
                            surface_paroi_opaque: Surface de paroi
                                opaque
                            enum_type_plancher_haut_id: type de plancher
                                haut
                            enum_type_isolation_id: type d'isolation du
                                plancher haut (ITI/ITE…..)
                            resistance_isolation: resistance isolation
                            epaisseur_isolation: epaisseur de
                                l'isolation (si plusieurs isolant
                                différents sommer leurs épaisseurs)
                            enum_methode_saisie_u_id: methode de saisie
                                du U (inclus les justifications à
                                produire en cas de saisie directe)
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        surface_aiu: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_aue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_cfg_isolation_lnc_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                            },
                        )
                        enum_type_adjacence_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 22,
                            },
                        )
                        surface_paroi_opaque: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_type_plancher_haut_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 16,
                                "nillable": True,
                            },
                        )
                        enum_type_isolation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 9,
                                "nillable": True,
                            },
                        )
                        resistance_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        epaisseur_isolation: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_methode_saisie_u_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 10,
                                "nillable": True,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            b: coefficient de réduction des déperditions
                                du planchers_hauts
                            uph: Coefficient de transmission thermique
                                du planchers_hauts uph
                            uph0: Coefficient de transmission thermique
                                du planchers hauts non isolé final
                        """

                        b: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "max_inclusive": 1.0,
                                "nillable": True,
                            },
                        )
                        uph: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        uph0: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )

            @dataclass
            class BaieVitreeCollection:
                baie_vitree: List[
                    "Dpe.LogementNeuf.Enveloppe.BaieVitreeCollection.BaieVitree"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class BaieVitree:
                    donnee_entree: Optional[
                        "Dpe.LogementNeuf.Enveloppe.BaieVitreeCollection.BaieVitree.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.LogementNeuf.Enveloppe.BaieVitreeCollection.BaieVitree.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            reference_paroi: reference projet de l'objet
                                paroi qui est associé à l'objet baie
                                vitrée. La codification et utilisation
                                des références peut différer entre
                                logiciels mais il devrait être attendu
                                que reference_paroi est la référence
                                d'une paroi de type mur,plancher_haut ou
                                plancher_bas
                            surface_aiu: surface aiu : surface des
                                parois du local non chauffé qui donnent
                                sur des locaux chauffés.
                            surface_aue: surface aue : surface des
                                parois du local non chauffé en contact
                                avec l'extérieur ou le sol
                            enum_cfg_isolation_lnc_id: configuration de
                                l'adjacence avec local non chauffé :
                                local chauffé (non) isolé/local non
                                chauffé (non) isolé/orientation véranda
                                qui permet de calculer le b
                            enum_type_adjacence_id: type d'adjacence de
                                la paroi
                            surface_totale_baie: surface totale de paroi
                                vitrée pour ce type de vitrage et sur
                                cette orientation (nombre de baies x
                                surface unitaire). La surface est la
                                surface de la baie dans son ensemble.
                                (vitrage + menuiserie inclus)
                            nb_baie: nombre de baies
                            enum_type_vitrage_id: type de vitrage
                            enum_inclinaison_vitrage_id: inclinaison du
                                vitrage
                            enum_type_gaz_lame_id: type de gaz présent
                                dans la lame
                            epaisseur_lame: epaisseur de la lame
                            vitrage_vir: est ce que le vitrage est à
                                isolation renforcée 0 : non 1 : oui
                            enum_methode_saisie_perf_vitrage_id: methode
                                de saisie des caractéristiques
                                thermiques des vitrage (valeurs
                                forfaitaires ou saisies en direct
                                lorsque issu d'un justificatif)
                            enum_type_materiaux_menuiserie_id: type de
                                matériaux des menuiseries
                            enum_type_baie_id: type de baie
                            enum_type_fermeture_id: type de fermeture
                                associé à la baie (volets/persiennes
                                etc..)
                            enum_type_pose_id: type de pose de la baie
                            enum_orientation_id: orientation de la baie
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_paroi: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        surface_aiu: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_aue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_cfg_isolation_lnc_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                            },
                        )
                        enum_type_adjacence_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 22,
                            },
                        )
                        surface_totale_baie: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        nb_baie: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_type_vitrage_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 6,
                                "nillable": True,
                            },
                        )
                        enum_inclinaison_vitrage_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 4,
                                "nillable": True,
                            },
                        )
                        enum_type_gaz_lame_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 3,
                                "nillable": True,
                            },
                        )
                        epaisseur_lame: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        vitrage_vir: Optional[SOuiNon] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        enum_methode_saisie_perf_vitrage_id: Optional[int] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 15,
                                    "nillable": True,
                                },
                            )
                        )
                        enum_type_materiaux_menuiserie_id: Optional[int] = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 7,
                                    "nillable": True,
                                },
                            )
                        )
                        enum_type_baie_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 8,
                                "nillable": True,
                            },
                        )
                        enum_type_fermeture_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 8,
                                "nillable": True,
                            },
                        )
                        enum_type_pose_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 4,
                                "nillable": True,
                            },
                        )
                        enum_orientation_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 5,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            b: coefficient de réduction des déperditions
                                de la baie vitrée
                            ug: Ug final de la baie : soit saisi
                                directement soit issu des tables
                                forfaitaires
                            uw: Uw final de la baie : soit saisi
                                directement soit issu des tables
                                forfaitaires
                            ujn: Ujn final de la baie : soit saisi
                                directement soit issu des tables
                                forfaitaires
                            u_menuiserie: U final de la menuiserie
                                utilisé dans le calcul : soit Ujn dans
                                le cas d'une baie avec protection
                                solaire soit Uw dans le cas d'une baie
                                sans protection solaire
                            sw: sw final de la baie: soit saisi
                                directement soit issu des tables
                                forfaitaires
                        """

                        b: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "max_inclusive": 1.0,
                                "nillable": True,
                            },
                        )
                        ug: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        uw: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        ujn: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        u_menuiserie: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        sw: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )

            @dataclass
            class PorteCollection:
                porte: List[
                    "Dpe.LogementNeuf.Enveloppe.PorteCollection.Porte"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class Porte:
                    donnee_entree: Optional[
                        "Dpe.LogementNeuf.Enveloppe.PorteCollection.Porte.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.LogementNeuf.Enveloppe.PorteCollection.Porte.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            reference_paroi: reference projet de l'objet
                                paroi qui est associé à l'objet porte.
                                La codification et utilisation des
                                références peut différer entre logiciels
                                mais il devrait être attendu que
                                reference_paroi est la référence d'une
                                paroi de type mur,plancher_haut ou
                                plancher_bas
                            enum_cfg_isolation_lnc_id: configuration de
                                l'adjacence avec local non chauffé :
                                local chauffé (non) isolé/local non
                                chauffé (non) isolé/orientation véranda
                                qui permet de calculer le b
                            enum_type_adjacence_id: type d'adjacence de
                                la paroi
                            surface_aiu: surface aiu : surface des
                                parois du local non chauffé qui donnent
                                sur des locaux chauffés.
                            surface_aue: surface aue : surface des
                                parois du local non chauffé en contact
                                avec l'extérieur ou le sol
                            surface_porte: surface totale de portes
                                déclaré (nb_porte x surface unitaire de
                                porte dans le cas de plusieurs portes)
                            enum_methode_saisie_uporte_id: méthode de
                                saisie du U de la porte
                            enum_type_porte_id: type de porte
                            nb_porte: nombre de portes
                            largeur_dormant: largeur du dormant de la
                                porte (cm)
                            presence_retour_isolation: y a-t-il un
                                retour d'isolant de la paroi opaque sur
                                la porte 0 : non 1 : oui
                            enum_type_pose_id: type de pose de la porte
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_paroi: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        enum_cfg_isolation_lnc_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 11,
                            },
                        )
                        enum_type_adjacence_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 22,
                            },
                        )
                        surface_aiu: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_aue: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        surface_porte: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_methode_saisie_uporte_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 3,
                                "nillable": True,
                            },
                        )
                        enum_type_porte_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 16,
                                "nillable": True,
                            },
                        )
                        nb_porte: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        largeur_dormant: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        presence_retour_isolation: Optional[SOuiNon] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        enum_type_pose_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 4,
                                "nillable": True,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            uporte: coefficient de transmission
                                thermique de la porte final : soit saisi
                                directement soit issu des tables de
                                valeurs forfaitaires
                            b: coefficient de transmission thermique de
                                la porte final : soit saisi directement
                                soit issu des tables de valeurs
                                forfaitaires
                        """

                        uporte: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        b: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 0.0,
                                "max_inclusive": 1.0,
                                "nillable": True,
                            },
                        )

            @dataclass
            class PontThermiqueCollection:
                pont_thermique: List[
                    "Dpe.LogementNeuf.Enveloppe.PontThermiqueCollection.PontThermique"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class PontThermique:
                    donnee_entree: Optional[
                        "Dpe.LogementNeuf.Enveloppe.PontThermiqueCollection.PontThermique.DonneeEntree"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    donnee_intermediaire: Optional[
                        "Dpe.LogementNeuf.Enveloppe.PontThermiqueCollection.PontThermique.DonneeIntermediaire"
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                    @dataclass
                    class DonneeEntree:
                        """
                        Attributes:
                            description: description textuelle de
                                l'objet
                            reference: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre logiciels
                            reference_1: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre
                                logiciels. Pour les ponts thermique il
                                est laissé la possibilité d'avoir 2
                                références complémentaires correspondant
                                aux référence de chacun des deux objets
                                concernés par le pont thermique
                            reference_2: reference projet de l'objet
                                (cette référence permet de faire
                                d'éventuels liens entre objets). La
                                codification et utilisation des
                                références peut différer entre
                                logiciels. Pour les ponts thermique il
                                est laissé la possibilité d'avoir 2
                                références complémentaires correspondant
                                aux référence de chacun des deux objets
                                concernés par le pont thermique
                            enum_methode_saisie_pont_thermique_id:
                                methode de saisie des ponts thermiques
                            l: longueur du pont thermique(m)
                            enum_type_liaison_id: type de liaison de
                                pont thermique
                        """

                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        reference: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_1: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        reference_2: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "max_length": 255,
                                "nillable": True,
                            },
                        )
                        enum_methode_saisie_pont_thermique_id: Optional[
                            int
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 3,
                                "nillable": True,
                            },
                        )
                        l: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_exclusive": 0.0,
                                "nillable": True,
                            },
                        )
                        enum_type_liaison_id: Optional[int] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": 1,
                                "max_inclusive": 5,
                                "nillable": True,
                            },
                        )

                    @dataclass
                    class DonneeIntermediaire:
                        """
                        Attributes:
                            k: valeur du pont thermique
                        """

                        k: Optional[float] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )

        @dataclass
        class VentilationCollection:
            ventilation: List[
                "Dpe.LogementNeuf.VentilationCollection.Ventilation"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

            @dataclass
            class Ventilation:
                donnee_entree: Optional[
                    "Dpe.LogementNeuf.VentilationCollection.Ventilation.DonneeEntree"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                donnee_intermediaire: Optional[
                    "Dpe.LogementNeuf.VentilationCollection.Ventilation.DonneeIntermediaire"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class DonneeEntree:
                    """
                    Attributes:
                        surface_ventile: surface ventilée. Dans le cas
                            d'une seule ventilation c'est la surface
                            habitable totale. Dans le cas d'un DPE
                            immeuble ou d'un DPE appartement à partir de
                            l'immeuble c'est la surface de
                            l'installation à l'immeuble qu'il faut
                            renseigner
                        description: description textuelle de l'objet
                        reference: reference projet de l'objet (cette
                            référence permet de faire d'éventuels liens
                            entre objets). La codification et
                            utilisation des références peut différer
                            entre logiciels
                        plusieurs_facade_exposee: est ce qu'il y a
                            plusieurs facades exposées au vent 0 : non 1
                            : oui
                        enum_methode_saisie_q4pa_conv_id: code de la
                            methode de saisie du q4paconv
                        enum_type_ventilation_id: code du type de
                            ventilation
                        ventilation_post_2012: est ce que le système de
                            ventilation est postérieur à 2012 0 : non 1
                            : oui
                        ref_produit_ventilation: référence produit et
                            marque du système de ventilation
                    """

                    surface_ventile: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    description: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    reference: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )
                    plusieurs_facade_exposee: Optional[SOuiNon] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    enum_methode_saisie_q4pa_conv_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 3,
                            "nillable": True,
                        },
                    )
                    enum_type_ventilation_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 38,
                            "nillable": True,
                        },
                    )
                    ventilation_post_2012: Optional[SOuiNon] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    ref_produit_ventilation: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )

                @dataclass
                class DonneeIntermediaire:
                    """
                    Attributes:
                        pvent_moy: puissance de la ventilation moyenne
                            soit saisie soit calculée avec la méthode
                            proposée
                        q4pa_conv: q4pa conv final soit issue d'une
                            saisie de mesure à l'étanchéité à l'air soit
                            d'une valeur forfaitaire. valeur
                            conventionnelle de la perméabilité sous 4Pa
                            (m3/(h.m2))
                        conso_auxiliaire_ventilation: Consommation des
                            auxilliaires de ventilation. Dans le cas
                            d'un DPE immeuble ou d'un DPE appartement à
                            partir de l'immeuble c'est la consommation
                            de l'installation à l'immeuble qu'il faut
                            saisir.
                        hperm: déperdition thermique par renouvellement
                            d'air due au vent
                        hvent: déperdition thermique par renouvellement
                            d'air due au système de ventilation
                    """

                    pvent_moy: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    q4pa_conv: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    conso_auxiliaire_ventilation: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    hperm: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    hvent: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 0.0,
                            "nillable": True,
                        },
                    )

        @dataclass
        class ClimatisationCollection:
            climatisation: List[
                "Dpe.LogementNeuf.ClimatisationCollection.Climatisation"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

            @dataclass
            class Climatisation:
                donnee_entree: Optional[
                    "Dpe.LogementNeuf.ClimatisationCollection.Climatisation.DonneeEntree"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                donnee_intermediaire: Optional[
                    "Dpe.LogementNeuf.ClimatisationCollection.Climatisation.DonneeIntermediaire"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class DonneeEntree:
                    """
                    Attributes:
                        description: description textuelle de l'objet
                        reference: reference projet de l'objet (cette
                            référence permet de faire d'éventuels liens
                            entre objets). La codification et
                            utilisation des références peut différer
                            entre logiciels
                        surface_clim: surface climatisée : si le
                            logement n'est pas climatisé dans son
                            ensemble la surface climatisée peut être
                            inférieure à la surface totale du
                            logement.Dans le cas spécifique d'un DPE
                            immeuble avec installation individuelle
                            échantillonée :saisir la surface climatisée
                            par la totalité des logements représentés
                            par le logement moyen surface_clim =
                            Shmoy*Nblgt. Dans le cas d'un DPE immeuble
                            ou d'un DPE appartement à partir de
                            l'immeuble c'est la surface de
                            l'installation à l'immeuble qu'il faut
                            renseigner
                        enum_type_generateur_fr_id: type de générateur
                            de froid
                        enum_type_energie_id: type d'énergie consommée
                            par le générateur de froid
                        enum_methode_saisie_carac_sys_id: methode de
                            saisie du seer : lecture de table
                            forfaitaire ou saisie justifiée
                        ref_produit_fr: référence produit et marque du
                            générateur de froid
                    """

                    description: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    reference: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )
                    surface_clim: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    enum_type_generateur_fr_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 23,
                            "nillable": True,
                        },
                    )
                    enum_type_energie_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 15,
                            "nillable": True,
                        },
                    )
                    enum_methode_saisie_carac_sys_id: Optional[
                        DonneeEntreeEnumMethodeSaisieCaracSysId
                    ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    ref_produit_fr: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )

                @dataclass
                class DonneeIntermediaire:
                    """
                    Attributes:
                        eer: coefficient d'efficience energétique du
                            système de climatisation final (SEER *0,95)
                        besoin_fr: besoin de refroidissement annuel.
                            Dans le cas d'un DPE immeuble ou d'un DPE
                            appartement à partir de l'immeuble c'est le
                            besoin de l'installation à l'immeuble qu'il
                            faut saisir.
                        conso_fr: consommation de refroidissement annuel
                            (kWh). Dans le cas d'un DPE immeuble ou d'un
                            DPE appartement à partir de l'immeuble c'est
                            la consommation de l'installation à
                            l'immeuble qu'il faut saisir.
                    """

                    eer: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    besoin_fr: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    conso_fr: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )

        @dataclass
        class ProductionElecEnr:
            donnee_entree: Optional[
                "Dpe.LogementNeuf.ProductionElecEnr.DonneeEntree"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
            donnee_intermediaire: Optional[
                "Dpe.LogementNeuf.ProductionElecEnr.DonneeIntermediaire"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
            panneaux_pv_collection: Optional[
                "Dpe.LogementNeuf.ProductionElecEnr.PanneauxPvCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

            @dataclass
            class DonneeEntree:
                """
                Attributes:
                    description: description textuelle de l'objet
                    reference: reference projet de l'objet (cette
                        référence permet de faire d'éventuels liens
                        entre objets). La codification et utilisation
                        des références peut différer entre logiciels
                    presence_production_pv: est ce qu'il y a de la
                        production de photovoltaique renouvelable 0 :
                        non 1 : oui
                    enum_type_enr_id: enumérateur listant les systèmes
                        de production d'éléctricité d'origine
                        renouvelables présents dans le bâtiment
                """

                description: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                reference: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "max_length": 255,
                        "nillable": True,
                    },
                )
                presence_production_pv: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                enum_type_enr_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 1,
                        "max_inclusive": 7,
                        "nillable": True,
                    },
                )

            @dataclass
            class DonneeIntermediaire:
                """
                Attributes:
                    taux_autoproduction: taux d'autoproduction Tap de la
                        production d'éléctricité d'origne renouvelable
                    production_pv: production d'éléctricité
                        photovoltaique (kWh)
                    conso_elec_ac: éléctricité photovoltaique
                        autoconsommée (kWh)
                """

                taux_autoproduction: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                production_pv: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                conso_elec_ac: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )

            @dataclass
            class PanneauxPvCollection:
                panneaux_pv: List[
                    "Dpe.LogementNeuf.ProductionElecEnr.PanneauxPvCollection.PanneauxPv"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class PanneauxPv:
                    """
                    Attributes:
                        surface_totale_capteurs: surface totale de
                            capteurs photovoltaïque. Dans le cas d'une
                            installation collective de PV pour un DPE
                            appartement, la surface est celle proratisé
                        nombre_module: nombre de modules photovoltaïque
                            standards posés.
                    """

                    surface_totale_capteurs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    nombre_module: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0,
                            "nillable": True,
                        },
                    )

        @dataclass
        class InstallationEcsCollection:
            installation_ecs: List[
                "Dpe.LogementNeuf.InstallationEcsCollection.InstallationEcs"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

            @dataclass
            class InstallationEcs:
                donnee_entree: Optional[
                    "Dpe.LogementNeuf.InstallationEcsCollection.InstallationEcs.DonneeEntree"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                donnee_intermediaire: Optional[
                    "Dpe.LogementNeuf.InstallationEcsCollection.InstallationEcs.DonneeIntermediaire"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                generateur_ecs_collection: Optional[
                    "Dpe.LogementNeuf.InstallationEcsCollection.InstallationEcs.GenerateurEcsCollection"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class DonneeEntree:
                    """
                    Attributes:
                        description: description textuelle de l'objet
                        reference: reference projet de l'objet (cette
                            référence permet de faire d'éventuels liens
                            entre objets). La codification et
                            utilisation des références peut différer
                            entre logiciels
                        enum_cfg_installation_ecs_id: code de
                            configuration de l'installation d'ECS
                            (installation simple, avec solaire ou avec
                            plusieurs systèmes d'ECS)
                        enum_type_installation_id: code du type
                            d'installation d'ECS (collective ou
                            individuelle)
                        surface_habitable: surface habitable
                            correspondant au(x) logement(x) desservi(s)
                            par l'installation d'ECS.(surface habitable
                            du logement ou de la totalité des logements
                            de l'immeuble) Dans le cas spécifique d'un
                            DPE immeuble avec installation individuelle
                            échantillonée :saisir la surface de la
                            totalité des logements représentés par le
                            logement moyen surface_habitable=
                            Shmoy*Nblgt. Dans le cas d'un DPE immeuble
                            ou d'un DPE appartement à partir de
                            l'immeuble c'est la surface de
                            l'installation à l'immeuble qu'il faut
                            renseigner
                        nombre_logement: nombre de logements desservis
                            par l'installation d'ECS. Dans le cas d'un
                            DPE immeuble avec installation individuelle
                            échantillonée : saisir le nombre de
                            logements qui sont équipés de ce type
                            d'installation d'ECS.
                        enum_type_installation_solaire_id: type
                            d'installation solaire (ECS+Chauffage , ECS
                            solaire seule etc…)
                        enum_bouclage_reseau_ecs_id: type de bouclage du
                            réseau d'ECS pour la prise en compte des
                            consommations d'auxiliaires de distribution
                        reseau_distribution_isole: est ce que le réseau
                            de distribution est isolé 0 : non 1 : oui
                    """

                    description: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    reference: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )
                    enum_cfg_installation_ecs_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 3,
                            "nillable": True,
                        },
                    )
                    enum_type_installation_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 4,
                            "nillable": True,
                        },
                    )
                    surface_habitable: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    nombre_logement: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    enum_type_installation_solaire_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 4,
                            "nillable": True,
                        },
                    )
                    enum_bouclage_reseau_ecs_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 3,
                            "nillable": True,
                        },
                    )
                    reseau_distribution_isole: Optional[SOuiNon] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                @dataclass
                class DonneeIntermediaire:
                    """
                    Attributes:
                        besoin_ecs: besoin d'ECS annuel pour l'ensemble
                            de l'installation (kWh). Dans le cas d'un
                            DPE immeuble ou d'un DPE appartement à
                            partir de l'immeuble c'est la consommation
                            de l'installation à l'immeuble qu'il faut
                            saisir.
                        production_ecs_solaire: production d'ecs solaire
                            annuelle (kWh). Dans le cas d'un DPE
                            immeuble ou d'un DPE appartement à partir de
                            l'immeuble c'est la consommation de
                            l'installation à l'immeuble qu'il faut
                            saisir.
                        conso_ecs: consommation d'energie annuelle de
                            l'installation d'ECS en energie finale kWh.
                            Dans le cas d'un DPE immeuble ou d'un DPE
                            appartement à partir de l'immeuble c'est la
                            consommation de l'installation à l'immeuble
                            qu'il faut saisir.
                    """

                    besoin_ecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    production_ecs_solaire: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    conso_ecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 0.0,
                            "nillable": True,
                        },
                    )

                @dataclass
                class GenerateurEcsCollection:
                    generateur_ecs: List[
                        "Dpe.LogementNeuf.InstallationEcsCollection.InstallationEcs.GenerateurEcsCollection.GenerateurEcs"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                    @dataclass
                    class GenerateurEcs:
                        donnee_entree: Optional[
                            "Dpe.LogementNeuf.InstallationEcsCollection.InstallationEcs.GenerateurEcsCollection.GenerateurEcs.DonneeEntree"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        donnee_intermediaire: Optional[
                            "Dpe.LogementNeuf.InstallationEcsCollection.InstallationEcs.GenerateurEcsCollection.GenerateurEcs.DonneeIntermediaire"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )

                        @dataclass
                        class DonneeEntree:
                            """
                            Attributes:
                                description: description textuelle de
                                    l'objet
                                reference: reference projet de l'objet
                                    (cette référence permet de faire
                                    d'éventuels liens entre objets). La
                                    codification et utilisation des
                                    références peut différer entre
                                    logiciels
                                enum_type_generateur_ecs_id: type de
                                    generateur d'ecs
                                ref_produit_generateur_ecs: référence
                                    produit et marque du générateur
                                    d'ECS
                                enum_usage_generateur_id: usages assurés
                                    par le générateur
                                    (chauffage/ecs/chauffage+ecs)
                                enum_type_energie_id: type d'énergie
                                    consommée par le générateur d'ECS
                                enum_methode_saisie_carac_sys_id:
                                    méthode de saisie des performances
                                    du système d'ECS
                                enum_type_stockage_ecs_id: Type de
                                    stockage d'ECS (intégré à la
                                    production ou indépendant)
                                position_volume_chauffe: est ce que le
                                    générateur est positionné dans le
                                    volume chauffé. (pour le calcul des
                                    pertes de génération récupérables)
                                position_volume_chauffe_stockage: est ce
                                    que le ballon de stockage est
                                    positionné dans le volume chauffé.
                                    (pour le calcul des pertes de
                                    stockage récupérables)
                                volume_stockage: volume de stockage
                                    associé au générateur d'ECS
                                presence_ventouse: présence d'un système
                                    de ventouse ou avec un ventilateur
                                    pour l'évacuation des fumées d'un
                                    système à combustion 0 : non 1 : oui
                                identifiant_reseau_chaleur: identifiant
                                    réseau de chaleur ou de froid
                                    utilisé (utilisé à partir du 18
                                    janvier 2022)
                            """

                            description: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            reference: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            enum_type_generateur_ecs_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 134,
                                    "nillable": True,
                                },
                            )
                            ref_produit_generateur_ecs: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            enum_usage_generateur_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 3,
                                    "nillable": True,
                                },
                            )
                            enum_type_energie_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 15,
                                    "nillable": True,
                                },
                            )
                            enum_methode_saisie_carac_sys_id: Optional[
                                DonneeEntreeEnumMethodeSaisieCaracSysId
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            enum_type_stockage_ecs_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 3,
                                    "nillable": True,
                                },
                            )
                            position_volume_chauffe: Optional[SOuiNon] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            position_volume_chauffe_stockage: Optional[
                                SOuiNon
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            volume_stockage: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            presence_ventouse: Optional[SOuiNon] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            identifiant_reseau_chaleur: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "pattern": r"[0-9]{4}[C-F]",
                                    "nillable": True,
                                },
                            )

                        @dataclass
                        class DonneeIntermediaire:
                            """
                            Attributes:
                                pn: puissance nominale du générateur à
                                    combustion. Dans le cas d'un
                                    générateur virtualisé pour DPE
                                    appartement avec ECS collective
                                    saisir Pe = a*Pn(collectif) (W)
                                qp0: pertes à l'arret du générateur à
                                    combustion. Dans le cas d'un
                                    générateur virtualisé pour DPE
                                    appartement avec ECS collective
                                    saisir Qp0 correspondant à Pe =
                                    a*Pn(collectif)
                                pveilleuse: puissance de la veilleuse du
                                    générateur à combustion (W)
                                rpn: rendement de génération à pleine
                                    charge du générateur à combustion
                                    (0-1,5)
                                cop: COP du chauffe-eau thermodynamique
                                    (inclus le rendement de stockage)
                                    (0-20)
                                ratio_besoin_ecs: ratio du besoin ecs de
                                    l'installation affecté au
                                    générateur. Ce ratio est de 1 pour
                                    les installations classiques et de
                                    0,5 pour les installations d'ECS
                                    avec deux générateurs
                                conso_ecs: consommation d'energie
                                    annuelle du générateur d'ECS (kWh)
                                    (Exprimé en kWh PCI pour les
                                    combustibles ). Dans le cas d'un DPE
                                    immeuble ou d'un DPE appartement à
                                    partir de l'immeuble c'est la
                                    consommation du générateur à
                                    l'immeuble qu'il faut saisir.
                            """

                            pn: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 100.0,
                                    "nillable": True,
                                },
                            )
                            qp0: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            pveilleuse: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            rpn: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.5,
                                    "nillable": True,
                                },
                            )
                            cop: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 1.0,
                                    "max_exclusive": 8.0,
                                    "nillable": True,
                                },
                            )
                            ratio_besoin_ecs: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            conso_ecs: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 0.0,
                                    "nillable": True,
                                },
                            )

        @dataclass
        class InstallationChauffageCollection:
            installation_chauffage: List[
                "Dpe.LogementNeuf.InstallationChauffageCollection.InstallationChauffage"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )

            @dataclass
            class InstallationChauffage:
                donnee_entree: Optional[
                    "Dpe.LogementNeuf.InstallationChauffageCollection.InstallationChauffage.DonneeEntree"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                donnee_intermediaire: Optional[
                    "Dpe.LogementNeuf.InstallationChauffageCollection.InstallationChauffage.DonneeIntermediaire"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                emetteur_chauffage_collection: Optional[
                    "Dpe.LogementNeuf.InstallationChauffageCollection.InstallationChauffage.EmetteurChauffageCollection"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                generateur_chauffage_collection: Optional[
                    "Dpe.LogementNeuf.InstallationChauffageCollection.InstallationChauffage.GenerateurChauffageCollection"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )

                @dataclass
                class DonneeEntree:
                    """
                    Attributes:
                        description: description textuelle de l'objet
                        reference: reference projet de l'objet (cette
                            référence permet de faire d'éventuels liens
                            entre objets). La codification et
                            utilisation des références peut différer
                            entre logiciels
                        surface_chauffee: surface chauffée par
                            l'installation de chauffage(surface du
                            logement ou de l'immeuble). Dans le cas
                            spécifique d'un DPE immeuble avec
                            installation individuelle échantillonée
                            :saisir la surface chauffée de la totalité
                            des logements représentés par le logement
                            moyen surface_habitable= Shmoy*Nblgt. Dans
                            le cas d'un DPE immeuble ou d'un DPE
                            appartement à partir de l'immeuble c'est la
                            surface de l'installation à l'immeuble qu'il
                            faut renseigner
                        enum_cfg_installation_ch_id: configuration de
                            l'installation de chauffage
                        enum_type_installation_id: type d'installation
                            de chauffage (collective ou individuelle ou
                            collective multi batiment
                    """

                    description: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                    reference: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "max_length": 255,
                            "nillable": True,
                        },
                    )
                    surface_chauffee: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    enum_cfg_installation_ch_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 11,
                            "nillable": True,
                        },
                    )
                    enum_type_installation_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 4,
                            "nillable": True,
                        },
                    )

                @dataclass
                class DonneeIntermediaire:
                    """
                    Attributes:
                        besoin_ch: Besoin de chauffage total de
                            l'installation (kWh)
                        conso_ch: consommation d'energie annuelle de
                            l'installation de chauffage en energie
                            finale kWh. Dans le cas d'un DPE immeuble ou
                            d'un DPE appartement à partir de l'immeuble
                            c'est la consommation de l'installation à
                            l'immeuble qu'il faut saisir.
                    """

                    besoin_ch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_exclusive": 0.0,
                            "nillable": True,
                        },
                    )
                    conso_ch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": 0.0,
                            "nillable": True,
                        },
                    )

                @dataclass
                class EmetteurChauffageCollection:
                    emetteur_chauffage: List[
                        "Dpe.LogementNeuf.InstallationChauffageCollection.InstallationChauffage.EmetteurChauffageCollection.EmetteurChauffage"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                    @dataclass
                    class EmetteurChauffage:
                        donnee_entree: Optional[
                            "Dpe.LogementNeuf.InstallationChauffageCollection.InstallationChauffage.EmetteurChauffageCollection.EmetteurChauffage.DonneeEntree"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )

                        @dataclass
                        class DonneeEntree:
                            """
                            Attributes:
                                description: description textuelle de
                                    l'objet
                                reference: reference projet de l'objet
                                    (cette référence permet de faire
                                    d'éventuels liens entre objets). La
                                    codification et utilisation des
                                    références peut différer entre
                                    logiciels
                                surface_chauffee: surface chauffée par
                                    l'emetteur (sous ensemble de la
                                    surface chauffée par
                                    l'installation). Dans le cas d'un
                                    DPE immeuble ou d'un DPE appartement
                                    à partir de l'immeuble c'est la
                                    surface de l'installation à
                                    l'immeuble qu'il faut renseigner
                                enum_type_emission_distribution_id:
                                    enumérateur qui couple les notions
                                    d'emission et de distribution pour
                                    produire une description complète
                                    des emetteurs de chauffage
                                reseau_distribution_isole: est ce que le
                                    réseau de distribution est isolé 0 :
                                    non 1 : oui
                                enum_periode_installation_emetteur_id:
                                    période d'installation des émetteurs
                                    de chauffage (utilisé pour le calcul
                                    des températures de fonctionnement
                                    des systèmes à combustion de type
                                    chaudière gaz ou fioul)
                                enum_temp_distribution_ch_id:
                                    température de distribution de
                                    l'installation de chauffage (pour le
                                    calcul des auxiliaires de
                                    distribution)
                            """

                            description: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            reference: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            surface_chauffee: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            enum_type_emission_distribution_id: Optional[
                                int
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 50,
                                    "nillable": True,
                                },
                            )
                            reseau_distribution_isole: Optional[SOuiNon] = (
                                field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "nillable": True,
                                    },
                                )
                            )
                            enum_periode_installation_emetteur_id: Optional[
                                int
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 3,
                                    "nillable": True,
                                },
                            )
                            enum_temp_distribution_ch_id: Optional[int] = (
                                field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                        "min_inclusive": 1,
                                        "max_inclusive": 4,
                                        "nillable": True,
                                    },
                                )
                            )

                @dataclass
                class GenerateurChauffageCollection:
                    generateur_chauffage: List[
                        "Dpe.LogementNeuf.InstallationChauffageCollection.InstallationChauffage.GenerateurChauffageCollection.GenerateurChauffage"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )

                    @dataclass
                    class GenerateurChauffage:
                        donnee_entree: Optional[
                            "Dpe.LogementNeuf.InstallationChauffageCollection.InstallationChauffage.GenerateurChauffageCollection.GenerateurChauffage.DonneeEntree"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )
                        donnee_intermediaire: Optional[
                            "Dpe.LogementNeuf.InstallationChauffageCollection.InstallationChauffage.GenerateurChauffageCollection.GenerateurChauffage.DonneeIntermediaire"
                        ] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "nillable": True,
                            },
                        )

                        @dataclass
                        class DonneeEntree:
                            """
                            Attributes:
                                description: description textuelle de
                                    l'objet
                                reference: reference projet de l'objet
                                    (cette référence permet de faire
                                    d'éventuels liens entre objets). La
                                    codification et utilisation des
                                    références peut différer entre
                                    logiciels
                                ref_produit_generateur_ch: référence
                                    produit et marque du générateur de
                                    chauffage
                                enum_type_generateur_ch_id: type de
                                    generateur de chauffage
                                enum_usage_generateur_id: usages assurés
                                    par le générateur
                                    (chauffage/ecs/chauffage+ecs)
                                enum_type_energie_id: type d'énergie
                                    consommée par le générateur de
                                    chauffage
                                position_volume_chauffe: est ce que le
                                    générateur est positionné dans le
                                    volume chauffé. (pour le calcul des
                                    pertes de génération récupérables)
                                tv_reseau_chaleur_id: id de la ligne de
                                    la table utilisée pour le calcul du
                                    contenu CO2 des réseaux de chaleurs
                                    (OBSOLETE et remplacé par
                                    identifiant_reseau_chaleur à partir
                                    du 18 janvier 2022 et la prise en
                                    compte du nouvel arrêté réseau de
                                    chaleur).
                                identifiant_reseau_chaleur: identifiant
                                    réseau de chaleur ou de froid
                                    utilisé (utilisé à partir du 18
                                    janvier 2022)
                                n_radiateurs_gaz: nombre de radiateurs
                                    gaz
                                presence_ventouse: présence d'un système
                                    de ventouse ou avec un ventilateur
                                    pour l'évacuation des fumées d'un
                                    système à combustion 0 : non 1 : oui
                                presence_regulation_combustion: présence
                                    d'un organe de régulation pour le
                                    système de chauffage à combustion 0
                                    : non 1 : oui
                                enum_methode_saisie_carac_sys_id:
                                    méthode de saisie des performances
                                    du système de chauffage
                            """

                            description: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            reference: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            ref_produit_generateur_ch: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "max_length": 255,
                                    "nillable": True,
                                },
                            )
                            enum_type_generateur_ch_id: Optional[
                                DonneeEntreeEnumTypeGenerateurChId
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            enum_usage_generateur_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 3,
                                    "nillable": True,
                                },
                            )
                            enum_type_energie_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 15,
                                    "nillable": True,
                                },
                            )
                            position_volume_chauffe: Optional[SOuiNon] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            tv_reseau_chaleur_id: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 1,
                                    "max_inclusive": 797,
                                    "nillable": True,
                                },
                            )
                            identifiant_reseau_chaleur: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "pattern": r"[0-9]{4}[C-F]",
                                    "nillable": True,
                                },
                            )
                            n_radiateurs_gaz: Optional[int] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0,
                                    "nillable": True,
                                },
                            )
                            presence_ventouse: Optional[SOuiNon] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            presence_regulation_combustion: Optional[
                                SOuiNon
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )
                            enum_methode_saisie_carac_sys_id: Optional[
                                DonneeEntreeEnumMethodeSaisieCaracSysId
                            ] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "nillable": True,
                                },
                            )

                        @dataclass
                        class DonneeIntermediaire:
                            """
                            Attributes:
                                scop: scop du générateur thermodynamique
                                    (en remplacement du Rg pour les
                                    générateurs thermodynamique) (0-20)
                                pn: puissance nominale du générateur à
                                    combustion (W)
                                qp0: pertes à l'arret du générateur à
                                    combustion. Dans le cas d'un
                                    générateur virtualisé pour DPE
                                    appartement avec chauffage collectif
                                    saisir Qp0 correspondant à Pe =
                                    a*Pn(collectif) (W)
                                pveilleuse: puissance de la veilleuse du
                                    générateur à combustion (W)
                                temp_fonc_30: température de
                                    fonctionnement à 30% de charge (°C)
                                temp_fonc_100: température de
                                    fonctionnement à 100% de charge (°C)
                                rpn: rendement de génération à pleine
                                    charge du générateur à combustion
                                    (0-1,5)
                                rpint: rendement de génération à charge
                                    intermédiaire du générateur à
                                    combustion (0-1,5)
                                conso_ch: consommation d'energie
                                    annuelle du générateur de chauffage
                                    en energie finale kWh (exprimée en
                                    kWh PCI pour les combustibles). Dans
                                    le cas d'un DPE immeuble ou d'un DPE
                                    appartement à partir de l'immeuble
                                    c'est la consommation du générateur
                                    à l'immeuble qu'il faut saisir.
                            """

                            scop: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 1.0,
                                    "max_inclusive": 8.0,
                                    "nillable": True,
                                },
                            )
                            pn: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 100.0,
                                    "nillable": True,
                                },
                            )
                            qp0: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            pveilleuse: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            temp_fonc_30: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            temp_fonc_100: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "nillable": True,
                                },
                            )
                            rpn: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.5,
                                    "nillable": True,
                                },
                            )
                            rpint: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_exclusive": 0.0,
                                    "max_inclusive": 1.5,
                                    "nillable": True,
                                },
                            )
                            conso_ch: Optional[float] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": 0.0,
                                    "nillable": True,
                                },
                            )

        @dataclass
        class Sortie:
            deperdition: Optional["Dpe.LogementNeuf.Sortie.Deperdition"] = (
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
            )
            apport_et_besoin: Optional[
                "Dpe.LogementNeuf.Sortie.ApportEtBesoin"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "nillable": True,
                },
            )
            ef_conso: Optional["Dpe.LogementNeuf.Sortie.EfConso"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            ep_conso: Optional["Dpe.LogementNeuf.Sortie.EpConso"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            emission_ges: Optional["Dpe.LogementNeuf.Sortie.EmissionGes"] = (
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
            )
            cout: Optional["Dpe.LogementNeuf.Sortie.Cout"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            production_electricite: Optional[
                "Dpe.LogementNeuf.Sortie.ProductionElectricite"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            sortie_par_energie_collection: Optional[
                "Dpe.LogementNeuf.Sortie.SortieParEnergieCollection"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            confort_ete: Optional["Dpe.LogementNeuf.Sortie.ConfortEte"] = (
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
            )
            qualite_isolation: Optional[
                "Dpe.LogementNeuf.Sortie.QualiteIsolation"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )

            @dataclass
            class Deperdition:
                """
                Attributes:
                    hvent: part des deperditions de renouvellement d'air
                        liées au système de(W/K) ventilation. Pour les
                        DPE immeubles et appartement à partir de
                        l'immeuble ces données sont à l'immeuble.
                    hperm: part des deperditions de renouvellement d'air
                        liées à la perméabilité à l'air du
                        bâtiment(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_renouvellement_air: deperditions par
                        renouvellement d'air totale (hvent +
                        hperm)(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_mur: deperditions par les murs(W/K).
                        Pour les DPE immeubles et appartement à partir
                        de l'immeuble ces données sont à l'immeuble.
                    deperdition_plancher_bas: deperditions par les
                        planchers bas(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_plancher_haut: deperditions par les
                        planchers hauts(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_baie_vitree: deperditions par les baies
                        vitrées (W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_porte: deperditions par les ponts
                        thermiques(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_pont_thermique: deperditions par les
                        ponts thermiques(W/K). Pour les DPE immeubles et
                        appartement à partir de l'immeuble ces données
                        sont à l'immeuble.
                    deperdition_enveloppe: deperditions par l'enveloppe
                        (GV). Pour les DPE immeubles et appartement à
                        partir de l'immeuble ces données sont à
                        l'immeuble.
                """

                hvent: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                hperm: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_exclusive": 0.0,
                        "nillable": True,
                    },
                )
                deperdition_renouvellement_air: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_exclusive": 0.0,
                        "nillable": True,
                    },
                )
                deperdition_mur: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                deperdition_plancher_bas: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                deperdition_plancher_haut: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                deperdition_baie_vitree: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                deperdition_porte: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                deperdition_pont_thermique: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                deperdition_enveloppe: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_exclusive": 0.0,
                        "nillable": True,
                    },
                )

            @dataclass
            class ApportEtBesoin:
                """
                Attributes:
                    besoin_ch: besoin de chauffage annuel total du
                        logement ou immeuble (kWh) . Pour les DPE
                        immeubles ces données sont à l'immeuble. Pour
                        les dpe appartements à partir de l'immeuble ces
                        données sont à l'appartement
                    besoin_ecs: besoin d'ecs annuel total du bâtiment
                        (kWh). Pour les DPE immeubles ces données sont à
                        l'immeuble. Pour les dpe appartements à partir
                        de l'immeuble ces données sont à l'appartement
                    besoin_fr: besoin de refroidissement annuel
                        (kWh).Pour les DPE immeubles ces données sont à
                        l'immeuble. Pour les dpe appartements à partir
                        de l'immeuble ces données sont à l'appartement
                """

                besoin_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                besoin_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )
                besoin_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_inclusive": 0.0,
                        "nillable": True,
                    },
                )

            @dataclass
            class EfConso:
                """
                Attributes:
                    conso_ch: consommation annuelle de chauffage en
                        energie finale (déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_ch_depensier: consommation annuelle de
                        chauffage en energie finale pour le scénario
                        dépensier(déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_ecs: consommation annuelle d'ECS en energie
                        finale (déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_ecs_depensier: consommation annuelle d'ECS en
                        energie finale pour le scénario dépensier
                        (déduit de la production pv autoconsommée)
                        (kWhef/an)
                    conso_eclairage: consommation annuelle d'eclairage
                        en energie finale (déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_auxiliaire_ventilation: consommation annuelle
                        d'auxilliaires de ventilation en energie finale
                        (kWhef/an)
                    conso_totale_auxiliaire: consommation annuelle de
                        l'ensemble des auxiliaires en énergie
                        finale(déduit de la production pv autoconsommée)
                        (kWhef/an)
                    conso_fr: consommation de refroidissement annuel en
                        energie finale (déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_fr_depensier: consommation de refroidissement
                        annuel en energie finale pour le scénario
                        dépensier (déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_5_usages: consommation annuelle 5 usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)en
                        energie finale(déduit de la production pv
                        autoconsommée) (kWhef/an)
                    conso_5_usages_m2: consommation annuelle 5 usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)en
                        energie finale(déduit de la production pv
                        autoconsommée) (kWhef/m²/an)
                """

                conso_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_ch_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_ecs_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_eclairage: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                conso_auxiliaire_ventilation: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_totale_auxiliaire: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_fr_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_5_usages: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                conso_5_usages_m2: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )

            @dataclass
            class EpConso:
                """
                Attributes:
                    ep_conso_ch: consommation annuelle de chauffage en
                        energie primaire(déduit de la production pv
                        autoconsommée) (kWhep/an)
                    ep_conso_ch_depensier: consommation annuelle de
                        chauffage en energie primaire pour le scénario
                        dépensier (déduit de la production pv
                        autoconsommée) (kWhep/an)
                    ep_conso_ecs: consommation annuelle d'ECS en energie
                        primaire (déduit de la production pv
                        autoconsommée) (kWhep/an)
                    ep_conso_ecs_depensier: consommation annuelle d'ECS
                        en energie primaire pour le scénario dépensier
                        (déduit de la production pv autoconsommée)
                        (kWhep/an)
                    ep_conso_eclairage: consommation annuelle
                        d'eclairage en energie primaire (déduit de la
                        production pv autoconsommée) (kWhep/an)
                    ep_conso_auxiliaire_ventilation: consommation
                        annuelle d'auxilliaires de ventilation en
                        energie primaire (kWhep/an)
                    ep_conso_totale_auxiliaire: consommation annuelle de
                        l'ensemble des auxiliaires en energie primaire
                        (déduit de la production pv autoconsommée)
                        (kWhep/an)
                    ep_conso_fr: consommation de refroidissement annuel
                        en énergie primaire (déduit de la production pv
                        autoconsommée) (kWhep/an)
                    ep_conso_fr_depensier: consommation de
                        refroidissement annuel en énergie primaire pour
                        le scénario dépensier (déduit de la production
                        pv autoconsommée) (kWhep/an)
                    ep_conso_5_usages: consommation annuelle 5 usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)en
                        energie primaire (déduit de la production pv
                        autoconsommée) (kWhep/an)
                    ep_conso_5_usages_m2: consommation annuelle 5 usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)en
                        energie primaire (déduit de la production pv
                        autoconsommée) (kWhep/m²/an)
                    classe_bilan_dpe: Classe du DPE issu de la synthèse
                        du double seuil sur les consommations énergie
                        primaire et les émissions de CO2 sur les 5
                        usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)
                """

                ep_conso_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_ch_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_ecs_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_eclairage: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                ep_conso_auxiliaire_ventilation: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_totale_auxiliaire: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_fr_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_5_usages: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                ep_conso_5_usages_m2: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                classe_bilan_dpe: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"[A-G]",
                    },
                )

            @dataclass
            class EmissionGes:
                """
                Attributes:
                    emission_ges_ch: estimation GES de chauffage (déduit
                        de la production pv autoconsommée) (kgCO2/an)
                    emission_ges_ch_depensier: estimation GES de
                        chauffage pour le scénario dépensier(déduit de
                        la production pv autoconsommée) (kgCO2/an)
                    emission_ges_ecs: estimation GES d'ECS (déduit de la
                        production pv autoconsommée) (kgCO2/an)
                    emission_ges_ecs_depensier: estimation GES d'ECS
                        pour le scénario dépensier (déduit de la
                        production pv autoconsommée) (kgCO2/an)
                    emission_ges_eclairage: estimation GES d'eclairage
                        (déduit de la production pv autoconsommée)
                        (kgCO2/an)
                    emission_ges_auxiliaire_ventilation: estimation GES
                        d'auxilliaires de ventilation (kgCO2/an)
                    emission_ges_totale_auxiliaire: estimation GES de
                        l'ensemble des auxiliaires (déduit de la
                        production pv autoconsommée) (kgCO2/an)
                    emission_ges_fr: estimation GES de refroidissement
                        annuel (déduit de la production pv
                        autoconsommée) (kgCO2/an)
                    emission_ges_fr_depensier: estimation GES de
                        refroidissement pour le scénario dépensier
                        (déduit de la production pv autoconsommée)
                        (kgCO2/an)
                    emission_ges_5_usages: estimation GES totale 5
                        usages (déduit de la production pv
                        autoconsommée)
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/an)
                    emission_ges_5_usages_m2: estimation GES totale 5
                        usages rapportée au m² (déduit de la production
                        pv autoconsommée)
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an)
                    classe_emission_ges: classe d'estimation ges du DPE
                        5 usages
                """

                emission_ges_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_ch_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_ecs_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_eclairage: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                emission_ges_auxiliaire_ventilation: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_totale_auxiliaire: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_fr_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_5_usages: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                emission_ges_5_usages_m2: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                classe_emission_ges: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "pattern": r"[A-G]",
                    },
                )

            @dataclass
            class Cout:
                """
                Attributes:
                    cout_ch: coût de chauffage(déduit de la production
                        pv autoconsommée) (€)
                    cout_ch_depensier: coût de chauffage pour le
                        scénario dépensier (déduit de la production pv
                        autoconsommée) (€)
                    cout_ecs: coût de l'ECS (déduit de la production pv
                        autoconsommée) (€)
                    cout_ecs_depensier: coût de l'ECS pour le scénario
                        dépensier (déduit de la production pv
                        autoconsommée) (€)
                    cout_eclairage: coût des eclairage (déduit de la
                        production pv autoconsommée) (€)
                    cout_auxiliaire_ventilation: coût des auxilliaires
                        de ventilation (€)
                    cout_total_auxiliaire: coût des auxilliaires de
                        l'ensemble des auxiliaires (déduit de la
                        production pv autoconsommée) (€)
                    cout_fr: coût de refroidissement annuel (déduit de
                        la production pv autoconsommée) (€)
                    cout_fr_depensier: coût de refroidissement pour le
                        scénario dépensier (déduit de la production pv
                        autoconsommée) (€)
                    cout_5_usages: coût totale 5 usages
                        (ecs/chauffage/climatisation/eclairage/auxiliaires)
                        (déduit de la production pv autoconsommée) (€)
                """

                cout_ch: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_ch_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_ecs: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_ecs_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_eclairage: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                cout_auxiliaire_ventilation: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_total_auxiliaire: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_fr: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_fr_depensier: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )
                cout_5_usages: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )

            @dataclass
            class ProductionElectricite:
                """
                Attributes:
                    production_pv: production d'éléctricité
                        photovoltaique(kWhep/an)
                """

                production_pv: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0.0,
                    },
                )

            @dataclass
            class SortieParEnergieCollection:
                sortie_par_energie: List[
                    "Dpe.LogementNeuf.Sortie.SortieParEnergieCollection.SortieParEnergie"
                ] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                    },
                )

                @dataclass
                class SortieParEnergie:
                    """
                    Attributes:
                        enum_type_energie_id: type d'énergie
                        conso_ch: consommation de chauffage en énergie
                            finale pour l'énergie considérée (kWhef/an)
                        conso_ecs: consommation d'ECS en énergie finale
                            pour l'énergie considérée (kWhef/an)
                        conso_5_usages: consommation totale en énergie
                            finale pour l'énergie considérée (kWhef/an)
                        emission_ges_ch: estimation GES de chauffage
                            pour l'énergie considérée (kgCO2/an)
                        emission_ges_ecs: estimation GES d'ECS pour
                            l'énergie considérée (kgCO2/an)
                        emission_ges_5_usages: estimation GES totale
                            pour l'énergie considérée (kgCO2/an)
                        cout_ch: coût lié au chauffage pour l'énergie
                            considérée (€)
                        cout_ecs: coût lié à l'ECS pour l'énergie
                            considérée (€)
                        cout_5_usages: coût totale pour l'énergie
                            considérée (€)
                    """

                    enum_type_energie_id: Optional[int] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 1,
                            "max_inclusive": 15,
                        },
                    )
                    conso_ch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    conso_ecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    conso_5_usages: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    emission_ges_ch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    emission_ges_ecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    emission_ges_5_usages: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    cout_ch: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    cout_ecs: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )
                    cout_5_usages: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_inclusive": 0.0,
                        },
                    )

            @dataclass
            class ConfortEte:
                """
                Attributes:
                    isolation_toiture: as-t-on une isolation de toiture
                        0 : non 1 : oui
                    protection_solaire_exterieure: as-t-on une
                        protection solair exteriaire sur les facades
                        vitrées (exception nord) 0 : non 1 : oui
                    aspect_traversant: est ce que le logement est
                        traversant 0 : non 1 : oui
                    brasseur_air: est ce que le logement est équipé de
                        brasseurs d'air 0 : non 1 : oui
                    inertie_lourde: est ce que le logement possède une
                        inerte lourde ou très lourde 0 : non 1 : oui
                    enum_indicateur_confort_ete_id: indicateur confort
                        été (bon moyen ou mauvais)
                """

                isolation_toiture: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                protection_solaire_exterieure: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                aspect_traversant: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                brasseur_air: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                inertie_lourde: Optional[SOuiNon] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                enum_indicateur_confort_ete_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 3,
                    },
                )

            @dataclass
            class QualiteIsolation:
                """
                Attributes:
                    ubat: Ubat(W/m²K)
                    qualite_isol_enveloppe: qualité d'isolation de
                        l'enveloppe
                    qualite_isol_mur: qualité d'isolation des murs
                    qualite_isol_plancher_haut_toit_terrasse: qualité
                        d'isolation de la toiture/planchers hauts partie
                        toit terrasse
                    qualite_isol_plancher_haut_comble_perdu: qualité
                        d'isolation de la toiture/planchers hauts partie
                        comble perdue
                    qualite_isol_plancher_haut_comble_amenage: qualité
                        d'isolation de la toiture/planchers hauts partie
                        comble aménagé
                    qualite_isol_plancher_bas: qualité de l'isolation
                        des planchers
                    qualite_isol_menuiserie: qualité d'isolation des
                        menuiseries
                """

                ubat: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_exclusive": 0.0,
                    },
                )
                qualite_isol_enveloppe: Optional[SQualite] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                qualite_isol_mur: Optional[SQualite] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                qualite_isol_plancher_haut_toit_terrasse: Optional[
                    SQualite
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                qualite_isol_plancher_haut_comble_perdu: Optional[SQualite] = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "nillable": True,
                        },
                    )
                )
                qualite_isol_plancher_haut_comble_amenage: Optional[
                    SQualite
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                qualite_isol_plancher_bas: Optional[SQualite] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "nillable": True,
                    },
                )
                qualite_isol_menuiserie: Optional[SQualite] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )

        @dataclass
        class Rset:
            """
            Attributes:
                any_element: xml RSET du bâtiment neuf provenant de
                    l'étude réglementaire RT2012 du bâtiment à sa
                    construction
            """

            any_element: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "process_contents": "skip",
                },
            )

        @dataclass
        class Rsee:
            """
            Attributes:
                any_element: xml RSEE du bâtiment neuf provenant de
                    l'étude réglementaire RE2020 du bâtiment à sa
                    construction
            """

            any_element: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "process_contents": "skip",
                },
            )
