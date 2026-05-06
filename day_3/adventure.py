hook = "You are traversing through the forest as you carry the Queen's Cargo. " \
    "You hear a loud crash in the trail up ahead. " \
        "What do you do? \n" \
        "A. Run and hide B. Turn around couragously C. Run towards the noise \n" \
        "Choose: "

decision = " "
decision2 = " "
decision3 = " "

#write what happens when you choose
decision_a = "You hide behind a tree and fall into a new dimension. You land on a mushroom. What do you do? \n" \
    "D. Slide off E. Run and hide F. Cry \n" \
    "Choose: "

decision_b = "You face a giant nargle and he is hungry. What do you do? \n" \
    "G. Fight the nargle H. Run and hide I. Befriend him \n" \
    "Choose: "

decision_c = "You find a kind elderly man who tripped. He offers you a wish. What do you do? \n" \
    "J. Run and hide K. Ask the conditions of the wish L. Wish for BYU chocolate milk \n" \
    "Choose: "

decision_d = "You land and wake up in your bed. What do you do? \n" \
    "M. Go back to bed N. Go tell your mom your dreams \n" \
    "Choose: "

decision_e = "You hide behind a tree and fall into a new dimension. You land on a mushroom."

decision_f = "You cry."

decision_g = "You pick up a stick and find the nargle following it with its eyes. You throw the stick and he runs to fetch it."

decision_h = decision_a

decision_i = "You pet him and you start your new life with a pet nargle."

decision_j = decision_a

decision_k = "The old man gets angry and curses you. You die."

decision_l = "You get a nice cold glass of BYU creamery chocolate milk. You win."

decision_m = "Sweet dreams."

decision_n = "Tragic, she doesn't believe you. Game over."

decision = input(hook).upper() #collect decision

if decision == "A":
    decision2 = input(decision_a).upper()
elif decision == "B":
    decision2 = input(decision_b).upper()
elif decision == "C":
    decision2 = input(decision_c).upper()
else:
    print("You are dead.")

if decision2 == "D":
    decision3 = input(decision_d)
elif decision2 == "E":
    print(decision_e)
elif decision2 == "F":
    print(decision_f)
elif decision2 == "G":
    print(decision_g)
elif decision2 == "H":
    print(decision_h)
elif decision2 == "I":
    print(decision_i)
elif decision2 == "J":
    print(decision_j)
elif decision2 == "K":
    print(decision_k)
elif decision2 == "L":
    print(decision_l)
else:
    print("You are dead.")

if decision3 == "M":
    print(decision_m)
elif decision3 == "N":
    print(decision_n)
else:
    print("You are dead.")