# #list
# #not hashable
# #are mutable
# l = [1,2,3]
# print(len(l))
# #3

# #is
# y = x = 3
# print(x is y)
# #True

# print(3 is 3)
# #True

# print([3] is [3])
# #False

# #adding elements
# #append
# l = [1,2,3]
# l.append(4)
# print(l, "list append")
# #insert
# l.insert(1,2)
# print(l, "list insert")
# #list concatenation
# print([1,2,3,4] + [5], 'concatenated lists')
# #extended
# l.extend([6,7,8])
# print(l, "list extended")
# #removing
# l.remove(7)
# print(l, "list remove")
# #reversing
# l.reverse()
# print(l, "list reverse")
# #sort
# l.sort()
# print(l, "list sort")
# #index
# print([2,2,4].index(2), "list index")
# print(l.index(4), "list index")

# #stack FIFO
# stack = [3]
# print(stack, "stack")
# #append
# print(stack.append(4), "stack append wrong")
# stack.append(4)
# print(stack, "stack append good")
# #pop
# stack.pop()
# print(stack, "stack popped")

# #list and set comprehension
# customers = [("John", 240000),
#              ("Alice", 120000),
#              ("Ann", 1100000),
#              ("Zach", 440000)]

# whales = [x for x,y in customers if y>1000000]
# print(whales, "whales")

# minions = [n for n,m in customers if m<1000000]
# print(minions, "minions")

#if elif and else

#x = int(input("your value:"))
# if x > 3:
#     print("Big")
# elif x == 3:
#     print("Medium")
# else:
#     print("Small")
    
# for i in [0,1,2]:
#     print(i, "test")
    
# j = 0
# while j < 5:
#     print(j)
#     j=j+1

# j = 0
# while j < 100:
#     print("hello world")
#     j += 1
    
# def appreciate(x, percentage):
#     return x + x * percentage / 100

# print(appreciate(5,5))

# while True:
#     continue
#     print(43)

print((lambda x,y : x + y + 3)(2,3))