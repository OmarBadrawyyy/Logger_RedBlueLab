#!/bin/bash

echo "🔍 [*] Scanning system for keylogger indicators..."

echo -e "\n[+] Checking for known keylogger log files..."
find ~ -name "keylog.enc" 2>/dev/null

echo -e "\n[+] Checking for suspicious binaries (e.g. input-mgr)..."
file ~/Desktop/Logger/input-mgr 2>/dev/null | grep -i "executable"

echo -e "\n[+] Searching for clipboard/keylogger modules in memory..."
ps aux | grep -E 'pynput|pyperclip|cryptography' | grep -v grep

echo -e "\n[+] Scanning for running binaries (e.g. input-mgr)..."
ps aux | grep -E './input-mgr' | grep -v grep

echo -e "\n[+] Checking .bashrc for persistence..."
grep "input-mgr" ~/.bashrc

echo -e "\n[+] Looking for suspicious crontab entries..."
crontab -l 2>/dev/null | grep -E 'input-mgr|logger|keylog'

echo -e "\n[+] Done. If any of these triggered, investigate further."
