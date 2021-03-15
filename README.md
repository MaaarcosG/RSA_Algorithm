# RSA_Algorithm
Codigo Fuente de la implementación: https://github.com/MaaarcosG/RSA_Algorithm.git

## Instalar Liberia Sympy
Esta libreria ayuda a ver si los numeros generados son primos
```bash
$ pip install sympy
```

## Uso Correcto

Primero generamos las llaves, con las condiciones necesarias para que el cifrado sea correcto.
```bash
$ python generate_keys.py 
```
Ya con las llaves generadas, podemos cifrar cualquier mensaje que deseamos, unicamente siguiente el menu interactivo.
- Encriptacion: Ingresar mensaje, y la llave publica generada anteriormente. (Esta llave se encuentra en el archivo de texto /Llaves/publicKey.txt)
- Desencriptacion: Lee el archivo encriptado, y con la llave privada hacer la desencriptación del mensaje. (Esta llave se encuentra en el archivo de texto /Llaves/privateKey.txt)

```bash
$ python main.py 
```