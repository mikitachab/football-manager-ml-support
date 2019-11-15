import static
from sklearn.decomposition import PCA
from sklearn.preprocessing import RobustScaler


def make_card_features(fifa_data):
    pace = fifa_data['SprintSpeed'] * 0.55 + fifa_data['Acceleration'] * 0.45

    shooting = fifa_data['Finishing'] * 0.45 + \
        fifa_data['LongShots'] * 0.2 + \
        fifa_data['ShotPower'] * 0.2 + \
        fifa_data['Positioning'] * 0.05 + \
        fifa_data['Penalties'] * 0.05 + \
        fifa_data['Volleys'] * 0.05

    passing = fifa_data['ShortPassing'] * 0.35 + \
        fifa_data['Vision'] * 0.2 + \
        fifa_data['Crossing'] * 0.2 + \
        fifa_data['LongPassing'] * 0.15 + \
        fifa_data['Curve'] * 0.05 + \
        fifa_data['FKAccuracy'] * 0.05

    dribbling = fifa_data['Dribbling'] * 0.5 + \
        fifa_data['BallControl'] * 0.3 + \
        fifa_data['Agility'] * 0.1 + \
        fifa_data['Balance'] * 0.05 + \
        fifa_data['Reactions'] * 0.05

    deffending = fifa_data['Marking'] * 0.3 + \
        fifa_data['StandingTackle'] * 0.3 + \
        fifa_data['Interceptions'] * 0.2 + \
        fifa_data['HeadingAccuracy'] * 0.1 + \
        fifa_data['SlidingTackle'] * 0.1

    physical = fifa_data['Strength'] * 0.5 + \
        fifa_data['Stamina'] * 0.25 + \
        fifa_data['Aggression'] * 0.2 + \
        fifa_data['Jumping'] * 0.05

    new_fifa_data = fifa_data.drop(columns=static.old_features)

    new_fifa_data['Pace'] = pace
    new_fifa_data['Shooting'] = shooting
    new_fifa_data['Passing'] = passing
    new_fifa_data['Dribbling'] = dribbling
    new_fifa_data['Deffending'] = deffending
    new_fifa_data['Physical'] = physical

    return new_fifa_data


def pca_transform(data):
    return PCA(n_components=1).fit_transform(RobustScaler().fit_transform(data))


def make_card_features_with_pca(fifa_data):
    new_fifa_data = fifa_data.drop(columns=static.old_features)
    new_features_map = {
        'Pace': ['SprintSpeed', 'Acceleration'],
        'Shooting': ['Finishing', 'LongShots', 'ShotPower', 'Positioning', 'Penalties', 'Volleys'],
        'Passing': ['ShortPassing', 'Vision', 'Crossing', 'LongPassing', 'Curve', 'FKAccuracy'],
        'Dribbling': ['Dribbling', 'BallControl', 'Agility', 'Balance', 'Reactions'],
        'Deffending': ['Marking', 'StandingTackle', 'Interceptions', 'HeadingAccuracy', 'SlidingTackle'],
        'Physical': ['Strength', 'Stamina', 'Aggression', 'Jumping']
    }
    for name, columns in new_features_map.items():
        new_fifa_data[name] = pca_transform(fifa_data[columns])
    return new_fifa_data


def transform_data(data, transform_type):
    transform_map = {
        'card_features': make_card_features,
        'no_transform': lambda data: data,
        'card_features_pca': make_card_features_with_pca
    }
    transform_func = transform_map.get(transform_type)
    if transform_func:
        print(f'Data transform: {transform_type}')
        print('Columns after transform')
        new_data = transform_func(data)
        print(new_data.columns)
        return new_data


def transofrm_skils(fifa_data):
    fwr_cols = ['RF', 'ST', 'LF', 'RS', 'LS', 'CF']
    mid_cols = ['LW', 'RCM', 'LCM', 'LDM', 'CAM', 'CDM',
                'RM', 'LAM', 'LM', 'RDM', 'RW', 'CM', 'RAM']
    def_cols = ['RCB', 'CB', 'LCB', 'LB', 'RB', 'RWB', 'LWB']
    fifa_data['FRWD'] = pca_transform(fifa_data[fwr_cols])
    fifa_data['MID'] = pca_transform(fifa_data[mid_cols])
    fifa_data['DEF'] = pca_transform(fifa_data[def_cols])
    return fifa_data.drop(fwr_cols + mid_cols + def_cols, axis=1)
