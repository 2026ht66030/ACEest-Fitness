import pytest
import tkinter as tk
from app import ACEestApp

@pytest.fixture(scope="module")
def app_instance():
    """Create a single root instance shared across all tests to prevent Tcl/Tk crashes."""
    root = tk.Tk()
    app = ACEestApp(root)
    yield app
    root.destroy()

def test_app_initialization(app_instance):
    """Verify that programs and variables initialize correctly."""
    assert app_instance.root is not None
    assert "Fat Loss (FL)" in app_instance.programs
    assert "Muscle Gain (MG)" in app_instance.programs
    assert "Beginner (BG)" in app_instance.programs
    assert app_instance.name_var.get() == ""

def test_calorie_calculation(app_instance):
    """Verify that calorie calculations update correctly based on weight and program."""
    app_instance.weight_var.set(70.0)
    app_instance.program_var.set("Fat Loss (FL)")
    app_instance.update_program()
    
    # 70 kg * 22 (calorie factor) = 1540 kcal
    assert "1540" in app_instance.calorie_label.cget("text")

def test_reset_functionality(app_instance):
    """Verify that reset clears all input fields."""
    app_instance.name_var.set("Test Client")
    app_instance.age_var.set(30)
    app_instance.weight_var.set(75.0)
    app_instance.reset()
    
    assert app_instance.name_var.get() == ""
    assert app_instance.age_var.get() == 0
    assert app_instance.weight_var.get() == 0.0