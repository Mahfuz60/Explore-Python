wordCount=0
letterCount=0
digitCount=0

text=input("Enter your text value:")
for x in text:
    x=x.lower()
    if x>='a' and  x<='z':
       letterCount=letterCount+1

    elif x >='0' and x <='9':
       digitCount=digitCount+1
    elif x==" ":
       wordCount=wordCount+1

print("Number of Letter:",letterCount)
print("Number of Digit:",digitCount)
print("Number of Word:",wordCount+1)