from collections import namedtuple

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

Estimator = namedtuple('Estimator', 'name, estimator, param_grid')

estimators = [
    Estimator(
        name='DecisionTreeClassifier',
        estimator=DecisionTreeClassifier(),
        param_grid={
            'max_depth': [10, 50, 100],
            'min_samples_leaf': [1],
            'min_samples_split': [2],
        }
    ),
    Estimator(
        name='RandomForestClassifier',
        estimator=RandomForestClassifier(),
        param_grid={
            'bootstrap': [True],
            'max_depth': [10, 50, 100],
            'max_features': [7],
            'min_samples_leaf': [1],
            'min_samples_split': [2],
            'n_estimators': [100, 500, 1000]
        }
    )
]


def get_estimators():
    return estimators
