# filename = "readFileDefault.py" # this code

# f = open(filename)
# lines = []
# for line in f:
#     lines.append(line.strip())
#     print(lines)
    
# f.close() -- not necessary

# print([line.strip() for line in open("readFile.py")])

## Data Input
# txt = ["lambda functions are anonymous functions.",
#        "anonymous functions don't have a name",
#        "functions are objects in Python"]

filename = "readFile.py"

f = open(filename)
lines = []
for line in f:
    lines.append(line.strip())

f.close()

## One liner
mark = map(lambda line: (True, line) if "anonymous" in line else (False, line), lines)

## Result
print(list(mark))