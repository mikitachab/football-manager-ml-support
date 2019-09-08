import numpy as np
import pandas as pd


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
fifa_data.drop(columns=drop_columns, inplace=True)

fifa_data = fifa_data[fifa_data['Position'] != 'GK']