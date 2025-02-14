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

#random numb generator
import random
numbers = ['1','2','3','4','5','6','7','8','9','10']
random_number = random.choice(numbers)
guessed_number = input("Guess the number:")
if guessed_number < random_number:  
    print(input("Higher, try again:"))
elif guessed_number > random_number:
    print(input("Lower, try again:"))
else:
    print("You guessed correctly")



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