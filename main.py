message = "Test message"
A_public = 130
A_private = 197
B_public = 141
B_private = 201

class hellman():
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.partkey = None
        self.fullkey = None

    def generate_partkey(self):
        self.partkey = self.public_key1 ** self.private_key
        self.partkey = self.partkey % self.public_key2

    def generate_fullkey(self, partkey):
        self.fullkey = partkey ** self.private_key
        self.fullkey = self.fullkey % self.public_key2

    def encrypt_message(self, message):
        encrypted = ''
        for i in message:
            encrypted += chr(ord(i) + self.fullkey)
        return encrypted

    def decrypt_message(self, message):
        decrypted = ''
        for i in message:
            decrypted += chr(ord(i) - self.fullkey)
        return decrypted

Alice = hellman(A_public, B_public, A_private)
Bob = hellman(A_public, B_public, B_private)

Alice.generate_partkey()
Bob.generate_partkey()

Alice.generate_fullkey(Bob.partkey)
Bob.generate_fullkey(Alice.partkey)

print (f'''Alice   Bob
Публичные ключи
{Alice.public_key1}     {Bob.public_key1}
{Alice.public_key2}     {Bob.public_key2}
Части ключей
{Alice.partkey}     {Bob.partkey}
Полные ключи
{Alice.fullkey}     {Bob.fullkey}''')

encrypted = Alice.encrypt_message(message)
print('Зашифрованное сообщение:', encrypted)

decrypted = Bob.decrypt_message(encrypted)
print('Расшифрованное сообщение:',decrypted)