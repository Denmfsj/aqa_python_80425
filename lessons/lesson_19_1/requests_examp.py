import requests
from requests.auth import HTTPDigestAuth, HTTPBasicAuth, HTTPProxyAuth


response = requests.get('https://api.example.com', auth=('username', 'password'))


response = requests.get('https://api.example.com',
                        auth=HTTPBasicAuth('username', 'password'))