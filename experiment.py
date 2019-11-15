from hypopt import GridSearch
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support as score


def perform_grid_search(data, estimator, grid_search_args=None):
    print('running GridSearch for', estimator.name)
    if grid_search_args is None:
        grid_search_args = {}
    grid_search = GridSearch(
        model=estimator.estimator,
        param_grid=estimator.param_grid,
        **grid_search_args
    )
    grid_search.fit(data['x_train'], data['y_train'], data['x_val'], data['y_val'])
    print_grid_search_result(grid_search, data, estimator.name)
    return eval_model(grid_search.best_estimator_, data)


def print_grid_search_result(gs, data, name):
    print(name, 'results')
    print('Best estimator params:', gs.best_params)
    y_pred = gs.best_estimator_.predict(data['x_test'])
    _, _, fscore, _ = score(data['y_test'], y_pred, average='weighted')
    print('Best estimator score:', fscore)
    # print(classification_report(data['y_test'], gs.best_estimator_.predict(data['x_test'])))


def eval_model(model, data):
    model.fit(data['x_train'], data['y_train'])
    y_pred = model.predict(data['x_test'])
    return get_score(data['y_test'], y_pred)


def get_score(y_true, y_pred):
    precision, recall, fscore, _ = score(y_true, y_pred, average='weighted')
    return dict(precision=precision, recall=recall, fscore=fscore)
