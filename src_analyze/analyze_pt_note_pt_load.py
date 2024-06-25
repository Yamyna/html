import os
from elftools.elf.elffile import ELFFile

def test_supported_extension_elf(file):
    '''
    Test if the extension of the file is supported and return True if the extension of the file is supported, otherwise return False
    '''
    try :
        with open(file, 'rb') as f:
            elf = ELFFile(f)
            return True
    except:
        return False

def search_pt_note_pt_load(file):
    '''
    Search for the presence of PT_NOTE and PT_LOAD in the file
    '''
    compteur_note = 0
    compteur_load = 0
    with open(file, 'rb') as f:
        elf = ELFFile(f)
        for segment in elf.iter_segments():
            if segment.header.p_type == 'PT_NOTE':
                compteur_note += 1
            if segment.header.p_type == 'PT_LOAD':
                compteur_load += 1
    if compteur_note <= 1 and compteur_load >= 5:
        return True
def check_e_entry(file):
    '''
    Check if the entry point is in the PT_LOAD section
    '''
    with open(file, 'rb') as f:
        elf = ELFFile(f)
        entry = elf.header['e_entry']
        for segment in elf.iter_segments():
            if segment.header.p_type == 'PT_LOAD':
                if entry >= segment.header.p_vaddr and entry <= segment.header.p_vaddr + segment.header.p_memsz:
                    return True
        return False
    
def check_p_memsz(file):
    
    '''
    Check if the p_memsz is greater than the p_filesz
    '''
    with open(file, 'rb') as f:
        elf = ELFFile(f)
        for segment in elf.iter_segments():
            if segment.header.p_memsz > segment.header.p_filesz:
                return True
    
def search_for_injected_code(file_path):
    '''
    Search for injected code in the ELF file
    '''
    with open(file_path, 'rb') as f:
        f.seek(-1024,os.SEEK_END)
        data = f.read(1024)
        if b'\x23\x21' in data:
            return True
        elif b'\x7F\x45\x4C\x46' in data:
            return True
        elif b'\xCA\xFE\xBA\xBE' in data:
            return True
        elif b'\x2F\x62\x69\x6E\x2F\x2F\x73\x68' in data:
            return True
        else:
            return False        

def analyze_file(file_path):
    extention = test_supported_extension_elf(file_path)
    with open('/tmp/scan_result.txt', 'a') as f:
        f.write('\n\n\'PT_NOTE TO PT_LOAD\' ANTIVIRUS')
        if extention == False:
            f.write('\n✗ file type not supported')
            return False
        else:
            pt_note = search_pt_note_pt_load(file_path)
            inject_code = search_for_injected_code(file_path)
            e_entry = check_e_entry(file_path)
            p_memsz = check_p_memsz(file_path)
            if pt_note:
                f.write('\n✓ pt_note to pt_load sections')
            else :
                f.write('\n✗ pt_note to pt_load sections')

            if e_entry:
                f.write('\n✓ e_entry in pt_load section')
            else:
                f.write('\n✗ e_entry in pt_load section')

            if p_memsz:
                f.write('\n✓ p_memsz greater than p_filesz')
            else :
                f.write('\n✗ p_memsz greater than p_filesz')    
            if inject_code:               
                f.write('\n✓ injected code')
            else :
                f.write('\n✗ injected code')