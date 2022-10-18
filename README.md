## Project 3: BGP Router 
 
### Description 
In this project, we will develop a client for the File Transfer Protocol (FTP) protocol. A FTP server has been set up to use when developing and debugging your client. The server is available at ftp://ftp.3700.network. 
 
### Approach 

This project required quite a few more functions than the last one. The main ones are the different send and receive functions I created depending on whether it was a data transfer or just a message, the login function, and the different command functions. I will explain them briefly. 

I am going to explain the functions in the order in which they happen in the _main_ one. First, the server connects to the given host and port specified by the user in the URL, by parsing this URL using the rse_url_ function. Then the _login_ function, in which all the arguments are read by the _read_args_ function which simply returns them, and the received URL is parsed to get the different elements of it. After that, the FTP server gets sent by the client to the user, and the password so the login can be made. 

An if statement will take place to select the correct operation specified in the command line. For the ones that do not require data transfer, the command specified in the statement gets passed with the path specified in the URL. However, if data transfer is needed, another socket will be opened with the host and port provided by the _’Passive Mode’_. Before that, all required modes are set with the _set_modes_ function. The command is sent to the control socket and the data is received at the data channel socket. The _makeDirectory_ and _removeDirectory_ functions are simple they just create and delete a directory in the given path; same with the _delFile_ which simply removes the file. 

The most complex functions are _copyFileFromLocal_ and _copyFileFromServer_. The first one sends to the control channel the instruction to store the file in the specified path inside the server, gets the data channel opened and sends through it the local file – in case this operation was a move operation, it will simply remove the file from the local directory – and then it will close the data channel, so it knows the transfer is completed. The second one does the same, but it gets the data from the server and tells the control socket where llocally it wants to store it. In case I want to receive data from the server I read each byte to know when it has finished (when I receive an empty byte). 

Then the server is closed using _‘QUIT’_, and so is the control socket. 
 
### Challenges and difficulties 
After the first project the socket connection was not a big deal, however, working with bytes was. At first, I was confused with the way we had to use the data channel to send and receive data, also receiving the data in the form of bytes was a headache but after that everything worked out fine. 

### Testing and debugging 
I tested the code locally most of the time, when I thought I was done I went to Gradescope and checked the different error messages I was getting. After a few tries and a lot of debugging, I got all the answers correct. I did not try any FTP clients different than mine since I did not feel the need to, nonetheless, I feel like it would have been a particularly clever way to test it and see the functionality of an FTP server. 

 

