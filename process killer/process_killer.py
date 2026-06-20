import psutil
import os 

def user_to_kill():
    data = set()
    
    for proc in psutil.process_iter(['username', 'pid']):
        try:
            pid = proc.info['pid']
            current_pid = os.getpid()
            if pid == current_pid:
                continue
            
            usrname = proc.info['username']
            if usrname is not None and not usrname.startswith(("NT","IIS","window","UMFD","DWM")):
                data.add(usrname)
        except (psutil.NoSuchProcess, psutil.AccessDenied)as e:
            print(f"Error: {e}")
            continue
    
    print("Safe to kill usernames: ")

    if len(data) > 1:
        for user in sorted(data):
            print(f"  - {user}")
        userchoice = input("Chose a user from the list: ").strip()
        if userchoice not in data:
            print("User not found, please chose from the list")
            return None
    else:
        userchoice = list(data)[0]
    print(f"target user selected: {userchoice}")
    return userchoice
    

S = user_to_kill()
if S is None:
    print("Exiting...")
    exit()
    
confirm = input("\nTerminate processes for this user? (yes/no): ").lower()

current_pid = os.getpid()

if confirm == 'yes':
    for proc in psutil.process_iter(['username', 'pid']):
        try:
            pid = proc.info['pid']
            
            if pid == current_pid:
                continue
            if proc.info['username'] == S:
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    print("Operation Finished!")
        
else:
    print("Operation cancelled.")
    exit()
    
    