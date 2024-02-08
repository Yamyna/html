import re

def check_sql_injection(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("Contenu du fichier:", content)

            sql_patterns = [
                r'\b(?:OR\s+1\s*=\s*1|1\s*=\s*1)\b',
                r'\b(?:UNION\s+ALL\s+SELECT|UNION\s+SELECT)\b',
                r'\b(?:DROP\s+TABLE)\b',
                r'\b(?:SELECT\s+\*\s+FROM)\b',
            ]

            for pattern in sql_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    return "Injection SQL détectée."

            return "Safe"

    except FileNotFoundError:
        return "Le fichier spécifié est introuvable."


file_path = "file_test.txt"
result = check_sql_injection(file_path)
print("Résultat de la détection:", result)
