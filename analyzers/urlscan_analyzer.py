import requests

class URLScanAnalyzer:
    def __init__(self):
        self.api_url = "https://urlscan.io/api/v1/scan/"
        self.api_key = 'your_urlscan_key'

    def analyze(self, ioc):
        headers = {"API-Key": self.api_key}
        data = {"url": ioc}
        response = requests.post(self.api_url, headers=headers, json=data)
        return response.json() if response.ok else {"error": "URLScan API error"}
