import sys
import pyclamd
import subprocess
from pysafebrowsing import SafeBrowsing
import requests
from API_KEY import *


def Analyse_urls_api_Google(Google_key, url):

    """
    This function is used to API call to Google form analysis the urls if malicious or not
    :param Google_key:  API key for Google
    :param url: URL to analyze
    :return: response from Google form analysis

    """

    client = SafeBrowsing(Google_key) #utilisé pour effectuer des recherches de menaces en utilisant l'API Google Safe Browsing.
    test_url = client.lookup_urls([url])
    return test_url


if __name__ == '__main__':

    print(Analyse_urls_api_Google(Google_key, 'http://malware.testing.google.test/testing/malware/'))
