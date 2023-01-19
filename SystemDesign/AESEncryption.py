'''
PyCryptodome
a self-contained python package of low-level cryptographic primitives.
It supports python 2.7, >=3.5, and PyPy
Features
 - Symmetric ciphers - AES, single and triple DES
 - Traditional modes of operations for symmetric ciphers: ECB, CBC
 - Authenticated Encryption: EAX (provides both authentication and privacy
 of a message in symmetric-key algorithms), CCM
 - Strem ciphers: Salsa20,
 - Cryptogtaphic hashes: SHA-1, SHA-2 hashes
 - Message Authentication Codes (MAC): HMAC, CMAC
 - Asymmetric key generation: RSA, DSA, ECC

'''

from Crypto.Cipher import AES   # import AES-128 module
from Crypto.Random import get_random_bytes # for genrating random string bytes

data = b'secret data'
key = get_random_bytes(16)  # generate a random string of bytes
 
cipher = AES.new(key, AES.MODE_EAX)  # create a new AES object with the random
# bytes and mode that allows reciever to detect any unauthorized modification
nonce = cipher.nonce


ciphertext, tag = cipher.encrypt_and_digest(data) # encrypt the data using the key generated
# from AES algorithm


cipher = AES.new(key, AES.MODE_EAX, nonce)  # generate the same key using AES algorithm to decrypt the
# encrypted message
decrypted_text = cipher.decrypt_and_verify(ciphertext, tag) # decrypt the encypted text using the key


print("Data:%s\n" %data)
print("Encrypted Data: %s\n" %ciphertext)
print("Decrypted Data: %s\n" %decrypted_text)
