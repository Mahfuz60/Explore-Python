# sum of 1+2+3+3+4+.......+n
n=int(input("Enter your Number(n):"))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print(sum)


# 2+4+6+-------+n
num=int(input("Enter your Number(num):"))
sum=0
for x in range(2,num+1,2):
    print(x)
    sum=sum+x
print("even number sum is:",sum)
print("program end")

# 1+3+5+-------+n
num1=int(input("Enter your Number(num1):"))
sum2=0
for y in range(1,num1+1,2):
    print(y)
    sum2=sum+y
print("Odd number sum is:",sum2)
print("program end")