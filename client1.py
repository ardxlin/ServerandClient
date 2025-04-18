import socket

#client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))  # Connect ke server (localhost)

# Mengirim pesan ke server
client.send("Halo server, ini adalah client!".encode())

# Menerima balasan dari server
response = client.recv(1024).decode()
print(f"Balasan dari server: {response}")

# Menutup koneksi
client.close()
