# config.py

VIRUSTOTAL_API_KEY = 'your_virustotal_key'
ABUSEIPDB_API_KEY  = 'your_abuseipdb_key'
MISP_URL           = 'https://your-misp-instance'
MISP_API_KEY       = 'your_misp_key'
OPENCTI_URL        = 'https://your-opencti-instance'
OPENCTI_TOKEN      = 'your_opencti_token'
XFORCE_API_KEY     = 'your_xforce_key'
XFORCE_API_PW      = 'your_xforce_password'
ALIENVAULT_KEY     = 'your_otx_key'
IPINFO_TOKEN       = 'your_ipinfo_token'

OLLAMA_SERVER = 'http://localhost:11434'
LLM_MODEL     = 'mistral'
LLM_PROMPT    = ("Analizując poniższy wynik z narzędzi SOC, określ czy wskaźnik IOC: {ioc} jest złośliwy. "
                 "Zwróć propozycję działań (np. blokada, zgłoszenie, eskalacja) uwzględniając dobre praktyki i matrycę MITRE ATT&CK:\n\n{results}")

DEFAULT_ANALYZERS = ['VirusTotal', 'AbuseIPDB', 'MISP', 'Vulners',
                     'URLScan', 'AbuseFinder', 'CyberCrimeTracker',
                     'OpenCTI', 'XForce', 'AlienVault', 'IPInfo']

