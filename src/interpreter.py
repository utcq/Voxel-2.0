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
    --save
    --run
    --justcpp
"""



def justcpp(file):
    code = open(file, "r").read()
    Lxr = Parser(code) 
    lexed = Lxr.parse()
    Trns = Transform(lexed, code)
    newcode = Trns.toCPP()
    newfile = file.split(".")[0]
    new = file.split(".")
    del new[-1]
    output = '.'.join(new)
    newcode = newcode.replace('#include <std.cpp>', '')
    open(output + ".cpp", "w").write(newcode)
    

def main():
    global debug
    global save
    global run
    debug = False
    save = False
    run = False

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
    file = sys.argv[1]
    if "--debug" in sys.argv:
        debug = True
    if "--save" in sys.argv:
        save = True
    if "--run" in sys.argv:
        run = True
    if "--justcpp" in sys.argv:
        justcpp(file)
        exit()
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
    if debug:
        print(f"Compiling with g++    [{file}] --> [{output}]")
    exitc = os.system(f"g++ -w -I{dirbase}libc/ -Wall -Wextra {output + '.cpp'} -o {output}")

    if exitc == 0:
        print(f"Sucess! > {output}")
    else:
        print(f"Failed!")
        if save == False:
            os.remove(output + ".cpp")
        exit()
    if save == False:
        os.remove(output + ".cpp")

    if run:
        print("\n\n" + "="*25 + "RUN" + "="*25 + "\n")
        os.system("./" + output)
        print("\n" + "="*53)
        os.remove(output)
    

if __name__ == "__main__":
    main()

