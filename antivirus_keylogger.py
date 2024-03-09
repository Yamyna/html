import psutil
import os
import time


## début d'idée verifier si un fichier et lancer dans
def analyze_process_execution():
    
    for process in psutil.process_iter(['pid', 'name']):
        
        if 'keylogger' in process.info['name'].lower():
            
            print("Keylogger détecté :", process.info)
            return True
        with open ("name_list.txt", "r") as file:
            
            for word in file :
                
                if word.strip().lower() in process.info['name'].lower():
                    print("Processus suspect détecté :", process.info)
                    return True
                    
    print("Aucun keylogger détecté.")
    return False



analyze_process_execution()
