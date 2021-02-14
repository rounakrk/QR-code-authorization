from cryptography.fernet import Fernet


def encrypt_pass(password_msg):
    # we will be encryting the below string. 
    message = password_msg

    # generate a key for encryptio and decryption 
    # You can use fernet to generate  
    # the key or use random key generator 
    # here I'm using fernet to generate key 

    key = Fernet.generate_key()

    # Instance the Fernet class with the key 

    fernet = Fernet(key)

    # then use the Fernet class instance  
    # to encrypt the string string must must  
    # be encoded to byte string before encryption 
    encMessage = fernet.encrypt(message.encode())

    # print("original string: ", message) 
    # print("encrypted string: ", encMessage) 

    return encMessage.decode('utf-8'), key.decode('utf-8')


def decrpyt_pass(key, password_msg):
    key = bytes(key, 'utf-8')
    fernet = Fernet(key)
    message = bytes(password_msg, 'utf-8')
    # decrypt the encrypted string with the  
    # Fernet instance of the key, 
    # that was used for encrypting the string 
    # encoded byte string is returned by decrypt method, 
    # so decode it to string with decode methos 
    decMessage = fernet.decrypt(message).decode()
    return decMessage

# print("Encrypted datatype: ", type(encMessage))
# print("Btye to string: ",encMessage.decode('utf-8'))
# rt = encMessage.decode('utf-8')
# print("String to byte", bytes(rt, 'utf-8'))


# print("decrypted string: ", decMessage)

# enc, key = encrypt_pass("Rounak Agarwal")
# print(enc)
# print(key)
# decrpyt_pass(key, enc)
