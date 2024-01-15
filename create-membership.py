import requests

access_token=''# Make sure to add your access token here
room_id=''# Add the room Id from the previous example
person_email=''# Add the email address of someone with a Webex account
url='https://webexapis.com/v1/memberships'
headers={
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'roomId': room_id, 'personEmail': person_email}
res=requests.post(url, headers=headers, json=params)
print(res.json())

# When you "create a membership" by sending a POST command to the /memberships resource, you add the person to a room.
# I haven't tested this script, but it should work. 
# to get the room_id, execute list-rooms.py