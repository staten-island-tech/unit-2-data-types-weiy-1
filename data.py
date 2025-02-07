#Strings are for representing characters, names, words, etc.
name = "divid"
#integers represent whole numbers
age: 14
#Floats represents decimals
wallet: 5.45
#booleans represents true/false, used in evaluations
graduated = False


""" def add(x,y):
    print(x + y) """
#input asks the user a question and stores their response as a value
#bill = float(input("How much did the bill cost?"))
#print(type(bill))
#add(25, bill)


#lists
#students = ["Joanna", "Divid", "Deivid", "other Deivid", "Etan"]
#this is similar to saying for i in range(5): print(students[i])
""" print(students[2]) """
""" for student in students:
    print(student) """
""" moneys = [1,2,3,4,5,6]
total: 0
for money in moneys: """


#tip calculator:
""" def add(x,y):
    print(x + y)
bill = float(input("How much does the bill cost?"))
print(type(bill))
tip = float(input("How much is the tip?"))
print(type(tip))
add(bill,tip)
total = (float(bill + tip))
print("Total:", total) """


#prints all numbers inside the brackets
""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

#prints only the 3rd(2) and 6th(5) number
""" values = [1,2.23,5,7,2,30,15]
print(values[2])
print(values[5]) """

#determines length of word(s)
""" string = (input("Input word(s):")) 
print(type(string))
length=len(string)
print("The length of this/those word(s) is", length) """


""" def login(password):
    #if statement evaluates to true we go to next line
    if password == "pasword123":
        print("Logged in")
    else:
        print("Incorrect")
x = input("what is the password?")
login(x) """

""" def grade(score):
    if score >= 92:
        print("A")
    elif score >= 82:
        print("B")
    elif score >= 72:
        print("C")
    else:
        print("F")
x = int(input("What's the score?"))
grade(x) """

""" def gamble(age, id):
    if age >= 21 and id == True:
        print("Gamble away")
    elif age >= 21 and id == False:
        print("You need ID verification")
    else:
        print("You're too young") """

""" raining = False #<-- change value (true or false)
if raining == True:
    print("dont go for a walk")
if raining == False:
    print("go for a walk")"""


#mad libs
food = (input("Input a food:"))
print(type(food))
name = (input("Input a celebrity's name"))
print(type(name))
verb = (input("Give me a past tense verb:"))
print(type(verb))
adjective = (input("Give me a adjective:"))
print(type(adjective))
noun = (input("Give me a name:"))
print(type(noun))
name2 = (input("Give me another name:"))
print(type(name2))
noun2 = (input("Give me another noun:"))
print(type(noun2))
verb2 = (input("Give me another verb:"))
print(type(verb2))
print("Me and my friend decided to get", food, ". Then, my friend", name, "forgot he had a class he had to go to. So he", verb, "to his class, but bumped into a", adjective, "looking man")
