import os
os.chdir('/var/www/html/analyze_result')
#récupère les fichiers de résultats:
if __name__ == "__main__":
    
    try:
        with open("scan_result_clam.txt", "r") as f:
            print("\nRésultats Clamav:")
            print(f.readline().strip())
          
        with open("scan_result_python.txt","r") as f:
            print("\nRésultats de l'analyse script Python:")
            print(f.read())
            
    except Exception as e:
        print(f"Erreur lors de l'ouverture des fichiers de résultats : {e}")
