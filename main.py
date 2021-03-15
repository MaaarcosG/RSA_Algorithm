import rsa

main = 'Bienvenido.\n 1. Encriptar\n 2. Desencriptar\n 3. Salir\nOpcion: '
print('-'*len(main))
opcion = input(main)

while True:
    if opcion == '1':
        mensaje = input('Escriba el mensaje que desea encriptar: ')
        plain_text = rsa.encrypt_file('encrypt.txt', mensaje)
        break

    if opcion == '2':
        # filename = input('Ingrese el nombre del archivo encriptado (encrypt.txt): ')
        filename = 'encrypt.txt'
        text = rsa.decrypt_file(filename)
        print(text)
        break
    
    if opcion == '3':
        break