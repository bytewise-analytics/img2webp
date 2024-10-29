import pytest
import tkinter as tk
from img2webp.gui import ImageConverterApp

@pytest.fixture
def root():
    """Create a Tk root instance."""
    root = tk.Tk()
    yield root
    root.destroy()

def test_app_creation(root):
    """Test that the app can be created."""
    app = ImageConverterApp(root)
    assert app is not None
    assert isinstance(app.root, tk.Tk)

def test_initial_values(root):
    """Test initial values of the app."""
    app = ImageConverterApp(root)
    assert app.input_files == []
    assert app.compression_slider.get() == 0.8  # Default compression value

def test_help_button(root):
    """Test the help button functionality."""
    app = ImageConverterApp(root)
    assert app.help_button.cget("text") == "?"

def test_convert_button(root):
    """Test the convert button functionality."""
    app = ImageConverterApp(root)
    assert app.convert_button.cget("text") == "Convert"

def test_progress_bar_initially_hidden(root):
    """Test that the progress bar is initially hidden."""
    app = ImageConverterApp(root)
    assert not app.progress_bar.winfo_ismapped()

def test_status_bar_initial_text(root):
    """Test the initial text of the status bar."""
    app = ImageConverterApp(root)
    assert app.status_bar.cget("text") == ""

def test_help_label_initial_text(root):
    """Test the initial text of the help label."""
    app = ImageConverterApp(root)
    assert app.help_label.cget("text") == ""