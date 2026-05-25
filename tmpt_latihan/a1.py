import socket
import sys
import os
os.system("cls")
#----
# penerima_nonstop.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))
server.listen(1)
print("Penerima: Siap menerima pesan terus-menerus...")

# Terima koneksi sekali di awal agar jalurnya tetap terbuka
koneksi, alamat = server.accept()
print(f"Penerima: Terhubung dengan {alamat}\n")

while True:
    try:
        # Menunggu kiriman data
        data = koneksi.recv(1024).decode()
        
        # Jika pengirim memutuskan koneksi atau mengirim pesan kosong 'exit'
        if not data or data.lower() == 'exit':
            print("Penerima: Pengirim keluar dari obrolan.")
            break
            
        print(f"Pesan Masuk: {data}")
        
    except Exception as e:
        print(f"Terjadi error: {e}")
        break

koneksi.close()
server.close()
print("Penerima: Program selesai.")