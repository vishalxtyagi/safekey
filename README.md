# Safe Key Server

This application is a Flask-based key blocking server that can run as a Windows service or as a standalone application.

## Project Structure

```
SafeKeyServer/
│
├── safekeyserver.py
├── windows_service.py
├── requirements.txt
└── README.md
```

## Installation Steps

1. **Install Requirements**:
   Make sure you have Python installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run as Standalone**:
   To run the application as a standalone server, simply execute:

   ```bash
   python safekeyserver.py
   ```

   This will start the Flask server and allow you to access its API.

3. **Install the Windows Service**:
   Open a Command Prompt with administrative privileges and run:

   ```bash
   python windows_service.py install
   ```

4. **Start the Service**:
   You can start the service with:

   ```bash
   python windows_service.py start
   ```

5. **Stop the Service**:
   To stop the service, use:

   ```bash
   python windows_service.py stop
   ```

6. **Remove the Service**:
   To remove the service:

   ```bash
   python windows_service.py remove
   ```

## Usage

- The service will start automatically on system startup and will run indefinitely.
- You can access the API to update blocked keys and toggle key blocking via HTTP requests.

### Summary

With these changes, you can now run your application as a standalone server or as a Windows service. 

1. **Standalone Execution**: You can simply run `safekeyserver.py` to start the Flask application, which allows for easier testing and debugging.
2. **Windows Service**: The service implementation remains intact, enabling automatic startup and management.

### Important Notes

1. **Run Command Prompt as Administrator**: When installing the service, ensure you run your command prompt as an administrator.
2. **Path Adjustments**: Update file paths in the logging setup to suit your system.
3. **Testing**: Make sure to thoroughly test both execution modes to ensure they behave as expected.

If you have any further questions or need additional modifications, feel free to ask!