import sys
import json

JSONpath = r''

def read_index():
    try:
        with open(JSONpath, 'r') as file:
            data = json.load(file)
        return(data)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("The data file has incorrect JSON")

def overwrite_index(data):
    try:
        with open(JSONpath, 'w') as file:
            json.dump(data,file,indent=4)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("The data file has incorrect JSON")

class token(object):
    def __init__(self, token: str, value: str):
        self.token = token
        self.value = value
    def __str__(self):
        return f"TOKEN: {self.token} | VALUE: {self.value}"
class tokenDictionary:
    STR = "STRING"
    INT = "INTEGER"
    KEY = "KEYWORD"
    keywords = ["ADD","EXIT","DUMP","FIND","SEARCH","HELP"]
    def isKeyword(self, key: str):
        return key in self.keywords

def tokenize(toTokenize: str):
    dictionary = tokenDictionary()
    curSpot = 0
    tokenList = []
    while curSpot < len(toTokenize):
        curToken = toTokenize[curSpot]
        if curToken.isalpha() or curToken == '"':
            if curToken == '"':
                curSpot += 1
                val = ""
                while curSpot < len(toTokenize) and toTokenize[curSpot] != '"':
                    val+=toTokenize[curSpot]
                    curSpot+=1
                newToken = token(dictionary.STR, val)
                tokenList.append(newToken)
                curSpot += 1
            else:
                val = ""
                while curSpot < len(toTokenize) and toTokenize[curSpot].isalpha():
                    val+=toTokenize[curSpot]
                    curSpot+=1
                if dictionary.isKeyword(val):
                    newToken = token(dictionary.KEY, val)
                    tokenList.append(newToken)
                else:
                    raise Exception(f"Unexpected character! {curToken}")
        elif(curToken.isspace()):
            curSpot+=1
        elif(curToken.isnumeric()):
            val = ""
            while curSpot < len(toTokenize) and toTokenize[curSpot].isnumeric():
                val+=toTokenize[curSpot]
                curSpot+=1
            curSpot+=1
            newToken = token(dictionary.INT, val)
            tokenList.append(newToken)
        else:
            raise Exception(f"Unexpected token! {curToken}")
    return tokenList

def cli():
    toTokenize = input('>> ')
    tokenized = tokenize(toTokenize)
    interpret(tokenized)
    cli()
def search(query: str):
    data = read_index()
    found = []
    for x in range(len(data)):
        keys = list(data.keys())
        if query in keys[x] or query in data[keys[x]]:
            print(f"{keys[x]} | {data[keys[x]]}")
            found.append(data[keys[x]])
    return found
def add_entry(name: str, value: str):
    data = read_index()
    data[name] = value
    overwrite_index(data)
def interpret(tokenList):
    dictionary = tokenDictionary()
    curIndex = 0
    for token in tokenList:
        if token.token == dictionary.KEY:
            if(token.value == "EXIT"):
                print("Exiting JSON Console Interpreter")
                sys.exit(0)
            if(token.value == "DUMP"):
                print(read_index())
            if(token.value == "FIND"):
                if tokenList[curIndex + 1].token == dictionary.STR:
                    if not tokenList[curIndex+1].value in read_index():
                        print("No such entry!")
                        return
                    print(f"{tokenList[curIndex+1].value} | {read_index()[tokenList[curIndex+1].value]}")
            if (token.value == "SEARCH"):
                if tokenList[curIndex + 1].token == dictionary.STR:
                    search(tokenList[curIndex+1].value)
            if(token.value == "ADD"):
                if tokenList[curIndex+1].token == dictionary.STR and tokenList[curIndex+2].token == dictionary.STR:
                    add_entry(tokenList[curIndex+1].value,tokenList[curIndex+2].value)
            if(token.value == "HELP"):
                print("This literally has a README.md")

        curIndex+=1
def initialize():
    args = sys.argv
    print("JSON Console Interpreter")
    print("Initializing...")
    print(f"Total arguments passed: {len(args)}")
    print(f"Arguments: {args}")
    if "--jsonpath" in args:
        pathArg = args[args.index("--jsonpath")+1]
        global JSONpath
        JSONpath = pathArg
    if "--debug" in args:
        debugCLI()
        return
    cli()
def debugCLI():
    newLine = input("DEBUG >>")
    tokenized = tokenize(newLine)
    for token in tokenized:
        print(f"{token.token} | {token.value}")
    interpret(tokenized)
    debugCLI()

initialize()
