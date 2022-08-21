num1={1,3,4,5,6,} #not allowed duplicate value
print(num1)
num2=set([2,3,54,6,7,8])
print(num2)
# num1.add(10)
# print(num1)
# num1.remove(4)
# print(num1)

print(4 in num1)

# union
print("union:",num1 |num2)
# intersection
print("intersection:",num1 & num2)
# difference
print("difference:",num1-num2)