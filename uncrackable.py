password = input()
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digit = '0123456789'

length = len(password)

uppercase_current = 0
lowercase_current = 0
digit_current = 0

for i in range(len(password)):
    current = password[i]
    for uppercase_index in range(len(uppercase)):
        if current == uppercase[uppercase_index]:
            uppercase_current = uppercase_current + 1
                
    for lowercase_index in range(len(lowercase)):
        if current == lowercase[lowercase_index]:
            lowercase_current = lowercase_current + 1
            
    for digit_index in range(len(digit)):
        if current == digit[digit_index]:
            digit_current = digit_current + 1

if uppercase_current >= 2 and lowercase_current >= 3 and digit_current >= 1 and (length > 7 and length <13) :
    print('Valid')
else:
    print('Invalid')