import array

a=array.array("d",[1,3,4,5])
a.append(1)
print(a)
a.extend([6,7,8])
print(a)
a.insert(2,100)
print(a)
a.pop(2)
print(a)