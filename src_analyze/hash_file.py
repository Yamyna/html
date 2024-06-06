import hashlib
import result_analyse

def hash_files(filename):
    """
    This function returns the MD5 hash
    of the file passed into it
    """
    h = hashlib.md5()

    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def is_hash_in_file(hash_value, hash_file):
    """
    This function checks if the hash of the file is present in our malicious md5 hash list
    """
    with open(hash_file, 'r', encoding='utf-8') as file: 
        lines = file.readlines()

    return any(hash_value in line for line in lines)

def add_hash_to_file(hash_value, hash_file):
    """
    This function adds the given hash to the specified hash file.
    """
    with open(hash_file, 'a', encoding='utf-8') as file:  
        file.write(hash_value + '\n')


def analyze_hash_file(file):
    """
    This function adds hash of the file if the hash of the file is present in our malicious md5 hash list and write into scan_result the information. 
    """
    if(is_hash_in_file("md5_hash.txt",hash_files(file))):
        add_hash_to_file("md5_hash.txt",hash_files(file))
        result_analyse.append_to_file_with_permissions('./scan_result.txt', 'The file has a hash present in our MD5 hash database.')
    else :
        result_analyse.append_to_file_with_permissions('./scan_result.txt', 'File is not present in the database of MD5 hashes.')