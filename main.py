import rsa
import generate_keys

main = 'Bienvenido.\n 1. Encriptar\n 2. Desencriptar\n 3. Salir\nOpcion: '
print('-'*len(main))
opcion = input(main)

while True:
    if opcion == '1':
        mensaje = input('Escriba el mensaje que desea encriptar: ')
        publicKeyFile = 'Llaves/publicKey.txt' 
        filename_encrypt = 'encrypt.txt'
        cyphertext = rsa.encrypt_file(mensaje, filename_encrypt, publicKeyFile)
        break

    if opcion == '2':
        privateKeyFile = 'Llaves/privateKey.txt'
        cypher = 'encrypt.txt'
        plaintext = rsa.decrypt_file(cypher, privateKeyFile)
        print(plaintext)
        break
    
    if opcion == '3':
        break