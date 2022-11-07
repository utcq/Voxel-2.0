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
        setup,
        info
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
        url = f"https://raw.githubusercontent.com/UnityTheCoder/vix/main/%40pkgs/{pkg}/package.toml"
        x = os.popen("curl --silent " + url).read()
        if "404" in str(x) or "Not Found" in str(x):
            print("Package not found!")
            exit()
        os.system(f"python3 {dirbase}src/getsubdir.py UnityTheCoder/vix -p @pkgs/{pkg} -r True")
        zz = os.system(f"sudo mkdir /usr/lib/voxel/libc/{pkg}")
        if zz != 0:
            print("[Failed to Install Lib] Possible Causes:\n    Library already Installed, if you want an update, remove and reinstall it")
            os.system("rm -r vix")
            exit()
        os.system(f"sudo cp -r vix/* /usr/lib/voxel/libc/{pkg}/")
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
            
            os.system(f"vxc src/{mainfile} -o output/main --inlibs --args")
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
            os.system("vix install " + pkgs)

        elif sys.argv[2] == "init":
            name =         input("Project name                 >  ")
            version =      input("Version                      >  ")
            authors =      input("Authors                      >  ")
            description =  input("Description                  >  ")
            dependencies = input("Packages                     >  ").strip()
            libraries =    input("Builtin Libraries (sqlite3)  >  ").strip()
            args        =  input("Compiler Arguments           >  ").strip()
            authors = authors.split(" ")
            dependencies = ["std"] + dependencies.split(" ")
            dependencies = list(filter(None, dependencies))
            libs = libraries.split(" ")
            libs = list(filter(None, libraries))
            args = args.split(" ")
            args = list(filter(None, args))

            toml = f'''[project]
name = "{name}"
version = "{version}"
authors = {str(authors)}
description = "{description}"
mainfile = "main.vx"
args = {str(args)}


[dependencies]
packages = {str(dependencies)}
libraries = {str(libs)}'''

            code = """
fun:int main() {
    return 0
}
"""

            open("vix.toml", "w").write(toml.strip())
            os.mkdir("src")
            os.mkdir("output")
            open("src/main.vx", "w").write(code)


        elif sys.argv[2] == "info":
            try:
                data = toml.load("vix.toml")
            except:
                print("No vix.toml file found\n  -> vix prj init")
                exit()

            name = data["project"]["name"]
            version = data["project"]["version"]
            authors = data["project"]["authors"]
            description = data["project"]["description"]
            dependencies = data["dependencies"]["packages"]
            libraries = data["dependencies"]["libraries"]

            print(f"Name:         {name}")
            print(f"Version:      {version}")
            print(f"Authors:      {', '.join(authors)}")
            print(f"Description:  {description}")
            print(f"Dependencies: ")
            for dep in dependencies:
                print("     - " + dep)
            print("Libs:          ")
            for lib in libraries:
                print("     - " + lib)

