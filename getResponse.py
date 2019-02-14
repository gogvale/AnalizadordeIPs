import requests

url = "https://10.4.29.121/api/"

querystring = {"type":"log","log-type":"traffic","query":"( addr in 68.183.70.42 )"}

payload = ""
headers = {
    'key': "LUFRPT1FMkhtM1Y2empPZFFuaE95anFDTmpvTGFjZXc9Y1hyeGlWdXpJUXFSRW81cy9DczVmaC9IUjVLZG9kc0VZZzBDQlYyQ05paz0=",
    'Authorization': "Basic ZWxveWE6TWNwbHVzMTEzYWRtIW4=",
    'cache-control': "no-cache",
    'Postman-Token': "a456d01a-989d-460f-9ef3-4834561f2917"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring, verify=False)

print(response.text)