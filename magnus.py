word = input()

H = 0
O = 0
N = 0
I = 0
        
for n in range(len(word)):
    current = word[n]
    previous = word[n-1]
    if current == 'H' and H <= O:
        H = H + 1
        # print(H, 'H')
    elif current == 'O' and O <= N:
        O = O + 1
        # print(O, "O")
    elif current == 'N' and N <= I:
        N = N + 1
        # print(N, "N")
    elif current == 'I' and previous != 'I':
        I = I + 1
        # print(I, "I")
        
print(I)
    
    