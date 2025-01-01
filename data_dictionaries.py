calories = {'apple': 52, 'banana': 100, 'chocolate': 10}

print(calories['apple'], "apple")

print(calories['apple'] > calories['chocolate'], "Apples more than chocolate")

print('apple' in calories.keys(), "apple in calories keys")

print(52 in calories.values(), '52 exists in the calories')

for k,v in calories.items():
    print(k) if v > 10 else None
    
print(42 in [2,39,42])

print("list" in {"list": [1,2,3],"set" : {1,2,3}})