import hashlib

while True:
    texto = input('Digite uma string: ')
    hash_obj = hashlib.sha1(texto.encode())
    hash_str = hash_obj.hexdigest()
    print('Hash: ', hash_str)