#list
#not hashable
#are mutable
l = [1,2,3]
print(len(l))
#3

#is
y = x = 3
print(x is y)
#True

print(3 is 3)
#True

print([3] is [3])
#False

#adding elements
#append
l = [1,2,3]
l.append(4)
print(l, "list append")
#insert
l.insert(1,2)
print(l, "list insert")
#list concatenation
print([1,2,3,4] + [5], 'concatenated lists')
#extended
l.extend([6,7,8])
print(l, "list extended")
#removing
l.remove(7)
print(l, "list remove")
#reversing
l.reverse()
print(l, "list reverse")
#sort
l.sort()
print(l, "list sort")
#index
print([2,2,4].index(2), "list index")
print(l.index(4), "list index")

#stack FIFO
stack = [3]
print(stack, "stack")
#append
print(stack.append(4), "stack append wrong")
stack.append(4)
print(stack, "stack append good")
#pop
stack.pop()
print(stack, "stack popped")