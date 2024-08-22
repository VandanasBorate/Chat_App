import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                # Move the cursor to the beginning of the line and clear it
                print(f"\r{' ' * 180}\r", end="")  # Clear the current line
                print(f"Boardcast message Received: {message}")
                print("Enter your message: ", end="", flush=True)
            else:
                break
        except:
            break

def send_messages(client_socket):
    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode('utf-8'))

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.daemon = True  # Ensure the thread exits when the main program exits
    receive_thread.start()

    send_messages(client)

if __name__ == "__main__":
    start_client()
