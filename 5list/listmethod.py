# 🔢 3️⃣ Accessing Elements

# Tu index ke through element access karta hai
# (index 0 se start hota hai 👇)

# numbers = [10, 20, 30, 40]
# print(numbers[0])  # Output: 10
# print(numbers[3])  # Output: 40


# Negative index bhi use kar sakta hai:

# print(numbers[-1])  # Output: 40 (last element)
# print(numbers[-2])  # Output: 30

# ✏️ 4️⃣ Changing (Modifying) Elements

# List mutable hoti hai — tu element update kar sakta hai.

# numbers = [10, 20, 30]
# numbers[1] = 25
# print(numbers)  # Output: [10, 25, 30]

# # ➕ 5️⃣ Adding Items

# # There are 3 ways:

# # 1. append() – adds at the end
# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)  # [1, 2, 3, 4]

# # 2. insert() – adds at specific index
# numbers.insert(1, 10)
# print(numbers)  # [1, 10, 2, 3, 4]

# # 3. extend() – add another list
# numbers.extend([5, 6])
# print(numbers)  # [1, 10, 2, 3, 4, 5, 6]

# # ❌ 6️⃣ Removing Items
# # 1. remove() – remove by value
# numbers.remove(10)
# print (numbers)

# # 2. pop() – remove by index (default last)
# numbers.pop(2)
# print(numbers)  # [1, 10, 3, 4, 5, 6]

# # 3. del – delete by index or whole list
# del numbers[0]
# print(numbers)  # [10, 3, 4, 5, 6]
# # 4. clear() – empty the list
# numbers.clear()

# print(numbers)  # Output: []


# Sorting a list in ascending and descending order

lst =[1,7,2,8,90,34,65,45,8,3]
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# # Reversing a list
# lst.reverse()
# print(lst)

# finding index of an element
index_of_90=lst.index(90)
print(index_of_90)

# counting occurrences of an element
count_of_8=lst.count(8) 
print(count_of_8)