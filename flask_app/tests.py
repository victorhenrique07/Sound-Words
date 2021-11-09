from httpx import get

url_base = 'http://localhost:5000/'

request = (get(url_base))

assert request.status_code == 200, "Código de resposta diferente de 200"
