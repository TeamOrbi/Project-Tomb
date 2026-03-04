from cryptography.fernet import Fernet
from orbiLib import type_message, updateCheck, libUpdate, greetingMessage
import time

TombVersion = '0.1.0'
OrbiProject = 'Tomb'


type_message('Orb Encrypt\n\n')
greetingMessage(OrbiProject)
connectToTeamOrbi = input('\nWould you like to connect to the TeamOrbi servers to check for updates? \nYour IP may be logged by Cloudflare. Type "n" to cancel connection... ')
if connectToTeamOrbi == ('n'):
    print('Skipping update check.')
else:
    updateCheck(TombVersion, OrbiProject)
    libUpdate()

print('Do you have a key? Type "n" or enter key.')
haveKey = input('>> ')
if haveKey == ('n'):
    key = Fernet.generate_key()
    print("It's your lucky day! I have a spare one!")
    print(key.decode('utf-8'))
else:
    cleanedKey = haveKey.strip()
    if (cleanedKey.startswith("b'") and cleanedKey.endswith("'")) or (cleanedKey.startswith('b"') and cleanedKey.endswith('"')):
        cleanedKey = cleanedKey[2:-1]
    key = cleanedKey.encode('utf-8')

f = Fernet(key)

print('\nAre we encrypting or decrypting today? (1) Encrypt (2) Decrypt')
programMode = input('>> ')
if programMode == ('1'):
    print("Phrase here.")
    encryptionInput = input('>> ').encode('utf-8')
    encryptionOutput = f.encrypt(encryptionInput)
    print(encryptionOutput.decode('utf-8'))
    time.sleep(1)
    input('Press enter to continue... ')
    type_message('Clearing up...')
    print("\033[H\033[J", end="")
    type_message('See ya later!')

elif programMode == ('2'):
    print('Whats the string?')
    decryptionInput = input('>> ').encode('utf-8')
    decryptionOutput = f.decrypt(decryptionInput)
    print(decryptionOutput.decode('utf-8'))
    time.sleep(1)
    type_message('Clearing up...')
    print("\033[H\033[J", end="")
    type_message('See ya later!')

else:
    print('ByeByes!')
