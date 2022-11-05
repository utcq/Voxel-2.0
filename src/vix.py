import os, sys
from pathlib import Path
import toml


dirbase = os.path.dirname(__file__) + "/"
dirbase = str(Path(dirbase).resolve().parents[0]) + "/"

def checkPKG(name):
    dirz = "/usr/lib/voxel/libc/" + name
    if os.path.exists(dirz):
        return True
    else:
        return False

helpz = """
COMMANDS:
    install
    remove
    prj  [
        build,
        run,
        init,
        setup
    ]
"""

if len(sys.argv) < 2:
    print("missing args use help")
    exit()

if sys.argv[1] == "help":
    print(helpz)
    exit()
elif sys.argv[1] == "install" and len(sys.argv) >= 3:
    pkgs = sys.argv
    del pkgs[0]
    del pkgs[0]
    for pkg in pkgs:
        url = f"https://raw.githubusercontent.com/UnityTheCoder/vix/main/%40pkgs/{pkg}/{pkg}.vx"
        url1 = f"https://raw.githubusercontent.com/UnityTheCoder/vix/main/%40pkgs/{pkg}/{pkg}.cpp"
        print(url1)
        x = os.popen("curl --silent " + url).read()
        x1 = os.popen("curl --silent " + url1).read()
        if "404" in str(x) or "Not Found" in str(x):
            if "404" in str(x1) or "Not Found" in str(x1):
                print("Package not found!")
                exit()
        os.system(f"python3 {dirbase}src/getsubdir.py UnityTheCoder/vix -p @pkgs/{pkg} -r True")
        zz = os.system(f"sudo mkdir /usr/lib/voxel/libc/{pkg}")
        if zz != 0:
            print("[Failed to Install Lib] Possible Causes:\n    Library already Installed, if you want an update, remove and reinstall it")
            os.system("rm -r vix")
            exit()
        os.system(f"sudo cp -r {dirbase}vix/* /usr/lib/voxel/libc/{pkg}/")
        os.system("rm -r vix")
        
elif sys.argv[1] == "remove" and len(sys.argv) >= 3:
    pkgs = sys.argv
    del pkgs[0]
    del pkgs[0]
    for pkg in pkgs:
        os.system(f"rm -r /usr/lib/voxel/libc/{pkg}")

elif sys.argv[1] == "prj":
    if len(sys.argv) >= 3:
        if sys.argv[2] == "build":
            try:
                data = toml.load("vix.toml")
            except:
                print("No vix.toml file found\n  -> vix prj init")
                exit()
            try:
                mainfile = data["project"]["mainfile"]
            except:
                print('No mainfile variable found in vix.toml\n  -> mainfile="FILE.vx"')
                exit()
            
            os.system(f"vxc src/{mainfile} -o output/main")
        elif sys.argv[2] == "run":
            os.system("./output/main")
        
        elif sys.argv[2] == "setup":
            try:
                data = toml.load("vix.toml")
            except:
                print("No vix.toml file found\n  -> vix prj init")
                exit()
            try:
                packages = data["dependencies"]["packages"]
            except:
                exit()
            
            pkgs = ' '.join(packages)
            os.system("python vix install " + pkgs)



