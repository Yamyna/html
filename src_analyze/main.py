#import analyze_file
import antivirus_keylogger
import analyze_steganography
#import analyze_url

if __name__ == "__main__":
    
    suspicious_word = ['pynput', 'keyboard', 'Listener', 'keylogger', 'log', 'keystroke', 'data', 'pyHook', 'pynput.keyboard', 'virus', 'getchar']
    analyze_steganography.analyze_steganography("Mushu.jpg.exe")
    antivirus_keylogger.analyze_anti_virus_keylogger("test.exe", suspicious_word)

 