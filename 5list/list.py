# 🧠 1️⃣ What is a List in Python?
# 👉 List ek collection hoti hai — jisme tu multiple items store kar sakta hai ek hi variable me.

# Example 👇

# fruits = ["apple", "banana", "cherry"]   
# Ye ek list hai.
# Har item ko comma ( , ) se separate karte hain.
# List square brackets [ ] ke andar likhi jaati hai.

# 🧩 2️⃣ Features of List
# ✅ Ordered → items ka order fix rehta hai (insertion order).
# ✅ Mutable → tu list ke elements ko change kar sakta hai.
# ✅ Allow duplicates → same element multiple times ho sakta hai.
# ✅ Can store different data types → numbers, strings, or mix.

lst =[23,45,32,12,54,54,32,12,67,89,90,"jagjeet","jaiswal",True,False]
print(lst)
print(type(lst))

lst[1]=100
print(lst)


print(lst[-4],lst[-3])



# # # 🔁 7️⃣ Looping through a List
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x=="banana":
#       print(x.upper(), "is my favorite fruit")


# fruit1 =["mango","guava","kiwi"]
# fruit1.extend(fruits)
# print(fruit1)
# # # Output:

# # apple
# # banana
# # cherry

# # 📐 8️⃣ Useful Functions
# numbers = [5, 2, 8, 1]

# print(len(numbers))   # 4
# print(max(numbers))   # 8
# print(min(numbers))   # 1
# print(sum(numbers))   # 16

# # 🔄 9️⃣ Slicing a List
# numbers = [10, 20, 30, 40, 50]
# print(numbers[1:4])   # [20, 30, 40]
# print(numbers[:3])    # [10, 20, 30]
# print(numbers[2:])    # [30, 40, 50]
# print(numbers[::-1])  # [50, 40, 30, 20, 10] (reverse)





# #  practice code 

# num = [1,2,3,4,5,6,7,8,9,10]
# print(sum(num))
# print(len(num))
# print(max(num))

# nums = [23,45,67,89,12,34,56]
# num.extend(nums)
# print (num)
# num.remove(89)
# print(num)
# num.append(100)
# print(num)
# num.insert(-10,101)
# print(num)


# # IN keyword used in the list
# # same thing can be used in string ,tuple ,dictionary also

# name=["zafar",'jaggie','manish','kaira']
# if 'jaggie' in name:
#     print('yes ,jaggie is present in the list')
# else:
#   print('no ,jaggie is not present in the list')