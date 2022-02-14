import requests
import random2
import json
auth = {
    "user": "admin",
    "password": "district"
}
url = "http://play.dhis2.org/demo/api/24/dataValueSets?dataSet=GoQawwqec4j&completeDate=2024-06-06&period=LAST_QUARTER&orgUnit=bVo3BRA2D2a"

payload=[
    {'Beginning Balance': 1000,
'Quality Dispenced': 450,
'Closing Balance': 550},

{'Beginning Balance': 1000,
'Quality Dispenced': 450,
'Closing Balance': 550},

{'Beginning Balance': 1000,
'Quality Dispenced': 450,
'Closing Balance': 550}
]


files=[

]
headers = {
  'Authorization': 'Basic YWRtaW46ZGlzdHJpY3Q=',
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)


def get_json(url, auth):
  user = auth['user'];
  password = auth['password']

  r = requests.get(url, auth=(user, password))
  return r.json()
