sms = input()

happiness = sms.count(':-)')
sadness = sms.count(':-(')

if (happiness > sadness):
    print('happy')
elif((sadness == happiness) and
    happiness != 0):
    print('unsure')
elif (sadness > happiness):
    print('sad')
else:
    print('none')