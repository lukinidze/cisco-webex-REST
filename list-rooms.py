#code lists all of the rooms for the authenticated user
import requests
import sys

access_token='MGJlOWNhYmItMGQ4Yi00ODkyLTk1MDAtYTViNzVmZWUwZjBmMjYxM2FhNjUtNTIw_P0A1_19365916-598f-457d-9ca7-51a422c8769e' # Make sure to add your access token here
url='https://webexapis.com/v1/rooms'
headers={
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'max': '100'}
res=requests.get(url, headers=headers, params=params)
print(res.json())

message = (
    "\nIf you would like to get more details for any specific room"
    "(such as for ex. to start a meeting), just copy the room id"
    "from the ouput above, and execute get-room-details.py"
)

print(message)


