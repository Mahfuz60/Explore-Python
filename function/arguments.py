# xargs
def student(*details):
    print(details)


student("mahfuz",1660,3.27)

def addSum(*numbers):
    sum=0
    for num in numbers:
        sum+=num
    print("sum:",sum)

addSum(10,20)
addSum(10,20,30)
addSum(10,20,20,50)


# xxargs

def student_details(**details):
    print(details)

student_details(id=1660,name="mahfuz alam",cgpa=3.27)