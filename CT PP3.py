import sys
import random
import time

#def function
def slowprint(text):
    for char in text:
        sys.stdout.write(char)
        time.sleep(0.1)
        
text = "Im chatbot, What's your name? "
slowprint (text)
answer = input()

text = "Hello " + answer + " how are you today?"
slowprint (text)
answer = input()

#if elif else
if answer == "good":
    print("Im glad! I am good also")

elif answer == "tired":
    print ("Oh no, I hope you can get some rest soon")

else:
    print ("I get that, me too")

text = "What is your favorite color"
slowprint (text)
answer = input()

#list
colors = ["sky blue", "leafy green" , "sunset orange"]
#random choice
text = "Nice choice! My favorite color is " + random.choice(colors)
slowprint (text)
