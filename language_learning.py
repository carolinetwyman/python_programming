lines = int(input())

sentence = []

for i in range(lines):
    user_sentence = input()
    sentence.append(user_sentence)

T = 'Tt'
S = 'Ss'

def detect_language(sentences):
    englishness = 0
    frenchness = 0
    
    for line in sentence:
        for char in line:
            if char in T:
                englishness += 1
            if char in S:
                frenchness += 1
    if englishness > frenchness:
        return 'English'
    elif frenchness > englishness:
        return 'French'
    elif frenchness == englishness:
        return 'French'
        
print(detect_language(sentence))