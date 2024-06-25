import argparse
import antivirus_keylogger
import analyze_steganography
import antivirus_ransomware
import hash_file
import analyze_pt_note_pt_load

def main(file_path):
    """
    Analyzes the specified file using various security modules to detect different types of threats.

    Args:
        file_path (str): The path to the file to be analyzed.

    Returns:
        None
    """
    suspicious_word = ['keylogger', 'log', 'keystroke', 'data', 'pyHook', 'pynput.keyboard', 'ctypes.GetAsyncKeyState', 'keyboard.record', 'keyboard.add_hotkey', 'keyboard.read_key', 'keyboard.read_hotkey', 'keyboard.is_pressed', 'keyboard.write', 'keyboard.wait']
    analyze_steganography.analyze_steganography(file_path)
    antivirus_keylogger.analyze_anti_virus_keylogger(file_path, suspicious_word)
    antivirus_ransomware.analyze_file_ransomware(file_path)
    analyze_pt_note_pt_load.analyze_file(file_path)
    hash_file.analyze_hash_file(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a file for various threats.")
    parser.add_argument('file', type=str, help='The file to be analyzed')
    args = parser.parse_args()
    main(args.file)