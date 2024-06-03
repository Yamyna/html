import hashlib

class HashFile:
    def __init__(self, filename):
        self.filename = filename
        self.file_hash = None

    def hash_files(self):
        """
        This function returns the MD5 hash
        of the file passed into it
        """
        h = hashlib.md5()

        with open(self.filename, 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                h.update(chunk)
        self.file_hash = h.hexdigest()
        return self.file_hash

    @staticmethod
    def is_hash_in_file(hash_value, hash_file):
        """
        This function checks if the hash of the file is present in our malicious md5 hash list
        """
        with open(hash_file, 'r') as file:
            lines = file.readlines()

        return any(hash_value in line for line in lines)
    
    @staticmethod
    def add_hash_to_file(hash_value, hash_file):
        """
        This function adds the given hash to the specified hash file.
        """
        with open(hash_file, 'a') as file:
            file.write(hash_value + '\n')

hash_file = HashFile('test.exe')
file_hash = hash_file.hash_files()
if not HashFile.is_hash_in_file(file_hash, 'md5_hash.txt'):
    HashFile.add_hash_to_file(file_hash, 'md5_hash.txt')