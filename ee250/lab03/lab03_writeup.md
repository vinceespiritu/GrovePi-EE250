Vince Espiritu <vespirit@usc.edu>
USC ID: 1472908880
Lab 3 Writeup

Part A

1.) How did the reliability of UDP change when you added 50% loss to your local environment? Why did this occur?
	ANSWER: It's been greatly reduced that it wasn't able to completely receive all the data that I have sent consecutively. This occurred because I was sending data too fast that it cannot processed the whole data quickly. Hence, it completely dropped the data since it cannot understand it or an error occurred. UDP can detect errors and data loss but it won't be able to recover the data loss.

2.) How did the reliability of TCP change? Why did this occur?
	ANSWER: The relaiability of TCP did not change but it's has slower response than before. The reliability didn't change because TCP can detect and recover data loss unlike UDP that can only detect errors and have no way to recover it. The slower response occurred because it's trying to recover the 50% of the data that has been lost.

3.) How did the speed of the TCP response change? Why might this happen?
	ANSWER: The speed of the TCP response has been cut to half because half of the data has been lost. Hence, the TCP spent time recovering that data loss.

Part C

1.) What is argc and *argv[]?
	Answer: argc holds the number of argument on the command line including the name of the file, while argv[] is an array of pointers that points to each argument on the command line.

2.) What is a UNIX file descriptor and file descriptor table?
	Answer: A file descriptor table holds an array of pointers to each open "resources" such as files, terminal I/O, network sockets, and etc. Every process that has been opened has STDIN, STDOUT, and STDERR on the file descriptor table, which has index/file descriptor 0, 1, and 2. Furthermore, a file descriptor is an integer indicator(or index) to an open "resources" in the file descriptor table.

3.) What is a struct? What's the structure of sockaddr_in?
	Answer: A struct is like a custom variable type that contains two or more attributes. The structure of sockaddr_in has the attributes serv_addr and cli_addr.

4.) What are the input parameters and return value of socket()
	Answer: socket() has an input parameters of IP Address Family (IPv4 - AF_INET and IPv6 - AF_INET6), the protocol for transporting data (TCP- SOCK_STREAM or UDP- SOCK_DGRAM)

5.) What are the input parameters of bind() and listen()?
	Answer: 
	bind(<host>,<port>)
		- host is a string that holds the hostname, IP Address of the server, or an empty string (which allows the server to listen to other incoming connections from other computers).
		- port is the port number where the server is listening for requests.
	listen(<waitlist>)
		- listen can have an int parameters that specifies the number of connections allowed to be waitlisted. Once the connection requests has reached the waitlist(queued) number, it would refuse other connection requests

6.) Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle?
	- It uses while(1) (loop forever) to remain open and look for connection requets to accept.
	- Based on the code, it won't be able to handle simultaneous connection since accept() is a blocking call function, which means it suspends other calls until it closes the socket connection to the current client or reached the max data size to be transferred to the server.

7.) Research how the command fork() works. How can it be applied here to better handle multiple connections?
	- fork() creates a duplicate of the process (child process)
	- We can use the fork() command here to handle multiple connections by duplicating the process of accepting connection, reading and writing. Hence, we call the command fork() right after the system call accept(). As a result, every time it processes the loop, the fork() is going to duplicate the whole process by creating a child process that handles other connection requests to the listening socket.

This program makes several system calls such as 'bind', and 'listen.' What exactly is a system call?
Answer: A system call is requests made by the program to the operating system.