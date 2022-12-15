import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Prompt the user to guess the number
print('Guess the number between 1 and 100:')
guess = int(input())

# Initialize the number of guesses
num_guesses = 1

# Keep prompting the user until they guess the number
while guess != number:
    if guess > number:
        print('Too high, try again:')
    else:
        print('Too low, try again:')
    guess = int(input())
    num_guesses += 1

# Display a message when the user guesses the number
print('Congratulations, you guessed the number in', num_guesses, 'guesses!')

# Calculate the score based on the number of guesses
score = 100 - num_guesses
if score < 0:
    score = 0
print('Your score is', score)

# Prompt the user to enter their name
print('Enter your name:')
name = input()

# Update the leaderboard with the user's score
leaderboard = []
with open('leaderboard.txt', 'r') as file:
    for line in file:
        name, score = line.strip().split()
        leaderboard.append((name, int(score)))
leaderboard.append((name, score))
leaderboard.sort(key=lambda x: x[1], reverse=True)

# Save the updated leaderboard to the file
with open('leaderboard.txt', 'w') as file:
    for entry in leaderboard:
        file.write(entry[0] + ' ' + str(entry[1]) + '\n')

# Display the leaderboard
print('\nLeaderboard:')
for i, entry in enumerate(leaderboard):
    print(i+1, entry[0], entry[1])
#AbhayChaudhary