import sys
from API_KEY import *
from pysafebrowsing import SafeBrowsing
from OTXv2 import OTXv2, IndicatorTypes
from pprint import pprint

def Analyse_urls_api_Google(url):

    client = SafeBrowsing(Google_key)
    res = client.lookup_urls([url])
    return res

def Analyse_urls_api_otx(url):
    otx_api = OTXv2(OTX_key)
    res = otx_api.get_indicator_details_full(IndicatorTypes.URL, url)
    return res

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print("Usage: python analyze_url.py <url>")
        sys.exit(1)
        
    url_test = 'http://malware.testing.google.test/testing/malware/'
    url = sys.argv[1]
    try:
    
        resultat_google = Analyse_urls_api_Google(url)
    except Exception as e:
        print(f"Erreur lors de l'analyse Google : {e}")
        
    print("Google Safe Browsing Analysis:\n")
    
    for info in resultat_google.items():
        print("pour l'url : {} les résultats d'analyse sont:\n ".format(info[0]))
        dictionnaire = info[1]
        for valeur in dictionnaire:
            print("{}: {}".format(valeur, dictionnaire[valeur]))
            
    print("OTX Safe Browsing Analysis:\n")
    try:
        resultat_otx = Analyse_urls_api_otx(url)
    except Exception as e:
        print(f"Erreur lors de l'analyse OTX : {e}")
        
    if 'url_list' in resultat_otx and isinstance(resultat_otx['url_list'], dict):
        url_list = resultat_otx['url_list'].get('url_list', [])
        for url_info in url_list:
            result_info = url_info.get('result', {}).get('urlworker', {}).get('error')
            if result_info:
                print("L'URL est malveillante.")
                if isinstance(result_info, Exception):
                    print(f"Détails de la menace : {type(result_info).__name__}: {result_info}")
                else:
                    print(f"Détails de la menace : {result_info}")
                break

        else:
            print("L'URL n'est pas malveillante.")
    else:
        print("Aucune information sur la malveillance trouvée pour l'URL.")