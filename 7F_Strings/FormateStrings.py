# letter="i am {} and i love {}"  
# name="jagjeet jaiswal"
# passion="coding"

# print(letter.format(name,passion))  

# uper ke code mai ek problem aa skta hai ki agar humne format mai values ka order change kr diya to output galat aaega is problem ko solve krne ke liye hum named placeholders ka use kr skte hai jaise ki niche diya gaya hai ya indexed placeholders ka use kr skte hai

# letter="i am {n} and i love {p}"  
# passion="coding"
# name="jagjeet jaiswal"

# print(letter.format(n=name,p=passion))

# indexed placeholders ka use krne ke liye hum niche diye gaye code ko dekh skte hai
# letter="i am {0} and i love {1}"
# name="jagjeet jaiswal"
# passion="coding"
# print(letter.format(name,passion))

# agr hamare pass agr multiple varibales ho to hum confuse ho skte hai ki konsa variable kaha place hoga is problem ko solve krne ke liye hum f-strings ka use kr skte hai jaise ki niche diya gaya hai aur multiple varibles ka index dena easy ni hota hai... uske liye f-strings ka use krna best hota hai

name="jagjeet jaiswal"
passion="coding"
address="india"

print(f"i am {name} and i am interested in {passion} and i live in {address}")

# if you want to print the curly braces {} in f-strings then you have to use double curly braces {{}} like below
print(f"this is how to print curly braces {{}} in f-strings")