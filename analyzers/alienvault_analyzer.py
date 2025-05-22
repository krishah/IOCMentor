import requests
from config import OTX_API_KEY

class AlienVaultAnalyzer:
    def analyze(self, ioc):
        headers = {
            "X-OTX-API-KEY": OTX_API_KEY,
            "Accept": "application/json"
        }
        url = f"https://otx.alienvault.com/api/v1/indicators/URL/{ioc}/general"
        response = requests.get(url, headers=headers)
        return response.json() if response.ok else {"error": response.text}
