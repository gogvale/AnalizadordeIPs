import requests

url = "https://10.4.29.121/api/"

querystring = {"type":"log","action":"get","job-id":"972"}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "c28534e4-9efe-4bfe-9032-773a6ddca49e"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)