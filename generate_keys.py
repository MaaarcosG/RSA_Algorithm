from random import randrange
from sympy import isprime

size = 20

def random_prime():
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

def generate_e(lambda_n):
    while True:
        e = randrange(2**(size-1), 2**(size))
        # revisamos si cumple con el algoritmo
        if euclidiano(e, lambda_n) == 1:
            break
    return e

def generate_keys():
    # tomamos los numeros randoms
    p = random_prime()
    q = random_prime()

    n = p*q
    lambda_n = (p - 1) * (q - 1)
    
    # tamano para las llaves
    size = 20

    e = generate_e(lambda_n)
    d = inverse(e, lambda_n)

    public_key = (n, e)
    private_key = (n, d)

    return (public_key, private_key)
    
if __name__ == '__main__':
    public, private = generate_keys()
    generate_key_file()
    n, e = public
    print(n)