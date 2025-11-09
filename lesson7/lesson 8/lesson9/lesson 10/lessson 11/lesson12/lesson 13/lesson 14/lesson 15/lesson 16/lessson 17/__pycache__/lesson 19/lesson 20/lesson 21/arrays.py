import array as a
num=a.array("i",[1,3,3,2,3,4,5,6,3,3,3,])
print("original array")
print(num)

print("number of occurences of the number 3 in the array:")
print(num.count(3))

num.reverse()
print("reverse the oder of the item:")
print(num)