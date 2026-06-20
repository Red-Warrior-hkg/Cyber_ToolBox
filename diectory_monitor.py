import os
import time


def path_checker():
    target = input("Enter the directory you want to monitor: ").strip()
    if os.path.exists(target):
        print(f"The target directory {target} is selected!")
        return target
    else:
        print("Error reading directory: ",target)
        return None

def snapshot(target):
    snapshot = {}
    try:
        for item in os.listdir(target):
            full_path = os.path.join(target, item)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                timestamp = os.path.getmtime(full_path)
                snapshot[item] =  (size, timestamp)
        return snapshot
    except (OSError, PermissionError) as e:
        print("Error: ",e)
        return {}


def monitor(target_dir):
    try:
        old_snapshot = snapshot(target_dir)
        while True:
            
            time.sleep(2)
            new_snapshot = snapshot(target_dir)
        
            old_files = set(old_snapshot.keys())#snapshot[item].keys() extracts only the filenames
            new_files = set(new_snapshot.keys())# set(...) turn the list into mathematical set
        
            created = new_files - old_files
            deleted = old_files - new_files
        
            for item in created:
                print(f"[CREATED] : {item} has been created!")

            for item in deleted:
                if deleted:
                    print(f"[DELETED] : {item} has been deleted!")

        
            match = old_files & new_files
            for item in match:
                old_size, old_time = old_snapshot[item]
                new_size, new_time = new_snapshot[item] #preven from additional variabels "old_size = old_snapshot[item][0]" etc
                            #python handle that automatically takes the first and second item of the tuple and place it
                modified_size = old_size != new_size
                if modified_size:
                    print(f"[MODIFIED] : {item} Size has been modified")
                modified_time = old_time != new_time
                if modified_time:
                    print(f"[MODIFIED] : {item} Timestamp has been modified")
                    
            old_snapshot = new_snapshot
            
    except KeyboardInterrupt:
        print("Monitoring stoped by user!")
        print("Exiting...")
        time.sleep(0.5)
        
target_dir = path_checker()
if target_dir:
    monitor(target_dir)
