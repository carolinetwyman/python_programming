word = input()

H = 0
O = 0
N = 0
I = 0
HONI = 4
HONIS = 0
        
for n in range(len(word)-1):
    current = word[n]
    next = word[n+1]
    if current == 'H':
        H = H + 1
        print(H, 'H')
        if next == 'O':
            O = O + 1
            print(O, "O")
            if next == 'N':
                N = N + 1
                print(N, "N")
    # elif current == 'O' and O <= N:
    #     O = O + 1
    #     print(O, "O")
    # elif current == 'N' and N <= I:
    #     N = N + 1
    #     print(N, "N")
    # elif current == 'I' and I <= HONIS:
    #     I = I + 1
    #     print(I, "I")

if (H + O + N + I) == 4:
    print('TRUE')
    HONIS = HONIS + 1
            
print(HONIS)