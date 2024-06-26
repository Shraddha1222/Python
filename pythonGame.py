import random                                                                                                       #import random module to get random numbers


def readPhoneNumbersFromFile(filename):                                                                             #define a function to read number from a file
    phoneList = []                                                                                      #empty list to store phone numbers
    try:                                        #useing try block to handle exception error
        file = open(filename, 'r')              #opening a file using open method and reading it using read mode
        for line in file:                             #using for loop to repeat each line in file
            line = line[:-1]                   #by the help of string slicing remove newline character 
            phoneList.append(line)                  #add phone number to the phone list
    except FileNotFoundError:                     #Except the error through except block
        print("File not found. Make sure the filename is correct and the mentioned location is proper.")             #Printing a message to indicate that the file can't found
    return phoneList                          #return the list of phone number

    


def guessPhoneNumber(filename):              #defining a function to guess a phone number              
    phoneList=readPhoneNumbersFromFile(filename)        #Calling a function 
    
    index = random.randint(0, len(phoneList) - 1)     #making a random index in the range of phoneList
    phoneNumber = phoneList[index]                     #taking the phone number to the index respectively

    print(userName+" Welcome to the Phone Number Guessing Game and break a leg!")             #printing a introduction message
    print("Guess the individual digits of the phone number.")                            #printing instructions
    print("Rmember You have 10 attempts for each digit.")                          #Giving instructions

    guessedNumber = ''               #empty string to store guesses phone number

    for i in range(10):                #using for loop repeat 10 times 
        attempts = 0                        #number of attempts for current digit
        correctDigit = phoneNumber[i]          #take the correct digit of phone number at index i

        while attempts < 10:              #using while loop to allow 10 attempts for each digit
                guess = input("Enter your guess for an indiviual digit   " + str(i + 1) + ": ")      #asking user for guessing the current digit
                
                if guess == correctDigit:       #checking if the guess matches with correctDigit
                    print("Correct!")            #print correct message
                    guessedNumber = guessedNumber + guess        #append the guessed digit to guessed number
                    break                #correct digit is guessed then exit the loop using break
                else:                      #if the guess don't match with correctdigit
                    print("Incorrect! Try again.")       #print a message of incorrect
                    attempts = attempts+1         #increment the number of attempts
        

    

    if guessedNumber == phoneNumber:        #checks if guessednumber is equal to phonenumber
        print("You rock! You have correctly predicted the phone number " + phoneNumber + " GOOD JOB!!!!")           #if the guessed number is right printing a message of congratulation
        print("You win the game")                     #winning message
    else:                                  #if is false then use else block
        print("Oops! The correct phone number was " + phoneNumber + " Take another shot")                #try again message




userName=input("What's your name?  ")                #asking name to user
print("Okay "+userName+" Do you want to enter in a guessing game and play it? (yes/no)")                #asking for user wants to play a game or not
play = input()                    #getting userinput

if play == 'yes':              #if user type yes
    filename = 'C:\\Users\\sharm\\OneDrive\\Desktop\\phone_number.txt'         #giving a name of a file which contains phone numbers
    guessPhoneNumber(filename)                #calling the function with argument filename
else:              #if user says no
    print("Okay, bye!")               #living the game and bye message



