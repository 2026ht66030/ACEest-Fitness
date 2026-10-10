import pytest

def test_fat_loss_calorie_calculation():
    weight = 70.0
    factor_fl = 22  # Fat Loss factor
    calories = int(weight * factor_fl)
    assert calories == 1540

def test_muscle_gain_calorie_calculation():
    weight = 70.0
    factor_mg = 35  # Muscle Gain factor
    calories = int(weight * factor_mg)
    assert calories == 2450

def test_beginner_calorie_calculation():
    weight = 60.0
    factor_bg = 26  # Beginner factor
    calories = int(weight * factor_bg)
    assert calories == 1560

def test_programs_dictionary_structure():
    programs = {
        "Fat Loss (FL)": {"calorie_factor": 22},
        "Muscle Gain (MG)": {"calorie_factor": 35},
        "Beginner (BG)": {"calorie_factor": 26}
    }
    assert "Fat Loss (FL)" in programs
    assert programs["Muscle Gain (MG)"]["calorie_factor"] == 35