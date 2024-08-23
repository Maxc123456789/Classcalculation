import random

def ask_name():
    name = input("What is your name? ")
    print(f"Welcome, {name}!")
    return name

def ask_age():
    age = int(input("What is your age? "))
    if 3 <= age <= 5:
        return age
    else:
        print("The age should be within the range of 3-5.")
        return ask_age()


def pick_operation():
    print("Pick an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter the number of your choice: "))
    if choice not in [1, 2, 3, 4]:
        print("Please pick a valid option.")
        return pick_operation()
    if choice == 1:
        return "Addition"
    elif choice == 2:
        return "Subtraction"
    elif choice == 3:
        return "Multiplication"
    else:
        return "/"

def generate_questions(operation, num_questions):
    questions = []
    for _ in range(num_questions):
        num1 = random.randint(1, 5)
        num2 = random.randint(1, 5)
        if operation == "Addition":
            correct_answer = num1 + num2
        elif operation == "Subtraction":
            correct_answer = num1 - num2
        elif operation == "Multiplication":
            correct_answer = num1 * num2
        else:
            correct_answer = round(num1 / num2)
        questions.append((num1, num2, operation, correct_answer))
    return questions

def ask_questions(name, questions):
    score = 0
    for num1, num2, operation, correct_answer in questions:
        user_answer = float(input(f"What is {num1} {operation} {num2}? "))
        if user_answer == correct_answer:
            print(f"You are correct, {name}!")
            score += 1
        else:
            print(f"Sorry, you are wrong. The correct answer is {correct_answer}")
    return score

def calculate_percentage(score, total_questions):
    percentage = (score / total_questions) * 100
    return percentage

def play_game():
    name = ask_name()
    age = ask_age()
    operation = pick_operation()
    questions = generate_questions(operation, 5)
    score = ask_questions(name, questions)
    percentage = calculate_percentage(score, 5)
    print(f"Your total score is {score} out of 10.")
    print(f"Your score percentage is {percentage}%.")

if __name__ == "__main__":
    play_game()