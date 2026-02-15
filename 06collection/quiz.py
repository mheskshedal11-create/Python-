questions = (
    'How many elements are in the periodic table?:',
    'Which animal lays the largest eggs?:',
    "What is the most abundant gas in Earth's atmosphere?:",
    'How many bones are in the human body?:'
)

options = (
    ('A. 116', 'B. 177', 'C. 118', 'D. 158'),
    ('A. Whale', 'B. Crocodile', 'C. Elephant', 'D. Ostrich'),
    ('A. Nitrogen', 'B. Oxygen', 'C. Carbon dioxide', 'D. Hydrogen'),
    ('A. 206', 'B. 207', 'C. 208', 'D. 209')
)

answers = ('D', 'D', 'A', 'A')

guesses = []
score = 0
question_num = 0

for question in questions:
    print('---------------------------------')
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input('Enter (A,B,C,D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT')
        print(f'{answers[question_num]} is the correct answer')
    question_num += 1

print('-----------------------------------------')
print('   Result          ')
print('-----------------------------------------')

# Print answers and guesses
print('Answers:', end=' ')
for ans in answers:
    print(ans, end=' ')
print()

print('Guesses:', end=' ')
for gus in guesses:
    print(gus, end=' ')
print()

# Calculate percentage score
score_percentage = int(score / len(questions) * 100)
print(f'Your score is {score_percentage}%')
