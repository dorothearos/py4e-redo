"""
Change your socket program so that it counts the number
of characters it has received and stops displaying any
text after it has shown 3000 characters. The program should retrieve
the entire document and count the total number of characters
and display the count of the number of characters at the end
of the document.
"""

import socket
import time
"""
    Open the socket(address family, port type)
    Connect to the socket(url, port):
        url(string): user input
        port(int)
"""
user_url = input('Enter URL: ')
try:
    url = user_url.split('/')[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((url, 80))
    cmd = ('GET ' + user_url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

except:
    print('Please enter a valid URL')
    exit()
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    count = ''
    #time.sleep(0.25)
    count = count + (data.decode())

    print(count[:3001], end='')

print("Total characters received:" ,len(count))
mysock.close()
