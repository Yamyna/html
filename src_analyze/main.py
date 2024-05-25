#import analyze_file
import antivirus_keylogger
import analyze_steganography
#import analyze_url

"""
    Main that identificate object (url or file) and use all of function.
    Awaiting testing.
"""

if __name__ == "__main__":
    
    suspicious_word = ['keylogger', 'log', 'keystroke', 'data', 'pyHook', 'pynput.keyboard', 'ctypes.GetAsyncKeyState', 'keyboard.record', 'keyboard.add_hotkey', 'keyboard.read_key', 'keyboard.read_hotkey', 'keyboard.is_pressed', 'keyboard.write', 'keyboard.wait']
    analyze_steganography.analyze_steganography("/tmp/src_analyze/Mushu.jpg.exe")
    antivirus_keylogger.analyze_anti_virus_keylogger("/tmp/src_analyze/test.exe", suspicious_word)