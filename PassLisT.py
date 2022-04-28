import requests
import json
import os , sys
from time import sleep
from colorama import Fore, init
from rich.console import Console
console = Console()
r = requests.session()
from rich import inspect
def ketik(s):
    for ASU in s + '\n':
        sys.stdout.write(ASU)
        sys.stdout.flush()
        sleep(50. / 1000)

os.system('clear')



red_color = "\033[1;31m"
info_color = "\033[1;33m"
detect_color = "\033[1;34m"
end_banner_color = "\33[00m"

print(red_color +"""
                          __    _      __ 
    ____  ____ ___________/ /   (_)____/ /_
   / __ \/ __ `/ ___/ ___/ /   / / ___/ __/
  / /_/ / /_/ (__  |__  ) /___/ (__  ) /_  
 / .___/\__,_/____/____/_____/_/____/\__/  
/_/                                        


""")






url = "http://flaah999.byethost7.com/pass/number.txt?i=1"



headers = {
    "Host": "flaah999.byethost7.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Cookie": "__test=9b51e69443d56c4c8ece50d8706d4d9b",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
response = requests.request ("GET", url, headers=headers).text




test_data = [
    {"Password": "2022", "file text": [ 2, 3, 4, 5, 6 ], "number": response,},
    {"Update": "1.0", "Developer": "FaLaH", "snapchat": ["flaah999"]},

]


url = "http://flaah999.byethost7.com/pass/flo.txt?i=1"



headers = {
    "Host": "flaah999.byethost7.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Cookie": "__test=9b51e69443d56c4c8ece50d8706d4d9b",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
response = requests.request ("GET", url, headers=headers).text



def test_log():
    "https://github.com/0xfff0800"
    updated = {
        response,
    }
    Attention = ["The rules are constantly updated"]
    console.log("Hello from","!")
    console.log(test_data, log_locals=True)


test_log()


print("""

""")
input(red_color+"To continue, press Enter : ")

ketik ("\033[1;33mPasswords are now displayed and saved....\033[1;33m")
sleep (0.5)


url = "http://flaah999.byethost7.com/pass/password.txt?i=1"



headers = {
    "Host": "flaah999.byethost7.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Cookie": "__test=9b51e69443d56c4c8ece50d8706d4d9b",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
response = requests.request ("GET", url, headers=headers)
print ("")
#___________________________________________________________

print("-------------------------------")
print(response.text)
with open ('password.txt', 'a',encoding='utf8') as x:
 x.write (response.text)
print(end_banner_color+"")
ketik ("Passwords are saved as follows: password.txt")
sleep (0.5)