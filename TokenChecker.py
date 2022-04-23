import colorama
import requests 
from colorama import Fore, Style, init
init()


op = requests.Session()


print(Fore.MAGENTA + """
___________     __                 _________ .__                   __               ____   ________ 
\__    ___/___ |  | __ ____   ____ \_   ___ \|  |__   ____   ____ |  | __ __________\   \ /   /_   |
  |    | /  _ \|  |/ // __ \ /    \/    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \   Y   / |   |
  |    |(  <_> )    <\  ___/|   |  \     \___<By GodzLory>_/\ \___|    <\  ___/|  | \/\     /  |   |
  |____| \____/|__|_ |\___  >___|  /\______  /___|  /\___  >\___  >__|_ |\___  >__|    \___/   |___|
                    \/    \/     \/        \/     \/     \/     \/     \/    \/                     

[1] Start the program [2] Help [3] Support
""")

R = int(input("Choice: "))

if R == 1:
       with open("Token.txt") as file:
                     for line in file.readlines():
                            token = line.strip("\n")
                            headers={
                            'Authorization': f'{token}'
                            }

                            link = op.get('https://discordapp.com/api/v6/auth/login', headers=headers)
                            if link.status_code in [200, 201, 204]:
                                   print(Fore.LIGHTGREEN_EX + '[+]:'+ token)
                            else:
                                   print(Fore.LIGHTRED_EX + "[-]:" + token)


       print(Fore.LIGHTBLUE_EX + "All tokens have been generated!")

if R == 2:
       print(Fore.MAGENTA + """
===================================
a)Where to insert the tokens?
a)Insert the tokens in the "Token.txt" file as in the example
===================================
b)What is it for?
b)This program is used to check if discord tokens work
===================================
""")

if R == 3:
       print(Fore.MAGENTA + "To get support for various problems, enter here: https://discord.gg/TZB9qsQEPK")
