# Quiz class to initialize the quiz components
class Quiz:
    def __init__(self, question, correct_letter, correct_word, multiple_choice_options):
        self.question = question
        self.correct_letter = correct_letter
        self.correct_word = correct_word
        self.multiple_choice_options = multiple_choice_options

# A list of Quiz Instances storing the questions, answers, and multiple choice options
multiple_choice = [
    Quiz("Who is the family pet?", "A", "Klause", ['A. Klause B. Brian C. Roger D. Mittens']),
    Quiz("Who is Snot obsessed with?", "C", "Haley", ['A. Debbie B. Francine C. Haley D. Lisa Silver']),
    Quiz("Where does Stan work?", "A", "CIA", ['A. CIA B. FBI C. NSA D. KGB']),
    Quiz("Who is Haley's boyfriend?", "D", "Jeff Fisher", ['A. Reginald B. Avery C. Principal Lewis D. Jeff']),
    Quiz("Where did Roger escape?", "B", "Area 51", ['A. The Smith Home B. Area 51 C. Pearl Bailey High School D. Quahog']),
    Quiz("What color is Stan's suit?", "C", "Blue", ['A. Gray B. Blue C. Black D. Burgundy']),
    Quiz("Which character is NOT one of Roger's aliases?", "A", "Stacy Huffman", ['A. Stacy Huffman B. Jeanie Gold C. Ricky Spanish D. Professor Baxter']),
    Quiz("Where does Roger live?", "D", "Attic", ['A. Basement B. Dog House C. Treehouse D. Attic'])
]

print("Good morning USA! \nLet's see how much you know about American Dad")

#Prompts the user to either play or quit the game
while(True):
    start_game_choice = input("Ready to play? \nEnter C to continue or Q to quit: ")
    start_game_choice = start_game_choice.casefold()

    if start_game_choice == "c":
        break
    elif start_game_choice == "q":
        print("Goodbye!")
        exit()
    else:
        print("Invalid Entry")
        continue

def trivia_game(multiple_choice):
    score = 0
 
    # Iterates over the multiple_choice list and takes in the user's inputted answer
    for option in multiple_choice:
        print(option.question) # Displays the question
        print(str(option.multiple_choice_options).strip("]['")) # Displays the 4 possible answers
        user_answer = input("Answer: ")
        if user_answer.casefold() == option.correct_letter.casefold() or user_answer.casefold() == option.correct_word.casefold():
            print("Correct!")
            score += 1
            print(f"Your current score: {score}")
        else:
            print(f"Incorrect. The correct answer is {option.correct_letter}. {option.correct_word}")
            print(f"Your current score: {score}")

    print(f"You scored a total of {score} out of {len(multiple_choice) - 1}")

    # Prompts the user to replay the game
    while(True):
        restart_game_choice = input("Play again? Enter R to replay or Q to quit: ")
        restart_game_choice = restart_game_choice.casefold()

        if restart_game_choice == "r":
            score = 0
            trivia_game(multiple_choice)
            break
        elif restart_game_choice == "q":
            print("Goodbye!")
            exit()
        else:
            print("Invalid Entry")
            continue


trivia_game(multiple_choice)