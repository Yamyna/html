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
    analyze_steganography.analyze_steganography("/tmp/virus/Compte-2023.exe")
    antivirus_keylogger.analyze_anti_virus_keylogger("/tmp/virus/test.exe", suspicious_word)
    antivirus_ransomware.analyze_file_ransomware("/tmp/virus/test.exe")

    if(hash_file.is_hash_in_file("md5_hash.txt",hash_file.hash_files("/tmp/virus/test.exe"))):
        hash_file.add_hash_to_file("md5_hash.txt",hash_file.hash_files("/tmp/virus/test.exe"))
        with open("/tmp/scan_result.txt", "a") as f:
            f.write("The file has a hash present in our MD5 hash database.")
    else :
        with open("/tmp/scan_result.txt", "a") as f:
            f.write("File is not present in the database of MD5 hashes.")