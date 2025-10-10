import httpx

rest_url = "https://api.sportsworldcentral.com/v0/players/1491"
rest_url = "http://0.0.0.0:8000/v0/players/1491"

api_response = httpx.get(rest_url)
print(api_response.json())
