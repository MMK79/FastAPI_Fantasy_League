import httpx

grpahql_url = "https://countries.trevorblades.com"

json_query = {
    "query": """
{
country(code:"US"){
    name
    native
    currency
        languages{
        code
        name
        }
    }
}
"""
}

api_response = httpx.post(grpahql_url, json=json_query)
print(api_response.json())
