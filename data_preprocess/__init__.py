from .preparation import run_data_preparation_pipeline
from .preprocess import run_preprocess_data_pipeline


def preprocess_fifa_data(data, target_transform='default'):
    prepared_data = run_data_preparation_pipeline(data, target_transform)
    preprocessed_data = run_preprocess_data_pipeline(prepared_data)
    return preprocessed_data


__all__ = ['preprocess_fifa_data']
