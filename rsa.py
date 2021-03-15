import generate_keys

def text_int(message):
    msg_ascii = message.encode('ascii')
    msg_convert_int = []
    for msg_int in range(0, len(msg_ascii), 128):
        interger = 0
        for i in range(msg_int, min(msg_int + 128, len(msg_ascii))):
            interger += msg_ascii[i] * (256 ** (i % 128))
        msg_convert_int.append(interger)
    return msg_convert_int

def int_text(msg_convert_int, len_msg):
    msg = []
    for msg_int in msg_convert_int:
        text = []
        for i in range(128-1, -1, -1):
            if (len(msg) + i) < len_msg:
                msg_ascii = msg_int // (256**i)
                msg_int = msg_int % (256**i)
                text.insert(0, chr(msg_ascii))
        msg.extend(text)
    return ''.join(msg)

def encrypt(message):
    msg_encrypt = []
    
    public_key, private_key = generate_keys.generate_keys()
    n, e = public_key

    # ciclo para encryptar con base a la conversión
    for i in text_int(message):
        # calculo exponencial cyphertext = plaintext ^ e mod n
        msg_encrypt.append(pow(i, e, n))
    return msg_encrypt

def decrypt(msg_encrypt, msg_len):
    msg_decrypt = []

    public_key, private_key = generate_keys.generate_keys()
    n, d = private_key
    
    # ciclo para desencriptar 
    for i in msg_encrypt:
        # plaintext = cyphertext ^ d mod n 
        msg_decrypt.append(pow(i, d, n))
    
    msg = int_text(msg_decrypt, msg_len)

    return msg

def encrypt_file(filename, message):
    # mensaje encriptado
    encrypted = encrypt(message)

    for i in range(len(encrypted)):
        encrypted[i] = str(encrypted[i])
    msg_encrypt = ','.join(encrypted)

    with open(filename, 'w') as file:
        file.write('%s_%s' % (len(message), msg_encrypt))
    file.close

def decrypt_file(filename):
    # abrimos el archivo encriptado
    with open(filename, 'r') as file:
        content = file.read()
    
    msg_len, msg_encrypt = content.split('_')

    msg_len = int(msg_len)

    encrypted = []
    for i in msg_encrypt.split(','):
        encrypted.append(int(i))
    
    return decrypt(encrypted, msg_len)