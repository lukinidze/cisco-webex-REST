import requests
import json

access_token='NzVkZDliNWQtYjYwMS00YTg5LTlhODYtNTY1OTQ5M2M5MDhhOTk5OTBjN2YtYTA1_P0A1_19365916-598f-457d-9ca7-51a422c8769e'# Make sure to add your access token here
url='https://webexapis.com/v1/people'
headers={
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={
    'email': 'lukinykhda@gmail.com'# Make sure you add your users's email address here
}
res=requests.get(url, headers=headers, params=params)
print(res.json())

#You can get additional details for a person, by sending a person ID to the API resource:

person_id='Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mODViZGE3ZC04MGMxLTQxYzgtYThhZC1kN2U3YTRkNTA0ZGU' # Add your ID here, which you get from the prior request
url='https://webexapis.com/v1/people/{}'.format(person_id)
headers={
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res=requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))