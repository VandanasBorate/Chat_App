import socket
import threading

clients = []

def handle_client(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received message: {message}")
                broadcast(message, client_socket)
            else:
                break
    except ConnectionResetError:
        print("Connection reset by peer.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the client socket is closed and removed from the list
        client_socket.close()
        if client_socket in clients:
            clients.remove(client_socket)
        print("Client disconnected.")

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message to client: {e}")
                client.close()
                if client in clients:
                    clients.remove(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)
    print("Server listening......")

    try:
        while True:
            client_socket, addr = server.accept()
            clients.append(client_socket)
            print(f"New connection from {addr}")
            threading.Thread(target=handle_client, args=(client_socket,)).start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the server socket and all client connections
        server.close()
        for client in clients:
            client.close()
        print("Server closed.")

if __name__ == "__main__":
    start_server()





# import socket
# import threading

# clients = []

# def handle_client(client_socket):
#     while True:
#         try:
#             message = client_socket.recv(1024).decode('utf-8')
#             if message:
#                 print(f"Received message: {message}")
#                 broadcast(message, client_socket)
#             else:
#                 break
#         except:
#             break
    
#     client_socket.close()
#     clients.remove(client_socket)

# def broadcast(message, sender_socket):
#     for client in clients:
#         if client != sender_socket:
#             try:
#                 client.send(message.encode('utf-8'))
#             except:
#                 client.close()
#                 clients.remove(client)

# def start_server():
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind(('0.0.0.0', 12345))
#     server.listen(5)
#     print("Server listening on port 12345")

#     while True:
#         client_socket, addr = server.accept()
#         clients.append(client_socket)
#         print(f"New connection from {addr}")
#         threading.Thread(target=handle_client, args=(client_socket,)).start()

# if __name__ == "__main__":
#     start_server()