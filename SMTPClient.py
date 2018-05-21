#!/usr/bin/env python

import ssl
import base64
from socket import *
from socket import socket

# Message to send
msg = '\r\nI love computer networks!'
endmsg = '\r\n.\r\n'


# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)

# Port number may change according to the mail server
clientSocket.connect((mailserver, 587))
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send EHLO command and print server response.
heloCommand = 'EHLO gmail.com\r\n'
clientSocket.send(heloCommand)
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '250':
    print '250 reply not received from server.'

# Create TLS connection for Gmail
clientSocket.send('STARTTLS\r\n')
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

# Use SSL wrapping and authorization, as required by Gmail
clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)
clientSocket.send('AUTH LOGIN\r\n')
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '334':
    print '334 reply not received from server.'

# Send authorization to Gmail using Base64 encoding
username = base64.b64encode('araihan1CS428@gmail.com')
password = base64.b64encode('networks123')
clientSocket.write(username + '\r\n')
clientSocket.write(password + '\r\n')

# Send MAIL FROM command and print server response.
mailfrom = 'MAIL FROM: <araihan1CS428@gmail.com>\r\n'

# Your code here
clientSocket.send(mailfrom)
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '334':
    print 'mail from 334 reply not received from server.'

# Send RCPT TO command and print server response.
rcptto = 'RCPT TO: <araihan1@binghamton.edu>\r\n'
# Your code here
clientSocket.send(rcptto)
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '235':
    print '235 reply not received from server.'

# Send DATA command and print server response.
data = 'DATA\r\n'
# Your code here
clientSocket.send(data)
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '250':
    print '250 reply not received from server.'

# Send message data.
# Your code here
clientSocket.send(msg + endmsg)
recv = clientSocket.recv(1024)
if recv[:3] != '250':
    print '250 reply not received from server.'

# Send QUIT command and get server response.
quitcommand = 'QUIT\r\n'
# Your code here
clientSocket.send(quitcommand)
recv = clientSocket.recv(1024)
if recv[:3] != '354':
    print '354 reply not received from server.'
