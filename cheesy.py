width = int(input())
extra_cheesiness = int(input())

if ((width == 3) and 
    (extra_cheesiness >= 95)):
    M = 'absolutely'
elif ((width == 1) and
    (extra_cheesiness <= 50)):
    M = 'fairly'
else:
    M = 'very'

print(f'C.C. is {M} satisfied with her pizza.')