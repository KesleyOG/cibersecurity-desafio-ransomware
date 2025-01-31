decrypter.py

Modularização: A descriptografia foi encapsulada em uma função (decrypt_file). Isso melhora a organização do código e facilita a reutilização.

Tratamento de Erros: Adicionou verificações para garantir que o arquivo existe antes de tentar abrir. Também incluiu um bloco try-except para lidar com exceções.

Uso de Context Managers: Utilizou with open para garantir que os arquivos sejam fechados corretamente após serem lidos ou escritos.

Nomes mais Descritivos: Substituiu o nome do novo arquivo removendo a extensão ".ransomwaretroll" automaticamente.

encrypter.py

Verificação de Existência: Antes de abrir o arquivo, verifica se ele existe usando os.path.isfile.

Uso de Context Managers: Utilizou with open para leitura e escrita, assegurando o fechamento correto dos arquivos.

Nomes mais Descritivos: O nome do arquivo criptografado é criado adicionando ".ransomwaretroll" ao nome original.
