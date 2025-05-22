import requests
from config import IPINFO_TOKEN

class IPInfoAnalyzer:
    def __init__(self):
        self.api_url = "https://ipinfo.io"

    def analyze(self, ioc):
        response = requests.get(f"{self.api_url}/{ioc}/json?token={IPINFO_TOKEN}")
        return response.json() if response.ok else {"error": "ipinfo API error"}
