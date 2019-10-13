import pytest

from data_transform import (
    transform_target_position,
    transfrom_height,
    transform_weight,
    transform_skill,
    transform_body_type
)


@pytest.mark.parametrize('test_input, expected', [
    ('RB', 'RB'),
    ('CB', 'CB'),
    ('LB', 'LB'),
    ('RWB', 'RB'),
    ('LWB', 'LB'),
    ('CDM', 'CM'),
    ('CM', 'CM'),
    ('CAM', 'CM'),
    ('LM', 'LM'),
    ('RW', 'F'),
    ('LW', 'F'),
    ('CF', 'F'),
    ('ST', 'ST'),
    ('LAM', 'LM'),
    ('LCB', 'LB'),
    ('LCM', 'LM'),
    ('LDM', 'LM'),
    ('LF', 'F'),
    ('LS', 'F'),
    ('RAM', 'RM'),
    ('RCB', 'RB'),
    ('RDM', 'RM'),
    ('RF', 'F'),
    ('RS', 'F'),
    ('RM', 'RM'),
])
def test_transform_target_positionn(test_input, expected):
    assert transform_target_position(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    (r"5'7", 170.18),
    (r"6'2", 187.96),
])
def test_transfrom_height(test_input, expected):
    assert transfrom_height(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('159lbs', 72.11),
    ('183lbs', 82.99),
])
def test_transform_weight(test_input, expected):
    assert transform_weight(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('88+3', 88),
])
def test_transform_skill(test_input, expected):
    assert transform_skill(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('Normal', 'Normal'),
    ('Lean', 'Lean'),
    ('test', 'Normal'),
])
def test_transform_body_type(test_input, expected):
    assert transform_body_type(test_input) == expected
