bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())

if ((bowl1 > bowl2 > bowl3) or
    (bowl3 > bowl2 > bowl1)):
    print(bowl2)
elif ((bowl2 > bowl1 > bowl3) or
    (bowl3 > bowl1 > bowl2)):
    print(bowl1)
elif ((bowl1 > bowl3 > bowl2) or
    (bowl2 > bowl3 > bowl1)):
    print(bowl3)
elif ((bowl1 == bowl2 == bowl3) or
    (bowl2 == bowl3 == bowl1)):
    print(bowl1)
elif (bowl1 == bowl2):
    print(bowl1)
elif (bowl2 == bowl3):
    print(bowl3)