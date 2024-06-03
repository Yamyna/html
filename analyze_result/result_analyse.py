import os
#récupère les fichiers de résultats:
if __name__ == "__main__":
    
    try:
        with open("scan_result_clam.txt", "r") as f:
            f.readlines()
            
            # Extraire les résultats de chaque fichier analysé
            results = []
            for line in f:
                if "/tmp/virus/" in line:
                    file_result = line.strip().split(":")[-1].strip()
                    results.append(file_result)
            # Afficher les résultats
            for result in results:
                print(result)
                
        with open("scan_result_python.txt","r") as f:
                print(f.read())
    except Exception as e:
        print(f"Erreur lors de l'ouverture des fichiers de résultats : {e}")
