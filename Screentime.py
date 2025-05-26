import psutil
import time
import pygetwindow as window
import win32gui
import win32process
import psutil
import csv
#create a tracking process(actively used tabs), that removes the .exe 
  


def get_active_window_process_name():
    try:
       
        hwnd = win32gui.GetForegroundWindow()
       
        
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process_name = psutil.Process(pid).name()
        return process_name
    except Exception as e:
        return f"Error: {e}"

def identify_java_processes():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # Check if the process is javaw.exe
            if proc.info['name'] == 'javaw.exe':
                cmdline = proc.info['cmdline']  # Command-line arguments
                print(f"PID: {proc.info['pid']}")
                print(f"Command Line: {cmdline}")
                print('-' * 40)

                # Example: Look for Minecraft or other tools in cmdline
                if any("minecraft" in arg.lower() for arg in cmdline):
                    print("This is Minecraft!")
                elif any("tool_name" in arg.lower() for arg in cmdline):  # Replace "tool_name"
                    print("This is another Java-based tool!")
                else:
                    print("Unidentified Java application.")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass





import time
vanilla_app_block_time_minutes = 5
vanilla_app_block_time = vanilla_app_block_time_minutes * 60
apps_used = []
blacklisted_programs = []
whitelisted_programs = ['explorer.exe', 'python.exe', 'Code.exe','notepad.exe','obs.exe','SeachHost.exe','ApplicationFrameHost.exe','System', 
'Idle', 
'explorer.exe', 
'python.exe', 
'Code.exe', 
'notepad.exe', 
'obs.exe', 
'SearchHost.exe', 
'ApplicationFrameHost.exe', 
'dwm.exe', 
'taskhostw.exe', 
'svchost.exe', 
'csrss.exe', 
'winlogon.exe', 
'smss.exe', 
'lsass.exe', 
'RuntimeBroker.exe', 
'spoolsv.exe', 
'sihost.exe', 
'fontdrvhost.exe', 
'ctfmon.exe', 
'audiodg.exe',  
'cmd.exe', 
'powershell.exe', 
'conhost.exe', 
'wscript.exe', 
'cscript.exe', 
'OneDrive.exe', 
'taskmgr.exe', 
'wininit.exe', 
'services.exe', 
'logonui.exe', 
'mstsc.exe','Spotify.exe']
while True:
    time.sleep(1)
    vanilla_app_block_time_minutes = input("how long do you want to block vanilla apps for? (in minutes): ")
    try:
        vanilla_app_block_time_minutes = int(vanilla_app_block_time_minutes)
        if vanilla_app_block_time_minutes > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
while True:
   
    current_time = time.localtime()
    
    if time.strftime('%H %M', current_time) == '00 00':
        print("Time to sleep")
        for proc in blacklisted_programs:
            print(-1)
            print(proc['name'])
            for app in apps_used:
                if proc['name'] in app['name']:
                    app['time_used'] = 0
                    blacklisted_programs.remove(proc)
    else:
        pass

    current_app_name = get_active_window_process_name()
    print(1) 
    print(current_app_name)
    result = next((item for item in apps_used if item['name'] == current_app_name), None)
    print(2)
    if result is None:
        print(3)
        current_app = {'name': current_app_name, 'time_used': 0}
        print(4)
        if current_app_name not in blacklisted_programs and current_app_name not in whitelisted_programs:
          print(5)
          apps_used.append(current_app)
          print(apps_used)
    else:
        for app in apps_used:
            print(6)
            if app['name'] in result['name']:
                print(7)
                if result['time_used'] == vanilla_app_block_time and result['name'] not in whitelisted_programs and result['name'] not in blacklisted_programs:
                    print(8)
                    try:
                        print(9)
                        blacklisted_programs.append(result)
                    except Exception as e:
                        
                        print(f"Error: {e}")
                        pass
                    print(blacklisted_programs)
                else:
                    if result['name'] not in whitelisted_programs:
                        result['time_used'] = result['time_used'] + 1
                        print(apps_used)
                if any(blacklisted['name'] == result['name'] for blacklisted in blacklisted_programs) and result['name'] not in whitelisted_programs:
                    print(3)
                    for proc in psutil.process_iter(['pid','name']):
                        
                        if proc.name() == result['name']:
                            try:
                                proc.kill()
                                print("kill")
                            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                                print("error")
                                pass
                else:
                    print(4)

    import os  
    datar = NotImplemented

    folder_path = "data_files"  

# Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  

# Define the file path within the folder
    file = os.path.join(folder_path, f"data_for_{time.strftime('%Y-%m-%d')}.csv")
    try:
        with open(file, mode='w', newline='') as csv_file:
            for i in apps_used:
                writer = csv.writer(csv_file)
                writer.writerow([i['name'], i['time_used']])

            csv_file.close()
    except Exception as e:
        print(f"Error writing to CSV: {e}")
        pass
    time.sleep(1)



#store the data


# create a scikit-learn model to know the category, use data bases and chat gtp



# create ui
