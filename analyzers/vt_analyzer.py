import requests
from config import VIRUSTOTAL_API_KEY

class VirusTotalAnalyzer:
    def __init__(self):
        self.api_url = "https://www.virustotal.com/api/v3"
        self.headers = {"x-apikey": VIRUSTOTAL_API_KEY}

    def analyze(self, ioc):
        if '.' in ioc:
            url = f"{self.api_url}/domains/{ioc}"
        else:
            url = f"{self.api_url}/ip_addresses/{ioc}"
        response = requests.get(url, headers=self.headers)
        return response.json() if response.ok else {"error": "VT API error"}
