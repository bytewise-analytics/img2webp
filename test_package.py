import subprocess
import sys
from pathlib import Path
import shutil
import tempfile
import venv

def run_command(cmd, cwd=None):
    """Run a command and return its output."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            check=True,
            text=True,
            capture_output=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Output: {e.output}")
        return False

def main():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        venv_path = temp_path / "venv"
        
        print("Creating virtual environment...")
        venv.create(venv_path, with_pip=True)
        
        # Get path to Python in virtual environment
        if sys.platform == "win32":
            python_path = venv_path / "Scripts" / "python.exe"
            pip_path = venv_path / "Scripts" / "pip.exe"
        else:
            python_path = venv_path / "bin" / "python"
            pip_path = venv_path / "bin" / "pip"
        
        print("Installing development dependencies...")
        if not run_command([str(pip_path), "install", "pytest", "pytest-cov", "build", "setuptools"]):
            return False
        
        print("Installing package in development mode...")
        if not run_command([str(pip_path), "install", "-e", "."]):
            return False
        
        print("Running tests...")
        if not run_command([str(python_path), "-m", "pytest"]):
            return False
        
        print("Building package...")
        if not run_command([str(python_path), "-m", "build"]):
            return False
        
        print("Installing built package...")
        wheel_file = next(Path("dist").glob("*.whl"))
        if not run_command([str(pip_path), "install", str(wheel_file)]):
            return False
        
        print("Testing CLI command...")
        if not run_command([str(python_path), "-m", "img2webp.cli", "--help"]):
            return False
        
        print("All tests passed successfully!")
        return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
