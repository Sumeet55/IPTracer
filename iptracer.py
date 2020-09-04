import requests
import json
import os

os.system("clear")
print('''\033[1;35;40m
  _____  _____    _______                           
 |_   _||  __ \  |__   __|                          
   | |  | |__) |    | | _ __  __ _   ___  ___  _ __ 
   | |  |  ___/     | || '__|/ _` | / __|/ _ \| '__|
  _| |_ | |         | || |  | (_| || (__|  __/| |   
 |_____||_|         |_||_|   \__,_| \___|\___||_|\033[0m  
                                
                                                    
            \033[1;40mTool Created By\033[0m\033[1;33;40m SKBROOT\033[0m
''')
while True:
        user=input("\033[1;33;40mENTER TARGET IP : \033[0m \033[32;40m")
        r =requests.get("http://ip-api.com/json/"+user)
        j=json.loads(r.text)
        for i in j:           
                print(f"\033[1;33;40m {i} : \033[0m \033[32;40m{j[i]}\033[0m")

        break            
