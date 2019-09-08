body_types = {'Stocky', 'Normal', 'Lean'}

def transform_body_type(x):
    if x in body_types:
        return x
    else:
        return 'Normal'


def transfrom_height(x):
    """
    transform U.S customary units to cm
    """
    foot_cm_multiplyer = 30.48
    inch_cm_multiplyer  = 2.54
    foot, inch = x.split("\'")
    foot, inch = int(foot), int(inch)  
    return (foot * foot_cm_multiplyer) + (inch*inch_cm_multiplyer)


def transform_weight(x):
    """
    transform lbs string data into float int 
    """
    lbs_kg_multiplyer = 1.0 / 2.205
    return round(int(x.split('l')[0]) * lbs_kg_multiplyer, 2)


def transform_skill(x):
    """
    transform data with string format  "x+y" into int x
    for x='88+3' will return int 88 
    """
    return int(x.split('+')[0])


new_positions_map = {
    'ST': ['ST'],
    'CF': ['СF'],
    'LF': ['LF', 'LS', 'LW'],
    'RF': ['RF', 'RS', 'RW'],
    'CM': ['CAM', 'CDM', 'CM'],
    'LM': ['LAM', 'LDM', 'LM', 'LCM',],
    'RM': ['RAM', 'RCM', 'RDM', 'RM'],
    'CB': ['CB'],
    'LB': ['LCB', 'LWB'],
    'RB': ['RCB', 'RWB'],
}

def transform_target_position(x):
    if x in new_positions_map.keys():
        return x
    for key, positions in new_positions_map.items():
        if x in positions:
            return key