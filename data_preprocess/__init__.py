from .preparation import run_data_preparation_pipeline
from .preprocess import run_preprocess_data_pipeline


def preprocess_fifa_data(data):
    prepared_data = run_data_preparation_pipeline(data)
    preprocessed_data = run_preprocess_data_pipeline(prepared_data)
    return preprocessed_data


__all__ = ['preprocess_fifa_data']
