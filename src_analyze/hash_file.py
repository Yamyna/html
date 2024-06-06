import hashlib
import result_analyse

def hash_files(filename):
    """
    Cette fonction retourne le hash MD5 du fichier passé en paramètre.
    """
    h = hashlib.md5()

    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def is_hash_in_file(hash_file, hash_value):
    """
    Cette fonction vérifie si le hash du fichier est présent dans notre liste de hash MD5 malveillants.
    """
    with open(hash_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return any(hash_value in line for line in lines)

def add_hash_to_file(hash_value, hash_file):
    """
    Cette fonction ajoute le hash donné au fichier de hash spécifié.
    """
    with open(hash_file, 'a', encoding='utf-8') as file:
        file.write(hash_value + '\n')

def analyze_hash_file(file):
    """
    Cette fonction ajoute le hash du fichier si celui-ci est présent dans notre liste de hash MD5 malveillants et écrit l'information dans scan_result.
    """
    result_analyse.append_to_file_with_permissions('./scan_result.txt', 'Result of MD5 hash database :')
    hash_value = hash_files(file)
    if is_hash_in_file("md5_hash.txt", hash_value):
        result_analyse.append_to_file_with_permissions('./scan_result.txt', 'The file has a hash present in our MD5 hash database.\n\n')
    else:
        result_analyse.append_to_file_with_permissions('./scan_result.txt', 'File is not present in the database of MD5 hashes.\n\n')