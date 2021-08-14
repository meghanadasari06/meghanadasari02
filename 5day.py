#list
x=[2,3,4,5,6,7,8,9,1,0]

# extract all list 
print("list x=",x[0:1])
print("list x=",x[0:5])
print("list x=",x)
print("list x=",x[7])
print("list x=",x[0:9])
print("list x=",x[1:9])
print("list x=",x[0:10])
print("list x=",x[10:0])

# extract index number 2to5
print("list x=",x[2:5])

# print list element reverse
print("list x in reverse:",x[::-1])

#using append,insert add element in list 

x.append(11)
print("after add 11 value in list =",x)

x.insert(3,"hi")
print("insert hi in list",x)

x.pop(8)
print("list after pop x[8]=",x)

x.remove(4)
print("list after remove x[4]=",x)

del(x[9])
print("list after deletex[9]",x)

x.clear()
print("list after clear list",x)

