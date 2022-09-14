#Quiz application using python...

from multiprocessing.sharedctypes import Value


quiz = {
    "que1": {
        "question": "1. what is the capital of Banglades",
        "answer": "Dhaka"
    },

    "que2": {
        "question": "2. What is the capital of USA",
        "answer": "W.Dc"
    },

    "que3": {
        "question": "3. What is the capital of Gremany",
        "answer": "Barlin"
    },

    "que4": {
        "question": "4. What is the capital of Spain",
        "answer": "Madrid"
    },

    "que5": {
        "question": "5. What is the capital of France",
        "answer": "Paris"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])

    answer = input("Enter Answer : ")

    if answer.lower() == value["answer"].lower():
        print("Correct")
        score += 1
        print("Your score is :", score)
        print("")
    
    else:
        print("Wrong Answer")
        print("The answer is :", value["answer"])
        print("Your score is :", score)
        print("")

print("You got", score, "out of 5")
print("Your percentage is ", int((score / 5)* 100), "%")