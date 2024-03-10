import ast
import modulefinder
import os 

def open_file(file):  
    
    _ , exention = os.path.splitext(file)
    if exention.lower() == '.py':
        with open(file, 'r') as f :
        
            analyze = f.read()
            
    if exention.lower() == '.exe':
        with open(file, 'rb') as f :
            
            analyze = f.read()
    return analyze, exention

def suspicious_word_count(file, list_word):
    
    count = 0
    analyze, extention = open_file(file)
    
    if extention.lower() == '.exe':
        for w in list_word :
            if w.encode() in analyze:
                print (f"suspicious word : {w}")
                count += 1
                
    elif extention.lower() == '.py':
        for w in list_word :
            if w in analyze:
                print (f"suspicious word : {w}")
                count += 1
    print(count)
            
def analyze_imported_libraries(file, list_word):
    
    analyze, extension = open_file(file)
    tree = ast.parse(analyze)

    imported_libraries = set()
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_libraries.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imported_libraries.add(node.module)
    
    for l in imported_libraries:
        if l in list_word:
           print (f"suspicious word : {l}")
    
    return imported_libraries



if __name__ == "__main__":
    suspicious_word = ['pynput','keyboard','Listener', 'socket', 'connect','keylogger', 'log', 'keystroke','data', 'pyHook', 'pynput.keyboard']
    suspicious_word_count('test.py',suspicious_word)
    libraries_used = analyze_imported_libraries('test.py',suspicious_word)


## pyinstaller --name=NomDuProgramme --onefile VotreScript.py

# Par exemple, avec pyinstaller, vous pouvez utiliser la commande suivante pour générer un fichier .spec contenant des informations sur les dépendances 