import hashlib

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
    with open(hash_file, 'r', encoding='utf-8') as file:  # Ajout de l'encodage 'utf-8'
        lines = file.readlines()

    return any(hash_value in line for line in lines)

def add_hash_to_file(hash_value, hash_file):
    """
    This function adds the given hash to the specified hash file.
    """
    with open(hash_file, 'a', encoding='utf-8') as file:  # Ajout de l'encodage 'utf-8'
        file.write(hash_value + '\n')

file_hash = hash_files('../virus/test.exe')
print(is_hash_in_file(file_hash, 'md5_hash.txt'))