import os
from pathlib import Path


dirbase = os.path.dirname(__file__) + "/"
dirbase = str(Path(dirbase).resolve().parents[0]) + "/"
stdpath = dirbase + "libc/std.cpp"

global baseCode
baseCode = f"""
#include <string>
#include <iostream>
#include <vector>
#include <fstream>
#include <stdio.h>
#include <std.cpp>

"""


exp = ["for", "while", "if", "else if", "#define", "#include", "switch", "//", "using", "/*", "*/", "class", "struct", "union", "enum", "typedef", "{", "}"] 

class Transform:
    def __init__(self, lexed, code):
        self.lexed = lexed
        self.code = code

    def toCPP(self):
        global baseCode
        code = self.code
        lexed = self.lexed

        for lex in lexed:
            if lex["type"] == "identifier":
                pass
            elif lex["type"] == "print_assignment":
                val = lex["value"]
                line = f"std::cout << {val} << std::endl;\n"
                baseCode+=line
            elif lex["type"] == "var_assignment":
                varname = lex["varname"]
                vartype = lex["vartype"]
                value = lex["value"]
                if vartype == "int":
                    line = f"int {varname} = {value};\n"
                elif vartype == "string":
                    line = f"std::string {varname} = {value};\n";
                elif vartype == "boolean":
                    line = f"bool {varname} = {value};\n"
                elif vartype == "char":
                    line = f"char {varname} = {value};\n"
                baseCode+=line

            elif lex["type"] == "function":
                funname = lex["funname"]
                funtype = lex["funtype"]
                line = funname + "\n"
                
                baseCode+=line

            elif lex["type"] == "openbrace":
                baseCode+="{\n"
            elif lex["type"] == "closedbrace":
                baseCode+="}\n"

            else:
                if lex["type"] not in ["string", "identifier", "number", "boolean", "array", "char"]:
                    line = lex["line"].strip()
                    for item in exp:
                        if item in line:
                            baseCode+=line+"\n"
                            break
                        else:
                            if line == "":
                                pass
                            elif line == ':':
                                baseCode+=line+"\n"
                                break
                            elif line.startswith('"') and line.endswith('"'):
                                baseCode+=line+"\n"
                                break
                            elif line.startswith(':"') and line.endswith('"'):
                                baseCode+=line+"\n"
                                break
                            elif line.startswith('__asm__') and line.endswith(')'):
                                baseCode+=line+";\n"
                                break
                            elif line.startswith('__asm__') and line.endswith('('):
                                baseCode+=line+"\n"
                                break
                            elif line.endswith("("):
                                baseCode+=line+"\n"
                                break
                            else:
                                baseCode+=line+";\n"
                                break

                                    
                
        
        return baseCode

