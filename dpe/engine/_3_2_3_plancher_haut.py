from enums import enums
from _3_1_b import b
from utils import tv, requestInput, getKeyByValue, bug_for_bug_compat

scriptName = __file__.split("/")[-1]


def tv_uph0(di, de, du):
    requestInput(de, du, "type_plancher_haut")
    matcher = {"enum_type_plancher_haut_id": de["enum_type_plancher_haut_id"]}
    row = tv("uph0", matcher)
    if row:
        di["uph0"] = float(row["uph0"])
        de["tv_uph0_id"] = int(row["tv_uph0_id"])
    else:
        print("!! pas de valeur forfaitaire trouvée pour uph0 !!")


def tv_uph(di, de, du, pc_id, zc, ej):
    type_adjacence = requestInput(de, du, "type_adjacence")
    type_ph = requestInput(de, du, "type_plancher_haut")
    type_toiture = "combles" if type_adjacence != "extérieur" else "terrasse"
    if type_ph == "combles aménagés sous rampant":
        type_toiture = "combles"
    if "donnant sur l'extérieur (combles aménagés)" in de["description"]:
        print(f"BUG({scriptName}) extérieur != combles")
        if bug_for_bug_compat:
            type_toiture = "combles"
    matcher = {
        "enum_periode_construction_id": pc_id,
        "enum_zone_climatique_id": zc,
        "effet_joule": ej,
        "type_toiture": type_toiture,
    }
    row = tv("uph", matcher)
    if row:
        di["uph"] = float(row["uph"])
        de["tv_uph_id"] = int(row["tv_uph_id"])
    else:
        print("!! pas de valeur forfaitaire trouvée pour uph !!")


def calc_uph0(di, de, du):
    methode_saisie_u0 = requestInput(de, du, "methode_saisie_u0")
    if methode_saisie_u0 in [
        "type de paroi inconnu (valeur par défaut)",
        "déterminé selon le matériau et épaisseur à partir de la table de valeur forfaitaire",
    ]:
        tv_uph0(di, de, du)
    elif methode_saisie_u0 in [
        "saisie direct u0 justifiée à partir des documents justificatifs autorisés",
        "saisie direct u0 correspondant à la performance de la paroi avec son isolation antérieure iti (umur_iti) lorsqu'il y a une surisolation ite réalisée",
    ]:
        di["uph0"] = requestInput(de, du, "uph0_saisi")
    elif methode_saisie_u0 == "u0 non saisi car le u est saisi connu et justifié.":
        pass
    else:
        print("methode_saisie_u0 inconnue:", methode_saisie_u0)


def calc_ph(ph, zc, pc_id, ej):
    de = ph["donnee_entree"]
    du = {}
    di = {}

    b(di, de, du, zc)

    methode_saisie_u = requestInput(de, du, "methode_saisie_u")

    if methode_saisie_u == "non isolé":
        calc_uph0(di, de, du)
        di["uph"] = di["uph0"]
    elif methode_saisie_u in [
        "epaisseur isolation saisie justifiée par mesure ou observation",
        "epaisseur isolation saisie justifiée à partir des documents justificatifs autorisés",
    ]:
        e = requestInput(de, du, "epaisseur_isolation", "int") * 0.01
        calc_uph0(di, de, du)
        di["uph"] = 1 / (1 / di["uph0"] + e / 0.04)
    elif methode_saisie_u in [
        "resistance isolation saisie justifiée observation de l'isolant installé et mesure de son épaisseur",
        "resistance isolation saisie justifiée  à partir des documents justificatifs autorisés",
    ]:
        r = requestInput(de, du, "resistance_isolation", "float")
        calc_uph0(di, de, du)
        di["uph"] = 1 / (1 / di["uph0"] + r)
    elif methode_saisie_u in [
        "isolation inconnue  (table forfaitaire)",
        "année d'isolation différente de l'année de construction saisie justifiée (table forfaitaire)",
    ]:
        tv_uph(di, de, du, de["enum_periode_isolation_id"], zc, ej)
        calc_uph0(di, de, du)
        di["uph"] = min(di["uph"], di["uph0"])
    elif methode_saisie_u == "année de construction saisie (table forfaitaire)":
        pi_id = pc_id
        pc = enums["periode_construction"][pc_id]
        if pc in ["avant 1948", "1948-1974"]:
            pi_id = getKeyByValue(enums["periode_isolation"], "1975-1977")
        calc_uph0(di, de, du)
        tv_uph_avant = de.get("tv_uph_id")
        tv_uph(di, de, du, pi_id, zc, ej)
        di["uph"] = min(di["uph"], di["uph0"])
        if de.get("tv_uph_id") != tv_uph_avant and pi_id != pc_id:
            print(
                f"BUG({scriptName}) Si année de construction <74 alors Année d'isolation=75-77 (3CL page 21)"
            )
            if bug_for_bug_compat:
                tv_uph(di, de, du, pc_id, zc, ej)
        di["uph"] = min(di["uph"], di["uph0"])
    elif methode_saisie_u in [
        "saisie direct u justifiée  (à partir des documents justificatifs autorisés)",
        "saisie direct u depuis rset/rsee( etude rt2012/re2020)",
    ]:
        di["uph"] = requestInput(de, du, "uph_saisi")
    else:
        print("methode_saisie_u inconnue:", methode_saisie_u)

    ph["donnee_utilisateur"] = du
    ph["donnee_intermediaire"] = di
