def encrypt(f, f2=0):
    if f2 != 0:
        encryptionInput = input('>> ').encode('utf-8')
        encryptionOutput = f.encrypt(encryptionInput)
        encryptionInput = encryptionOutput
        encryptionOutput = f2.encrypt(encryptionInput)
        print(encryptionOutput.decode('utf-8'))
    else:
        encryptionInput = input('>> ').encode('utf-8')
        encryptionOutput = f.encrypt(encryptionInput)
        print(encryptionOutput.decode('utf-8'))
    

def decrypt(f, f2=0):
    if f2 != 0:
        decryptionInput = input('>> ').encode('utf-8')
        decryptionOutput = f2.decrypt(decryptionInput)
        decryptionInput = decryptionOutput
        decryptionOutput = f.decrypt(decryptionInput)
        print(decryptionOutput.decode('utf-8'))
    else:
        decryptionInput = input('>> ').encode('utf-8')
        decryptionOutput = f.decrypt(decryptionInput)
        print(decryptionOutput.decode('utf-8'))
    