VIRUSTOTAL_API_KEY = "b9fc29222b30f1a4bed16796b6701428c074eb9e81c9dc3fbfced182082439dd"
ABUSEIPDB_API_KEY  = "d9d28b65bf54b727aab0f8a0e924e37e9a7cda3128dffd7c7ffc52f4dde05cf7c9e5fa5af2942b17"
MISP_API_URL       = 'https://misp.aliorleasing.pl'
MISP_API_KEY       = "mTcQUZegMfl0Cs33q9XEj3k6If6sqQOKeux4nm2n"
OPENCTI_URL        = 'https://opencti.hackint.pl'
OPENCTI_TOKEN      = 'your_opencti_token'
XFORCE_API_KEY     = "647efed90a2f57575ce7e026aa3c4f69c6b04e98305bc0abd74473ef11e0d9c7"
XFORCE_API_PASS    = 'your_xforce_password'
OTX_API_KEY        = "647efed90a2f57575ce7e026aa3c4f69c6b04e98305bc0abd74473ef11e0d9c7"
IPINFO_TOKEN       = "acb394ae6fb2ba"
URLSCAN_API_KEY     = "947f5975-7eb3-4818-a1cb-d5e18856200d"

OLLAMA_SERVER = "https://ollama.hackint.pl"
LLM_MODEL     = 'phi4'
LLM_PROMPT    = ("Analizując poniższy wynik z narzędzi SOC, określ czy wskaźnik IOC: {ioc} jest złośliwy. "
                 "Zwróć propozycję działań (np. blokada, zgłoszenie, eskalacja) uwzględniając dobre praktyki i matrycę MITRE ATT&CK:\n\n{results}")

DEFAULT_ANALYZERS = ['VirusTotal', 'AbuseIPDB', 'MISP', 'Vulners',
                     'URLScan', 'AbuseFinder', 'CyberCrimeTracker',
                     'OpenCTI', 'XForce', 'AlienVault', 'IPInfo']

