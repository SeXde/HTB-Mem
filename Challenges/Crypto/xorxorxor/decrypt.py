#!/usr/bin/python3
encrypted_flag = bytes.fromhex(open('output.txt', 'r').read().strip().replace(" ", "").split(":")[1])
plain_string = "HTB{".encode()

key = b''

for i in range(len(plain_string)):
    key += bytes([encrypted_flag[i] ^ plain_string[i]])

flag = b''
for i in range(len(encrypted_flag)):
    flag += bytes([encrypted_flag[i] ^ key[i % len(key)]])

flag = flag.decode('UTF-8')
print("The flag is: ", flag)