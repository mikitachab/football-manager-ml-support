import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler


def train_target_split(data):
    return data.drop('Position', axis=1), data['Position']


def draw_countplot(col):
    sns.countplot(col, order=col.value_counts().index)


def resample_data(sampler, x, y):
    return sampler.fit_resample(x, y)


def split_learning_data(x, y):
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.33, random_state=42, stratify=y)

    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=0.25, random_state=42, stratify=y_train)

    return dict(
        x_train=X_train,
        y_train=y_train,
        x_test=X_test,
        y_test=y_test,
        x_val=X_val,
        y_val=y_val
    )


def scale_data(data):
    scaler = RobustScaler()
    scaled_data = {}
    scaled_data['x_train'] = scaler.fit_transform(data['x_train'])
    scaled_data['x_test'] = scaler.transform(data['x_test'])
    scaled_data['x_val'] = scaler.transform(data['x_val'])
    return {**data, **scaled_data}
