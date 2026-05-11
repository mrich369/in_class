'''

INPUTS
- player class (string)
- player level (int)

PROCESSES
- suggest a quest type based on player level and class
- different quests for level ranges (1-10, 11-25, 26+), modified by class (warrior, mage. rogue)

OUTPUTS
- print a recommended quest

'''

# INPUTS

class_types = {
    "Wizard" : ["Find a wand", "Find a spellbook", "Duel your professor"],
    "Fighter" : ["Find a sword", "Find a shield", "Defend your professor from the wizard"]
}

# find a specifc quest in the data structure
quest_to_find = input("What quest do you want? ")

for class_key in class_types:
    class_quests = class_types[class_key]
    for quest in class_quests:
        if quest == quest_to_find:
            print(f"Your quest is performed by the {class_key}")

#  validation
player_class = input("What is your class? ").capitalize()
player_level = ""
while not player_level.isdigit():
    player_level = input("What is your current level? (enter a number): ")

player_level=int(player_level)

# Calculate quest level based on the player level

quest_level = 0
if player_level >= 26:
    quest_level = 2
elif player_level >= 11:
    quest_level = 1

recommended_quest = class_types[player_class][quest_level]
print(f"You should do this quest: {recommended_quest}")

"""
 - - - same thing as above, another way to do it
users_class_quests = class_types[player_class]
print(users_class_quests)
recommended_quest = users_class_quests[quest_level]
print(recommended_quest)
"""