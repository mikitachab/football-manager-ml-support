import pytest

new_positions_map = {
    'ST': ['ST'],
    'CF': ['СF'],
    'LF': ['LF', 'LS', 'LW'],
    'RF': ['RF', 'RS', 'RW'],
    'CM': ['CAM', 'CDM', 'CM'],
    'LM': ['LAM', 'LDM', 'LM', 'LCM', ],
    'RM': ['RAM', 'RCM', 'RDM', 'RM'],
    'CB': ['CB'],
    'LB': ['LCB', 'LWB'],
    'RB': ['RCB', 'RWB'],
}


def tranform_target_position(x):
    if x in new_positions_map.keys():
        return x
    for key, positions in new_positions_map.items():
        if x in positions:
            return key


@pytest.mark.parametrize("test_input, expected", [
    ('RB', 'RB'),
    ('CB', 'CB'),
    ('LB', 'LB'),
    ('RWB', 'RB'),
    ('LWB', 'LB'),
    ('CDM', 'CM'),
    ('CM', 'CM'),
    ('CAM', 'CM'),
    ('LM', 'LM'),
    ('RW', 'RF'),
    ('LW', 'LF'),
    ('CF', 'CF'),
    ('ST', 'ST'),
    ('LAM', 'LM'),
    ('LCB', 'LB'),
    ('LCM', 'LM'),
    ('LDM', 'LM'),
    ('LF', 'LF'),
    ('LS', 'LF'),
    ('RAM', 'RM'),
    ('RCB', 'RB'),
    ('RDM', 'RM'),
    ('RF', 'RF'),
    ('RS', 'RF'),
    ('RM', 'RM'),
])
def test_tranform(test_input, expected):
    assert tranform_target_position(test_input) == expected
