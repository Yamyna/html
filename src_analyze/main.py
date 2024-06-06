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

    #analyze_steganography.analyze_steganography("/uploads_docker/RACI.pdf")
    #antivirus_keylogger.analyze_anti_virus_keylogger("/uploads_docker/RACI.pdf", suspicious_word)
    antivirus_ransomware.analyze_file_ransomware("/uploads_docker/RACI.pdf")
    hash_file.analyze_hash_file("/uploads_docker/RACI.pdf")