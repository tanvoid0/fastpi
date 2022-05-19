from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import rsa

_keyPair = RSA.generate(3072)

_pubKey = _keyPair.publickey()
_pubKeyPEM = _pubKey.exportKey()

_privateKeyPEM = _keyPair.exportKey()
encryptor = PKCS1_OAEP.new(_pubKey)


class EnigmaRSA:
    @staticmethod
    def encrypt(message, key):
        return rsa.encrypt(message.encode('ascii'), key)

    @staticmethod
    def decrypt(ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except:
            return False

    @staticmethod
    def generate_keys():
        (publicKey, privateKey) = rsa.newkeys(1024)
        with open('keys/publicKey.pem', 'wb') as p:
            p.write(publicKey.save_pkcs1('PEM'))
        with open('keys/privateKey.pem', 'wb') as p:
            p.write(privateKey.save_pkcs1('PEM'))

    @staticmethod
    def load_keys():
        with open('keys/publicKey.pem', 'rb') as p:
            publicKey = rsa.PublicKey.load_pkcs1(p.read())
        with open('keys/privateKey.pem', 'rb') as p:
            privateKey = rsa.PrivateKey.load_pkcs1(p.read())
        return privateKey, publicKey

    @staticmethod
    def sign(message, key):
        return rsa.sign(message.encode('ascii'), key, 'SHA-1')

    @staticmethod
    def verify(message, signature, key):
        try:
            return rsa.verify(message.encode('ascii'), signature, key, ) == 'SHA-1'
        except:
            return False


'''
    Demo
    message = "Hello FAST API"
    Enigma.generate_keys()
    publicKey, privateKey = Enigma.load_keys()
    ciphertext = Enigma.encrypt(message, publicKey)
    signature = Enigma.sign(message, privateKey)

    text = Enigma.decrypt(ciphertext, privateKey)

    if text:
        print(f'Message text: {text}')
    else:
        print("Unable to decrypt message")

    if Enigma.verify(text, signature, publicKey):
        print("Successfully verified signature")
    else:
        print("The message signature could not be verified")

    return {
        "message": message,
        "publicKey": publicKey,
        "privateKey": privateKey,
        "ciphertext": ciphertext,
        "signature": signature,
        "text": text
    }
'''