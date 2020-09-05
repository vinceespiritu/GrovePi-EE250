"""
Server IP is 34.209.114.30, ports are 5000-5008, socket is UNIX TCP 
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
"""
import socket
import random

def main():

    HOST = "34.209.114.30"
    PORT = random.randint(5000,5008)
    # TODO: Create a socket and connect it to the server at the designated IP and port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
    # TODO: Get user input and send it to the server using your TCP socket
    send_data = input("Enter data to send to server")
    sock.sendall(bytes(send_data, 'utf-8'))
    # TODO: Receive a response from the server and close the TCP connection
    response = sock.recv(1024)
    sock.close()

    print ("Server response:",repr(response))
	    

if __name__ == '__main__':
    main()
