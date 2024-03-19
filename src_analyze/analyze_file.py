import clamd
import yara
import pefile
import hashlib
import subprocess
from scapy.all import *
"""
    Function that analyze a file with Clamav

"""
def scan_with_clamd(file_path):
    try:
        clam = clamd.ClamdUnixSocket()
        result = clam.scan_file(file_path)
        if 'OK' in result[file_path]:
            print("Fichier sans virus.")
        else:
            print("Fichier infecté. Attention !")

    except Exception as e:
        print("Une erreur s'est produite lors de l'analyse du fichier:", e)

"""
    Function that analyze a file with Yara and rules of Yara
    
"""
def scan_with_yara(file_path, rules_file):
    try:
        rules = yara.compile(rules_file)
        matches = rules.match(file_path)
        if matches:
            print("Le fichier est malveillant selon les règles YARA.")
        else:
            print("Le fichier semble sûr selon les règles YARA.")
    except Exception as e:
        print("Une erreur s'est produite lors de l'analyse avec YARA:", e)
"""
    Function that analyze a file with Yara and rules of PE
    
"""
def analyze_pe_file(file_path):
    try:
        pe = pefile.PE(file_path)
        print("Analyse du fichier PE terminée.")
    except Exception as e:
        print("Une erreur s'est produite lors de l'analyse avec pefile:", e)

"""
    Function that calculate the hash file for identificate the file and save the vilain hash file.
"""
def calculate_file_hash(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            file_hash = hashlib.sha256(content).hexdigest()
            print("Empreinte SHA256 du fichier:", file_hash)
    except Exception as e:
        print("Une erreur s'est produite lors du calcul du hash:", e)

"""
    Function that analyze file with Suricate and config suricate.
"""
def analyze_with_suricata(file_path, suricata_config):
    try:
        subprocess.run(['suricata', '-c', suricata_config, '-r', file_path])
        print("Analyse avec Suricata terminée.")
    except Exception as e:
        print("Une erreur s'est produite lors de l'analyse avec Suricata:", e)
"""
    Function that analyze the traffic netword d'un fichier. Awaiting testing.
"""
def analyze_network_traffic(packet_file):
    try:
        packets = rdpcap(packet_file)
        print("Analyse du trafic réseau terminée.")
    except Exception as e:
        print("Une erreur s'est produite lors de l'analyse avec Scapy:", e)


if __name__ == "__main__":
    file_path = "test.exe"
    scan_with_clamd(file_path)
    scan_with_yara("fichier.exe", "regles.yara")
    analyze_pe_file("fichier.exe")
    calculate_file_hash("fichier.exe")
    analyze_with_suricata("fichier.pcap", "suricata.yaml")
    analyze_network_traffic("trafic.pcap")