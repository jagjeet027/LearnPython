#----------------------------------------------Simple Arguments-------------------------------------------------------


# def arguments(a,b):
#     print('the average of the no. is',(a+b)/2)
    
# arguments(10,12)


# #---------------------------------------------Default Arguments------------------------------------------------------

# def default(a=13,b=10):
#     print('the avg no is:' ,(a+b)/2)
    
# default()

# #-----------------------------------------------keyword Arguments----------------------------------------------------

# def keyword(a,b):
#     print('the avg of the no is:',(a+b)/3)

# keyword(a=12,b=13)



# Function that accepts any number of positional arguments
def argument(*numbers):
    # *numbers stores all arguments as a tuple
    print(type(numbers))   # Output: <class 'tuple'>
    sum = 0
    for i in numbers:      # Loop through all given numbers
        sum += i           # Add each number to sum
        # Print the average after adding each number
        print('The avg of the numbers is:', sum / len(numbers))

# Calling the function with two numbers
argument(12, 13)

#  🔹 1️⃣ *numbers — (args / positional arguments)
# 👉 Ye use hota hai jab hume unknown number of values leni ho function ke andar.

# 🧠 Explanation:

# *numbers sab arguments ko tuple me store karta hai.

# Tu jitne chahe numbers pass kare, wo tuple ban jaayega.

# 🔹 2️⃣ **numbers — (kwargs / keyword arguments)

# 👉 Ye use hota hai jab arguments key-value pair ke form me diye jayein.

# 🧠 Explanation:

# **numbers sab arguments ko dictionary me store karta hai.

# Keys = argument name

# Values = argument value

def parameter(**numbers):
    print(type(numbers))
    sum = 0
    for key in numbers:
        sum += numbers[key]   # Access values using key
    print('The avg of the numbers is:', sum / len(numbers))

parameter(a=12, b=13)
