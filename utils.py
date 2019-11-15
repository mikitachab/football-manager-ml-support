import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler


from data_preprocess import preprocess_fifa_data


def train_target_split(data):
    return data.drop('Position', axis=1), data['Position']


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


def select_features(selector, data):
    selected_data = {}
    selector.fit(data['x_train'], data['y_train'])
    selected_data['x_train'] = selector.transform(data['x_train'])
    selected_data['x_test'] = selector.transform(data['x_test'])
    selected_data['x_val'] = selector.transform(data['x_val'])
    if hasattr(selector, 'n_features_'):
        print('selected', selector.n_features_, 'features with', type(selector))
    return {**data, **selected_data}


def resample_data(sampler, x, y):
    return sampler.fit_resample(x, y)


def plot_experiment_result(scores, title=''):
    fscores = sorted([(name, score['fscore']) for name, score in scores.items()], key=lambda x: x[1])
    n_estimators = len(fscores)
    plt.figure(figsize=(12, 6))
    plt.barh(range(n_estimators), [s[1] for s in fscores], align='center')
    plt.yticks(range(n_estimators), [s[0] for s in fscores])
    plt.xlabel('score')
    plt.title(f'Experiment Models Score ({title})')
    plt.show()


def draw_countplot(col, title='', xlabel=''):
    sns.countplot(col)
    plt.title(title)
    plt.xlabel(xlabel)


def get_fifa_data(target_type='default'):
    return preprocess_fifa_data(pd.read_csv('csv/data.csv'), target_type)


def setup_learning_data(fifa_data):
    fifa_train_data, target = train_target_split(fifa_data)
    learning_data = split_learning_data(fifa_train_data, target)
    learning_data = scale_data(learning_data)
    return learning_data


def oversampling(data, sampler):
    resampled_x, resampled_y = resample_data(sampler, data['x_train'], data['y_train'])
    new_data = {
        'x_train': resampled_x,
        'y_train': resampled_y
    }
    return {**data, **new_data}
