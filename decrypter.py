import os
import pyaes

## Abre o arquivo criptografado

file_name= 'texto.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()


## Chave de descriptografia

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)


## Remove o arquivo criptografado

os.remove(file_name)


## Cria um novo arquivo descriptografado

new_file = 'texto.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()