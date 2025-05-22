import requests
from config import IBM_API_KEY, IBM_API_PASS

class IBMXForceAnalyzer:
    def analyze(self, ioc):
        url = f"https://api.xforce.ibmcloud.com/url/{ioc}"
        response = requests.get(url, auth=(IBM_API_KEY, IBM_API_PASS))
        return response.json() if response.ok else {"error": response.text}
