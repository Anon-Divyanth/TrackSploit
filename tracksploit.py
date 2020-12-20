import os, sys
from time import sleep
from os import system
from core.banners import *
from core.trackers.trackers import *
try:
  import requests
except ImportError:
  print("\033[1;31m [!] Import Error., type'\033[1;32m pip install -r requirements.txt \033[1;31m' for installing requirements\033[0m")
  exit()

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
P = "\033[1;35m"
C = "\033[1;36m"
W = "\033[1;37m"
O = "\033[0m"

def checknet():
  try:
    requests.get("https://github.com")
  except Exception:
    print("\033[1;31m [!] Check your internet\033[0m")
    exit()
checknet()

def restart():
     x = input("\n \033[1;31m[🌟]\033[1;37m Return to menu [y/n] = ")
     if x == "y" or x == "Y":
       sleep(0.5)
       system("clear")
       print(banner)
       sleep(0.5)
       menu()
     else:
       exit()


banner = ("""\n{}

█████████████████████████████████████████████████████████████████████
██{}█████████████████████████████████████████████████████████████████{}██
██{}█─▄─▄─█▄─▄▄▀██▀▄─██─▄▄▄─█▄─█─▄█─▄▄▄▄█▄─▄▄─█▄─▄████─▄▄─█▄─▄█─▄─▄─█{}██
██{}███─████─▄─▄██─▀─██─███▀██─▄▀██▄▄▄▄─██─▄▄▄██─██▀██─██─██─████─███{}██
██{}▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▄▀▄▄▄▀▀▄▄▄▀▀{}██
██{}█████████████████████████████████████████████████████████████████{}██
█████████████████████████████████████████████████████████████████████\033[0m
""".format(R,G,R,G,R,G,R,G,R,G,R))
system("clear")
sleep(0.5)
print(banner)
sleep(0.3)

def menu():
  print("""{}
  [ {}1{} ] {}Track Phonenumber{}
  [ {}2{} ] {}Track Ip Address{}
  [ {}3{} ] {}Track Mac Address{}
  [ {}4{} ] {}Whois Lookup{}
  [ {}5{} ] {}Dns Lookup{}
  [ {}6{} ] {}Nmap Port Scanner{}
  [ {}7{} ] {}Subdomain Scanner{}
  [ {}8{} ] {}Traceroute{}
  [ {}9{} ] {}Hash Generator{}
  [ {}10{} ] {}Download YouTube Videos{}
  [ {}00{} ] {}Exit{}
 """.format(R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,W))
  sleep(0.5)
  choice = input(" {}[🌟]{} Select Option = {}".format(R,Y,W))
  sleep(1)
  if choice == "1" or choice == "01":
   sleep(0.2)
   system("clear")
   sleep(0.4)
   phonebanner()
   sleep(0.3)
   phonetrack()
   restart()
  elif choice == "2" or choice == "02":
   sleep(0.2)
   system("clear")
   sleep(0.4)
   ipbanner()
   sleep(0.3)
   ipaddress()
   restart()
  elif choice == "3" or choice == "03":
   sleep(0.2)
   system("clear")
   sleep(0.4)
   macbanner()
   sleep(0.3)
   macaddress()
   restart()
  elif choice == "4" or choice == "04":
   sleep(0.2)
   system("clear")
   sleep(0.4)
   whoisbanner()
   sleep(0.3)
   whois()
   restart()
  elif choice == "5" or choice == "05":
   sleep(0.2)
   system("clear")
   sleep(0.4)
   dnsbanner()
   sleep(0.3)
   dns()
   restart()
  elif choice == "6" or choice == "06":
   sleep(0.2)
   system("clear")
   sleep(0.4)
   portbanner()
   sleep(0.3)
   port()
   restart()
  elif choice == "7" or choice == "07":
   sleep(0.2)
   system("clear")
   sleep(0.4)
   subbanner()
   sleep(0.3)
   subdomain()
   restart()
  elif choice == "8" or choice == "08":
   sleep(0.2)
   system("clear")
   sleep(0.4)
   tracebanner()
   sleep(0.3)
   traceroute()
   restart()
  elif choice == "9" or choice == "09":
   sleep(0.2)
   system("clear")
   sleep(0.4)
   hashbanner()
   sleep(0.3)
   hash()
   restart()
  elif choice == "10":
   sleep(0.2)
   system("clear")
   sleep(0.4)
   youtubebanner()
   sleep(0.3)
   youtube()
   restart()
  else:
   exit()
menu()

