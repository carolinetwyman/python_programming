P = int(input()) #total liters of paint
B = int(input()) #liters of paint per badge
D = int(input()) #retail of each badge

C = P//B #ratio of paint out of total paint

R = P%B #remainder of paint that can be sold for $1

Profit = (C * D) + R

print(Profit)