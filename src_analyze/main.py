#import analyze_file
import antivirus_keylogger
import analyze_steganography
import antivirus_ransomware
import hash_file
#import analyze_url

"""
    Main that identificate object (url or file) and use all of function.
    Awaiting testing.
"""

if __name__ == "__main__":
    
    suspicious_word = ['keylogger', 'log', 'keystroke', 'data', 'pyHook', 'pynput.keyboard', 'ctypes.GetAsyncKeyState', 'keyboard.record', 'keyboard.add_hotkey', 'keyboard.read_key', 'keyboard.read_hotkey', 'keyboard.is_pressed', 'keyboard.write', 'keyboard.wait']
    analyze_steganography.analyze_steganography("/var/www/html/virus/Compte-2023.exe")
    antivirus_keylogger.analyze_anti_virus_keylogger("/var/www/html/virus/test.exe", suspicious_word)
    antivirus_ransomware.analyze_file_ransomware("/var/www/html/virus/test.exe")
    hash_file.analyze_hash_file()