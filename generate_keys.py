from random import randrange
from sympy import isprime

'''
    SIZE = indica el tamano para la oracion
'''

def random_prime(size=100):
    while True:
        # genera numeros primos a la azar, similares en magnitud, pero diferentes en longitud
        prime = randrange(2**(size-1), 2**(size))
        # isprime prueba de primalidad
        if isprime(prime):
            return prime

# algoritmo euclidiano
def euclidiano(a, b):
    while a != 0:
        a, b = b % a, a
    return b

# calcular d inverso modular
def inverse(e, lambda_n):
    if euclidiano(e, lambda_n) != 1:
        return None

    '''
       Algoritmo extenso de euclidiano
       http://gordosfrikis.blogspot.com/2012/12/algoritmo-de-euclides-extendidopython.html

    '''
    u1, u2, r0 = 1, 0, e
    v1, v2, r1 = 0, 1, lambda_n

    while r1 != 0:
        q = r0 // r1 
        v1, v2, r1, u1, u2, r0 = (u1 - q * v1), (u2 - q * v2), (r0 - q * r1), v1, v2, r1
    
    # print(u1)
    return u1 % lambda_n

def generate_e(lambda_n, size=100):
    while True:
        e = randrange(2**(size-1), 2**(size))
        # revisamos si cumple con el algoritmo
        if euclidiano(e, lambda_n) == 1:
            break
    return e

def generate_keys(size):
    # tomamos los numeros randoms
    p = random_prime(size)
    q = random_prime(size)

    n = p * q
    lambda_n = (p - 1) * (q - 1)

    e = generate_e(lambda_n)
    d = inverse(e, lambda_n)

    public_key = (n, e)
    private_key = (n, d)

    with open('Llaves/publicKey.txt', 'w') as file:
        file.write('%s,%s' % (public_key[0], public_key[1]))
    file.close()

    with open('Llaves/privateKey.txt', 'w') as file:
        file.write('%s,%s' % (private_key[0], private_key[1]))
    file.close()

    return (public_key, private_key)
    
def main_keys():
    public, private = generate_keys(100)
    n, e = public
    n, d = private
    print('Llaves generadas....')

if __name__=='__main__':
    main_keys()