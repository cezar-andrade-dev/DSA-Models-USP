import requests

URL = "https://www.ibge.gov.br/acesso-informacao/institucional/trabalhe-conosco/45199-2025-05-supervisor-de-coleta-e-qualidade.html"
URL1 = "https://www.google.com/?hl=pt_BR&zx=1784832899187"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}

try:
    res = requests.get(URL, headers=headers, timeout=10)
    res.raise_for_status()  # Levanta um erro se o status não for 200
    print(res.text)
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")