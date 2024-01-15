# prior executing this script, you need to know your Room ID.
# to find out your room ID, execute list-rooms.py

import requests

access_token='NzVkZDliNWQtYjYwMS00YTg5LTlhODYtNTY1OTQ5M2M5MDhhOTk5OTBjN2YtYTA1_P0A1_19365916-598f-457d-9ca7-51a422c8769e' # Make sure to add your access token here
room_id=input("Please paste the room ID and press Enter ") # Make sure you add the room ID value that was returned from the previous call you made
url='https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers={
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res=requests.get(url, headers=headers)
print(res.json())