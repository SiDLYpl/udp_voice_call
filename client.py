import socket
import threading
import pyaudio

SERVER_IP = '0.0.0.0'  # adres twojego serwera
PORT = 50007

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

# Stream do nagrywania
input_stream = p.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      input=True,
                      frames_per_buffer=CHUNK)

# Stream do odtwarzania
output_stream = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       output=True,
                       frames_per_buffer=CHUNK)

def send_audio(sock):
    while True:
        data = input_stream.read(CHUNK, exception_on_overflow=False)
        sock.sendall(data)

def receive_audio(sock):
    while True:
        data = sock.recv(CHUNK)
        if data:
            output_stream.write(data)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        print("Połączono z serwerem")

        threading.Thread(target=send_audio, args=(s,), daemon=True).start()
        receive_audio(s)

if __name__ == '__main__':
    main()