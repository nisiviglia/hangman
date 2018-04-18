'''
Nick Siviglia
CS100
6/25/2016
'''
from random import randint

def printBoard(incorrect):
    step0 = '''
   _____
  |     
  |
  |
  |
  |
  |
__|_______
'''


    step1 = '''
   _____
  |     |
  |
  |
  |
  |
  |
__|_______
'''

    step2 = '''
   _____
  |     |
  |     O
  |
  |
  |
  |
__|_______
'''

    step3 = '''
   _____
  |     |
  |     O
  |     |
  |
  |
  |
__|_______
'''

    step4 = '''
   _____
  |     |
  |     O
  |     |/
  |
  |
  |
__|_______
'''
    step5 = '''
   _____
  |     |
  |     O
  |    \|/
  |
  |
  |
__|_______
'''
    step6 = '''
   _____
  |     |
  |     O
  |    \|/
  |     |
  |
  |
__|_______
'''
    step7 = '''
   _____
  |     |
  |     O
  |    \|/
  |     |
  |    /
  |
__|_______
'''
    step8 = '''
   _____
  |     |
  |     O
  |    \|/
  |     |
  |    / \\
  |
__|_______
'''
    boards = [step0, step1, step2, step3, step4, step5, step6, step7, step8]
    return boards[len(incorrect)]

def printIncorrectGuessed(incorrect):

  #setup for no incorrect guesses (new game)   
  if len(incorrect) == 0:
    print('|_guessed_letters_|')
    return

  #sandwitch incorrect guesses between bars
  print('|', end='')
  for letter in incorrect:
    if letter == incorrect[0]:
      print(letter, end='')
    else:
      print(',', letter, end='')
  print('|', end='\n')

def printCorrectGuess(correct):
  #show 'correct' with initialized ?'s and guessed letters
  #with spaces btwn them
  print('---'*len(correct))
  for letter in correct:
    print(letter, ' ', end='')
  print(end='\n')


def getRandomWord(length):
  #Load dictionry file and pick random length+ letter word
  dictionaryFile = open('dictionary.txt', 'r')
  wordList = dictionaryFile.read().lower().split()

  while True:
      randomWord = wordList[randint(0, len(wordList))]
      if len(randomWord) >= length:
        break

  dictionaryFile.close()
  return randomWord

################################
#-- MAIN PROGRAM STARTS HERE --#
################################

#get random word of atleast length 5
wordLength = 5
randomWord = getRandomWord(wordLength)

#initilize markers, fill 'correct' with ?'s equal to length of our word
correct = '?' * len(randomWord)
incorrect = ''

#start playing game
while True:

  #update the visuals
  print(printBoard(incorrect), end='')
  printIncorrectGuessed(incorrect)
  printCorrectGuess(correct)

  #check for win or loss
  if correct == randomWord:
    print("---WINNER---")
    break
  if len(incorrect) >= 8:
    printCorrectGuess(randomWord)
    print("---Sorry, play again---")
    break

  #get valid input
  while True:
    currentGuess = input('Input letter: ').lower()
    if currentGuess.isalpha() and len(currentGuess) == 1:
      break
    #hints
    if currentGuess == 'hint':
      while True:
        num = randint(0, len(randomWord)-1)
        if correct[num] == '?':
          currentGuess = randomWord[num]
          break
      break
    #new game
    if currentGuess == 'restart':
      #reset everything
      randomWord = getRandomWord(wordLength)
      correct = '?' * len(randomWord)
      incorrect = ''
      currentGuess = ''
      break

  #check input against randomWord and update markers
  for i in range(len(randomWord)):
    if randomWord[i] == currentGuess:
      #if correct change corresponding '?' with letter
      correct = correct[0:i] + currentGuess + correct[i+1:]
  if currentGuess not in randomWord and currentGuess not in incorrect:
    incorrect += currentGuess

#QUESTIONS
'''
-How could the program be modified to make it more difficult(without altering printboard())?

A simple way would be to increase the minimum length requirenment for
the random word to 8. that can be done by changing wordLength at
the beginning of the program.

wordLength = 8

'''

'''
-How could you modify your program to give the user hints?

Id just add some code to the "get valid input" section like so.

#get valid input
  while True:
    currentGuess = input('Input letter: ').lower()
    if currentGuess.isalpha() and len(currentGuess) == 1 and currentGuess not in incorrect:
      break
    #hints
    if currentGuess == 'hint':
      while True:
        num = randint(0, len(randomWord)-1)
        if correct[num] == '?':
          currentGuess = randomWord[num]
          break
      break


'''

'''
-How could you modify it so that the user can immediately play another game if they want?

In the "get valid input" section i can just look for the user to enter
"restart" and reset all the variables like so.

#new game
    if currentGuess == 'restart':
      #reset everything
      randomWord = getRandomWord(5)
      correct = '?' * len(randomWord)
      incorrect = ''
      currentGuess = ''
      break
'''
