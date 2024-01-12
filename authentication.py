import requests
import json
# This access token may be a (limited duration) personal access token, a Bot token, or an OAuth token from an Integration or Guest Issuer application.
# the following token was taken from here https://developer.webex.com/docs/getting-your-personal-access-token

access_token='NzVkZDliNWQtYjYwMS00YTg5LTlhODYtNTY1OTQ5M2M5MDhhOTk5OTBjN2YtYTA1_P0A1_19365916-598f-457d-9ca7-51a422c8769e'
url='https://webexapis.com/v1/people/me'
headers={
    'Authorization': 'Bearer {}'.format(access_token)
}
res=requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

