# if month <= 2 
# and date < 18 print before
# if date > 2//18, print after 
# if date == 2/18, print special

month = int(input())
day = int(input())

if ((month <= 2) and
    (day < 18)):
    print('Before')
elif (month < 2):
    print('Before')
elif ((month == 2) and
    (day > 18)):
    print('After')
elif ((month > 2)):
    print('After')
elif ((month == 2) and
    (day == 18)):
    print('Special')