import requests

access_token='MGJlOWNhYmItMGQ4Yi00ODkyLTk1MDAtYTViNzVmZWUwZjBmMjYxM2FhNjUtNTIw_P0A1_19365916-598f-457d-9ca7-51a422c8769e'# Make sure to add your access token here
room_id='Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNDUwODkwZDAtYjFhYS0xMWVlLTk4YzctYTNmZjYzNTQ0NmU1'# Add the roomId here

url='https://webexapis.com/v1/messages'
headers={
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'roomId': room_id}
res=requests.get(url, headers=headers, params=params)
print(res.json())
