try:
  import requests
except ImportError:
  print("\033[1;31m [!] Import Error,Type'\033[1;32m pip install -r requirements.txt \033[1;31m' for installing requirements\033[0m")
  exit()

import mechanize, json
import phonenumbers,sys
import pytube
from phonenumbers import geocoder, timezone
from pytube import YouTube
from bs4 import BeautifulSoup
from os import system
from time import sleep


R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
P = "\033[1;35m"
C = "\033[1;36m"
W = "\033[1;37m"
O = "\033[0m"



def phonetrack():
  try:
    country = input("{} [🌟] {}country code = {}".format(R,B,W))
  except KeyboardInterrupt:
    exit()
  if country == "91":
    br = mechanize.Browser()
    number = input("{} [🌟] {}Phone number = {}".format(R,B,W))
    url = 'https://www.findandtrace.com/trace-mobile-number-location'
    phoneNumber = phonenumbers.parse("+"+country+number)
    Country = geocoder.country_name_for_number(phoneNumber, "en")
    state = geocoder.description_for_number(phoneNumber, 'en')
    validate = phonenumbers.is_valid_number(phoneNumber)
    time = timezone.time_zones_for_number(phoneNumber)
    br.open(url)
    br.select_form(name='trace')
    br['mobilenumber'] = number
    res = br.submit().read()
    soup = BeautifulSoup(res,'html.parser')
    tbl = soup.find_all('table',class_='shop_table')
    data = tbl[0].find('tfoot')
    print("{}\n [{}✴{}]{} country: ".format(R,G,R,G)+Country)
    c=0
    for i in data:
        c+=1
        if c in (1,4,6,8):
            continue
        th = i.find('th')
        td = i.find('td')
        print("{}\n [{}✴{}]{} ".format(R,G,R,G)+th.text,td.text)
    try:
      data = tbl[1].find('tfoot')
    except:
      print("{}\n [{}✴{}]{} state: ".format(R,G,R,G)+state)
      print("{}\n [{}✴{}]{} valid mobile number: ".format(R,G,R,G),validate)
      print("{}\n [{}✴{}]{} Timezone: ".format(R,G,R,G),time)
    c=0
    for i in data:
        c+=1
        if c in (2,20,22,26):
            th = i.find('th')
            td = i.find('td')
            print("{}\n [{}✴{}]{} ".format(R,G,R,G)+th.text,td.text+"\033[0m")
  else:
    number =  input("{} [🌟]{} Phone number = {}".format(R,B,W))
    phoneNumber = phonenumbers.parse("+"+country+number)
    Country = geocoder.country_name_for_number(phoneNumber, "en")
    state = geocoder.description_for_number(phoneNumber, 'en')
    validate = phonenumbers.is_valid_number(phoneNumber)
    time = timezone.time_zones_for_number(phoneNumber)
    res = requests.get("https://api.telnyx.com/anonymous/v2/number_lookup/"+country+number).content
    load = json.loads(res)
    data = load['data']
    carrier = data['carrier']
    print("\n{} [{}✴{}]{} Country prefix = {}+".format(R,G,R,G,W)+country)
    code = ("\n{} [{}✴{}]{} Country code = {}".format(R,G,R,G,W)+data['country_code'])
    national = ("\n{} [{}✴{}]{} National Format = {}".format(R,G,R,G,W)+data['national_format'])
    phone = ("\n{} [{}✴{}]{} International Format = {}".format(R,G,R,G,W)+data['phone_number'])
    name = ("\n{} [{}✴{}]{} Carrier = {}".format(R,G,R,G,W)+carrier['name'])
    type = ("\n{} [{}✴{}]{} Line type = {}".format(R,G,R,G,W)+carrier['type'])
    for i in  national, phone, type:
      print(i)
    print("\n{} [{}✴{}]{} Valid mobile number ={}".format(R,G,R,G,W),validate)
    for i in name, code:
      print(i)
    print("\n{} [{}✴{}]{} Country = {}".format(R,G,R,G,W)+Country)
    print("\n{} [{}✴{}]{} State = {}".format(R,G,R,G,W)+state)
    print("\n{} [{}✴{}]{} Timezone ={}".format(R,G,R,G,W),time)

def ipaddress():
  try:
    ip = input("{} [🌟]{} Ip Address = {}".format(R,B,W))
  except KeyboardInterrupt:
    exit()
  req = requests.get("https://whatismyipaddress.com/ip/{}".format(ip)).content
  soup = BeautifulSoup(req,"html.parser")
  td = soup.find_all("td")
  req2 = requests.get("https://ipapi.co/{}".format(ip)).content
  soup2 = BeautifulSoup(req2,"html.parser")
  table = soup2.find("table")
  td2 = table.find_all("td",class_="ipval")

  c=0
  for i in td:
   c+=1
   if c in (1,20):
     print("\n{} [{}*{}]{} Ip Address = {}".format(R,G,R,G,W)+i.text)
   if c in (2,20):
     print("{} [{}*{}]{} Decimal = {}".format(R,G,R,G,W)+i.text)
   if c in (3,20):
     print("{} [{}*{}]{} Hostname = {}".format(R,G,R,G,W)+i.text)
   if c in (4,20):
     print("{} [{}*{}]{} ASN = {}".format(R,G,R,G,W)+i.text)
   if c in (5,20):
     print("{} [{}*{}]{} ISN = {}".format(R,G,R,G,W)+i.text)
   if c in (6,20):
     print("{} [{}*{}]{} Orginzation= {}".format(R,G,R,G,W)+i.text)
   if c in (7,20):
     print("{} [{}*{}]{} Services= {}".format(R,G,R,G,W)+i.text)
   if c in (8,20):
     print("{} [{}*{}]{} Type = {}".format(R,G,R,G,W)+i.text)
   if c in (9,20):
     print("{} [{}*{}]{} Assignment = {}".format(R,G,R,G,W)+i.text)
   if c in (11,20):
     print("{} [{}*{}]{} Continent  = {}".format(R,G,R,G,W)+i.text)
   if c in (12,20):
     print("{} [{}*{}]{} Country = {}".format(R,G,R,G,W)+i.text)
   if c in (13,20):
     print("{} [{}*{}]{} State/Region = {}".format(R,G,R,G,W)+i.text)
   if c in (14,20):
     print("{} [{}*{}]{} Location = {}".format(R,G,R,G,W)+i.text)
     c=0
     for i in td2:
       c+=1
       if c in (5,20):
         print("{} [{}*{}]{} Postal Code = {}".format(R,G,R,G,W)+i.text)
       if c in (6,20):
         print("{} [{}*{}]{} Europen Union = {}".format(R,G,R,G,W)+i.text)
       if c in (7,20):
         print("{} [{}*{}]{} Latitude/Longitude = {}".format(R,G,R,G,W)+i.text)
       if c in (9,20):
         print("{} [{}*{}]{} Calling Code =  {}".format(R,G,R,G,W)+i.text)
       if c in (10,20):
         print("{} [{}*{}]{} Currency = {}".format(R,G,R,G,W)+i.text)
       if c in (11,20):

         print("{} [{}*{}]{} Languages = {}".format(R,G,R,G,W)+i.text)
         req = requests.get("https://ipapi.co/{}".format(ip)).content
         soup = BeautifulSoup(req,"html.parser")
         table = soup.find("table")
         td = table.find_all("td",class_="ipval")
         c=0
         for i in td:
           c+=1
           if c in (7,20):
            print("{} [{}*{}]{} Google Maps = {}http://www.google.com/maps/place/".format(R,G,R,G,W)+i.text)


def macaddress():
   try:
     mac = input(" {}[🌟]{} Mac Address = {}".format(R,B,W))
     req = requests.get("https://udger.com/resources/mac-address-vendor-lookup?macaddress="+mac).content
     soup = BeautifulSoup(req,"html.parser")
     table = soup.find("table")
     a = table.find_all("td")
   except KeyboardInterrupt:
    exit()
   except:
     print("{} Error., check your mac address{}".format(R,O))
     exit()
   c=0
   for i in a:
     c+=1
     if c in (2,15):
       print(" \n {}[{}*{}]{} vender = {}".format(R,G,R,G,W)+i.text)
     if c in (4,15):
       print(" {}[{}*{}]{} vender code = {}".format(R,G,R,G,W)+i.text)
     if c in (6,8,15):
       print(" {}[{}*{}]{} company address = {}".format(R,G,R,G,W)+i.text)
     if c in (10,15):
       print(" {}[{}*{}]{} country = {}".format(R,G,R,G,W)+i.text)
     if c in (12,15):
       print(" {}[{}*{}]{} code = {}".format(R,G,R,G,W)+i.text)


def whois():
  try:
    url = input("{} [🌟]{} Domain or ip Address = {}".format(R,B,W))
    req = requests.get("https://www.whois.com/whois/{}".format(url)).content
    soup = BeautifulSoup(req,'html.parser')
    anon = soup.find('pre',class_='df-raw')
    c=0
    for i in anon:
      c+=1
      if c in (1,2,3):
         print("\033[1;32m",i,"\033[0m")
  except KeyboardInterrupt:
    exit()
  except:
    print("\033[1;31m [!] Invalid URL. check your given url\033[0m")




def dns():
  try:
    site = input("\033[{} [🌟] {}Enter Website without({}http{}/{}https{}) ={} ".format(R,B,R,G,R,B,W))
  except KeyboardInterrupt:
    exit()
  print("\033[1;32m")
  system("curl https://api.hackertarget.com/dnslookup/?q="+site)
  print("\033[0m")


def port():
  try:
    site = input("{} [🌟] {}Website or IP Address = {}".format(R,B,W))
  except KeyboardInterrupt:
    exit()
  print("\033[1;32m")
  system("curl https://api.hackertarget.com/nmap/?q="+site)
  print("\033[0m")



def subdomain():
  try:
    site = input("\033[{} [🌟] {}Enter Website without({}http{}/{}https{}) ={} ".format(R,B,R,G,R,B,W))
  except KeyboardInterrupt:
    exit()
  print("\033[1;32m")
  system("curl https://api.hackertarget.com/hostsearch/?q="+site)
  more = ("\n\033[1;34m Please wait ✋ Getting more Links ░ ░ ░\033[0m \n\033[1;32m")
  for t in more:
    sys.stdout.write (t)
    sys.stdout.flush()
    sleep(0.1)
  system("curl https://api.hackertarget.com/pagelinks/?q="+site)
  print("\033[0m")


def traceroute():
  try:
    site = input("{} [🌟] {}Website or IP Address = {}".format(R,B,W))
  except KeyboardInterrupt:
    exit()
  sleep(1)
  print("\033[1;37m Please wait.,sending packets\033[1;32m")
  system("curl https://api.hackertarget.com/mtr/?q="+site)
  print("\033[0m")


def hash():

  user = input("{} [🌟] {}Enter your text = {}".format(R,B,W))
  req = requests.get("https://md5calc.com/hash/md5/"+user).content
  soup = BeautifulSoup(req,"html.parser")
  pre = soup.find("pre")
  table = soup.find("table",class_="table table-condensed table-striped")
  td = table.find_all("td")
  print("\n{} [{}✴{}]{} MD5 Hash for '\033[1;31m{}\033[32m' = {}".format(R,G,R,G,user,W)+pre.text+"\n")
  sleep(1)
  more = "\033[1;34m Please wait ✋ Getting more Hashes ░ ░ ░\033[0m \n\n"
  for t in more:
    sys.stdout.write (t)
    sys.stdout.flush()
    sleep(0.1)
  sleep(3)

  c=0
  for i in td:
    c+=1
    if c in (2,200):
      print("{}[{}✵{}]{} MD2 =".format(O,Y,O,Y)+i.text)
    if c in (4,200):
      print("{}[{}✵{}]{} MD4 =".format(O,P,O,P)+i.text)
    if c in (8,200):
      print("{}[{}✵{}]{} SHA1 =".format(O,C,O,C)+i.text)
    if c in (10,200):
      print("{}[{}✵{}]{} SHA224 =".format(O,B,O,B)+i.text)
    if c in (12,200):
      print("{}[{}✵{}]{} SHA256 =".format(O,G,O,G)+i.text)
    if c in (14,200):
      print("{}[{}✵{}]{} SHA348 =".format(O,Y,O,Y)+i.text)
    if c in (16,200):
      print("{}[{}✵{}]{} SHA512/224 =".format(O,P,O,P)+i.text)
    if c in (18,200):
      print("{}[{}✵{}]{} SHA512/256 =".format(O,C,O,C)+i.text)
    if c in (20,200):
      print("{}[{}✵{}]{} SHA512 =".format(O,B,O,B)+i.text)
    if c in (22,200):
      print("{}[{}✵{}]{} SHA3-224 =".format(O,G,O,G)+i.text)
    if c in (24,200):
      print("{}[{}✵{}]{} SHA3-256 =".format(O,Y,O,Y)+i.text)
    if c in (26,200):
      print("{}[{}✵{}]{} SHA3-384 =".format(O,P,O,P)+i.text)
    if c in (28,200):
      print("{}[{}✵{}]{} SHA3-512 =".format(O,C,O,C)+i.text)
    if c in (30,200):
      print("{}[{}✵{}]{} RIPEMD128 =".format(O,B,O,B)+i.text)
    if c in (32,200):
      print("{}[{}✵{}]{} RIPEMD160 =".format(O,G,O,G)+i.text)
    if c in (34,200):
      print("{}[{}✵{}]{} RIPEMD256 =".format(O,Y,O,Y)+i.text)
    if c in (36,200):
      print("{}[{}✵{}]{} RIPEMD320 =".format(O,P,O,P)+i.text)
    if c in (38,200):
      print("{}[{}✵{}]{} WHIRLPOOL =".format(O,C,O,C)+i.text)
    if c in (40,200):
      print("{}[{}✵{}]{} Tiger128,3 =".format(O,B,O,B)+i.text)
    if c in (42,200):
      print("{}[{}✵{}]{} Tiger160,3 =".format(O,G,O,G)+i.text)
    if c in (44,200):
      print("{}[{}✵{}]{} Tiger192,3 =".format(O,Y,O,Y)+i.text)
    if c in (46,200):
      print("{}[{}✵{}]{} Tiger128,4 =".format(O,P,O,P)+i.text)
    if c in (48,200):
      print("{}[{}✵{}]{} Tiger160,4 =".format(O,C,O,C)+i.text)
    if c in (50,200):
      print("{}[{}✵{}]{} Tiger192,4 =".format(O,B,O,B)+i.text)
    if c in (52,200):
      print("{}[{}✵{}]{} SNEFRU =".format(O,G,O,G)+i.text)
    if c in (54,200):
      print("{}[{}✵{}]{} SNEFRU256 =".format(O,Y,O,Y)+i.text)
    if c in (56,200):
      print("{}[{}✵{}]{} GOST =".format(O,P,O,P)+i.text)
    if c in (58,200):
      print("{}[{}✵{}]{} GOST-CRYPTO =".format(O,C,O,C)+i.text)
    if c in (60,200):
      print("{}[{}✵{}]{} ALDER32 =".format(O,B,O,B)+i.text)
    if c in (62,200):
      print("{}[{}✵{}]{} CRC32 =".format(O,G,O,G)+i.text)
    if c in (64,200):
      print("{}[{}✵{}]{} CRC32B =".format(O,Y,O,Y)+i.text)
    if c in (66,200):
      print("{}[{}✵{}]{} FNV132 =".format(O,P,O,P)+i.text)
    if c in (68,200):
      print("{}[{}✵{}]{} FNV1A32 =".format(O,C,O,C)+i.text)
    if c in (70,200):
      print("{}[{}✵{}]{} FNV164".format(O,B,O,B)+i.text)
    if c in (72,200):
      print("{}[{}✵{}]{} FNV1A64".format(O,G,O,G)+i.text)
    if c in (74,200):
      print("{}[{}✵{}]{} JOAAT =".format(O,Y,O,G)+i.text)
    if c in (76,200):
      print("{}[{}✵{}]{} HAVAL128,3 =".format(O,P,O,P)+i.text)
    if c in (78,200):
      print("{}[{}✵{}]{} HAVAL160,3 =".format(O,C,O,C)+i.text)
    if c in (80,200):
      print("{}[{}✵{}]{} HAVAL192,3 =".format(O,B,O,B)+i.text)
    if c in (82,200):
      print("{}[{}✵{}]{} HAVAL224,3 =".format(O,G,O,G)+i.text)
    if c in (84,200):
      print("{}[{}✵{}]{} HAVAL256,3 =".format(O,Y,O,Y)+i.text)
    if c in (86,200):
      print("{}[{}✵{}]{} HAVAL128,4 =".format(O,P,O,P)+i.text)
    if c in (88,200):
      print("{}[{}✵{}]{} HAVAL160,4 =".format(O,C,O,C)+i.text)
    if c in (90,200):
      print("{}[{}✵{}]{} HAVAL192,4 =".format(O,B,O,B)+i.text)
    if c in (92,200):
      print("{}[{}✵{}]{} HAVAL224,4 =".format(O,G,O,G)+i.text)
    if c in (94,200):
      print("{}[{}✵{}]{} HAVAL256,4 =".format(O,Y,O,Y)+i.text)
    if c in (96,200):
      print("{}[{}✵{}]{} HAVAL128,5 =".format(O,P,O,P)+i.text)
    if c in (98,200):
      print("{}[{}✵{}]{} HAVAL160,5 =".format(O,C,O,C)+i.text)
    if c in (100,200):
      print("{}[{}✵{}]{} HAVAL192,5 =".format(O,B,O,B)+i.text)
    if c in (102,200):
      print("{}[{}✵{}]{} HAVAL224,5 =".format(O,G,O,G)+i.text)
    if c in (104,200):
      print("{}[{}✵{}]{} HAVAL256,5 =".format(O,Y,O,Y)+i.text+"\033[0m")


def youtube():
  try:
     link = input(" {}[🌟]{} youtube url = {}".format(R,B,W))
     yt = YouTube(link)
     print("\n {}[{}*{}]{} video title = {}".format(R,G,R,G,W)+yt.title)
     sleep(1)
     print(" {}[{}*{}]{} video thumnail = {}".format(R,G,R,G,W)+yt.thumbnail_url)
     sleep(1)
     print(" {}[{}*{}]{} video ID = {}".format(R,G,R,G,W)+yt.video_id)
     sleep(1)
     print(" {}[{}*{}]{} video length(s) = {}".format(R,G,R,G,W),yt.length)
     sleep(1)
     print(" {}[{}*{}]{} video views = {}".format(R,G,R,G,W),yt.views)
     sleep(1)
     print(" {}[{}*{}]{} video Rating = {}".format(R,G,R,G,W),yt.rating)
     sleep(1)
     print(" {}[{}*{}]{} Age Restricted = {}".format(R,G,R,G,W),yt.age_restricted)
     sleep(1)
     print(" {}[{}*{}]{} video Description = {}\n".format(R,G,R,G,W)+yt.description)
     sleep(1)
  except KeyboardInterrupt:
    exit()
  except Exception:
    sleep(1)
    print("\033[1;31m [!]Invalid link., check your given link\033[0m")
    exit()

  choice = input(" {}[🌟]{} If you want to Download video type ({}y/n{}) {}".format(R,B,G,B,W))
  for i in choice:
   if i == "y" or i == "Y":
     continue
   else:
    exit()
  sleep(1)
  try:
    res = input("\n {}[🌟]{} High Quality(H)/Low Quality(L) ({}H/L{}) {}".format(R,B,G,B,W))
  except KeyboardInterrupt:
    exit()

  if res == "H" or res == "h":
    print(G)
    print(system("pytube {} -t /sdcard --itag=22".format(link)))
    print(O)
  elif res == "L" or res == "l":
   print(G)
   print(system("pytube {} -t /sdcard --itag=18".format(link)))
   print(O)
  else:
    exit()

