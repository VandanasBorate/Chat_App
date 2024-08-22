Project Overview:
This project involves creating a simple chat application using Python and WebSockets. The goal is to establish real-time communication between multiple clients connected to a server. The chat application will allow users to send and receive messages instantly, showcasing the use of WebSockets for maintaining a persistent connection between the server and the clients.

Technology Stack:
Programming Language:

Socket Library: Socket (Python library), websockets (Python library),

Concurrency: Threading (to handle multiple client connections simultaneously)

System Requirements
Python 3.x installed on your system.

Basic understanding of Socket protocol , websockets and Python programming.

Detailed Implementation:
1. Server-Side Implementation
Code File: server.py




Purpose: Manages WebSocket connections, handles incoming messages, and broadcasts them to all connected clients, handling clients disconnection.
Client-Side Implementation
File: client.py


Purpose: Connects to the Socket server, sends messages, and receives broadcasts from other clients.
Usage Instructions
Run the Server:
Start the Socket server by running the server.py script.

Ensure the server is running before any clients attempt to connect.

Run server.py:



Client connected to the server:



Message are received from client:



Run the Client(s):
Run the client.py script on multiple terminals to simulate multiple clients.

Each client will be able to send messages that will be broadcast to all other connected clients.

Run client.py



Client 2 :receives the broadcasted message:



Client 3:



Usage Instructions:
server.py




Index.html



Broadcast Message





