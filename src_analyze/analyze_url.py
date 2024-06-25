import sys
from API_KEY import Google_key, OTX_key
from pysafebrowsing import SafeBrowsing
from OTXv2 import OTXv2, IndicatorTypes

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
        print("Usage: python3 analyze_url.py <url>")
        sys.exit(1)
        
    url = sys.argv[1]
    
    with open('/app/result_url.txt', 'a') as f:
        f.write("-------------------------- SCAN URL --------------------------\n")
        f.write(f"\nURL : '{url}'\n")

        # Analyse Google Safe Browsing
        try:
            resultat_google = Analyse_urls_api_Google(url)
            if resultat_google:
                malicious_found = False
                for info in resultat_google.items():
                    dictionnaire = info[1]
                    if 'malicious' in dictionnaire and dictionnaire['malicious'] == True:
                        malicious_found = True
                        f.write("\n✗ GOOGLE API\n")
                        for key, value in dictionnaire.items():
                            f.write(f"{key}: {value}\n")
                        break  # Sortir de la boucle si une menace est trouvée
                if not malicious_found:
                    f.write("\n✓ GOOGLE API\n")
                    f.write("No threats found.\n")
            else:
                f.write("\n✓ GOOGLE API\n")
                f.write("No threats found.\n")
        except Exception as e:
            f.write("\n✗ GOOGLE API\n")
            f.write(f"Error: {e}\n")
        f.write("\n")

        # Analyse OTX
        try:
            resultat_otx = Analyse_urls_api_otx(url)
            if 'url_list' in resultat_otx and isinstance(resultat_otx['url_list'], dict):
                url_list = resultat_otx['url_list'].get('url_list', [])
                if url_list:
                    for url_info in url_list:
                        result_info = url_info.get('result', {}).get('urlworker', {}).get('error')
                        if result_info:
                            f.write("\n✗ OTX API\n")
                            f.write(f"Threat Details: {result_info}\n")
                            break
                    else:
                        f.write("\n✓ OTX API\n")
                        f.write("The URL is not malicious.\n")
                else:
                    f.write("\n✓ OTX API\n")
                    f.write("No malicious information found for the URL.\n")
            else:
                f.write("\n✓ OTX API\n")
                f.write("No malicious information found for the URL.\n")
        except Exception as e:
            f.write("\n✗ OTX API\n")
            f.write(f"Error: {e}\n")
        f.write("\n")