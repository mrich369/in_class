"""

Inputs
- a string containing an attribute guess or guess of the animal's name

Processes
- randomly select an animal
- allow the user to guess until they guess the correct animal
- when they guess, tell them if the animal has the attribute or not
- tell the uer when they guess correctly

Outputs
- attribute guess correctness 
- congratulations message

"""

import random      # teach python how to do random stuff

ANIMALS = {
    "Lion" : ["Mammal", "Four legs", "Predator", "Furry", "Fast", "Savannnah", "Cat", "King", "Land"],
    "Whale" : ["Mammal", "No legs", "Fins", "Sea", "Smooth", "Big"],
    "Bunny" : ["Mammal", "Four legs", "Soft", "Furry", "Small", "Pet", "Cute", "Land"],
    "Snake" : ["Reptile", "Scales", "No legs", "Land", "Pet", "Predator", "Land", "Long"],
    "Pigeon" : ["Bird", "Flies", "Wings", "Two legs", "Feathers", "Small", "Land", "City", "Scavenger"],
    "Crocodile" : ["Reptile", "Predator", "Dangerous", "Sea", "Land", "Tropical", "Teeth"],
    "Chicken" : ["Bird", "Two legs", "Edible", "Wings", "Flies", "Land"],
    "Human" : ["Two legs", "Mammal", "Fingers", "Omnivore", "Land", "Hair", "Intelligent"],
    "Turtle" : ["Amphibean", "Omnivore", "Green", "Sea", "Shell", "Pet", "Swim"]
}

WELCOME_MESSAGE = """Animal Guessing Game:
I have picked a random animal. Guess an
attribute or name the animal.
"""

CONGRATULATIONS_MESSAGE = "You won!"

list_of_animal_names = list(ANIMALS.keys())
random_animal = random.choice(list_of_animal_names)
random_animal_attributes = ANIMALS[random_animal]

guess = ""

while guess != random_animal:
    guess = input("Please guess an attachment or an animal name: ").capitalize()
    if guess in random_animal_attributes:
        print(f"Yes, {guess} is an attribute of the animal.")
    elif guess == random_animal:
        print(CONGRATULATIONS_MESSAGE)
    else:
        print(f"No, {guess} is not an attribute of the aniaml.")