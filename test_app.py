import pytest

def test_calorie_calculation():
    weight = 70.0
    factor_fl = 22  # Fat Loss factor
    calories = int(weight * factor_fl)
    assert calories == 1540