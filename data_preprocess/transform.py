from functools import partial


def transform_body_type(x):
    body_types = {'Stocky', 'Normal', 'Lean'}

    if x in body_types:
        return x
    else:
        return 'Normal'


def transfrom_height(x):
    """
    transform U.S customary units to cm
    """
    foot_cm_multiplyer = 30.48
    inch_cm_multiplyer = 2.54
    foot, inch = x.split("\'")
    foot, inch = int(foot), int(inch)
    return (foot * foot_cm_multiplyer) + (inch * inch_cm_multiplyer)


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
    # 'ST': ['ST'],
    'F': ['CF', 'RF', 'RS', 'RW', 'LF', 'LS', 'LW', 'ST'],
    'CM': ['CAM', 'CDM', 'CM'],
    'LM': ['LAM', 'LDM', 'LM', 'LCM'],
    'RM': ['RAM', 'RCM', 'RDM', 'RM'],
    'CB': ['CB'],
    'LB': ['LCB', 'LWB'],
    'RB': ['RCB', 'RWB'],
}

new_positions_map_3_classes = {
    'F': ['CF', 'RF', 'RS', 'RW', 'LF', 'LS', 'LW', 'ST'],
    'M': ['CAM', 'CDM', 'CM', 'LAM', 'LDM', 'LM', 'LCM', 'RAM', 'RCM', 'RDM', 'RM'],
    'B': ['CB', 'LCB', 'LWB', 'RCB', 'RWB', 'RB', 'LB']
}


def transform_target(x, transform_map):
    if x in transform_map.keys():
        return x
    for key, positions in transform_map.items():
        if x in positions:
            return key


def transform_target_position(dataframe, target_column, target_transform):
    if target_transform == 'default':
        transform_map = new_positions_map
    elif target_transform == '3_classes':
        transform_map = new_positions_map_3_classes
    else:
        raise ValueError('invalid target_transform value, can be default or 3_classes')
    transform_func = partial(transform_target, transform_map=transform_map)
    return dataframe[target_column].apply(transform_func)
