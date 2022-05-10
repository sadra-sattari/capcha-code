# pip install captcha

import time
from captcha.image import  ImageCaptcha
import random
import os
from colorama import Fore , init
from  tqdm import  tqdm 
init()

def logo():
    print(Fore.CYAN + """
                 __             __  __       _    __              __
   _________/ /       _____/ /_/ /______(_)  / /_____  ____  / /
  / ___/ __  /       / ___/ __/ __/ ___/ /  / __/ __ \/ __ \/ / 
 (__  ) /_/ /_      (__  ) /_/ /_/ /  / /  / /_/ /_/ / /_/ / /  
/____/\__,_/(_)____/____/\__/\__/_/  /_/   \__/\____/\____/_/   
             /_____/                                              v : 1.0.0 


    """)

U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L = "abcdefghijklmnopqrstuvwxyz"
N = "0123456789"
X = U + L + N

res = "".join(random.sample(X , 5))
cap = ImageCaptcha(width=200 , height=90)
Img = str(res)
code = cap.generate(Img)
cap.write(Img , 'code.png')
logo ()
for i in tqdm(range(20)):
    time.sleep(0.25)
os.system('cls')
logo()
option = input("enter the captcha code: ")
option = str(option)

if (option == Img) :
    print("login")
else:
    print("failed..!")

os.system('pause')