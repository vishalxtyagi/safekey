import os
import subprocess

SERVICE_NAME = "SafeKeyServer"
SERVICE_DISPLAY_NAME = "Safe Key Server"
SERVICE_DESCRIPTION = "Service to monitor and block specific keys."
FLASK_APP_PATH = os.path.join(os.getcwd(), "safekeyserver.py")
NSSM_EXE = os.path.join(os.getcwd(), "executables", "nssm.exe")

def install_service():
    """Install the Flask app as a Windows service using NSSM."""
    if os.path.exists(NSSM_EXE):
        print(f"Installing {SERVICE_NAME} service...")
        
        # Install the service
        subprocess.run([NSSM_EXE, "install", SERVICE_NAME, FLASK_APP_PATH])

        # Set service display name
        subprocess.run([NSSM_EXE, "set", SERVICE_NAME, "DisplayName", SERVICE_DISPLAY_NAME])
        
        # Set service description
        subprocess.run([NSSM_EXE, "set", SERVICE_NAME, "Description", SERVICE_DESCRIPTION])

        # Set service start mode to auto
        subprocess.run([NSSM_EXE, "set", SERVICE_NAME, "Start", "SERVICE_AUTO_START"])

        # Start the service
        subprocess.run([NSSM_EXE, "start", SERVICE_NAME])

if __name__ == "__main__":
    # Ensure the Flask app exists
    if not os.path.exists(FLASK_APP_PATH):
        print(f"Flask app not found at {FLASK_APP_PATH}. Please ensure it exists.")
        exit(1)

    install_service()