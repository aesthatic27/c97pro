import random
Number= random.randint(1,9)
chances = 0
print ("GUESS A NUMBER")
while chances <5:
    guess = int(input("Enter your GUESS"))
    if guess == Number:
       print ("YOu Won")
       break
    elif guess < Number:
        print ("guess a higher No.")
    else : 
        print ("guess a lower No.")

    chances += 1

if not chances < 5
print ("you lose ,the No.,Number")