# JSON-Console
## A simple JSON CLI python script.
### Developed by @bigdancingmonkeyballs on discord

## Syntax
### Strings
Strings are enclosed in "" and ONLY "". This application does not support singles quotes.
### Integers
Just numbers. No floats or doubles.
### Commands
Really basic. Examples:
```
EXIT
ADD "name" "value"
FIND "name"
SEARCH "keyword"
```

## Python Arguments
### --filepath <path>
Sets the path for the JSON file
### --debug
Opens a debug CLI that prints all token infromation. Eg. > name | value

## Keywords
### FIND <query: string>
Looks for an entry in the JSON file which title matches the exact query string

### SEARCH <query: string>
Outputs all entries that includes the query inside of the name. Doesn't have to be an exact match unlike FIND.

### DUMP
Dumps all the JSON information to the CLI.

### ADD <name: string> <value: string>
Adds an entry to the specified JSON file. Eg. ```ADD "name" "value"```

### HELP
Outputs some help stuff or smth.

### EXIT
Exits out of the program.
