import pytest
import unittest.mock as mock
from unittest.mock import patch

from src.static.diets import from_string
from src.controllers.receipecontroller import ReceipeController

@pytest.fixture
def sut(readiness):
    with patch('src.util.calculator.calculate_readiness', autospec=True) as mockedcalculate_readiness:
        mockedcalculate_readiness.return_value = readiness
        sut = ReceipeController({})

        return sut



# Test different readiness values
@pytest.mark.unit
@pytest.mark.parametrize(
    'available, receipe, diet, readiness, expected',
    [
        ({}, {'diets': ['normal']}, from_string('normal'), 0.09, None),
        ({}, {'diets': ['normal']}, from_string('normal'), 0.1, 0.1),
        ({}, {'diets': ['normal']}, from_string('normal'), 0.11, 0.11),
    ]
)
def test_getReceipe_readiness(sut, available, receipe, diet, expected):
    result = sut.get_receipe_readiness(available, receipe, diet)
    assert result == expected

# Test diet compliant 
@pytest.mark.unit
@pytest.mark.parametrize(
    'available, receipe, diet, readiness, expected',
    [
        ({}, {'diets': ['normal']}, from_string('normal'), 0.11, 0.11),
        ({}, {'diets': ['normal']}, from_string('vegan'), 0.11, None),
    ]
)
def test_getReceipe_diet(sut, available, receipe, diet, expected):
    result = sut.get_receipe_readiness(available, receipe, diet)
    assert result == expected