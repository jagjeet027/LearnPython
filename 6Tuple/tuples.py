# 🧠 What is a Tuple?
# Tuple ek collection data type hai Python me,
# jo list jaisa dikhta hai, par ek main difference hota hai —
# 👉 tuple immutable hota hai, matlab ek baar ban gaya to badla nahi ja sakta.

# 🧩 Example:
# numbers = (10, 20, 30, 40)

# Ye ek tuple hai
# Parentheses () me likhte hain
# Indexing list jaise hi hoti hai (start = 0)

# 🔍 Deep Concept — Immutability
# List me tu kuch bhi change kar sakta hai, par tuple me nahi.
# Jaise:
# numbers = (1, 2, 3)
# numbers[1] = 5   # ❌ Error — tuple object does not support item assignment

# Why immutability matters:
# Tu tuple ko accidentally modify nahi kar sakta (safe for data integrity)
# Isliye tuple hashable hota hai — yani use dictionary ke key ya set ke element ke roop me rakh sakta hai.
# List ko kabhi set/dictionary key me use nahi kar sakte, par tuple ko kar sakte ho ✅

# 🧩 Tuple vs List (internal concept)
# List stored as a dynamic array in emory — extend ho sakti hai.
# Tuple fixed memory block hota hai — isliye faster aur more memory-efficient hota hai.
# Matlab agar data change nahi hona,
# tuple use karne se Python ko internally pata hota hai ki ye fixed hai —
# optimization kar leta hai (execution thoda faster hota hai). ⚡

