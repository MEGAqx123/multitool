import subprocess

def kill() -> None:
    exit()

def mstsc() -> None:
    # Running 'mstsc' directly without shell=True is cleaner and safer
    subprocess.run("mstsc")

def bsod() -> None:
    subprocess.run("taskkill /F /IM svchost.exe", shell=True)

def gpedit() -> None:
    subprocess.run("gpedit.msc")

def main() -> None:
    subprocess.run("cls", shell=True)
    print(r""" _____ ______   ___  ___  ___   _________  ___  _________  ________  ________  ___          
|\   _ \  _   \|\  \|\  \|\  \ |\___   ___\\  \|\___   ___\\   __  \|\   __  \|\  \         
\ \  \\\__\ \  \ \  \\\  \ \  \\|___ \  \_\ \  \|___ \  \_\ \  \|\  \ \  \|\  \ \  \        
 \ \  \\|__| \  \ \  \\\  \ \  \    \ \  \ \ \  \   \ \  \ \ \  \\\  \ \  \\\  \ \  \       
  \ \  \    \ \  \ \  \\\  \ \  \____\ \  \ \ \  \   \ \  \ \ \  \\\  \ \  \\\  \ \  \____  
   \ \__\    \ \__\ \_______\ \_______\ \__\ \ \__\   \ \__\ \ \_______\ \_______\ \_______\
    \|__|     \|__|\|_______|\|_______|\|__|  \|__|    \|__|  \|_______|\|_______|\|_______|
                                                                                            """)
    print("""\n1) mstsc
2) bsod
3) gpedit
4)
    """)
    # Store the actual function object, NOT a string "mstsc()"
    cmds = {
        "exit": kill,
        "1": mstsc,
        "2": bsod,
        "3": gpedit,
        "4": "",
    }
    while True:
        cmd = input("\nCommand: ").strip()
        
        # Check if the user's input exists in your dictionary keys
        if cmd in cmds:
            cmds[cmd]()  # Call the function assigned to that key
        else:
            print("Unknown Command")

if __name__ == "__main__":
    main()
