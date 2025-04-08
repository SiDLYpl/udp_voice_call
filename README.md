# UDP Voice Calling

## Server Code Summary:
The server facilitates a voice call between two clients by forwarding audio data between them.

- It listens for incoming TCP connections on port 50007.
- Once two clients connect, it starts a pairing session between them.
- Each client has a dedicated thread that listens for incoming audio data and relays it to the other client, effectively creating a two-way audio communication channel.
- When either client disconnects, both sockets are closed, and the server waits for the next pair of clients.


## Client Code Summary:
The client captures audio from the microphone and sends it to the server, while also playing back audio received from the server.

- It connects to the server at a specified IP and port.
- Uses PyAudio to:
  - Record microphone input.
  - Play received audio through speakers or headphones.
- Two threads are used:
  - One to send audio data to the server.
  - One to receive and play audio coming from the server (i.e., from the other client).

