import ast
import modulefinder
import os 

def open_file(file):  
    
    '''
    
    Open the file and return the content of the file and the extention of the file
    
    '''
    
    _ , exention = os.path.splitext(file)
    if exention.lower() == '.py' or exention.lower() == '.c':
        with open(file, 'r') as f :
        
            analyze = f.read()
            
    if exention.lower() == '.exe':
        with open(file, 'rb') as f :
            
            analyze = f.read()
    return analyze, exention

def test_supported_extention(file):
        
        '''
        
        Test if the extention of the file is supported and return True if the extention of the file is supported, otherwise return False
        
        '''
        _ , test_supported_extention = open_file(file)
        
        if test_supported_extention.lower() == '.py' or test_supported_extention.lower() == '.c' or test_supported_extention.lower() == '.exe':
            return True
        else:
            
            print('The extention of the file is not supported')
            
            return False

def suspicious_word_count(file, list_word):
    
    '''
    
    Count the number of suspicious words in the file and return True 
    if the number of suspicious words is greater than or equal to half of 
    the length of the list of suspicious words, otherwise return False
    
    '''
    
    count = 0
    analyze, extention = open_file(file)
    
    if extention.lower() == '.exe':
        for w in list_word :
            if w.encode() in analyze:
                count += 1
    elif extention.lower() == '.py' or extention.lower() == '.c':
        for w in list_word :
            if w in analyze:
                count += 1
    if count == 0:
        return False
    elif count >= len(list_word)/3:
        return True
    else:
        return False
      
def analyze_connection(file):
    
    ''' 
        analyze if the file contains connection and send data.
        return True if the file contains connection and send data, otherwise return False.
    '''
    analyze, extention = open_file(file)
    if extention.lower() == '.exe':
        if b'socket' in analyze and b'connect' in analyze or b'send' in analyze:
            return True
        else:
            return False
    elif extention.lower() == '.py' or extention.lower() == '.c':
        
        if 'socket' in analyze and 'connect' in analyze or 'send' in analyze:
            return True
        else:
            return False
def analyze_contain_storage_file(file):
    
    '''
    Analyze if the file contains storage file and return True if the file contains storage file, otherwise return False.
    '''
    analyze, extention = open_file(file)
    if extention.lower() == '.exe':
        if b'open' in analyze or b'write' in analyze or b'add' in analyze:
            return True
        else:
            return False
    elif extention.lower() == '.py':
        if 'open' in analyze or 'write' in analyze or 'add' in analyze:
            return True
        else:
            return False
    elif extention.lower() == '.c':
        if 'fopen' in analyze or 'fwrite' in analyze or 'add' in analyze:
            return True
        else:
            return False
    
        
def analyze_anti_virus_keylogger(file, list_word):
    
    ''' 
        analyze if the file is suspicious and return True if the file is suspicious, otherwise return False.
    '''
    if suspicious_word_count(file, list_word) and analyze_connection(file) and analyze_contain_storage_file(file):
        print('The file is suspicious because it contains suspicious words, connection and storage file')
        return True
    elif suspicious_word_count(file, list_word) and analyze_connection(file):
        print('The file is suspicious because it contains suspicious words and connection')
        return True
    elif suspicious_word_count(file, list_word) and analyze_contain_storage_file(file):
        print('The file is suspicious because it contains suspicious words and storage file')
        return True
    else:
        print('The file is safe')
        return False
    
if __name__ == "__main__":
    
    suspicious_word = ['pynput', 'keyboard', 'Listener', 'keylogger', 'log', 'keystroke', 'data', 'pyHook', 'pynput.keyboard', 'virus', 'getchar']
    
    if test_supported_extention('test.exe'):       
    
        analyze_anti_virus_keylogger('test.exe', suspicious_word)


