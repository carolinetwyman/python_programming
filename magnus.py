word = input()

H = 0
O = 0
N = 0
I = 0
HONI = 4
HONIS = 0
        
for n in range(len(word)):
    current = word[n]
    # previous = word[n-1]
    if current == 'H' and H <= O and (H % 1 == 0):
        H = H + 1
        HONIS = HONIS + 1
        print(H, 'H', HONIS)
    elif current == 'O' and O <= N and (O % 2 == 0):
        O = O + 1
        HONIS = HONIS + 1
        print(O, "O", HONIS)
    elif current == 'N' and N <= I and (N % 3 == 0):
        N = N + 1
        HONIS = HONIS + 1
        print(N, "N", HONIS)
    elif current == 'I' and (I % 4 == 0):
        I = I + 1
        HONIS = HONIS + 1
        print(I, "I", HONIS)

amount = HONIS // HONI
print(amount)
    