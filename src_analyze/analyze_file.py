import clamd

def clamscan_file(file_path):
    try:
        clam = clamd.ClamdUnixSocket()
        result = clam.scan_file(file_path)
        if 'OK' in result[file_path]:
            print("Fichier sans virus.")
        else:
            print("Fichier infecté. Attention !")

    except Exception as e:
        print("Une erreur s'est produite lors de l'analyse du fichier:", e)

if __name__ == "__main__":
    file_path = "test.exe"
    clamscan_file(file_path)