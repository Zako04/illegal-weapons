import os
os.system("clear")
print("""
\033[1;32m  / ____|              | |  | \ | |     | |   (_)   | |
 | |     _ __ __ _  ___| | _|  \| | __ _| |__  _  __| |
 | |    | '__/ _` |/ __| |/ / . ` |/ _` | '_ \| |/ _` |
 | |____| | | (_| | (__|   <| |\  | (_| | | | | | (_| |
  \_____|_|  \__,_|\___|_|\_\_| \_|\__,_|_| |_|_|\__,_|\033[1;37m
  --------------------------------------------------
[•] AUTHOR     : \033[1;32mCrackNahid\033[1;37m
[•] Whatapp    : \033[1;32m+8801909451729\033[1;37m
[•] STATUS     : \033[1;32mPaid\033[1;37m
[•] \033[1;37mVERSION    :\033[1;32m 0.0.1 \033[1;37m\033[1;37m
--------------------------------------------------
""")

import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')


try:
    key1=open("/storage/emulated/0/android8.txt",'r').read()
except IOError:
    kok=open("/storage/emulated/0/android8.txt",'w')
    myid=uuid.uuid4().hex[:12]
    f="Crack-Nahid"
    key=myid+f
    kok.write(key)
    kok.close()
    print(key)

a=requests.get(" https://github.com/srnboys/illegal-weapons/blob/main/approval.txt ").text
b=str(a)
key1=open("/storage/emulated/0/android8.txt",'r').read()
key2=str(key1)  
if key2 in b:
    pass
    
else:
    os.system("clear")
    print
    print("Your key  : "+key2)
    print("\n\t\tContact Admin ")
    os.system('xdg-open wa.me/+8801909451729')
    exit()
    
print("[1] Random Clone")
print("[2] File Clone")
print("[3] Dump Make")
print("[4] Join Whatsapp Group")
print("[5] install Update")
print("[6] exit")
nahid = input(' choice : ')
if nahid in ['1']:
   os.system("python Crack-random.py")
if nahid in ['2']:
   os.system("python Crack-File.py")
if nahid in ['3']:
   os.system("python2 Dump.py")
if nahid in ['4']:
   os.system("python Join.py")
if nahid in ['5']:
	   os.system("python Nahid.py")
if nahid in ['6']:
	   os.system("python exit.py")