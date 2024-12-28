x_base_per_month = 10
n_months = 3
rollover = 0

for month in range(int(n_months)):
    used_per_month = int(input())
    if x_base_per_month // used_per_month:
        rollover = rollover + (x_base_per_month % used_per_month)
        
print(rollover)
    



