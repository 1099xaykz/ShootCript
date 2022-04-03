import time
import os
import sys
import random as rd
import requests

BLACK = '\033[1;30m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
RESET = '\033[1;39m'

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)

def banner():
    print(RED + "           ▄▄▄▄▄▄▄▄▄▄██▄▄▄▄▄▄▄▄▄    ▄ ")
    print(MAGENTA + "▄███████████████████████▀▀▀▀▀▀▀██████▀")
    print(RED + "██████▀▀▀ ▄██▀  ███                   ")
    print(MAGENTA + "▀▀▀▀      ██     ▀██▄                 " + WHITE + "TikTok: @ds.8mqk")
    print(RED + "                   ▀██                " + WHITE + "Telegram: @ds8mqk")
    print(RED + "                     ▀                ")
    print(RED + "            # " + WHITE + "Type 'help' for a list of commands")

def help():
	print(WHITE + """
 Command                                 Function
---------                               ---------
help                                     - Help command
iptk [ip]                                - Ip tracker
genw [extension ex: com, org, gov]       - Generate web pages
genc                                     - Generate emails
genp                                     - Generate passwords
gent [bin]                               - Generate credits or debits cards through bins
binc                                     - Information of a bin
vrtg [bin]                               - View previously generated cards with a especific bin
vrcg                                     - See previously generated emails
vrpg                                     - View previously generated passwords
vrsw                                     - View previously generated websites
idso [ip]                                - Identify operating system
htph                                     - HTTP headers
sbnl                                     - Subnet lookup
""")

def main():
    banner()
    while True:
        console = input(RED + "# " + WHITE)
        v = console[0:4]
        v2 = console[5:10000]
        if console == "help":
            help()
        elif v == "iptk":
            os.system("curl -s http://ip-api.com/"+v2)
        elif v == "ejec":
            os.system(v2)
        elif v == "binc":
            os.system("cd tools && bash bin.sh")
        elif v == "gent":
            os.system("touch bin-"+v2+".txt")
            while True:
                # tarjeta
                n1 = rd.choice("123456789")
                n2 = rd.choice("123456789")
                n3 = rd.choice("123456789")
                n4 = rd.choice("123456789")
                n5 = rd.choice("123456789")
                n6 = rd.choice("123456789")
                n7 = rd.choice("123456789")
                n8 = rd.choice("123456789")
                n9 = rd.choice("123456789")
                n10 = rd.choice("123456789")
                # cvv
                c1 = rd.choice("123456789")
                c2 = rd.choice("123456789")
                c3 = rd.choice("123456789")
                # mes
                m1 = rd.choice("123456789")
                # año
                year = ["2024", "2025", "2026"]
                y = rd.choice(year)
                tarjeta = str(v2 + n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + "|" + str(c1 + c2 + c3) + "|" + str(m1) + "/" + y + "\n")
                print(RED + "# " + v2 + WHITE + str(n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + "|" + str(c1 + c2 + c3) + "|" + str(m1) + "/" + y))
                ruta = "data/bin-" + v2 + ".txt"
                a = open(ruta, "a")
                a.write(tarjeta)
                a.close()
        elif v == "vrtg":
            o = "cd data && cat bin-" + v2 + ".txt"
            os.system(o)
        elif v == "genw":
            while True:
                l1 = rd.choice("abcdefghijklmnopqrstuvwxyz")
                l2 = rd.choice("abcdefghijklmnopqrstuvwxyz")
                l3 = rd.choice("abcdefghijklmnopqrstuvwxyz")
                l4 = rd.choice("abcdefghijklmnopqrstuvwxyz")
                l5 = rd.choice("abcdefghijklmnopqrstuvwxyz")
                web = "http://" + l1 + l2 + l3 + l4 + l5 + "." + v2
                try:
                    r = requests.get(web)
                    if r.status_code == 200:
                        print(GREEN + web)
                        a = open("data/paginas.txt", "a")
                        a.write(web+"\n")
                        a.close()
                except:
                    print(RED + web)
        elif v == "genc":
            while True:
                l1 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789")
                l2 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789")
                l3 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789")
                l4 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789")
                l5 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789")
                l6 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789")
                l7 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789")
                l8 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789")
                correo = str(l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + "@gmail.com")
                print(RED + "# " + WHITE + correo)
                a = open("data/correos.txt", "a")
                a.write(correo+"\n")
                a.close()
        elif v == "genp":
            while True:
                l1 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l2 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l3 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l4 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l5 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l6 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l7 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l8 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l9 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l10 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l11 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l12 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l13 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l14 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                l15 = rd.choice("abcdefghijklmnopqrstuvwxyz123456789!$=?")
                password = str(l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10 + l11 + l12 + l13 + l14 + l15)
                print(RED + "# " + WHITE + password)
                a = open("data/contraseñas.txt", "a")
                a.write(password+"\n")
                a.close()
        elif v == "vrcg":
            os.system("cat data/correos.txt")
        elif v == "vrpg":
            os.system("cat data/contraseñas.txt")
        elif v == "vrsw":
            os.system("cat data/paginas.txt")
        elif v == "idso":
            os.system("python3 tools/so.py " + v2)
        elif v == "htph":
            os.system("python2 tools/http_headers.py")
        wlif v == "sbnl":
            os.system("python2 tools/subnet_lookup.py")
        else:
            print(WHITE + "The command '" + v + "' does not exist")

if __name__ == '__main__':
    main()
