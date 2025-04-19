# 🛡️🔐 Encrypted Keylogger Simulation – Red/Blue Team Lab Tool

This is an advanced educational keylogger built for **red team simulation** and **blue team detection** within a controlled lab. It helps demonstrate real-world malware behavior including stealth, persistence, and encrypted data exfiltration — alongside countermeasure scripting.

> ⚠️ For **educational use only**. Do not run on unauthorized systems.

---

## 🎯 Features

- 🔐 **Encrypted keystroke logging** with AES-based Fernet
- 🪟 Tracks active window titles + clipboard contents
- 📋 Clipboard stealing triggered by window switch and timer
- 🕵️ Runs **stealthily** as a compiled binary (`input-mgr`)
- 📬 Optional **email exfiltration** (commented out by default)
- 🛡️ Blue team **detection script** included (process/file/startup checks)

---

## 🔴 Red Team Tactics

This tool simulates the following adversarial techniques:

| Technique | Description |
|----------|-------------|
| 🔹 Keylogging | Captures user keystrokes, encrypted using Fernet |
| 🔹 Clipboard Hijacking | Reads clipboard data on window switch and timer |
| 🔹 Binary Obfuscation | Bundled as `--onefile --noconsole` binary using PyInstaller |
| 🔹 Persistence | Optionally add to `.bashrc` or startup tasks (for Linux) |
| 🔹 Covert Logging | No stdout, logs encrypted to `.enc` file silently |
| 🔹 Modular | Supports stealth upgrades (screenshotting, exfiltration)

---

## 🛡️ Blue Team Countermeasures

Included `detect_keylogger.sh` scans for:

- Known artifact filenames (e.g. `keylog.enc`)
- Suspicious binaries like `input-mgr`
- Background processes (`pynput`, PyInstaller)
- Startup persistence (`.bashrc`, `crontab`)

---

## 🧩 Components

| File | Description |
|------|-------------|
| `logger.py` | Core keylogger (encrypts + logs) |
| `decrypt.py` | Decrypts the encrypted keystroke logs |
| `detect_keylogger.sh` | Blue team scanner |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Clean repo structure |
| `input-mgr` | Red team stealth binary (formerly logger) |

---

## 🚀 Setup

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 Run the Keylogger

```bash
python3 logger.py
```

### 🔹 Decrypt Captured Logs

```bash
python3 decrypt.py
```

---

## 🧪 Run Blue Team Scanner

```bash
chmod +x detect_keylogger.sh
./detect_keylogger.sh
```

---

## ⚠️ Legal Disclaimer

This tool is intended for **educational use only** in a **controlled environment**. Do not use on systems you don’t own or don’t have explicit permission to test. The author takes no responsibility for any misuse.

---

## 💬 Questions / Feedback?

This project was built as a hands-on red/blue team lab challenge. Contributions, ethical forks, and blue team enhancements are welcome.
