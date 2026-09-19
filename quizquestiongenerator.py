import random

questions = {
    "Python": [
        {
            "question": "Which keyword is used to define a function?",
            "options": ["A. function", "B. def", "C. fun", "D. define"],
            "answer": "B"
        },
        {
            "question": "Which data type is immutable?",
            "options": ["A. List", "B. Set", "C. Dictionary", "D. Tuple"],
            "answer": "D"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["A. //", "B. /*", "C. #", "D. --"],
            "answer": "C"
        },
        {
            "question": "What is the output of len('Python')?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 4"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to handle exceptions?",
            "options": ["A. catch", "B. error", "C. try", "D. exception"],
            "answer": "C"
        }
    ],

    "SQL": [
        {
            "question": "Which command is used to retrieve data?",
            "options": ["A. GET", "B. SELECT", "C. FETCH", "D. SHOW"],
            "answer": "B"
        },
        {
            "question": "Which key uniquely identifies a record?",
            "options": ["A. Foreign Key", "B. Candidate Key", "C. Primary Key", "D. Super Key"],
            "answer": "C"
        },
        {
            "question": "Which command is used to remove a table?",
            "options": ["A. DELETE", "B. REMOVE", "C. DROP", "D. CLEAR"],
            "answer": "C"
        },
        {
            "question": "Which clause is used to filter rows?",
            "options": ["A. WHERE", "B. FILTER", "C. HAVING", "D. ORDER"],
            "answer": "A"
        },
        {
            "question": "Which command adds a new record?",
            "options": ["A. ADD", "B. INSERT", "C. CREATE", "D. UPDATE"],
            "answer": "B"
        }
    ],

    "DSA": [
        {
            "question": "Which data structure follows LIFO?",
            "options": ["A. Queue", "B. Stack", "C. Array", "D. Linked List"],
            "answer": "B"
        },
        {
            "question": "Which data structure follows FIFO?",
            "options": ["A. Stack", "B. Tree", "C. Queue", "D. Graph"],
            "answer": "C"
        },
        {
            "question": "Which search algorithm requires sorted data?",
            "options": ["A. Linear Search", "B. Binary Search", "C. DFS", "D. BFS"],
            "answer": "B"
        },
        {
            "question": "Which data structure uses nodes and pointers?",
            "options": ["A. Array", "B. Linked List", "C. Stack", "D. Queue"],
            "answer": "B"
        },
        {
            "question": "What is the worst-case time complexity of Linear Search?",
            "options": ["A. O(1)", "B. O(log n)", "C. O(n)", "D. O(n²)"],
            "answer": "C"
        }
    ]
}


def display_questions(category):
    selected_questions = random.sample(questions[category], 5)

    score = 0
    correct_answers = []
    wrong_answers = []

    for number, q in enumerate(selected_questions, start=1):

        print("\n" + "=" * 50)
        print(f"Question {number}: {q['question']}")

        for option in q["options"]:
            print(option)

        while True:
            user_answer = input("Your answer (A/B/C/D): ").upper()

            if user_answer in ["A", "B", "C", "D"]:
                break

            print("Invalid answer! Please enter A, B, C or D.")

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
            correct_answers.append(q["question"])
        else:
            print("Incorrect!")
            print("Correct answer:", q["answer"])
            wrong_answers.append(q["question"])

    return score, correct_answers, wrong_answers


def main():

    print("=" * 50)
    print("        SMART QUIZ GENERATOR")
    print("=" * 50)

    name = input("Enter your name: ")

    print("\nChoose a category:")
    print("1. Python")
    print("2. SQL")
    print("3. DSA")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            category = "Python"
            break
        elif choice == "2":
            category = "SQL"
            break
        elif choice == "3":
            category = "DSA"
            break
        else:
            print("Invalid choice! Please select 1, 2 or 3.")

    print(f"\nWelcome {name}!")
    print(f"Category: {category}")
    print("You will get 5 random questions.")

    score, correct, wrong = display_questions(category)

    total = 5
    percentage = (score / total) * 100

    print("\n" + "=" * 50)
    print("              QUIZ RESULT")
    print("=" * 50)

    print("Name:", name)
    print("Category:", category)
    print("Correct Answers:", len(correct))
    print("Wrong Answers:", len(wrong))
    print("Score:", score, "/", total)
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 60:
        print("Good performance!")
    elif percentage >= 40:
        print("Keep practicing!")
    else:
        print("You need more practice.")

    print("\nThank you for taking the quiz!")


main()