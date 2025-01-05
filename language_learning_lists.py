# given a multiline string
# create a list of lists
# each containing all the words in a line that have more than 3 characters

text= '''Some years ago—never mind how long
precisely—having little or no money in my purse,
and nothing particular to interest me on shore,
I thought I would sail about a little and see the watery part of the world.'''

# print(text)

#solution 1

words = []

for line in text.split('\n'):
    lines = []
    for word in line.split():
        if len(word) > 3:
            lines.append(word)
    words.append(lines)
            
print(words, "words")

#solution#2

w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]
print(w)