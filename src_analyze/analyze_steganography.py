
import os
import result_analyse

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
    
    ''' 
        This function is used to analyze the file for steganography and return the list of file type that may be hidden in the file
    '''
    data, _ = open_file(file)
    list_filetype = []
    signatures = {
        b'\x4D\x5A': '.exe',
        b'\x23\x21': '.py',
        b'\x7F\x45\x4C\x46': '.elf', 
        b'\xCA\xFE\xBA\xBE': '.java',  
    }

    for signature, filetype in signatures.items():
        if signature in data:
            list_filetype.append(filetype)
    result_analyse.append_to_file_with_permissions('./scan_result.txt', f'Result of steganography analysis :\nFile: {file} may contain hidden {list_filetype} content\n\n')
    return list_filetype