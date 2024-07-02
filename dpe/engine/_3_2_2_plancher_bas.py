from enums import enums
from _3_1_b import b
from utils import tv, requestInput, requestInputID, getKeyByValue, bug_for_bug_compat

scriptName = __file__.split('/')[-1]

def tv_upb0(di, de, du):
    requestInput(de, du, 'type_plancher_bas')
    matcher = {
        'enum_type_plancher_bas_id': de['enum_type_plancher_bas_id']
    }
    row = tv('upb0', matcher)
    if row:
        di['upb0'] = float(row['upb0'])
        de['tv_upb0_id'] = int(row['tv_upb0_id'])
    else:
        print('!! pas de valeur forfaitaire trouvée pour upb0 !!')

def tv_upb(di, de, du, pc_id, zc, ej):
    matcher = {
        'enum_periode_construction_id': pc_id,
        'enum_zone_climatique_id': zc,
        'effet_joule': ej
    }
    row = tv('upb', matcher)
    if row:
        di['upb'] = float(row['upb'])
        de['tv_upb_id'] = int(row['tv_upb_id'])
    else:
        print('!! pas de valeur forfaitaire trouvée pour upb !!')

def ue_ranges(inputNumber, ranges):
    result = []

    if inputNumber < ranges[0]:
        result.append(ranges[0])
        result.append(ranges[1])
    if inputNumber > ranges[-1]:
        result.append(ranges[-2])
        result.append(ranges[-1])
    if inputNumber in ranges:
        result.append(inputNumber)
        result.append(inputNumber)
    else:
        for index, range_value in enumerate(ranges):
            if inputNumber < range_value:
                if index > 0:
                    result.append(ranges[index - 1])
                else:
                    result.append(ranges[index])
                result.append(ranges[index])
                break
    return result

values_2s_p = [3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]

def tv_ue(di, de, du, pc_id, pb_list):
    type_adjacence = enums.type_adjacence[de['enum_type_adjacence_id']]
    if type_adjacence == 'terre-plein':
        if pc_id < 7:
            type_adjacence_plancher = 'terre plein bâtiment construit avant 2001'
            upb1, upb2 = ue_ranges(di['upb'], [0.46, 0.59, 0.85, 1.5, 3.4])
        else:
            type_adjacence_plancher = 'terre plein bâtiment construit à partir de 2001'
            upb1, upb2 = ue_ranges(di['upb'], [0.31, 0.37, 0.46, 0.6, 0.85, 1.5, 3.4])
    else:
        type_adjacence_plancher = 'plancher sur vide sanitaire ou sous-sol non chauffé'
        upb1, upb2 = ue_ranges(di['upb'], [0.31, 0.34, 0.37, 0.41, 0.45, 0.83, 1.43, 3.33])
    
    S = sum(pb['donnee_entree']['surface_paroi_opaque'] for pb in pb_list if enums.type_adjacence[pb['donnee_entree']['enum_type_adjacence_id']] in ['vide sanitaire', 'sous-sol non chauffé', 'terre-plein'])
    surface_ue = requestInput(de, du, 'surface_ue', 'float') or S
    perimetre_ue = requestInput(de, du, 'perimetre_ue', 'float')
    
    matcher = {
        'type_adjacence_plancher': type_adjacence_plancher,
        '2s_p': round((2 * surface_ue) / perimetre_ue)
    }
    matcher['2s_p'] = min(values_2s_p, key=lambda x: abs(x - matcher['2s_p']))
    matcher['2s_p'] = f'^{matcher["2s_p"]}$'
    
    matcher_1 = {**matcher, 'upb': str(upb1)}
    matcher_2 = {**matcher, 'upb': str(upb2)}
    
    row_1 = tv('ue', matcher_1)
    row_2 = tv('ue', matcher_2)
    
    delta_ue = float(row_2['ue']) - float(row_1['ue'])
    delta_upb = upb2 - upb1
    
    if delta_upb == 0:
        ue = float(row_1['ue'])
    else:
        ue = float(row_1['ue']) + (delta_ue * (di['upb'] - upb1)) / delta_upb
    
    de['ue'] = ue

def calc_upb0(di, de, du):
    methode_saisie_u0 = requestInput(de, du, 'methode_saisie_u0')
    if methode_saisie_u0 in ['type de paroi inconnu (valeur par défaut)', 'déterminé selon le matériau et épaisseur à partir de la table de valeur forfaitaire']:
        tv_upb0(di, de, du)
    elif methode_saisie_u0 in ['saisie direct u0 justifiée à partir des documents justificatifs autorisés', "saisie direct u0 correspondant à la performance de la paroi avec son isolation antérieure iti (umur_iti) lorsqu'il y a une surisolation ite réalisée"]:
        di['upb0'] = requestInput(de, du, 'upb0_saisi', 'float')
    elif methode_saisie_u0 == 'u0 non saisi car le u est saisi connu et justifié.':
        pass
    else:
        print('methode_saisie_u0 inconnue:', methode_saisie_u0)

def calc_pb(pb, zc, pc_id, ej, pb_list):
    de = pb['donnee_entree']
    du = {}
    di = {}

    b(di, de, du, zc)
    methode_saisie_u = requestInput(de, du, 'methode_saisie_u')
    print("methode: ",methode_saisie_u)
    if methode_saisie_u == 'non isolé':
        calc_upb0(di, de, du)
        di['upb'] = di['upb0']
    elif methode_saisie_u in ['epaisseur isolation saisie justifiée par mesure ou observation', 'epaisseur isolation saisie justifiée à partir des documents justificatifs autorisés']:
        e = requestInput(de, du, 'epaisseur_isolation', 'float') * 0.01
        calc_upb0(di, de, du)
        di['upb'] = 1 / (1 / di['upb0'] + e / 0.042)
    elif methode_saisie_u in ["resistance isolation saisie justifiée observation de l'isolant installé et mesure de son épaisseur", 'resistance isolation saisie justifiée  à partir des documents justificatifs autorisés']:
        r = requestInput(de, du, 'resistance_isolation', 'float')
        calc_upb0(di, de, du)
        di['upb'] = 1 / (1 / di['upb0'] + r)
    elif methode_saisie_u in ['isolation inconnue  (table forfaitaire)', "année d'isolation différente de l'année de construction saisie justifiée (table forfaitaire)"]:
        pi = requestInputID(de, du, 'periode_isolation')
        calc_upb0(di, de, du)
        tv_upb(di, de, du, pi, zc, ej)
        if "upb0" in di:
            di['upb'] = min(di['upb'], di['upb0'])
    elif methode_saisie_u == 'année de construction saisie (table forfaitaire)':
        pi_id = pc_id
        pc = enums.periode_construction[pc_id]
        if pc in ['avant 1948', '1948-1974']:
            pi_id = getKeyByValue(enums.periode_isolation, '1975-1977')
        calc_upb0(di, de, du)
        tv_upb_avant = de.get('tv_upb_id')
        tv_upb(di, de, du, pi_id, zc, ej)
        if de.get('tv_upb_id') != tv_upb_avant and pi_id != pc_id:
            print(f'BUG({scriptName}) Si année de construction <74 alors Année d\'isolation=75-77 (3CL page 17)')
            if bug_for_bug_compat:
                tv_upb(di, de, du, pc_id, zc, ej)
        di['upb'] = min(di['upb'], di['upb0'])
    elif methode_saisie_u in ['saisie direct u justifiée  (à partir des documents justificatifs autorisés)', 'saisie direct u depuis rset/rsee( etude rt2012/re2020)']:
        di['upb'] = requestInput(de, du, 'upb_saisi', 'float')
    else:
        print('methode_saisie_u inconnue:', methode_saisie_u)

    type_adjacence = requestInput(de, du, 'type_adjacence')
    print("type_adjacence: ",type_adjacence)
    if type_adjacence in ['vide sanitaire', 'sous-sol non chauffé', 'terre-plein']:
        tv_ue(di, de, du, pc_id, pb_list)
        di['upb_final'] = de['ue']
    else:
        if 'upb' in di:
            di['upb_final'] = di['upb']

    pb['donnee_utilisateur'] = du
    pb['donnee_intermediaire'] = di

