# name function
def calculator(a,b):
    return a*a+ 2*a*b +b*b

result=calculator(2,3)
print("nameFunc:",result)

# lamda function
# lambda parameter :expression
result2=(lambda a,b:a*a+ 2*a*b +b*b)(2,3)
print("lamda:",result2)