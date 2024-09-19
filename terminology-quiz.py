import random
import json

print("Welcome to AWS re/Start Terminology quiz")

player = input("Do you want to play? (yes/no) ")

if player.lower() != "yes":
    quit()

print("Okay! Let's play :)")

with open("quiz_json.json") as file_object:
    data = json.load(file_object)

quiz_questions = data["quiz_questions"]


random.shuffle(quiz_questions)
selected_questions = quiz_questions[:5]

score = 0

for element in selected_questions:
    question = element["question"]
    correct_answer = element["answer"].lower()

    answer = input(element["question"] + " ")

    if answer.lower() == correct_answer:
        print("Correct answer! :)")
        score += 1
    else:
        print(f"Incorrect!!! The correct answer is {correct_answer} :(")

print("You got " + str(score) + " questions correct! :)")
print("Your Score is " + str((score / 5) * 100) + "%.")
