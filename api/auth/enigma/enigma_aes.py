# import base64
# from Crypto.Cipher import AES
# from Crypto import Random
# from Crypto.Protocol.KDF import PBKDF2
from decouple import config
from cryptography.fernet import Fernet

BLOCK_SIZE = 16
KEY = config("AES_KEY")
IV = config("AES_IV")
PASSWORD = config("AES_PASSWORD")
FERNET_KEY = config("FERNET_KEY")
#
# pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
# unpad = lambda s: s[:-ord(s[len(s) -1:])]
#


class AESCipher:
    def __init__(self):
        self.algo = Fernet(FERNET_KEY.encode())

    def encrypt(self, msg: str):
        return self.algo.encrypt(msg.encode())

    def decrypt(self, msg):
        return self.algo.decrypt(msg.encode())
#
if __name__ == '__main__':
    # print(Fernet.generate_key())
    msg = "Hello world"
    aes = AESCipher()
    enc = aes.encrypt(msg)
    print(enc)
    dec = aes.decrypt(enc)
    print(dec)
#
#     data = "study hard"
#     rData = aes.encrypt(data)
#     print("Ciphertext:", rData)
#     eData = aes.decrypt(rData)
#     print("Plaintext:", eData)


# from Crypto import Random
# from Crypto.Cipher import AES
# import base64
# import binascii
#
#
# # Data class
# from decouple import config
#
#
# class MData():
#     def __init__(self, data=b"", characterSet='utf-8'):
#         # data must be bytes
#         self.data = data
#         self.characterSet = characterSet
#
#     def saveData(self, FileName):
#         with open(FileName, 'wb') as f:
#             f.write(self.data)
#
#     def fromString(self, data):
#         self.data = data.encode(self.characterSet)
#         return self.data
#
#     def fromBase64(self, data):
#         self.data = base64.b64decode(data.encode(self.characterSet))
#         return self.data
#
#     def fromHexStr(self, data):
#         self.data = binascii.a2b_hex(data)
#         return self.data
#
#     def toString(self):
#         return self.data.decode(self.characterSet)
#
#     def toBase64(self):
#         return base64.b64encode(self.data).decode()
#
#     def toHexStr(self):
#         return binascii.b2a_hex(self.data).decode()
#
#     def toBytes(self):
#         return self.data
#
#     def __str__(self):
#         try:
#             return self.toString()
#         except Exception:
#             return self.toBase64()
#
#
# # key = str.encode(config("AES_KEY"))
# key = Random.get_random_bytes(32)
# iv = str.encode(config("AES_IV"))
#
# ### Encapsulation class
# class EnigmaAES():
#     def __init__(self,
#                  # key,
#                  mode,
#                  # iv:bytes='',
#                  paddingMode="NoPadding", characterSet="utf-8"):
#         '''
#         Build a AES object
#         key: Secret key, byte data
#         mode: There are only two usage modes, AES.MODE_CBC, AES.MODE_ECB
#         iv:  iv Offset, byte data
#         paddingMode: Fill mode, default to NoPadding, Optional NoPadding，ZeroPadding，PKCS5Padding，PKCS7Padding
#         characterSet: Character set encoding
#         '''
#         self.key = key
#         self.mode = mode
#         self.iv = iv
#         self.characterSet = characterSet
#         self.paddingMode = paddingMode
#         self.data = ""
#
#     def __ZeroPadding(self, data):
#         data += b'\x00'
#         while len(data) % 16 != 0:
#             data += b'\x00'
#         return data
#
#     def __StripZeroPadding(self, data):
#         data = data[:-1]
#         while len(data) % 16 != 0:
#             data = data.rstrip(b'\x00')
#             if data[-1] != b"\x00":
#                 break
#         return data
#
#     def __PKCS5_7Padding(self, data):
#         needSize = 16 - len(data) % 16
#         if needSize == 0:
#             needSize = 16
#         return data + needSize.to_bytes(1, 'little') * needSize
#
#     def __StripPKCS5_7Padding(self, data):
#         paddingSize = data[-1]
#         return data.rstrip(paddingSize.to_bytes(1, 'little'))
#
#     def __paddingData(self, data):
#         if self.paddingMode == "NoPadding":
#             if len(data) % 16 == 0:
#                 return data
#             else:
#                 return self.__ZeroPadding(data)
#         elif self.paddingMode == "ZeroPadding":
#             return self.__ZeroPadding(data)
#         elif self.paddingMode == "PKCS5Padding" or self.paddingMode == "PKCS7Padding":
#             return self.__PKCS5_7Padding(data)
#         else:
#             print("I won't support it Padding")
#
#     def __stripPaddingData(self, data):
#         if self.paddingMode == "NoPadding":
#             return self.__StripZeroPadding(data)
#         elif self.paddingMode == "ZeroPadding":
#             return self.__StripZeroPadding(data)
#
#         elif self.paddingMode == "PKCS5Padding" or self.paddingMode == "PKCS7Padding":
#             return self.__StripPKCS5_7Padding(data)
#         else:
#             print("I won't support it Padding")
#
#     def setCharacterSet(self, characterSet):
#         '''
#         Set character set encoding
#         characterSet: Character set encoding
#         '''
#         self.characterSet = characterSet
#
#     def setPaddingMode(self, mode):
#         '''
#         Set fill mode
#         mode: Optional NoPadding，ZeroPadding，PKCS5Padding，PKCS7Padding
#         '''
#         self.paddingMode = mode
#
#     def decryptFromBase64(self, entext):
#         '''
#         from base64 Encoding string encoding AES decrypt
#         entext: data type str
#         '''
#         mData = MData(characterSet=self.characterSet)
#         self.data = mData.fromBase64(entext)
#         return self.__decrypt()
#
#     def decryptFromHexStr(self, entext):
#         '''
#         from hexstr Encoding string encoding AES decrypt
#         entext: data type str
#         '''
#         mData = MData(characterSet=self.characterSet)
#         self.data = mData.fromHexStr(entext)
#         return self.__decrypt()
#
#     def decryptFromString(self, entext):
#         '''
#         From string AES decrypt
#         entext: data type str
#         '''
#         mData = MData(characterSet=self.characterSet)
#         self.data = mData.fromString(entext)
#         return self.__decrypt()
#
#     def decryptFromBytes(self, entext):
#         '''
#         From binary AES decrypt
#         entext: data type bytes
#         '''
#         self.data = entext
#         return self.__decrypt()
#
#     def encryptFromString(self, data):
#         '''
#         String AES encryption
#         data: String to be encrypted, data type: str
#         '''
#         self.data = data.encode(self.characterSet)
#         return self.__encrypt()
#
#     def __encrypt(self):
#         if self.mode == AES.MODE_CBC:
#             aes = AES.new(self.key, self.mode, self.iv)
#         elif self.mode == AES.MODE_ECB:
#             aes = AES.new(self.key, self.mode)
#         else:
#             print("This mode is not supported")
#             return
#
#         data = self.__paddingData(self.data)
#         enData = aes.encrypt(data)
#         return MData(enData)
#
#     def __decrypt(self):
#         if self.mode == AES.MODE_CBC:
#             aes = AES.new(self.key, self.mode, self.iv)
#         elif self.mode == AES.MODE_ECB:
#             aes = AES.new(self.key, self.mode)
#         else:
#             print("This mode is not supported")
#             return
#         data = aes.decrypt(self.data)
#         mData = MData(self.__stripPaddingData(data), characterSet=self.characterSet)
#         return mData
#
#
# if __name__ == '__main__':
#     # key = b"1234567812345678"
#     # iv = b"0000000000000000"
#     aes = EnigmaAES(
#         # key,
#         AES.MODE_CBC,
#         # iv,
#         paddingMode="ZeroPadding", characterSet='utf-8')
#
#     data = "study hard"
#     rData = aes.encryptFromString(data)
#     print("Ciphertext:", rData.toBase64())
#     rData = aes.decryptFromBase64(rData.toBase64())
#     print("Plaintext:", rData)