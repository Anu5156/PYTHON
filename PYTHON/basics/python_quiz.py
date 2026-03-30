#Python_quiz
questions = ("What is the capital of India? ",
             "What is 2 + 2? ",
             "What is the capital of USA? ",
             "What is 5 * 6? ")
options= (["1. New Delhi","2. Mumbai","3. Kolkata","4. Chennai"],
            ["1. 2","2. 3","3. 4","4. 5"],
            ["1. New York","2. Washington DC","3. Los Angeles","4. Chicago"],
            ["1. 11","2. 30","3. 28","4. 32"])
answers=[1,3,2,2]
score=0
for q in questions:
    print("-------------------------")
    print(q, end="\n")
    for o in options[questions.index(q)]:
        print(o, end="\n")
    user_answer=int(input("Enter the option number: "))
    if user_answer==answers[questions.index(q)]:
        print("Correct Answer!")
        score+=1
    else:
        print("Wrong Answer!")
    print("-------------------------")
score_percentage = (score / len(questions)) * 100
print(f"\n🎯 Your final score: {score_percentage}%")  
