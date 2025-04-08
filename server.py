import socket
import threading

HOST = '0.0.0.0'
PORT = 50007

def handle_client(source, destination):
    try:
        while True:
            data = source.recv(1024)
            if not data:
                break
            destination.sendall(data)
    except:
        pass
    finally:
        source.close()
        destination.close()
        print("Rozłączono klientów")

def client_pairing(conn1, conn2):
    t1 = threading.Thread(target=handle_client, args=(conn1, conn2))
    t2 = threading.Thread(target=handle_client, args=(conn2, conn1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print("Serwer działa i czeka na klientów...")

        while True:
            clients = []

            while len(clients) < 2:
                conn, addr = s.accept()
                print(f"Połączono z {addr}")
                clients.append(conn)

            print("Dwóch klientów połączonych. Rozpoczynanie sesji głosowej...")
            threading.Thread(target=client_pairing, args=(clients[0], clients[1]), daemon=True).start()

if __name__ == '__main__':
    main()