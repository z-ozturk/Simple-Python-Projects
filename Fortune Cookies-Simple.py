#/////////////Fortune cookie\\\\\\\\\\\\\\\\

import random

fortune_messages = [
    "Opportunities don't happen. You create them.",
    "Happiness is a journey, not a destination.",
    "The best way to predict the future is to create it.",
    "Something wonderful is about to happen.",
    "A fresh start will put you on your way.",
    "Adventure awaits those who dare to dream.",
    "Your hard work will soon pay off in unexpected ways.",
    "A kind word can change someone’s entire day."
]

def fortuneCookie():
    
    yes_or_no = input("Hi! Do you want a fortune cookie? \n Y/N \n")

    if (yes_or_no.upper() == ("Y")):
        
        input("AWESOME! Enter your name to reveal your fortune \n")
        print(random.choice(fortune_messages))
        fortuneCookie()

    elif(yes_or_no.upper() == ("N")):
        
        print("OK :( see you later then.")
    
    else:
    
        print("Invalid input. Please try again.")
        fortuneCookie()

fortuneCookie()