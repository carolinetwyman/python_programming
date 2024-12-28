x_base_per_month = int(input())
n_months = int(input())

rollover = 0

for month in range(int(n_months)):
    used_per_month = int(input())
    # print('used_per_month', used_per_month)
    if (x_base_per_month - used_per_month) > 0:
        rollover = x_base_per_month + (x_base_per_month - used_per_month)
        # print('rollover', + rollover)
    elif (used_per_month - x_base_per_month) > 0:
        rollover = x_base_per_month + (rollover - used_per_month)
        # print('overflow', rollover)
        # minutes_new = x_base_per_month + rollover
        # print('minutes_new', minutes_new)
        
print('minutes_new', rollover)