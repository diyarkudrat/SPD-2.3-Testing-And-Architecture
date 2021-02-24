import math
import pytest

T_HALF = 5730
DECAY_CONSTANT = -0.693


def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
    in the sample conpared to the amount in living 
    tissue (unitless). 
    """
    if carbon_14_ratio < 0 or carbon_14_ratio > 1:
        raise TypeError('Please provide input between the range of 0 and 1')

    age = math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF

    return round(age, 2)


def test_get_age_carbon_14_dating():
    carbon_14_ratio = 0.35
    carbon_14_ratio2 = 1.45

    assert get_age_carbon_14_dating(carbon_14_ratio) == 8680.35

    with pytest.raises(TypeError):
        get_age_carbon_14_dating(carbon_14_ratio2)
