import requests

difficulty = int(input("Choose the difficulty of your game (1,2,or 3): "))

def generateWord():
    resonse = "3"
    if difficulty == 1:
        response = requests.get("https://random-word-api.herokuapp.com/word?length=5")
    elif difficulty == 2:
        response = requests.get("https://random-word-api.herokuapp.com/word?length=7")
    elif difficulty == 3:
        response = requests.get("https://random-word-api.herokuapp.com/word?length=10")
    randomWord = response.json()[0]
    return randomWord

word = generateWord()
wordlist = []

def playGame():
    mistakes = 5
    for index, char in enumerate(word):
        # print("_ ", end ="")
        wordlist.append(" _ ")
        print(wordlist[index],end="")
    print("")
    while mistakes > 0 and " _ " in wordlist: 
        guess = input("Guess a letter: ")
        mistakes = letterCheck(guess, mistakes)
    if mistakes == 0:
        print("Sorry! The word was " + word + ".")
    elif " _ " not in wordlist:
        print("Congratulations! The word was " + word + ".")  
        

def letterCheck(letter, mistakes):
    inword = False
    for index, char in enumerate(word):
        if char == letter:
            wordlist[index] ="" + letter + ""
            inword = True
        print(wordlist[index],end="")
    print("")
    if inword == False:
        mistakes -= 1
        print("That letter is not in the word. You have " + str(mistakes) + " mistakes left.")
    return mistakes

playGame()