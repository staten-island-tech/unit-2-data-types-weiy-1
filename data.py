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



#challenge 1
""" number = (int(input("Input a number:")))
print(type(number))

if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd") """


#challenge 2
""" def add(x,y):
    print(x + y)
bill = float(input("Cost of bill: "))
print(type(bill))
print("Tip amounts:")
print("1. 0% (Service was bad) ")
print("2. 15% (Service was okay) ")
print("3. 20% (Service was good) ")
print("4. 25% (Service was great) ")
tipchoice = input("Enter the number of your choice (between 1 and 4): ")
if tipchoice == '1':
    print("Your total will be", bill + bill*0)
elif tipchoice == '2':
    print("Your total will be", bill + bill*0.15)
elif tipchoice == '3':
    print("Your total will be", bill + bill*0.2)
elif tipchoice == '4':
    print("Your total will be", bill + bill*0.25)
else:
    print("Invalid choice (please choose a number between 1 and 4)") """


#challenge 3
""" factors = []
number = int(input("Enter a number: "))
for i in range(1,number + 1):
    if number % i == 0:
        factors.append(i)
print(f"The factors of {number} is {factors}") """


#challenge 4
""" def gcf():  #defines gcf as a function
    number1 = int(input("Enter 1st number:"))
    number2 = int(input("Enter 2nd number:"))
    common_factors = []
    list_of_factor1 = []        #list for store the factors
    list_of_factor2 = []
    for i in range(1, number1 + 1): #for anynumber/i between of i and number1, start at 1 and keep add 1 to number1
        if number1 % i == 0:    #divide number1 + 1 by i and if remainder = 0 store fir list1
            list_of_factor1.append(i)
    for i in range(1, number2 + 1): #for anynumber/i in range of i and number2, starts at 1 keeps adding 1 to number2
        if number2 % i == 0:    #divide number2 + 1 by i and if remainder = 0 store for list2
            list_of_factor2.append(i)
    for i in list_of_factor1:
        if i in list_of_factor2:        #check for same numbers in both lists and founded same numbers get add to common_factors list
            common_factors.append(i)
    gcf = max(common_factors)   #max find biggest number in common_factors list and define it as variable gcf
    print(f"The GCF of {number1} and {number2} is {gcf}")

gcf() """



#mad libs
""" name = (input("Input a celebrity's name: "))
print(type(name))
food = (input("Input a food: "))
print(type(food))
verb = (input("Input a past tense verb: "))
print(type(verb))
adjective = (input("Input an adjective: "))
print(type(adjective))
noun = (input("Input a plural noun: "))
print(type(noun))
noun_2 = (input("Input another noun (place): "))
print(type(noun_2))
name_2 = (input("Input another name: "))
print(type(name_2))
verb_2 = (input("Input another verb: "))
print(type(verb_2))
print("Today,", name, "tried to eat some", food, "but then someone came to his doorstep and", verb, "his house. It was very", adjective, "and", name, "started running until the house was 14.628 miles away. This person had chased", name, "since", name, "took 451", noun, "from", noun_2, "yesterday.", name_2, "saw", name, "running and wanted to", verb_2, name, "for stealing those 451", noun,".")
 """