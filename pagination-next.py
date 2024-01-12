# Make the next paginated API request
import requests
import json

access_token='NzVkZDliNWQtYjYwMS00YTg5LTlhODYtNTY1OTQ5M2M5MDhhOTk5OTBjN2YtYTA1_P0A1_19365916-598f-457d-9ca7-51a422c8769e'# Make sure to add your access token here
url='https://webexapis.com/v1/memberships'
headers={
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={
    "max": 1
}
res=requests.get(url, headers=headers, params=params)

second_response=requests.get(res.links['next']['url'], headers=headers)
formatted_message="""
Webex Second API Response
----------------------------------
Response Status Code   : {}
Response Link Header   : {}
Response Body          : {}
-----------------------------------
""".format(second_response.status_code,  second_response.headers.get('Link'), json.dumps(second_response.json(), indent=4))
print(formatted_message)
