from lexer import Parser
from trans import Transform
import os, sys
from pathlib import Path


dirbase = os.path.dirname(__file__) + "/"
dirbase = str(Path(dirbase).resolve().parents[0]) + "/"

help = """
Usage: vxc FILE.vx 
Usage: vxc FILE.vx -o main

Args:
    --help
    -o
    --debug
"""



def main():
    global debug
    debug = False

    if len(sys.argv) < 2:
        print("Missing arguments use --help for help")
        exit()

    if sys.argv[1] == "--help":
        print(help)
        exit()
    
    if sys.argv[1].endswith(".vx"):
        try:
            code = open(sys.argv[1], "r").read()
        except:
            print("File not found!")
            exit()
    if "--debug" in sys.argv:
        debug = True
    file = sys.argv[1]
    if len(sys.argv) >= 4:
        if sys.argv[2] == "-o":
            output = sys.argv[3]
    else:
        output="a"

    Lxr = Parser(code) 
    lexed = Lxr.parse()
    if debug:
        for lex in lexed:
            print(lex)
            pass
    Trns = Transform(lexed, code)
    newcode = Trns.toCPP()
    newfile = file.split(".")[0]
    open(output + ".cpp", "w").write(newcode)
    print(f"Compiling with g++    [{file}] --> [{output}]")
    exitc = os.system(f"g++ -w -I{dirbase}libc/ -Wall -Wextra {output + '.cpp'} -o {output}")

    if exitc == 0:
        print(f"Sucess! > {output}")
    else:
        print(f"Failed!")
    os.remove(output + ".cpp")
    

if __name__ == "__main__":
    main()

