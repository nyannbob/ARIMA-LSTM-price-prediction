import os
import subprocess
import sys
import glob

def install_requirements():
    """Installs the necessary packages from requirements.txt."""
    if os.path.exists('requirements.txt'):
        print("Installing required packages from requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    else:
        print("requirements.txt not found. Please make sure it is in the current directory.")

def run_notebooks():
    """Runs all Jupyter Notebooks in the current directory in alphabetical order."""
    notebooks = sorted(glob.glob("*.ipynb"))
    
    if not notebooks:
        print("No Jupyter Notebooks found in the current directory.")
        return
    
    for notebook in notebooks:
        print(f"Running {notebook}...")
        try:
            # Execute the notebook using nbconvert
            subprocess.run(
                [
                    sys.executable, 
                    "-m", 
                    "jupyter", 
                    "nbconvert", 
                    "--to", 
                    "notebook", 
                    "--execute", 
                    "--inplace", 
                    notebook
                ],
                check=True
            )
            print(f"Successfully ran {notebook}.")
        except subprocess.CalledProcessError as e:
            print(f"Error running {notebook}: {e}")

if __name__ == "__main__":
    install_requirements()
    run_notebooks()
