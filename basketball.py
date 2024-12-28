apples_three = int(input())
apples_jumpshot = int(input())
apples_freethrow = int(input())
bananas_three = int(input())
bananas_jumpshot = int(input())
bananas_freethrow = int(input())

apples_total = apples_three * 3 + apples_jumpshot * 2 + apples_freethrow

bananas_total = bananas_three * 3 + bananas_jumpshot * 2 + bananas_freethrow

if apples_total > bananas_total:
    print('A')
    print('Apples win!')
elif bananas_total > apples_total:
    print('B')
    print('Bananas win!')
elif bananas_total == apples_total:
    print('T')
    print('Tie!')
else:
    print('Error')
