import time
import logging
import keyboard
from flask import Flask, jsonify, request
from flask_cors import CORS
from concurrent.futures import ThreadPoolExecutor

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
executor = ThreadPoolExecutor(max_workers=2)

class SafeKeyServer:
    def __init__(self):
        self.blocked_keys = set()  # Use a set to store blocked keys
        self.blocking_enabled = True  # Flag to enable or disable blocking
        self.is_alive = True  # Flag to keep the server running

    def start(self):
        logging.info("Key monitoring started.")
        while self.is_alive:
            time.sleep(1)  # Keep the thread alive

    def stop(self):
        logging.info("Stopping key monitoring.")
        self.is_alive = False  # Stop the monitoring

    def update_keys(self, keys):
        """Update the keys based on the current blocking status."""
        if not self.blocking_enabled:
            logging.warning("Key blocking is currently disabled.")
            return jsonify(success=False, message="Key blocking is disabled."), 403
        
        for key in keys:
            if key in self.blocked_keys:
                keyboard.unblock_key(key)
                self.blocked_keys.remove(key)
            else:
                keyboard.block_key(key)
                self.blocked_keys.add(key)
        logging.info(f"Blocked keys updated: {self.blocked_keys}.")
        return jsonify(success=True, message=f"Keys {keys} have been updated."), 200

    def toggle_blocking(self, enable):
        self.blocking_enabled = enable
        status = "enabled" if enable else "disabled"

        if enable:
            for key in self.blocked_keys:
                keyboard.block_key(key)
        else:
            for key in self.blocked_keys:
                keyboard.unblock_key(key)

        logging.info(f"Key blocking {status}.")

@app.route('/safekey', methods=['POST'])
def handle_keys():
    """Route to enable/disable key blocking and update keys."""
    data = request.json
    enable = data.get('enable', True)
    keys = data.get('keys', [])

    # Toggle blocking status
    server.toggle_blocking(enable)

    # If blocking is enabled and keys are provided, update the keys
    if enable and keys:
        return server.update_keys(keys)

    return jsonify(success=True, message=f"Key blocking has been {'enabled' if enable else 'disabled'}."), 200

def run_flask():
    """Run the Flask application."""
    app.run(port=5000, host='127.0.0.1')

def main():
    # Start the key monitoring in a separate thread
    executor.submit(server.start)
    # Run the Flask app
    run_flask()

if __name__ == '__main__':
    # Create an instance of SafeKeyServer
    server = SafeKeyServer()
    main()
