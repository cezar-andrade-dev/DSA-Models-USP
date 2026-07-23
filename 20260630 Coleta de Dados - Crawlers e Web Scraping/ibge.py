import requests

URL = "https://www.ibge.gov.br/acesso-informacao/institucional/trabalhe-conosco/45199-2025-05-supervisor-de-coleta-e-qualidade.html"

res = requests.get(URL)

print("Status code: ", res.status_code)