import subprocess
import sys
import os

def auto_install_missing_packages():
    """Install packages from requirements.txt only if any are missing."""
    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    requirements_file = os.path.join(project_root, "requirements.txt")
    
    if not os.path.exists(requirements_file):
        print("[WARNING] requirements.txt not found")
        return
    
    # Read requirements.txt and extract package names
    try:
        with open(requirements_file, "r") as f:
            packages = []
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    # Extract package name by removing version specifiers
                    package = line.split("==")[0].split(">=")[0].split("<=")[0]
                    packages.append(package)
    except Exception as e:
        print(f"[ERROR] Failed to read requirements.txt: {e}")
        return
    
    # Check if any packages are missing
    missing_packages = []
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    # Install only if packages are missing
    if missing_packages:
        print(f"[INFO] Missing packages detected: {', '.join(missing_packages)}")
        try:
            print("[INFO] Installing packages from requirements.txt...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
            print("[INFO] Packages installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to install packages: {e}")
    else:
        print("[INFO] All packages already installed")

auto_install_missing_packages()
