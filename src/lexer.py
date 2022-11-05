import re 
import json

_spc = "\s?"
__spc = "\s"



string = ['"[^"]*"']
boolean=["true|false"]
char = ["'[^']'"]
array=[r"\{[^\]]*\}"]

exceptions = ["true", "false", "puts", "var", "fun"]
digit = ["[0-9]+"]
number = [f"^{digit[0]}.{digit[0]}.$|^.{digit[0]}.$"]
identifier = ["^(?!"]
for ex in exceptions:
    identifier[0] += ex + "|"
if len(exceptions) != 0:
    identifier[0] = identifier[0][:-1] 
    identifier[0] += ")([A-Za-z]+)"
else:
    identifier[0] = "[A-Za-z]+"

operator=["+", "-", "*", "/"]

binary_expression=""
unary_expression=number[0]
expression = f"{unary_expression}|{binary_expression}"
binary_expression=expression + _spc + f"{operator[0]}|{operator[1]}|{operator[2]}|{operator[3]}" + _spc + expression
expression = f"{unary_expression}|{binary_expression}|{identifier[0]}".replace("||", "|") 
binary_expression=expression + _spc + f"{operator[0]}|{operator[1]}|{operator[2]}|{operator[3]}" + _spc + expression
expression = [f"{unary_expression}|{binary_expression}|{identifier[0]}".replace("||", "|")]

openbrace = ["^{$"]
closedbrace = ["^}"]

# BUILTIN
value = [string, identifier, number, boolean, char, array]
puts=["puts\(.*?\)"]
var= [r"(var)\s*?:\s*?(int|bool|char|array|string|short|long|float|double|void)\s*?(.*?)=>\s*?[\s\S]*"]
fun =  [r"fun\s*?:\s*?(int|bool|char|array|string|void|short|long|float|double)\s*([a-z_A-Z.,#-() {} \[\]]+)\s*?\{?"]
comment = [r"/^\s*[;\//].*?$/m"]
vxinclude = ["^@include\s(.*?)$"]



elements = [vxinclude,
            identifier, 
            number, 
            boolean, 
            string, 
            char,
            array,
            puts,
            var,
            fun,
            openbrace,
            closedbrace]
elemname = ["vxinclude", "identifier", "number", "boolean", "string", "char", "array", "print_assignment", "var_assignment", "function", "openbrace", "closedbrace"]



lexed = []


class Parser:
    def __init__(self, code):
        self.code = code

    def parse(self):
        code = self.code
        for line in code.splitlines():
            dd = 0
            notfound = False
            for element in elements:
                for item in element:
                    token=elemname[dd]
                    if token == "var_assignment":
                        matches = re.finditer(item, line)

                        for matchNum, match in enumerate(matches, start=1):
                            mat= match.group()
                            #print(token + ":  " + str(mat))
                            data = {
                                "type": token,
                                "varname": mat.split(":")[1].split(" ")[1].strip(),
                                "vartype": mat.split(":")[1].split(" ")[0].strip(),
                                "value": mat.split(":")[1].split("=>")[1].strip()
                            }
                            #print(str(data) + "  =  " + str(mat))
                            lexed.append(data)
                            notfound=False
                    
                    elif token == "print_assignment":
                        x= re.finditer(item, line)
                        for matchNum, match in enumerate(x, start=1):
                            iz = match.group()
                            break
                        reg = "^\([^)]*\)$"
                        try:
                            data = {
                                "type": token,
                                "value": re.findall(reg, iz.split("puts")[1])[0][:-1][1:]
                            }
                        except:
                            break

                        #print(str(data) + "  =  " + str(iz))
                        lexed.append(data)
                        notfound=False

                    
                    elif token == "function":
                        x= re.finditer(item, line, re.MULTILINE)
                        for matchNum, match in enumerate(x, start=1):
                            iz = match.group()
                            break
                        try:
                            funtype = iz.split(":")[1].split(" ")[0]
                            funname = iz.split(":")[1]
                            if funname.endswith("}"):
                                funname = funname[:-1]
                                funname += " {"
                            elif funname.endswith("}"):
                                funname = funname[:-1][:-1]
                                funname += "  {}"
                            data = {
                                "type": token,
                                "funtype": funtype,
                                "funname": funname
                            }
                        except Exception as e:
                            break
                        
                        lexed.append(data)
                        notfound=False

                        

                    else:
                        x=re.findall(item, line)
                        for iz in x:
                            if type(iz) == tuple:
                                iz = " ".join(iz)
                            
                            data = {
                                    "type": token,
                                    "line": iz
                            }
                            #print(str(data["type"]) + "  =  " + str(iz))
                            #print(token + ":  " + str(iz))
                            lexed.append(data)
                            notfound=False
                        if len(x) == 0 and "puts" not in line and "fun:" not in line and "var:" not in line:
                            notfound=True
                dd+=1

            if notfound:
                data = {
                    "type": "unknown",
                    "line": line
                }
                lexed.append(data)


        excp = ["{'type': 'closedbrace', 'line': '}'}"]
        res = []
        for i in lexed:
            if excp and i not in res:
                res.append(i)
            else:
                for ex in excp:
                    if ex in str(i):
                        res.append(i)
        return res
