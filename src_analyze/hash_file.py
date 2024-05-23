import hashlib

def hash_files(filename):
    """
    This function returns the MD5 hash
    of the file passed into it
    """
    h = hashlib.md5()

    with open(filename,'rb') as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def is_hash_in_file(hash_value, hash_file):
    with open(hash_file, 'r') as file:
        lines = file.readlines()

    return any(hash_value in line for line in lines)

file_hash = hash_files('test.exe') # On doit d'abord analyzer avec les autres codes, voir s'il y a des suspicions de malware et s'il y en a l'ajouter aux fichiers. On peut ajouter cette fonctionnalité dans le code de l'analyseur.
print(is_hash_in_file(file_hash, 'md5_hash.txt'))