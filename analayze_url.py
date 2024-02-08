import sys
import pyclamd
from pysafebrowsing import SafeBrowsing
from API_KEY_google import *

def Analyse_urls_api_Google(Google_key, url):
    """
    This function is used to API call to Google for analyzing the URLs for malicious content.
    :param Google_key: API key for Google
    :param url: URL to analyze
    :return: response from Google for analysis
    """
    client = SafeBrowsing(Google_key)
    test_url = client.lookup_urls([url])
    return test_url

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python analyze_url.py <url>")
        sys.exit(1)

    url_input = sys.argv[1]
    result = Analyse_urls_api_Google(Google_key, url_input)
    print(result)
