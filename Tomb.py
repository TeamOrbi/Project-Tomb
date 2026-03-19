from cryptography.fernet import Fernet
from orbiLib import *
import time
import fernetManagment as fm

TombVersion = '0.2.2'
OrbiProject = 'Tomb'


type_message('Project Tomb\n\n')
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
    print('\nWould you like to double the encryption? (Press "y" to double.)')
    doubleEncrypt = input('>> ')
    if doubleEncrypt == "y":
        print('Do you have a second key? Type "n" or enter key.')
        haveSecondKey = input('>> ')
        if haveSecondKey == "n":
            key2 = Fernet.generate_key()
            print("It's your lucky day! I have a spare one!")
            print(key2.decode('utf-8'))
        else:
            cleanedKey = haveSecondKey.strip()
            if (cleanedKey.startswith("b'") and cleanedKey.endswith("'")) or (cleanedKey.startswith('b"') and cleanedKey.endswith('"')):
                cleanedKey = cleanedKey[2:-1]
            key2 = cleanedKey.encode('utf-8')

        f2 = Fernet(key2)
        print("Phrase here")
        fm.encrypt(f,f2)
        time.sleep(1)
        input('Press enter to continue... ')
        type_message('Clearing up...')
        print("\033[H\033[J", end="")
        type_message('See ya later!')

    else:
        print("Phrase here.")
        fm.encrypt(f)
        time.sleep(1)
        input('Press enter to continue... ')
        type_message('Clearing up...')
        print("\033[H\033[J", end="")
        type_message('See ya later!')

elif programMode == ('2'):
    print('\nWas this double Encrypted? (Press "y" to double.)')
    doubleDecrypt = input('>> ')
    if doubleDecrypt == "y":
        print('Second key?')
        haveSecondKey = input('>> ')
        cleanedKey = haveSecondKey.strip()
        if (cleanedKey.startswith("b'") and cleanedKey.endswith("'")) or (cleanedKey.startswith('b"') and cleanedKey.endswith('"')):
            cleanedKey = cleanedKey[2:-1]
        key2 = cleanedKey.encode('utf-8')

        f2 = Fernet(key2)
        print('Phrase here')
        fm.decrypt(f,f2)
        time.sleep(1)
        input('Press enter to continue...')
        type_message('Clearing up...')
        print("\033[H\033[J", end="")
        type_message('See ya later!')
    else:
        print('Whats the string?')
        fm.decrypt(f)
        time.sleep(1)
        input('Press enter to continue...')
        type_message('Clearing up...')
        print("\033[H\033[J", end="")
        type_message('See ya later!')

else:
    print('ByeByes!')
