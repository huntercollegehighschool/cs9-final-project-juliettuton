"""
Name(s): Juliet Tuton
Name of Project: Hangman
"""
#random library used to pick a word at random
import random
#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

#create a list to store possible words
possible_words = 'math', 'school', 'science', 'history', 'english', 'music', 'french', 'spanish', 'pencil', 'paper'
#pick a random number
num = random.randint(0,9)
won = 1
#print statement are here so we can see whats going on
#choosew a random word

choice = possible_words[num]
#shows the length of that word


#create an empty list called letters_guessed
letters_guessed = []

attempts = 6

progress = []
#this for loop appends 0 to an empty list for each letter in the word choosen
for letter in range(len(choice)):
  progress.append(0)
print(progress)

print("ready to play hangman?")
while(attempts > 0):
  print("you have", attempts, "guesses")
  guess = input("guess a letter: ")
  letters_guessed.append(guess)
  #this will hold either nothing or a list index(s) were the guess was positioned in the word choosen
  correct_positions = []
  #this for loop checks each letter in the word choosen and if it matches guess adds its position to correct_positions
  for index in range(len(choice)):
    if guess == choice[index]:
      correct_positions.append(index)
  if len(correct_positions) == 0:
    print("sorry no luck!")
    attempts = attempts - 1
  else:
    print("good job!")

  for num in correct_positions:
    progress[num] = guess
  
  print(progress)
  print(letters_guessed)
  won = 1
  for item in progress:
    if item == 0:
     won = 0

  if won == 1:
    print("you win the word was", choice)
    attempts = 0

  if attempts < 1:
    print("sorry, you lose. the word was", choice)