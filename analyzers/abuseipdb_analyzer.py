import requests
from config import ABUSEIPDB_API_KEY

class AbuseIPDBAnalyzer:
    def __init__(self):
        self.api_url = "https://api.abuseipdb.com/api/v2/check"
        self.headers = {"Key": ABUSEIPDB_API_KEY, "Accept": "application/json"}

    def analyze(self, ioc):
        params = {"ipAddress": ioc, "maxAgeInDays": 90}
        response = requests.get(self.api_url, headers=self.headers, params=params)
        return response.json().get("data", {}) if response.ok else {"error": "AbuseIPDB API error"}
