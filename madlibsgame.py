#mad libs game

#taking input from the user

print("Welcome to madlibs. ")
print("Enter adjectives, nouns, and verbs to make a story. ") #instructions
print()
characterName = input("Enter a name, one suited for a hero. \n ")
mysteriousBeing = input("Enter a mythical creature. \n ")
verbMysteriousBeing = input("Enter a verb for the mythical creature. \n ")
characterVerbOne = input("Enter a verb for the character. \n ")
characterNounOne = input("Enter a noun, what the hero is verb-ing. \n")



story = "The main character, " + characterName + " charged through the woods, stepping over brambles and fallen trees. Suddenly, a huge " + mysteriousBeing + " stepped into the clearing. It " \
+ verbMysteriousBeing + " and the trees shook." + characterName + " whipped out a sword and stood tall and brave. " \
+ " The " + mysteriousBeing + " swung its limb and to scratch " + characterName + " but, " + characterName + " " + characterVerbOne + " the " + characterNounOne 


print(story)
