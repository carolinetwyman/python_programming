base_per_month = int(input())
n_months = int(input())

rollover = 0

for month in range(int(n_months)):
    used_per_month = int(input())
    # print('used_per_month', used_per_month)
    rollover = base_per_month + rollover - used_per_month
    # print('overflow', rollover)
print(rollover + base_per_month)