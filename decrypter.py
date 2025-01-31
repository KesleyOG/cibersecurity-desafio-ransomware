import os
import pyaes

# Função para descriptografar
def decrypt_file(file_name, key):
    try:
        # Verificar se o arquivo existe
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"O arquivo {file_name} não foi encontrado.")
        
        # Abrir o arquivo criptografado de forma segura
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Iniciar a descriptografia com a chave fornecida
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado após a descriptografia
        os.remove(file_name)

        # Criar e escrever no novo arquivo descriptografado
        new_file_name = file_name.replace(".ransomwaretroll", "")  # Remove a extensão ".ransomwaretroll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo descriptografado com sucesso e salvo como {new_file_name}.")
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro durante a descriptografia: {e}")

# Chave para a descriptografia
key = b"testeransomwares"

# Nome do arquivo criptografado
file_name = "teste.txt.ransomwaretroll"

# Chamar a função para descriptografar o arquivo
decrypt_file(file_name, key)
