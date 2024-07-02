from enums import enums
from utils import tv, requestInput, requestInputID, getKeyByValue, bug_for_bug_compat
from _3_1_b import b

script_name = __file__

def tv_umur0(di, de, du):
    matcher = {
        'enum_materiaux_structure_mur_id': de['enum_materiaux_structure_mur_id']
    }
    if de['enum_materiaux_structure_mur_id'] not in [1, 20]:
        matcher['epaisseur_structure'] = requestInput(de, du, 'epaisseur_structure', 'float')
        if not matcher['epaisseur_structure']:
            desc = de['description']
            matcher['epaisseur_structure'] = desc.match(r'(\d+) cm')[1]
    row = tv('umur0', matcher)
    # row = tv('umur0', matcher, de)
    if row:
        di['umur0'] = float(row['umur0'])
        de['tv_umur0_id'] = int(row['tv_umur0_id'])
    else:
        print('!! pas de valeur forfaitaire trouvée pour umur0 !!')

def tv_umur(di, de, du, pc_id, zc, ej):
    matcher = {
        'enum_periode_construction_id': pc_id,
        'enum_zone_climatique_id': zc,
        'effet_joule': ej
    }
    row = tv('umur', matcher, de)
    if row:
        di['umur'] = float(row['umur'])
        de['tv_umur_id'] = int(row['tv_umur_id'])
    else:
        print('!! pas de valeur forfaitaire trouvée pour umur !!')

def calc_umur0(di, de, du):
    umur0_avant = di.get('umur0')
    methode_saisie_u0 = requestInput(de, du, 'methode_saisie_u0')
    if methode_saisie_u0 == 'type de paroi inconnu (valeur par défaut)':
        de['enum_materiaux_structure_mur_id'] = getKeyByValue(enums["materiaux_structure_mur"], 'inconnu')
        tv_umur0(di, de, du)
    elif methode_saisie_u0 == 'déterminé selon le matériau et épaisseur à partir de la table de valeur forfaitaire':
        requestInput(de, du, 'materiaux_structure_mur')
        tv_umur0(di, de, du)
    elif methode_saisie_u0 in [
        'saisie direct u0 justifiée à partir des documents justificatifs autorisés',
        "saisie direct u0 correspondant à la performance de la paroi avec son isolation antérieure iti (umur_iti) lorsqu'il y a une surisolation ite réalisée"
    ]:
        di['umur0'] = requestInput(de, du, 'umur0_saisi', 'float')
    elif methode_saisie_u0 == 'u0 non saisi car le u est saisi connu et justifié.':
        pass
    else:
        print('methode_saisie_u0 inconnue:', methode_saisie_u0)

    if requestInput(de, du, 'enduit_isolant_paroi_ancienne', 'bool') == 1:
        if umur0_avant == di.get('umur0'):
            print(f'BUG({script_name}) correction isolation pour parois anciennes pas appliqué')
            if bug_for_bug_compat:
                di['umur0'] = umur0_avant
            else:
                di['umur0'] = 1 / (1 / di['umur0'] + 0.7)
        else:
            di['umur0'] = 1 / (1 / di['umur0'] + 0.7)

    type_doublage = requestInput(de, du, 'type_doublage')
    if type_doublage == "doublage indéterminé ou lame d'air inf 15 mm":
        di['umur0'] = 1 / (1 / di['umur0'] + 0.1)
    elif type_doublage in ["doublage indéterminé avec lame d'air sup 15 mm", 'doublage connu (plâtre brique bois)']:
        di['umur0'] = 1 / (1 / di['umur0'] + 0.21)
    di['umur0'] = min(2.5, di['umur0'])

def calc_mur(mur, zc, pc_id, ej):
    de = mur['donnee_entree']
    du = {}
    di = {}
    di['umur0'] = mur['donnee_intermediaire'].get('umur0')  # pour comparaison

    requestInput(de, du, 'surface_paroi_totale', 'float')
    requestInput(de, du, 'orientation')

    b(di, de, du, zc)

    methode_saisie_u = requestInput(de, du, 'methode_saisie_u')
    if methode_saisie_u == 'non isolé':
        calc_umur0(di, de, du)
        di['umur'] = min(di['umur0'], 2.5)
    elif methode_saisie_u in ['epaisseur isolation saisie justifiée par mesure ou observation', 'epaisseur isolation saisie justifiée à partir des documents justificatifs autorisés']:
        calc_umur0(di, de, du)
        e = requestInput(de, du, 'epaisseur_isolation', 'int') * 0.01
        di['umur'] = 1 / (1 / di['umur0'] + e / 0.04)
    elif methode_saisie_u in ["resistance isolation saisie justifiée observation de l'isolant installé et mesure de son épaisseur", 'resistance isolation saisie justifiée  à partir des documents justificatifs autorisés']:
        calc_umur0(di, de, du)
        r = requestInput(de, du, 'resistance_isolation', 'float')
        di['umur'] = 1 / (1 / di['umur0'] + r)
    elif methode_saisie_u == 'isolation inconnue  (table forfaitaire)':
        calc_umur0(di, de, du)
        tv_umur(di, de, du, pc_id, zc, ej)
        di['umur'] = min(di['umur'], di['umur0'])
    elif methode_saisie_u == "année d'isolation différente de l'année de construction saisie justifiée (table forfaitaire)":
        calc_umur0(di, de, du)
        pi_id = requestInputID(de, du, 'periode_isolation')
        tv_umur(di, de, du, pi_id, zc, ej)
        di['umur'] = min(di['umur'], di['umur0'])
    elif methode_saisie_u == 'année de construction saisie (table forfaitaire)':
        calc_umur0(di, de, du)
        pi_id = de.get('enum_periode_isolation_id') or pc_id
        if not de.get('enum_periode_isolation_id'):
            pc = enums["periode_construction"][pc_id]
            if pc in ['avant 1948', '1948-1974']:
                pi_id = int(getKeyByValue(enums["periode_isolation"], '1975-1977'))
        tv_umur_avant = de.get('tv_umur_id')
        tv_umur(di, de, du, pi_id, zc, ej)
        if de.get('tv_umur_id') != tv_umur_avant and pi_id != pc_id:
            print(f'BUG({script_name}) Si année de construction <74 alors Année d\'isolation=75-77 (3CL page 13)')
            if bug_for_bug_compat:
                tv_umur(di, de, du, pc_id, zc, ej)
        di['umur'] = min(di['umur'], di['umur0'])
    elif methode_saisie_u in ['saisie direct u justifiée  (à partir des documents justificatifs autorisés)', 'saisie direct u depuis rset/rsee( etude rt2012/re2020)']:
        di['umur'] = requestInput(de, du, 'umur_saisi', 'float')
    else:
        print('methode_saisie_u inconnue:', methode_saisie_u)
    mur['donnee_utilisateur'] = du
    mur['donnee_intermediaire'] = di
