a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
c=input("enter the arithematic operator to calculate the numbers:")

if (c=='+'):
 print(" The sum of two numbers is:", a+b)
 
elif (c=='-'):
    print(" The difference of two numbers is:", a-b)
elif(c=='*'):
    print(" The product of two numbers is:", a*b)
elif(c=='/'):
    print("The division of two number is:",a/b)
elif(c=="%"):
    print("The modulus of two numbers is:",a%b)
else:
    print("Invalid operator")
 
if (a>b):
    print("a is greater than b")
elif (a<b):
    print("b is greater than a")
else:
    print("a is equal to b")
    
print ("enter the two numeric values:")


#----------------------------------------Nested if-else conditions---------------------------------------------

if (a>0):
    print("a is positive")
    if(a<10):
        print("a is less than 10")
    elif (a<20)&(a>10):
        print("a is between 10 and 20")
    elif(a<50)&(a>20):
        print("a is between 20 and 50")
    else:
        print("no number required")
        
elif(a<0):
    print("a is negative")
    
else:
    print("a is zero")