import os
from elftools.elf.elffile import ELFFile
def open_file(file):
    '''
    Open the file and return the content of the file and the extension of the file
    '''
    try:
        analyze = None
        _, extension = os.path.splitext(file)
        with open(file, 'rb') as f:
            analyze = f.read()
            try:
                elffile = ELFFile(f)
                if elffile: 
                    extension = '.elf'
            except:
                pass
    except:
        analyze = None
    return analyze, extension 

def analyze_steganography(file):
    ''' 
    This function is used to analyze the file for steganography and return the list of file types that may be hidden in the file
    '''
    data, extension = open_file(file)
    with open('/tmp/scan_result.txt', 'a') as f:
        f.write('\n\nANALYZE STEGANOGRAPHY')
        if data is None:
            f.write('\n✗ file type supported')
            return []

        list_filetype = []
        list_filetype.append(extension)
        signatures = {
        b'\x4D\x5A': '.exe',
        b'\x7F\x45\x4C\x46': '.elf',
        b'\xCA\xFE\xBA\xBE': '.class',
        b'\x89\x50\x4E\x47': '.png',
        b'\x47\x49\x46\x38': '.gif',
        b'\xFF\xD8\xFF': '.jpg',
        b'\x25\x50\x44\x46': '.pdf',
        b'\x50\x4B\x03\x04': '.zip',
        b'\x52\x61\x72\x21': '.rar',
        b'\x1F\x8B\x08': '.gz',
        b'\x42\x5A\x68': '.bz2',
        b'\x00\x00\x01\xBA': '.mpg',
        b'\x49\x44\x33': '.mp3',
        b'\x2E\x73\x6E\x64': '.au',
        b'\x25\x21': '.ps',
        b'\x2F\x62\x69\x6E\x2F\x2F\x73\x68' : '.sh',
        b'\x23\x21': '.py',
        }
        for signature, filetype in signatures.items():
            if (signature in data) and (extension != filetype):
                list_filetype.append(filetype)
        if len(list_filetype) > 1:
            f.write(f"\n✓ hidden content {list_filetype}")
        else:
            f.write(f"\n✗ hidden content {list_filetype}")       
    return list_filetype