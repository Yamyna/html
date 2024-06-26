def open_file(file):
    '''
    Open the file and return the content of the file and the extension of the file
    '''
    try:
        with open(file, 'rb') as f:
                analyze = f.read()
        return analyze
    except:
        return False

def suspicious_word_count(file, list_word):
    '''
    Count the number of suspicious words in the file and return True 
    if the number of suspicious words is greater than or equal to half of 
    the length of the list of suspicious words, otherwise return False.
    '''
    count = 0
    analyze = open_file(file)
    if analyze is None:
        return False
    for w in list_word:
        if w.encode() in analyze:
            count += 1
    if count == 0:
        return False
    elif count >= len(list_word) / 3:
        return True
    else:
        return False
    
def analyze_connection(file):
    ''' 
    Analyze if the file contains connection and send data.
    Return True if the file contains connection and send data, otherwise return False.
    '''
    analyze = open_file(file)
    connction_word = ['socket', 'connect', 'send', 'exec', "telnet", "ssh", "ftp","smtp", "pop3", "imap", "TCP", "UDP", "port"]
    if analyze is None:
        return False
    for word in connction_word:
        if word.encode() in analyze:
            return True
    return False


def analyze_contain_storage_file(file):
    '''
    Analyze if the file contains storage file and return True if the file contains storage file, otherwise return False.
    '''
    analyze = open_file(file)
    
    if analyze is None:
        return False
    if b'open' in analyze or b'write' in analyze or b'add' in analyze:
        return True
    else:   
        return False

def analyze_listener_keyboard(file):
    keywords = [
        'pynput.keyboard.Listener',
        'ctypes.GetAsyncKeyState',
        'pynput.keyboard',
        'Listener',
        r'pynput\.keyboard\.Listener',
        r'ctypes\.windll\.user32\.GetAsyncKeyState',
        r'keyboard\.on_press',
        r'keyboard\.on_release',
        r'keyboard\.add_hotkey',
        r'keyboard\.read_key',
        r'keyboard\.read_hotkey',
        r'keyboard\.is_pressed',
        r'keyboard\.write',
        r'keyboard\.wait',
        r'pyHook\.HookManager',
        r'pythoncom\.PumpMessages',
        r'GetKeyState',
        r'SetWindowsHookEx',
        r'CallNextHookEx',
        r'UnhookWindowsHookEx'
    ]
    
    analyze= open_file(file)
    
    if analyze is None:
        return False
    for k in keywords:
        if k.encode() in analyze:
            return True     
    return False
        
def analyze_anti_virus_keylogger(file, list_word):
    ''' 
    Analyze if the file is suspicious and return True if the file is suspicious, otherwise return False.
    '''
    with open('/tmp/scan_result.txt', 'a') as f:
        f.write("\n\nKEYLOGGER ANTIVIRUS")

        if open_file(file) is False:
            f.write('\n✗ extension supported')
            return False

        if suspicious_word_count(file, list_word):
            f.write('\n✓ suspicious words')
        else :
            f.write('\n✗ suspicious words')

        if analyze_connection(file) :
            f.write('\n✓ connection and send data')
        else :
            f.write('\n✗ connection and send data')

        if analyze_contain_storage_file(file) :
            f.write('\n✓ storage file')
        else :
            f.write('\n✗ storage file')

        if analyze_listener_keyboard(file) :
            f.write('\n✓ listener keyboard')
        else :
            f.write('\n✗ listener keyboard')