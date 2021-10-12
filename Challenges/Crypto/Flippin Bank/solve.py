import socket
import re

ip = '167.71.128.208'
port = 30640
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send(b'admip')
s.recv(1024)
s.send(b'g0ld3n_b0y')
s.recv(1024).decode('utf-8')
data = s.recv(1024).decode('utf-8')

leaked_ciphertext = re.search('Leaked ciphertext: (.+?)\n', data).group(1)
leaked_ciphertext_byte_array = bytearray(bytes.fromhex(leaked_ciphertext))
leaked_ciphertext_byte_array[4] = leaked_ciphertext_byte_array[4] ^ ord('p') ^ ord('n')
payload_bytes = bytes(leaked_ciphertext_byte_array)
payload_ciphertext = payload_bytes.hex()

s.send(payload_ciphertext.encode())
data = s.recv(1024).decode('utf-8')
s.close()

print(data)

