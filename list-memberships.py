# The roomId is optional. To list all memberships, do not include the roomId. 
# To list memberships associated with a room, add the roomId to the request.
# To get roomId, execute list-rooms.py

import requests

access_token='MGJlOWNhYmItMGQ4Yi00ODkyLTk1MDAtYTViNzVmZWUwZjBmMjYxM2FhNjUtNTIw_P0A1_19365916-598f-457d-9ca7-51a422c8769e' # Make sure to add your access token here


room_id=input("Please paste the room ID and press Enter \nTo list all memberships hit Enter without pasting the room ID: ") # Make sure you add the room ID value that was returned from the previous call you made
url='https://webexapis.com/v1/memberships'
headers={
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
if room_id != "":
    params={'roomId': room_id}
    res=requests.get(url, headers=headers, params=params)
else:
    res=requests.get(url, headers=headers)
print(res.json())