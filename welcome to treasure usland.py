print( "welcome to the Treasure Island. ")
print("your mission is to find the treasure.")
choice1= input('you are at a crossroad " '
                '" Where do you want to go? type " " left or right? ' ).lower ()
if choice1 == "left":
    choice2= input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake.'
                    'Type "wait" to wait for a boat.'
                    'type "swim" to swim across.\n').lower()
    if choice2 =="wait":
        choice3 = input(" you arrived at the island unharmed."
                       "There is house with three doors . one red, "
                       "one yellow and one blue."
                       "which colour do you choose?\n") .lower()
        if choice3 == "Red":
            print (" room full of fire.Game over")
        elif choice3=="yellow":
            print("you found the treasure.you win")
        elif choice3 =="blue":
            print("you enter  a room with full of toxic Gas.game over.")

    else:
        print("you chose a door that doesn't exit.Game over.")
else:
     print("you fell in to a hole .Game over ")



