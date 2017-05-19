#assign an integer to a variable
personCount = 1
nameNotConfirmed = True
#use a while loop
while nameNotConfirmed:
    #assign a string to a variable
    userName = input("What is your name? ").capitalize()
    confirm = input("You said your name is {}. Is this correct? (y/n)".format(userName))
    #Use of conditional statements: if, elif, else
    if confirm == "y":
        #Use the print founction and .format() notation to print out the variable you assigned
        print("Hello, {}. I hope you are having a lovely day.".format(userName))
        nameNotConfirmed = False
    elif confirm == "n":
        print("I'm very sorry that you entered your name wrong. Please re-enter it.")
        nameNotConfirmed = True
    else:
        print("I'm sorry, that is not a valid command.")
        nameNotConfirmed = True
print ("Good job that's your name!")
age = input("Noow, how old are you? Please enter an integer or float.")
userAge = int(age)
print("Wow! You are {} years old!".format(userAge))
print("Now we're going to do some calculations on your age!")
#Use each of these operators +, - , * , / , +=, ­= , %
ageTimesTwo = (userAge * 2)
print("Your age multipled by two is {}!".format(ageTimesTwo))
#Assign a float to a variable 
ageOverTwo = float(userAge / 2)
print("Your age divided by two is {}!".format(ageOverTwo))
agePlusTwentyFive = (userAge + 25)
print("Your age plus 25 is {}!".format(agePlusTwentyFive))
ageMinusTwentyFive = (userAge - 25)
print("If you were 25 years younger you would be {}!".format(ageMinusTwentyFive))
agePlusEqualsTwo = (userAge)
agePlusEqualsTwo += 2
print("Your age plus two is {}!".format(agePlusEqualsTwo))
ageMinusEqualsTwo = (userAge)
ageMinusEqualsTwo -= 2
print("Your age minus two is {}!".format(ageMinusEqualsTwo))
ageModulusTwo = (userAge % 2)
print("Your age modulus two is {}!".format(ageModulusTwo))

#Define a function that returns a string variable
def ageAndNameLength(userAge, userName):
    youngOrLongName = "You are either young or have a long name!"
    olderOrShortName = "You are either older or have a short name!"
    #Use of logical operators: and, or, not
    if (not (userAge > 40) or (userAge > 41 and len(userName) > 6)):
        return youngOrLongName
    else:
        return olderOrShortName
#Call the function you defined above and print the result to the shell
print (ageAndNameLength(userAge, userName))
print ("I am going to select only the fruits from this tuple: ")
tup1 = ('bananas', 'apples', 'grapefruit', 'pineapples', 'pears', 'anxiety');
#Use of a for loop
#Create a tuple and iterate through it using a for loop to print each item out on a new line
for x in range(5):
    print(tup1[x])



#Create a list and iterate through that list using a for loop to print each item out on a new line
print ("And for my final trick, I will iterate through this list of famous game designers!")
epic_game_designer_list = ["Tim Shafer",
                           "Hideo Kojima",
                           "Amy Hennig",
                           "Neil Druckmann",
                           "Nina Freeman",
                           "Hidetaka Suehiro",]
for designer in epic_game_designer_list:
    print(designer)

print("Thank you for reading all this!")
input("Press Enter to continue...")
