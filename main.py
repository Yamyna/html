import sys
import pyclamd
import subprocess
from pysafebrowsing import SafeBrowsing
import requests
from API_KEY import *
from OTXv2 import OTXv2, IndicatorTypes

def Analyse_urls_api_Google(url):

    """
    This function is used to API call to Google form analysis the urls if malicious or not
    :param Google_key:  API key for Google
    :param url: URL to analyze
    :return: response from Google form analysis

    """

    client = SafeBrowsing(Google_key) #utilisé pour effectuer des recherches de menaces en utilisant l'API Google Safe Browsing.
    test_url = client.lookup_urls([url])
    return test_url

def Analyse_urls_api_otx(url):
    otx_api = OTXv2(OTX_key)
    test_url = otx_api.get_indicator_details_full(IndicatorTypes.URL, url)
    return test_url
url = 'http://malware.testing.google.test/testing/malware/'

if __name__ == '__main__':
    print("Google Safe Browsing Analysis:")
    resultat_google = Analyse_urls_api_Google(url)
    for i in resultat_google.items():
        print(i[1])
        tab = i[1]
    print(tab)
    print("\nOTX Analysis:")
    print(Analyse_urls_api_otx(url))

'''{'http://malware.testing.google.test/testing/malware/': {'malicious': True, 'platforms': ['ANY_PLATFORM'], 'threats': ['MALWARE'], 'cache': '300s'}}'''
