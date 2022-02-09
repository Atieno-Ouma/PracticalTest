import requests

auth = {
    "user": "admin",
    "password": "district"
}
url = "https://play.dhis2.org/2.34.9/api/29/dataSets/GoQawwqec4j"

payload={'Beginning Balance': '1000,100,700',
'Quality Dispenced': '450,300,500',
'Closing Balance': '550,700,200'}
files=[

]
headers = {
  'Date': '2022-02-09',
  'Cookie': 'JSESSIONID=3CD9B0BC2EF1773ABB317112AB8F536C'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)


def get_json(url, auth):
  user = auth['user'];
  password = auth['password']

  r = requests.get(url, auth=(user, password))
  return r.json()
