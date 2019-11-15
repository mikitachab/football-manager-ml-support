import numpy as np
import pandas as pd

from .transform import (
    transform_target_position,
    transfrom_height,
    transform_weight,
    transform_skill,
    transform_body_type
)
from static import columns_for_drop, skills_columns
from logger import logger

TARGET_COLUMN = 'Position'

transform_map = {
    'Body Type': transform_body_type,
    'Height': transfrom_height,
    'Weight': transform_weight,
}
transform_map.update({skill: transform_skill for skill in skills_columns})


def run_transform_pipeline(transform_map, dataframe, target_transform):
    logger.info('transform data')
    for column, transform_func in transform_map.items():
        logger.info(f'transform column {column}')
        dataframe[column] = dataframe[column].apply(transform_func)
    dataframe[TARGET_COLUMN] = transform_target_position(dataframe, TARGET_COLUMN, target_transform)
    return dataframe


def drop_columns(dataframe):
    logger.info('droping columns')
    return dataframe.drop(columns=columns_for_drop)


def drop_nan(dataframe):
    logger.info('droping records with nan values')
    return dataframe.dropna()


def drop_goalkeepers(dataframe):
    logger.info('droping goalkeepers')
    return dataframe[dataframe['Position'] != 'GK']


def run_data_preparation_pipeline(dataframe, target_transform):
    logger.info('run data preparation pipeline')
    dataframe = drop_columns(dataframe)
    dataframe = drop_nan(dataframe)
    dataframe = drop_goalkeepers(dataframe)
    dataframe = run_transform_pipeline(transform_map, dataframe, target_transform)
    return dataframe


def main():
    fifa_data = pd.read_csv('csv/data.csv')
    fifa_data = run_data_preparation_pipeline(fifa_data)
    new_filename = 'csv/new_prepared_data_st_to_f.csv'
    logger.info(f'save data to {new_filename}')
    fifa_data.to_csv(new_filename, index=False)


if __name__ == '__main__':
    main()
