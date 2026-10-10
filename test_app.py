import pytest
import tkinter as tk
from app import ACEestApp

@pytest.fixture
def app_instance():
    root = tk.Tk()
    app = ACEestApp(root)
    yield app
    root.destroy()

def test_app_initialization(app_instance):
    """Verify that programs dictionary initializes correctly."""
    assert app_instance.root is not None
    assert "Fat Loss (FL)" in app_instance.programs
    assert "Muscle Gain (MG)" in app_instance.programs
    assert "Beginner (BG)" in app_instance.programs

def test_update_program_calories(app_instance):
    """Verify calorie calculation logic based on weight and factor."""
    app_instance.weight_var.set(70.0)
    app_instance.program_var.set("Fat Loss (FL)")
    app_instance.update_program()
    
    # 70 kg * calorie_factor 22 = 1540 kcal
    assert "1540" in app_instance.calorie_label.cget("text")

def test_reset_functionality(app_instance):
    """Verify that reset clears all form fields and resets calories."""
    app_instance.name_var.set("John Doe")
    app_instance.age_var.set(25)
    app_instance.weight_var.set(80.0)
    app_instance.reset()
    
    assert app_instance.name_var.get() == ""
    assert app_instance.age_var.get() == 0
    assert app_instance.weight_var.get() == 0.0
    assert "Estimated Calories: --" in app_instance.calorie_label.cget("text")