# ✅ Tuple ke Main Methods


# if you want to manipulate the data in tuple then you have to convert it into list and then after manipulation convert it back to tuple because tuple is immutable.

countries = ('India', 'USA', 'UK', 'Germany', 'Canada')
print(countries)
print(type(countries))

temp = list(countries)  # tuple to list
temp.append('France')   # manipulating the list
countries = tuple(temp)  # list to tuple
print(countries)


# 1️⃣ count()
# Use: Kis value ka tuple me kitni baar aana hua hai, ye batata hai.
t = (1, 25, 3, 2, 4, 2, 5, 2, 6)
print(t.count(2))    # Output: 3
print("finding index between the range of 1 to 6 is: ",t.index(2,1,6))
print("lenght of the tuple is :",len(t))

# Explanation:
# 👉 2 tuple me 3 baar aya hai, isliye output 3.

# 2️⃣ index()
# Use: Kis element ka first index (position) kya hai, ye return karta hai.
t = (10, 20, 30, 20, 40)
print("index of t is : ", t.index(20))   # Output: 1

# Explanation:
# 👉 Pehla 20 index 1 pe hai (yaani 2nd position pe).
# Note:
# Agar element nahi mila → error aayega.
# print(t.index(50))   # ❌ ValueError: tuple.index(x): x not in tuple


# 🧩 Bas ye hi 2 methods officially hote hain 😅
# Tuple immutable hai, isliye:


# append(), remove(), pop()


# extend(), insert(), etc.
# ye sab list ke methods hain, tuple ke nahi.



# 🔍 But tuple ke saath ye built-in functions kaam karte hain:
# Ye methods nahi hain, par tuple ke liye useful functions hain 👇
# t = (5, 10, 15, 20, 25)

# FunctionDescriptionExampleOutputlen()elements ki total sankhyalen(t)5max()sabse bada elementmax(t)25min()sabse chhota elementmin(t)5sum()sab elements ka total (agar numeric ho)sum(t)75

# ⚙️ Bonus Trick: Convert list to tuple and vice versa
# Kabhi tuple me update karna ho to:
# t = (1, 2, 3)
# temp = list(t)   # tuple → list
# temp.append(4)
# t = tuple(temp)  # list → tuple
# print(t)         # (1, 2, 3, 4)


# 💬 Summary:
#                      Method                                       Description
#            count(value)                                  Counts how many times a value appears
#            index(value)                                  Returns the first index of the given value
