import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import colorama 
import socket 
from colorama import Fore
import os 
import sys 
import datetime 
from datetime import datetime
import os
import requests
import json
import colorama 
import urllib
from urllib.request import urlopen as open
import webbrowser
import os 
from colorama import Fore, Back, Style 
import requests 
from termcolor import colored
import time
from requests import get 
import sys 
import pyfiglet
import sys
import socket
from datetime import datetime

os.system('clear')
def banner():
    print(Fore.MAGENTA+"""
  _____    _____     ____                ____   ______       ____     ___       ___   _____      
 / ____\  / ___/    / ___)              / ___) (   __ \     (    )   (  (       )  ) (_   _)     
( (___   ( (__     / /      ________   / /      ) (__) )    / /\ \    \  \  _  /  /    | |       
 \___ \   ) __)   ( (      (________) ( (      (    __/    ( (__) )    \  \/ \/  /     | |       
     ) ) ( (      ( (                 ( (       ) \ \  _    )    (      )   _   (      | |   __  
 ___/ /   \ \___   \ \___              \ \___  ( ( \ \_))  /  /\  \     \  ( )  /    __| |___) ) 
/____/     \____\   \____)              \____)  )_) \__/  /__(  )__\     \_/ \_/     \________/  
                                                                                                
    """)

banner()
print("To view more info on this and how to use it type info ")
print(".")
print(".")
target1 = str(input(" www link to target @>> "))
print("-------------------------------------------------")
target2 = str(input(" Url to Crawl @>> "))


r = requests.get(f'{target2}')

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)


if 'info' in ():
    os.systen('cat info.txt')
#sudo nmap -F -sC

def host_tracer():
    print("------------------ HOST INFO -------------------- ")
    s = socket.gethostbyname(target1)
    print("\033[32m [*] HOST IPA ==> ", s)
    print("--------------------------------------------------")
    url = "http://ip-api.com/json/"
    response = open(url + s)
    data = response.read()
    values = json.loads(data)
    status = values['status']
    success = "success"
    lat = str(values['lat'])
    lon = str(values['lon'])
    a = lat + ","
    b = lon + "/"
    c = b + "data=!3m1!1e3?hl=en"
    location = a + c
    time.sleep(0.1)
    print("")
    print("\033[33m[!] RUNNING WHO IS..... ")
    print("")
    print("")
    print("\033[32m [+]\033[36m Response      ====> ", response)
    print("\033[32m [+]\033[36m Response URL  ====> ", response.url)
    print("\033[32m [+]\033[36m HOST IPA      ====> ", s)
    print("\033[32m [+]\033[36m IP            ====> " + values['query']        )
    print("\033[32m [+]\033[36m Status        ====> " + values['status']   )
    print("\033[32m [+]\033[36m city          ====> " + values['city']       )
    print("\033[32m [+]\033[36m ISP           ====> " + values['isp']         )
    print("\033[32m [+]\033[36m latitude      ====> " + lat              )
    print("\033[32m [+]\033[36m longitude     ====> " + lon             )
    print("\033[32m [+]\033[36m country       ====> " + values['country'] )
    print("\033[32m [+]\033[36m region        ====> " + values['regionName'])
    print("\033[32m [+]\033[36m city          ====> " + values['city']       )
    print("\033[32m [+]\033[36m zip           ====> " + values['zip']         )
    print("\033[32m [+]\033[36m AS            ====> " + values['as']           )
    print("")
    print("")
    print("")
    print(" -------------------------------------------------------")
    print("\033[33m [!] Running Nmap [!] ")
    print("")
    print("\033[35m")
    os.system(f'sudo nmap -F -sC {s}')
    print(" -----------------------------------------------------------")
    print("")
    print("\033[37m ")
    print(" [*] Running request response for json....[*] ")
    r = requests.get(f'{target2}')
    print("-------------------------------------")
    print("Response      ====>  ",response)
    print("-------------------------------------")
    print("Response URL  ====> ",response.url)
    print("--------------------------------------")
    print("Response Code ====> ",r.status_code)
    print(" ")
    print("\033[34m")
    print("")
    print(" --------------- Running URL Crawler -------------- ")

def scanner():
        print("--------------------------------------------------")
        target = str(input(" Url to port scan @>> "))
        sock1 = socket.gethostbyname(f'{target}')
        print("-------------------------------------------------")
        print('\033[36m [*] hostname ==>\033[35m', sock1)
        print("-------------------------------------------------")
        sock2 = str(input(" Your Host you want to scan @>> "))
        print("\033[31m [*] Scanning host ", sock1)
        t1 = datetime.now()
        try:
            for port in range(1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((sock2,port))
                if result ==0: # number color format print(Fore.RED+" isnt avalible for str and multiple brackets and variables")
                    timescan = '[DATA] At ==>' + str(datetime.now())
                    print(timescan)
                    print("----------------------------------------------------------------------------------------------")
                    print("\033[35m Port ===> \033[36m [\033[35m {} \033[36m ] \033[35m Appears To Be Open".format(port))
                    print("----------------------------------------------------------------------------------------------")
                    s.close()#finally fucking close it after spending hours on color format just to find out like rust you forgot a ; that messed the enteire script up
        except KeyboardInterrupt: # instead of it being a damn semi colon you forgot to put fucking m SMH FML(programmer rage)
            t.sleep(1)
            print(" [!] CONTINUING [!]")
            t.sleep(1)




class Crawler:
    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'[DATA] CRAWLING ===> {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'[!] WARNING ===> FAILED TO CRAWL {url}')
            finally:
                self.visited_urls.append(url)

if __name__ == '__main__':
    host_tracer()
    Crawler(urls=[f'{target2}']).run()