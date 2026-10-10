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
    """Verify that programs and the client list initialize correctly."""
    assert app_instance.root is not None
    assert "Fat Loss (FL)" in app_instance.programs
    assert "Muscle Gain (MG)" in app_instance.programs
    assert len(app_instance.clients) == 0

def test_save_client(app_instance):
    """Verify saving a client successfully appends them to the client list."""
    app_instance.name_var.set("John Doe")
    app_instance.age_var.set(30)
    app_instance.weight_var.set(75.0)
    app_instance.program_var.set("Muscle Gain (MG)")
    app_instance.progress_var.set(85)
    
    app_instance.save_client()
    
    assert len(app_instance.clients) == 1
    assert app_instance.clients[0][0] == "John Doe"
    assert app_instance.clients[0][4] == 85

def test_reset_functionality(app_instance):
    """Verify that reset clears all form fields."""
    app_instance.name_var.set("Test User")
    app_instance.age_var.set(40)
    app_instance.reset()
    
    assert app_instance.name_var.get() == ""
    assert app_instance.age_var.get() == 0