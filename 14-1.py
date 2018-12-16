
input = "37"
elf1 = 0
elf2 = 1

def createNewRecipes():
    global input
    newRecipe = int(input[elf1]) + int(input[elf2])
    bonus = ""
    if (newRecipe > 10):
        newRecipe = newRecipe - 10
        bonus = "1"
    input = input + bonus
    input = input + str(newRecipe)

def moveElves():
    global elf1
    global elf2

    elf1ToMove = int(input[elf1]) + 1
    while (elf1ToMove > 0):
        elf1ToMove = elf1ToMove - 1
        elf1 = elf1 + 1
        if (elf1 >= len(input)):
            elf1 = 0
    elf2ToMove = int(input[elf2]) + 1
    while (elf2ToMove > 0):
        elf2ToMove = elf2ToMove - 1
        elf2 = elf2 + 1
        if (elf2 >= len(input)):
            elf2 = 0

while (len(input) < (165061 + 10)):
    createNewRecipes()
    moveElves()
    # print "Recipes are now: " + input
print input[len(input) - 10:]
