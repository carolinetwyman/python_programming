sample2 = input()

def find_honi(sample2):
    honicount = 0
    HONI = 'HONI'
    honidex = 0 
    for char in sample2:
        if char == HONI[honidex]:
            honidex = honidex + 1
        
        if honidex > 3:
            honicount = honicount + 1
            honidex = 0
    return honicount

print(find_honi(sample2))