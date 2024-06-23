# Bran Odom
# April 16, 2024
# This game will allow the user to choose from 4 mini games to play.

from time import sleep
from random import randint


#Return: 1 int for selection
#Parameters: None
#Purpose: To display a menu and get the user's selection.
def GameMenu():
    #Declare and intialize variables.
    selection = 0

    while selection != 1 and selection != 2 and selection != 3:
        try:
            #Display menu.
            print("1) See Rules\n2) Play Game\n3) Return to Main Menu\n")
            #Prompt for choice.
            selection = int(input("Please choose from the menu: "))
            if selection != 1 and selection != 2 and selection != 3:
                print("\nPlease enter only 1, 2, or 3\n")
                
        except ValueError:
            print("\nPlease enter a number only.\n")
    

    #Return selection.
    return selection

def sideOne():
    print(" ___________")
    print("|           |")
    print("|    ---    |")
    print("|   |   |   |")
    print("|    ---    |")
    print("|___________|")


def sideTwo():
    print(" ___________")
    print("|       _   |")
    print("|      |_|  |")
    print("|   _       |")
    print("|  |_|      |")
    print("|___________|")

    
def sideThree():
    print(" ___________")
    print("|        _  |")
    print("|     _ |_| |")
    print("|  _ |_|    |")
    print("| |_|       |")
    print("|___________|")


def sideFour():
    print(" ___________")
    print("|  _    _   |")
    print("| |_|  |_|  |")
    print("|  _    _   |")
    print("| |_|  |_|  |")
    print("|___________|")


def sideFive():
    print(" ___________")
    print("|  _     _  |")
    print("| |_| _ |_| |")
    print("|  _ |_| _  |")
    print("| |_|   |_| |")
    print("|___________|")


def sideSix():
    print(" ___________")
    print("|  _    _   |")
    print("| |_|  |_|  |")
    print("|  _    _   |")
    print("| |_|  |_|  |")
    print("|  _    _   |")
    print("| |_|  |_|  |")
    print("|___________|")



#Return: 1 int for dice roll.
#Parameters: None
#Purpose: Generate a random number 1 - 6 and display a dice roll.
def DiceRoll():
    #Declare and initialize variables.
    dice_num = 0
    
    #Generate a random number.
    dice_num = randint(1,6)    #3
    
    #Display the dice picture.
    if dice_num == 1:
        sideOne()
    elif dice_num == 2:
        sideTwo()
    elif dice_num == 3:
        sideThree()
    elif dice_num == 4:
        sideFour()
    elif dice_num == 5:
        sideFive()
    elif dice_num == 6:
        sideSix()
        
    #Return dice number.
    return dice_num    #3


#Return: None
#Parameters: None
#Purpose: Game that asks the user to guess a dice roll total.
def GuessTheRoll():
    #Create a constant to store 5 rounds.
    ROUNDS = 5
    #Declare and initialize variables.
    menu_select = user_guess = dice1 = dice2 = dice_sum = user_score = cpu_score = 0
    
    #Display title.
    print("\n\nWelcome to my Guess the Dice game!\n")
    sleep(1)
    print("             GUESS\n")
    sleep(1)
    print("              THE\n")
    sleep(1)
    print("              SUM\n")
    sleep(1)


    while menu_select != 3:
        
        #Display menu and prompt for choice.
        menu_select = GameMenu()

        #If user picked 1, display rules.
        if menu_select == 1:
            print(f"\n{'*'*40}\n")
            print("Roll 2 dice and try to guess the total.\nIf you guess correctly, you get 1 point.\nIf you're wrong, the CPU gets 1 point.\n\nGood luck!")
            print(f"\n{'*'*40}\n")
        #If user picked 2, play game.
        elif menu_select == 2:
            #Reset scores.
            user_score = cpu_score = 0
            #Loop game 5 times.
            for i in range(ROUNDS):
                #Reset user_guess to seed loop.
                
                user_guess = 0
                #Display round #.
                print(f"{'*'*40}")
                print(f"Round {i+1} of {ROUNDS}.")
                print(f"{'*'*40}")
                
                #Prompt user for guess of sum of 2 dice.
                while user_guess < 2 or user_guess > 12:
                    try:
                        user_guess = int(input("\nGuess a sum of the two dice (2 - 12): "))
                        if user_guess < 2 or user_guess > 12:
                            print("\nYou must enter a number 2 - 12. Please try again.")
                    except:
                        print("\nPlease enter a numerical value 2 - 12.")
                
                #Roll/display dice.
                sleep(1)
                print("\nHere comes the first roll...")
                sleep(.5)
                dice1 = DiceRoll()
                print("\nHere comes the second roll...")
                sleep(.5)
                dice2 = DiceRoll()
                
                #Sum dice.
                dice_sum = dice1 + dice2
                print(f"\nThe roll totaled {dice_sum}.")
                
                #If user is correct, give 1 point.
                if user_guess == dice_sum:
                    print(f"\nYour guess was {user_guess}. You were right!")
                    user_score += 1
                #If user is wrong, computer gets 1 point.
                else:
                    print(f"\nYour guess was {user_guess}. Try again!")
                    cpu_score += 1

                print(f"\nCurrent score: \nPlayer: {user_score}\nComputer: {cpu_score}\n\n")

            if user_score > cpu_score:
                print(f"All {ROUNDS} rounds are finished. The Player has won!")
            else:
                print(f"All {ROUNDS} rounds are finished. The CPU has won!")
                  
        #If user picked 3, exit back to main menu.
        else:
            print("\nThanks for playing the Guess The Sum game!")


#Return: None
#Parameters: 1 string for name.
#Purpose: This game lets the player and computer draw a card - high card wins.
def HighCardWins(name):
    #Create cards
    ACE = "*- - -*\n| ♣   |\n|  A  |\n|   ♣ |\n*- - -*"
    KING = """ *- - -*
 | ♣   |
 |  K  |
 |   ♣ |
 *- - -*"""
    QUEEN = """ *- - -*
 | ♣   |
 |  Q  |
 |   ♣ |
 *- - -*"""
    JACK = """ *- - -*
 | ♣   |
 |  J  |
 |   ♣ |
 *- - -*"""
    TEN = """ *- - -*
 | ♣   |
 |  10 |
 |   ♣ |
 *- - -*"""
    NINE = """ *- - -*
 | ♣   |
 |  9  |
 |   ♣ |
 *- - -*"""
    EIGHT = """ *- - -*
 | ♣   |
 |  8  |
 |   ♣ |
 *- - -*"""
    SEVEN = """ *- - -*
 | ♣   |
 |  7  |
 |   ♣ |
 *- - -*"""
    SIX = """ *- - -*
 | ♣   |
 |  6  |
 |   ♣ |
 *- - -*"""
    FIVE = """ *- - -*
 | ♣   |
 |  5  |
 |   ♣ |
 *- - -*"""
    FOUR = """ *- - -*
 | ♣   |
 |  4  |
 |   ♣ |
 *- - -*"""
    THREE = """ *- - -*
 | ♣   |
 |  3  |
 |   ♣ |
 *- - -*"""
    TWO = """ *- - -*
 | ♣   |
 |  2  |
 |   ♣ |
 *- - -*"""

    #Create a list to store the cards
    cardList = [TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE,TEN,JACK,QUEEN,KING,ACE]

    #Declare and initialize variables.
    winner = ""
    menu_select = user_card = cpu_card = user_score = cpu_score = round_num = 0
    
    #Display title.
    print("\n\nWelcome to High Card Wins!\n")
    sleep(1)
    print("             HIGH\n")
    sleep(1)
    print("             CARD\n")
    sleep(1)
    print("             WINS\n")
    sleep(1)

    
        #Display menu.
    while menu_select != 3:
        menu_select = GameMenu()
        
        #If user picked 1, display rules.
        if menu_select == 1:
            print(f"\n{'*'*40}\n")
            print("The user draws a card\nThen the computer draws a card\nHighest card wins!")
            print(f"\n{'*'*40}\n")
            
        #If user picked 2, play game.
        elif menu_select == 2:
            #Reset scores and round number.
            user_score = cpu_score = round_num = 0
            #Loop the game until someone gets 5 points.
            while user_score < 5 and cpu_score < 5:
                round_num += 1
                #Display round number.
                print()
                print(f"Round {round_num}".center(40, '♣'))
                input(f"\nOkay {name}, press Enter to draw a card: ")
                sleep(.5)
                #Generate a random card for the player.
                user_card = randint(2,14)   #2
                #Generate a random card for the CPU.
                cpu_card = randint(2,14)    
                #Display player card.
                print(f"\nPlayer card is \n{cardList[user_card - 2]}")
                sleep(.5)
                #Display CPU card.
                print("\nNow it's the computer's turn...")
                sleep(.5)
                print(f"\nCPU card is \n{cardList[cpu_card - 2]}")
                sleep(.5)
                #If user card is higher, user gets 1 point.
                #If CPU card is higher, CPU gets 1 point.
                #Display round winner.
                if user_card > cpu_card:
                    user_score += 1
                    print(f"\nNice job! The winner of round {round_num} is {name}.")
                elif cpu_card > user_card:
                    cpu_score += 1
                    print(f"\nOof! The CPU wins round {round_num}.")
                else:
                    print(f"\nRound {round_num} is a tie...Nobody gets a point!")
                #Display score.
                print(f"\n{'*'*40}")
                print(f"ROUND {round_num} SCORE".center(40))
                print(f"{name}: {user_score}\nCPU: {cpu_score}")
                print(f"\n{'*'*40}")
                
                
            #Display game winner.
            sleep(1)
            if user_score == 5:
                print(f"Game over! The winner is {name}.")
            elif cpu_score == 5:
                print(f"Game over! The CPU has won.")

                
            
        #If user picked 3, exit back to main menu.
        else:
            print("\nThanks for playing!\n")

#Return: none
#Parameters: 1 string for name
#Purpose: This game will ask questions and award points or take them away
def TriviaGame(playerName):
    #Declare and initialize variables.
    category = question_ans = ""
    menu_select = score = 0
    
    Animals = [
        ["What is the state animal of Florida?",["Panther","Iguana","Alligator","Zebra"],"A"],
        ["Which animal has the ability to change colors to match its surroundings?",["Panda","Koala","Chameleon","Cheetah"],"C"],
        ["What do pandas primarily eat?",["Fish","Bamboo","Insects","Small Mammals"],"B"],
        ["What is the only mammal capable of sustained flight?",["Bat","Flying Squirrel","Pigeon","Hummingbird"],"A"],
        ["What is the largest mammal on Earth?",["African Elephant","Giraffe","Hippopotamus","Blue Whale"],"D"]
        ]

    Music = [
        ['Who is nicknamed the "King of Pop"?',["Elvis Presley","Madonna","Michael Jackson","Prince"],"C"],
        ["Which of these is not a strings instrument?",["Violin","Viola","Cello","Trumpet"],"D"],
        ["What is the smallest musical interval used in Western music?",["Semitone","Whole tone","Octave","Tone"],"A"],
        ["Which famous composer was deaf for much of his adult life?",["Wolfgang Amadeus Mozart","Ludwig van Beethoven","Johann Sebastian Bach","Franz Schubert"],"B"],
        ['Who is nicknamed the "Queen of Pop"?',["Madonna","Lady Gaga","Taylor Swift","Ariana Grande"],"A"]
        ]

    Food = [
        ["What is the main ingredient in sushi?",["Pasta","Rice","Potatoes","Bread"],"B"],
        ["Where was pizza invented?",["Greece","Spain","France","Italy"],"D"],
        ["What type of pastry is used to make a croissant?",["Shortcrust","Choux","Puff","Filo"],"C"],
        ["What is the main ingredient in naan?",["Flour","Chickpeas","Lentils","Rice"],"A"],
        ["What is the main ingredient in guacamole?",["Avocados","Tomatoes","Onions","Peppers"],"A"]
        ]


    #Display title.
    print("\n\nWelcome to Trivia!\n")
    sleep(1)
    print("             TRIVIA\n")
    sleep(1)
    print("             NIGHT!\n")

    #Display menu.
    while menu_select != 3:
        #Reset category and score for new game.
        category = ""
        score = 0
        menu_select = GameMenu()
        #If user picked 1, display rules.
        if menu_select == 1:
            print(f"\n{'*'*40}\n")
            print("Choose a category and try to answer all\n5 questions correctly!\nIf you get one right, you get 10 points.\nIf you get one wrong, you lose 5 points.")
            print(f"\n{'*'*40}\n")
        #If user picked 2, play game.
        elif menu_select == 2:
            #Prompt for category and validate answer.
            while category != "A" and category != "B" and category != "C":
                category = input("\nPlease choose a category:\nA) Animals\nB) Music\nC) Food\nSelection: ").strip().upper()

                if category == "A":
                    q_list = Animals
                elif category == "B":
                    q_list = Music
                elif category == "C":
                    q_list = Food
                else:
                    print("\nMust choose A, B, or C.")
                    continue
                    
                for ques in q_list:
                    question_ans = ""
                    while question_ans not in ["A","B","C","D"]:
                        #Show question and answers.
                        #Prompt player for answer and validate.
                        print(f"\nQuestion: {ques[0]}\nA) {ques[1][0]}\nB) {ques[1][1]}\nC) {ques[1][2]}\nD) {ques[1][3]}")
                        question_ans = input("Please select your answer: ").strip().upper()

                        if question_ans not in ["A","B","C","D"]:
                            print(f"Please read, {playerName}...Must choose A, B, C, or D!")
                        #If player is correct, add 10 points.
                        elif question_ans == ques[2]:
                            sleep(.5)
                            print("\nThat answer is ...")
                            sleep(.5)
                            print("\nCorrect!\n")
                            score += 10
                        #If player is incorrect, subtract 5 points.
                        else:
                            sleep(.5)
                            print("\nThat answer is ...")
                            sleep(.5)
                            print("\nIncorrect!!\n")
                            score -= 5
                        #Display running score.
                        print(f"Current score: {score}/50")
                #Show final score.
                if score > 30:
                    print(f"\nGreat job, {playerName}!\nFinal Score: {score}/50\n")
                elif score > 10:
                    print(f"\nDecent job, {playerName}!\nFinal Score: {score}/50\n")
                else:
                    print(f"\nReally, {playerName}? REALLY?\nFinal Score: {score}/50\n")
            
        #If user picked 3, exit back to main menu.
        else:
            print("\nThanks for playing!\n")


#Return: none
#Parameters: 1 string for name
#Purpose: This game will offer 3 difficulties, ask questions, add points, and take them away
def MathGame(name):
    #Declare constant for number of questions.
    QUESTIONS = 10
    #Declare and initialize variables.
    difficulty = question_ans = ""
    menu_select = score = score_add = score_sub = 0
    
    #Display title.
    print("\n\nWelcome to the Math Game!\n")
    sleep(1)
    print("             MATH\n")
    sleep(1)
    print("             WHIZZ!\n")
    #Display menu.
    while menu_select != 3:
        #Declare/reset lists.
        Easy = [
            ["What is 4 plus 3?",["7","8","13","12"],"A"],
            ["What is a shape with 3 sides?",["Square","Triangle","Rhombus","Octagon"],"B"],
            ["Which is NOT a multiple of 2?",["600","262,626","3","8"],"C"],
            ["Which number is NOT odd?",["2","3","7","851"],"A"],
            ["What is 30 minus 10?",["40","25","20","35"],"C"]
            ]

        Moderate = [
            ["What is 4 times 3?",["8","7","12","16"],"C"],
            ["How many sides are in a decagon?",["10","6","8","5"],"A"],
            ["What is the area of a 2 ft by 5 ft room?",["7 sq ft","15 sq ft","10 sq ft","8 sq ft"],"C"],
            ["Claire has 4 apples. If Michael has twice as many, how many apples does Michael have?",["8","9","10","6"],"A"],
            ["What equation is used to find the slope of a line?",["x = bx + y","e = mc2","a2 + b2 = c2","y = mx + b"],"D"]
            ]

        Hard = [
            ["What is the square root of 64?",["24","16","8","4"],"C"],
            ["What is 3 to the power of 6?",["81","250","600","729"],"D"],
            ["What is the supplement of an angle measuring 150 degrees?",["50 degrees","180 degrees","30 degrees","10 degrees"],"C"],
            ["What is the volume of a cube whose side lengths are 2 ft each?",["8 cubic ft","4 cubic ft","2 cubic ft","12 cubic ft"],"A"],
            ["What is the factorial of 9?",["40,320","362,880","81","900"],"B"]
            ]
        #Reset category and score for new game.
        difficulty = ""
        menu_select = GameMenu()
        #If user picked 1, display rules.
        if menu_select == 1:
            print(f"\n{'*'*40}\n")
            print("Easy questions are worth 5 points.\nModerate questions are worth 10 points.\nHard questions are worth 15 points.\nThere are a total of 125 points available.\nSelect your difficulties and try to get a high score!")
            print(f"\n{'*'*40}\n")
        #If user picked 2, play game.
        elif menu_select == 2:
            #Reset score.
            score = 0
            #Ask user 10 questions total.
            for i in range(QUESTIONS):
                #Reset difficulty and answer inputs.
                difficulty = ""
                question_ans = ""
                #Prompt for difficulty and validate answer.
                while difficulty != "A" and difficulty != "B" and difficulty != "C":
                    difficulty = input(f"\nPlease choose a difficulty, {name}:\nA) Easy\nB) Moderate\nC) Hard\nSelection: ").strip().upper()

                    if difficulty == "A":
                        qlist = Easy
                        score_add = 5
                        score_sub = 3
                    elif difficulty == "B":
                        qlist = Moderate
                        score_add = 10
                        score_sub = 7
                    elif difficulty == "C":
                        qlist = Hard
                        score_add = 15
                        score_sub = 12
                    else:
                        print("\nMust choose A, B, or C.")
                        continue

                    #Validate that the list still contains questions.
                    if len(qlist) == 0:
                        print("You answered all the questions in this category!")
                        difficulty = ""
                        continue

                    while question_ans not in ["A","B","C","D"]:
                        #Display question and answers.
                        #Prompt player for answer and validate.
                        print(f"\nQuestion {i+1}: {qlist[0][0]}\nA) {qlist[0][1][0]}\nB) {qlist[0][1][1]}\nC) {qlist[0][1][2]}\nD) {qlist[0][1][3]}")
                        question_ans = input("\nPlease select your answer: ").strip().upper()

                        if question_ans not in ["A","B","C","D"]:
                            print(f"Try again, {name}! Must choose A, B, C, or D!")
                        #If player is correct, add 10 points.
                        elif question_ans == qlist[0][2]:
                            sleep(.5)
                            print("\nThat answer is ...")
                            sleep(.5)
                            print("\nCorrect!\n")
                            score += score_add
                        #If player is incorrect, subtract 5 points.
                        else:
                            sleep(.5)
                            print("\nThat answer is ...")
                            sleep(.5)
                            print("\nIncorrect!!\n")
                            score -= score_sub
                        #Remove question from list to avoid repetition.
                        qlist.pop(0)
                    #Display running score.
                    print(f"Current score: {score}/50")
            #Display final score.
            if score > 30:
                print(f"\nAmazing, {name}!\nFinal Score: {score}/125\n")
            elif score > 10:
                print(f"\nAlright, {name}!\nFinal Score: {score}/125\n")
            else:
                print(f"\nBetter luck next time, {name}!\nFinal Score: {score}/125\n")
                    
                
                
        #If user picked 3, exit back to main menu.
        else:
            print("\nThanks for playing!\n")



def main():
    #Declare and initialize variables.
    name = menu_choice = ""
    
    #Display title.
    sleep(.5)
    print("   BRAN'S   ".center(40,"*"))
    sleep(.5)
    print("   MINIGAME   ".center(40,"*"))
    sleep(.5)
    print("   PROGRAM!   ".center(40,"*"))
    sleep(.5)
    
    #Prompt user for name.
    name = input("\n\nPlease enter your name: ")
    sleep(.5)
    print(f"\nHi, {name}. Get ready to play!\n")
    sleep(.5)
    print("Choose a game to play from the menu below.")

    while menu_choice != "5":
        #Display menu and prompt user for mini game to play.
        print("\n1) Guess The Roll\n2) High Card Wins\n3) Trivia Game\n4) Math Game\n5) Exit")
        menu_choice = input("\nPlease select from the menu: ")

        #If menu selection is 1, call Guess The Roll.
        if menu_choice == "1":
            print("\nLet's play!")
            sleep(.5)
            GuessTheRoll()
        #If menu selection is 2, call High Card Wins.
        elif menu_choice == "2":
            print("\nLet's play!")
            sleep(.5)
            HighCardWins(name)
        #If menu selection is 3, call Trivia Game.
        elif menu_choice == "3":
            print("\nLet's play!")
            sleep(.5)
            TriviaGame(name)
        #If menu selection is 4, call Math Game.
        elif menu_choice == "4":
            print("\nLet's play!")
            sleep(.5)
            MathGame(name)
        #If menu selection is 5, end game with outro.
        elif menu_choice == "5":
            print("\n\nThanks for playing!")
        else:
            print("\nPlease type a number 1 - 5.")


#Call the main function.
main()
