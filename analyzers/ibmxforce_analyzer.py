import requests
from config import XFORCE_API_KEY, XFORCE_API_PASS

class IBMXForceAnalyzer:
    def analyze(self, ioc):
        url = f"https://api.xforce.ibmcloud.com/url/{ioc}"
        response = requests.get(url, auth=(XFORCE_API_KEY, XFORCE_API_PASS))
        return response.json() if response.ok else {"error": response.text}
