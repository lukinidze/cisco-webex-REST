#the following code creates room named "Devnet Training" using POST request

import requests

access_token='NzVkZDliNWQtYjYwMS00YTg5LTlhODYtNTY1OTQ5M2M5MDhhOTk5OTBjN2YtYTA1_P0A1_19365916-598f-457d-9ca7-51a422c8769e' # Make sure to add your access token here
url='https://webexapis.com/v1/rooms'
headers={
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'DevNet Associate Training!'}

res=requests.post(url, headers=headers, json=params)
print(res.json())