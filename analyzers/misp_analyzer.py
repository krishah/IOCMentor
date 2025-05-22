import requests
from config import MISP_API_KEY, MISP_API_URL

class MISPAnalyzer:
    def analyze(self, ioc):
        headers = {
            "Authorization": MISP_API_KEY,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        data = {"value": ioc}
        response = requests.post(f"{MISP_API_URL}/attributes/restSearch", json=data, headers=headers, verify=False)
        return response.json() if response.ok else {"error": response.text}
