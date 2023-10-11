Quiz = {
    "question1": {
        "question": "Best footballer in the world",
        "answer": "Ronaldo"
    },
    "question2": {
        "question": "Most Golden Boot Winner",
        "answer": "Messi"
    },
    "question3": {
        "question": "Most Golden Ball Winner",
        "answer": "Messi"
    },
    "question4": {
        "question":"Most World Cup Winner",
        "answer":"Brazil"
    },
    "question5": {
        "question":"Most UCL winner",
        "answer":"Real Madrid"
    }
}

score = 0

for key, value in Quiz.items():
    print(value['question'])
    answer = input("answer? ")

    if answer.lower() == value['answer'].lower():
        print('correct')
        score = score + 1
        print("Your score is : " + str(score))
    
    else:
        print("wrong!")
        print("The answer is : " + value['answer'])
        print("Your Score is " + str(score))
        print("")
        print("")

print("You Got" + str(score) + " out of 5 question corrently")
print("Your percentage is " + str(int(score/7 * 100)) + "%")