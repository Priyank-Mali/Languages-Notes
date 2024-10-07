# import socket

# mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysocket.connect(('data.pr4e.org',80))
# cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
# mysocket.send(cmd)

# while True:
#     data = mysocket.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end="")

# mysocket.close()

import requests

url = "https://api.freeapi.app/api/v1/public/randomusers"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    # for key in data['data']:
    #       print(data['data'][key])

