
print("Please think of a number between 0 and 100!")
high = 100
low = 0
ans = False

while ans == False:
    guess = (high + low) // 2.0
    print("Is your secret number" + str(guess) + "?")
    choose = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if choose == "h":
        high = guess
    elif choose == "l":
         low = guess
    elif choose == "c":
        print("Game over. Your secret number was: " + str(guess))
        ans = True
    else:
        print("Sorry, I did not understand your input.")




