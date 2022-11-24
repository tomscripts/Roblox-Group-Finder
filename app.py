import os
import threading
import requests, random
from dhooks import Webhook
import ctypes


def groupfinder():
    id = random.randint(1000000, 1150000)
    r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") 
    if 'owned' not in r.text:
        re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
        if 'isLocked' not in re.text and 'owner' in re.text:
            if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                hook.send(f'Hit: https://www.roblox.com/groups/group.aspx?gid={id}')
                print(f"[+] Hit: {id}")
            else:
                print(f"[-] No Entry Allowed: {id}")
        else:
            print(f"[-] Group Locked: {id}")
    else:
        print(f"[-] Group Already Owned: {id}")


print("You are using Tom's Roblox Group Finder!")
print("https://github.com/tomscripts/Roblox-Group-Finder")

#your webhook
hook = os.environ['webhook']
#number of threads
threads = 750

while True:
    if threading.active_count() <= threads:
      threading.Thread(target=groupfinder).start()
    
