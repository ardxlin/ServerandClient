import socket

#server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
server.listen(1)

print("Menunggu pesan dari client....")
client_socket, addr = server.accept()
print(f"Terhubung dari: {addr}")

#pesan dari client
data = client_socket.recv(1024).decode()
print(f"Pesan dari client: {data}")

# Mengirim balasan ke client
client_socket.send("Hallo ini server, selamat datang hiii..".encode())

# Menutup koneksi
client_socket.close()
server.close()
