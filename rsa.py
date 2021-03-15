import generate_keys
import sys

# print(sys.maxsize)

def text_int(message, size=128):
    msg_ascii = message.encode('ascii')
    # print(len(msg_ascii))
    msg_convert_int = []
    for msg_int in range(0, len(msg_ascii), size):
        interger = 0
        for i in range(msg_int, min(msg_int + size, len(msg_ascii))):
            interger += msg_ascii[i] * (256 ** (i % size))
        msg_convert_int.append(interger)
    return msg_convert_int
    
def int_text(msg_convert_int, len_msg, size=128):
    msg = []
    for msg_int in msg_convert_int:
        text = []
        for i in range(size-1, -1, -1):
            if (len(msg) + i) < len_msg:
                msg_ascii = msg_int // (256**i)
                msg_int = msg_int % (256**i)
                text.insert(0, chr(msg_ascii))
        msg.extend(text)
    return ''.join(msg)

def encrypt(message, key, size=128):
    msg_encrypt = []
    # llave para la encriptación
    n, e = key
    # ciclo para encryptar con base a la conversión
    for i in text_int(message, size):
        # calculo exponencial cyphertext = plaintext ^ e mod n
        msg_encrypt.append(pow(i, e, n))
    return msg_encrypt


def decrypt(msg_encrypt, msg_len, key, size=128):
    msg_decrypt = []
    # llave para la encriptación
    n, d = key
    # ciclo para desencriptar 
    for i in msg_encrypt:
        # plaintext = cyphertext ^ d mod n 
        msg_decrypt.append(pow(i, d, n))

    return int_text(msg_decrypt, msg_len, size)

def encrypt_file(message, filename_encrypt, keyFile, size=128):
    # leemos el archivo de las llaves
    with open(keyFile, 'r+') as file:
        content = file.read()
    file.close()

    n, e = content.split(',')
    #print(e)

    n = int(n)
    e = int(e)
    key = n, e 
    # print(key)
    # Encrypt the message
    encrypted = encrypt(message,  key, size)

    for i in range(len(encrypted)):
        encrypted[i] = str(encrypted[i])
    content = ','.join(encrypted)

    content = '%s_%s' % (len(message), content)
    with open(filename_encrypt, 'w+') as file:
        file.write(content)
    file.close()

def decrypt_file(filename_encrypt, keyFilename, size=100):
    # leemos el archivo de las llaves
    with open(keyFilename, 'r+') as file:
        content = file.read()
    file.close()

    n, d = content.split(',')
    n = int(n)
    d = int(d)
    key = n, d 
    # print(d)

    with open(filename_encrypt, 'r+') as file:
        content = file.read()
    file.close()
        
    # print(content)
    # obtenemos los datos del archivo encriptado
    msg_len, msg_encrypt = content.split('_')
    msg_len = int(msg_len)

    desencrypted = []
    for i in msg_encrypt.split(','):
        desencrypted.append(int(i))

    msg = decrypt(desencrypted, msg_len, key, size)

    with open('decrypt.txt', 'w+') as file:
        file.write(msg)
    file.close()

    return msg