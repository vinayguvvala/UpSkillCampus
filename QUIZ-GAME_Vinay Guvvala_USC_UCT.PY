import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()
# Create the "questions" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        answer TEXT
    )
''')

# Insert questions into the table
question_data = [
    ('What is the capital of France?', 'Paris', 'Rome', 'Berlin', 'Madrid', 'A'),
    ('Which planet is known as the Red Planet?', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'B'),
    ('Who painted the Mona Lisa?', 'Leonardo da Vinci', 'Pablo Picasso', 'Vincent van Gogh', 'Michelangelo', 'A'),
    ('What is the chemical symbol for gold?', 'Ag', 'Fe', 'Au', 'Hg', 'C'),
    ('Which country is home to the kangaroo?', 'Australia', 'Canada', 'Brazil', 'South Africa', 'A'),
    ('Who wrote the play "Romeo and Juliet"?', 'William Shakespeare', 'George Orwell', 'Jane Austen', 'Charles Dickens', 'A'),
    ('What is the largest ocean in the world?', 'Atlantic Ocean', 'Arctic Ocean', 'Indian Ocean', 'Pacific Ocean', 'D'),
    ('In which year did World War II end?', '1939', '1945', '1942', '1950', 'B'),
    ('What is the tallest mountain in the world?', 'Kilimanjaro', 'Everest', 'K2', 'Matterhorn', 'B'),
    ('Who is the CEO of Tesla?', 'Bill Gates', 'Elon Musk', 'Jeff Bezos', 'Mark Zuckerberg', 'B'),
    ('What is the capital of Andhra Pradesh?','Amaravathi','Vizag','Kurnool','All the above','D')
]
# Insert the questions into the table
cursor.executemany('''
    INSERT INTO questions (question, option_a, option_b, option_c, option_d, answer)
    VALUES (?, ?, ?, ?, ?, ?)
''', question_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

import sqlite3
import random

# Connect to the SQLite database
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

def retrieve_question():
    # Retrieve a random question from the database
    cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 1")
    question = cursor.fetchone()
    return question

def display_question(question):
    # Display the question and options
    print(question[1])  # Assuming the question is stored in the second column
    print("A. " + question[2])  # Assuming options are stored in the third to sixth columns
    print("B. " + question[3])
    print("C. " + question[4])
    print("D. " + question[5])

def check_answer(question, user_answer):
    # Compare the user's answer with the correct answer
    if user_answer.upper() == question[6]:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        print("The correct answer is:", question[6])
        return False

def play_game():
    score = 0
    num_questions = 5  # Number of questions to be asked

    for _ in range(num_questions):
        question = retrieve_question()
        display_question(question)
        user_answer = input("Your answer (A/B/C/D): ")
        if check_answer(question, user_answer):
            score += 1
        print()  # Empty line for readability

    print("Game Over!")
    print("Your final score is:", score)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing!")

# Start the game
play_game()
# Close the database connection
conn.close()