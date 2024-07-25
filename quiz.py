def new_game():
    answers = []
    correct_answers = 0
    question_number = 0

    for question in questions:
        counter = "A", "B", "C", "D"
        print(f"Question {question_number + 1}: {question}")
        for count in counter:
            print(f"{count}: {options[question_number][count]}")

        answer = input("Enter your answer (A, B, C or D): ").upper()

        while answer not in counter:
            print("Invalid answer! Please enter A, B, C or D")
            answer = input("Enter your answer (A, B, C or D): ").upper()

        check_answer(answer, question)

        answers.append(answer)
        question_number += 1

def get_scores():
    pass


def check_answer(answer, question):
    if answer == questions[question]:
        print("Correct!")
        
    else:
        print("Wrong!")

def play_again():
    pass


questions = {
    "Who is the president of the United States?": "A",
    "What is the capital of Nigeria?": "B",
    "Why did the chicken cross the road?": "A",
    "Who sang the song 'Lonely at the top'?": "A",
    "Who is the GOAT of football?": "Christiano A",
    "When was the first episode of spongebob aired?": "B",
    "Who main director of Ratouille?": "D",
}

options = [
    {
        "A": "Joe Biden",
        "B": "Donald Trump",
        "C": "Barack Obama",
        "D": "George Bush",
    },
    {
        "A": "Lagos",
        "B": "Abuja",
        "C": "Kano",
        "D": "Port Harcourt",
    },
    {
        "A": "To get to the other side",
        "B": "To meet the other chicken",
        "C": "To find food",
        "D": "To find shelter",
    },
    {
        "A": "Asake",
        "B": "Davido",
        "C": "Wizkid",
        "D": "Burna Boy",
    },
    {
        "A": "Christiano Ronaldo",
        "B": "Lionel Messi",
        "C": "Neymar",
        "D": "Mbappe",
    },
    {
        "A": "2000",
        "B": "1999",
        "C": "2001",
        "D": "2002",
    },
    {
        "A": "Angelina Jolie",
        "B": "Tom Cruise",
        "C": "Will Smith",
        "D": "Brad Bird",
    },
]

new_game()
