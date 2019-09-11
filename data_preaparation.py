import numpy as np
import pandas as pd

from data_transform import (
    transform_target_position,
    transfrom_height,
    transform_weight,
    transform_skill,
    transform_body_type
)
from logger import logger

drop_columns = [
    'Unnamed: 0',
    'ID',
    'Name',
    'Photo',
    'Flag',
    'Club Logo',
    'Club',
    'Special',
    'Real Face',
    'Release Clause',
    'Joined',
    'Contract Valid Until',
    'Nationality',
    'Loaned From',
    'GKDiving',
    'GKHandling',
    'GKKicking',
    'GKPositioning',
    'GKReflexes',
    'Jersey Number',
    'Value',
    'Wage',
    'International Reputation',
]

skills_columns = [
    'LS',
    'ST',
    'RS',
    'LW',
    'LF',
    'CF',
    'RF',
    'RW',
    'LAM',
    'CAM',
    'RAM',
    'LM',
    'LCM',
    'CM',
    'RCM',
    'RM',
    'LWB',
    'LDM',
    'CDM',
    'RDM',
    'RWB',
    'LB',
    'LCB',
    'CB',
    'RCB',
    'RB',
]

transform_map = {
    'Body Type': transform_body_type,
    'Height': transfrom_height,
    'Weight': transform_weight,
    'Position': transform_target_position
}
transform_map.update({skill: transform_skill for skill in skills_columns})


def run_transform_pipeline(transform_map, dataframe):
    for column, transform_func in transform_map.items():
        logger.info(f'transform column {column}')
        dataframe[column] = dataframe[column].apply(transform_func)
    return dataframe


def run_data_preparation_pipeline(dataframe):
    logger.info('droping columns')
    dataframe.drop(columns=drop_columns, inplace=True)
    logger.info('droping records with nan values')
    dataframe.dropna(inplace=True)
    logger.info('droping goalkeepers')
    dataframe = dataframe[dataframe['Position'] != 'GK']
    logger.info('transform data')
    dataframe = run_transform_pipeline(transform_map, dataframe)
    return dataframe


def main():
    fifa_data = pd.read_csv('csv/data.csv')
    fifa_data = run_data_preparation_pipeline(fifa_data)
    new_filename = 'csv/new_prepared_data.csv'
    logger.info(f'save data to {new_filename}')
    fifa_data.to_csv(new_filename, index=False)


if __name__ == '__main__':
    main()

# TODO tranform to DataPreparationPipeline
