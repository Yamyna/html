
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


def analyze_steganography(file):
    
    data, ext = open_file(file)
    
    signatures = {
        b'\x4D\x5A': '.exe',
        b'\x23\x21': '.py',
        b'\x7F\x45\x4C\x46': '.elf', 
        b'\xCA\xFE\xBA\xBE': '.java',  
    }

    for signature, filetype in signatures.items():
        if signature in data:
            print(f"Warning: File may contain hidden {filetype} content")
            
analyze_steganography("test.txt")