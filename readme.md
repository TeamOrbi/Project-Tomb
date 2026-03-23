# Project Tomb

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Not%20specified-lightgrey)
![Status](https://img.shields.io/badge/Status-CLI%20Prototype-orange)

Project Tomb is a command-line encryption utility built in Python.
It uses Fernet symmetric encryption to securely encrypt and decrypt text.


- [Features](#features)
- [Requirements](#requirements)
- [Usage Flow](#usage-flow)
- [Security Reminder](#security-reminder)
- [Important Notes](#important-notes)
- [Contributing](#contributing)
- [AI Usage] (#ai-usage)

## Features

- Encrypt text with a Fernet key.
- Decrypt Fernet-encrypted text with the matching key.
- Optional double encryption and double decryption using two keys.
- Automatic key generation if you do not provide one.
- Optional update-check prompt on startup.

## Requirements

- Python 3.10+
- `cryptography`
- `orbiLib`

## Usage Flow

1. Launch the script.
2. Choose whether to check TeamOrbi servers for updates.
3. Enter a key, or type `n` to generate a new key.
4. Select mode:
	- `1` for Encrypt
	- `2` for Decrypt
5. Choose whether to use double encryption/decryption (`y` for yes).
6. Enter your plaintext or encrypted token when prompted.


## Security Reminder

- Never share encryption keys in chats, screenshots, or logs.
- Keep keys safe. Anyone with the key can decrypt your data.
- If a key is exposed, consider any encrypted data with that key compromised.

## Important Notes

- This tool currently encrypts/decrypts text entered in the terminal.
- Save generated keys immediately. Lost keys mean lost data.
- Double encryption requires both keys in the correct order for successful decryption.

## Contributing

Feel free to make a pull request!

## AI Useage

Around 10% of this project was AI generated, including this README.
At Team Orbi we try to keep AI usage to a minimum, as writing the code is more fun for us!

