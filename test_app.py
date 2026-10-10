import pytest
import tkinter as tk
from app import ACEestApp

def test_app_initialization():
    """Verify that programs and variables initialize correctly."""
    root = tk.Tk()
    app = ACEestApp(root)
    
    assert app.root is not None
    assert "Fat Loss (FL)" in app.programs
    assert "Muscle Gain (MG)" in app.programs
    assert "Beginner (BG)" in app.programs
    assert app.name_var.get() == ""
    
    root.destroy()

def test_calorie_calculation():
    """Verify that calorie calculations update correctly based on weight and program."""
    root = tk.Tk()
    app = ACEestApp(root)
    
    app.weight_var.set(70.0)
    app.program_var.set("Fat Loss (FL)")
    app.update_program()
    
    # 70 kg * 22 (calorie factor) = 1540 kcal
    assert "1540" in app.calorie_label.cget("text")
    
    root.destroy()

def test_reset_functionality():
    """Verify that reset clears all input fields."""
    root = tk.Tk()
    app = ACEestApp(root)
    
    app.name_var.set("Test Client")
    app.age_var.set(30)
    app.weight_var.set(75.0)
    app.reset()
    
    assert app.name_var.get() == ""
    assert app.age_var.get() == 0
    assert app.weight_var.get() == 0.0
    
    root.destroy()