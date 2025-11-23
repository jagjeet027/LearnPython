
print("Welcome to Kaun Banega Crorepati!")
print("Answer the following questions to win money.")
# i am taking list to store multiple items in a single variable
questions=[
    "What is the capital of India?\n a) Mumbai \n b) Chennai \n c) New Delhi \n d) Kolkata\n",
    "Who is the Prime Minister of India?\n a) Narendra Modi \n b) Rahul Gandhi \n c) Amit Shah \n d) Arvind Kejriwal\n",
    "What is the currency of India?\n a) Dollar \n b) Euro \n c) Pound \n d) Indian Rupee\n",
    "Which is the largest state in India?\n a) Maharashtra \n b) Rajasthan \n c) Madhya Pradesh \n d) Uttar Pradesh\n"
]
options=['c','a','d','b']
answers=[2000,5000,10000,50000]

score=0
for i in range(len(questions)):
    print(questions[i])
    user_answer=input("Enter your answer (a/b/c/d): ")
    if user_answer.lower()==options[i]:
        print("Correct answer!")
        score+=answers[i]
    else:
        print("Wrong answer!")
    print(f"Your current score is: {score}\n")
print(f"Your total score is: {score}")

if score>=20000:
    print("Congratulations! You are a Crorepati!")
else:
    print("Better luck next time!")

