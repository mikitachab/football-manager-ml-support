from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import LabelEncoder
from pprint import pprint

VARIANCE_THRESHHOLD = 0.2


def drop_quasi_constant_features(data):
    data_no_category = data.select_dtypes(exclude=['category'])
    qconstant_filter = VarianceThreshold(threshold=VARIANCE_THRESHHOLD)
    qconstant_filter.fit(data_no_category)
    selected_features = data_no_category.columns[qconstant_filter.get_support()]
    qconstant_features = [feature for feature in data_no_category.columns if feature not in selected_features]
    print(f'Dropping constant columns: {qconstant_features}')
    return data.drop(columns=qconstant_features, axis=1)


def find_duplicate_columns(data):
    no_duplicates_data = data.T.drop_duplicates(keep='first').T
    return [c for c in data.columns if c not in no_duplicates_data.columns]


def drop_duplicate_columns(data):
    duplicate_columns = find_duplicate_columns(data)
    print(f'Dropping duplicate columns: {duplicate_columns}')
    return data.drop(columns=duplicate_columns, axis=1)


def filter_players_by_overall(fifa_data):
    overall_threshold = 70
    print(f'Filtering players by overall {overall_threshold}')
    return fifa_data[fifa_data['Overall'] >= overall_threshold]


def get_labels_map(le):
    return dict(zip(le.classes_, le.transform(le.classes_)))


def encode_column_labels(col):
    label_encoder = LabelEncoder()
    transform = label_encoder.fit_transform(col)
    print(f'{col.name} encoding:')
    pprint(get_labels_map(label_encoder))
    return transform


def encode_labels(data):
    print('Label encoding')
    categories = data.select_dtypes('category')
    data[categories.columns] = data[categories.columns].apply(encode_column_labels)
    return data


def run_preprocess_data_pipeline(data):
    category_cols = ['Preferred Foot', 'Body Type', 'Work Rate', 'Position']
    data[category_cols] = data[category_cols].astype('category')

    before_shape = data.shape
    print(f'shape before preprocess {before_shape}')

    preprocess_pipeline = [
        drop_quasi_constant_features,
        drop_duplicate_columns,
        encode_labels,
        filter_players_by_overall,
    ]

    for processor in preprocess_pipeline:
        data = processor(data)

    after_shape = data.shape
    print(f'shape after preprocess {after_shape}')
    print(f'dropped {before_shape[0]-after_shape[0]} rows')
    print(f'dropped {before_shape[1]-after_shape[1]} columns')

    return data
