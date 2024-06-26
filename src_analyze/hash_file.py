import hashlib
import os

os.chdir('/tmp/src_analyze') 

def hash_files(filename):
    """
    Returns the MD5 hash of the specified file.

    Args:
        filename (str): The path to the file to be hashed.

    Returns:
        str: The MD5 hash of the file.
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
    Checks if the given hash value is present in the specified hash file.

    Args:
        hash_file (str): The path to the file containing a list of hash values.
        hash_value (str): The hash value to check for.

    Returns:
        bool: True if the hash value is found in the file, False otherwise.
    """
    with open(hash_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return any(hash_value in line for line in lines)

def add_hash_to_file(hash_value, hash_file):
    """
    Adds the given hash value to the specified hash file.

    Args:
        hash_value (str): The hash value to add.
        hash_file (str): The path to the file where the hash value will be added.

    Returns:
        None
    """
    with open(hash_file, 'a', encoding='utf-8') as file:
        file.write(hash_value + '\n')

def analyze_hash_file(file):
    """
    Analyzes the hash of the specified file against a list of known malicious MD5 hashes and logs the result.

    Args:
        file (str): The path to the file to be analyzed.

    Writes:
        A summary of the analysis to '/tmp/scan_result.txt'.
    """
    hash_value = hash_files(file)
    with open('/tmp/scan_result.txt', 'a') as f:
        f.write('\n\nMD5 HASH DATABASE')
        if is_hash_in_file("md5_hash.txt", hash_value):
            f.write('\n✓ in our MD5 hash database')
        else:
            f.write('\n✗ in our MD5 hash database')