import subprocess

def clamscan_file(file_path):
    try:
        result = subprocess.run(['clamscan', file_path], capture_output=True, text=True, timeout=300)
        
        if "Infected files: 0" in result.stdout:
            print("Fichier sans virus.")
        else:
            print("Fichier infecté. Attention !")
        
    except subprocess.TimeoutExpired:
        print("La commande clamscan a dépassé le délai imparti.")
    except Exception as e:
        print("Une erreur s'est produite lors de l'exécution de la commande clamscan:", e)

if __name__ == "__main__":

    file_path = "file_test.txt"
    clamscan_file(file_path)
