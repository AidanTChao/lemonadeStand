
print(" ")

inventoryD = {'money': 50.00,
'lemons': 0,
'cupsOfIce': 0,
'gramsOfSugar': 0}
howManyLemons = 0
howManyLemonsClarify = 0
howManyIce = 0
howManyIceClarify = 0
howManySugar = 0
howManySugarClarify = 0
cupsOfLemonade = 0
val = 0
recipe = {'lemonRecipe': 0,
          'sugarRecipe': 0,
          'iceRecipe': 0}

def decision(): 
    return int(input("What do you want to do? See Inventory - 1 | Go To Shop - 2 | Edit Recipe - 3 | Quit - 4: "))
def inventory(): 
    return "You have", str(inventoryD['lemons']), "lemons,", str(inventoryD['cupsOfIce']), "cups of ice,", str(inventoryD['gramsOfSugar']), "grams of sugar, and $"+ str(inventoryD['money'])
def shopF(): 
    return int(input("What do you want to buy? Lemons - 1 | Cups Of Ice - 2 | Grams of Sugar - 3: "))

while val != 4:
    val = decision()
    if val == 2:
        shop = shopF()
        if shop == 1:
            howManyLemons = int(input("How many lemons do you want to buy? "))
            if howManyLemons <= inventoryD['money']:
                howManyLemonsClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManyLemons * 1.5)+ ". ")
                if howManyLemonsClarify == "yes":
                    inventoryD['lemons'] += howManyLemons
                    inventoryD['money'] -= howManyLemons * 1.5
                    
        elif shop == 2:
            howManyIce = int(input("How many cups of ice do you want to buy? "))
            if howManyIce <= inventoryD['money']:
                howManyIceClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManyIce * 0.75)+ ". ")
                if howManyIceClarify == "yes":
                    inventoryD['cupsOfIce'] += howManyIce
                    inventoryD['money'] -= howManyIce * 0.75
        elif shop == 3:
            howManySugar = int(input("How many grams of sugar do you want to buy? "))
            if howManySugar <= inventoryD['money']:
                howManySugarClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManySugar * 0.05)+ ". ")
                if howManySugarClarify == "yes":
                    inventoryD['gramsOfSugar'] += howManySugar
                    inventoryD['money'] -= howManySugar * 0.05
        else:
            print("Sorry, you don't have enough money.")
    elif val == 1:
        print(*inventory())
    elif val == 3:
        print("Your current recipie is", str(recipe))
        recipe = {'lemonRecipe': 0,
                  'sugarRecipe': 0,
                  'iceRecipe': 0}
        makeRecipeLemon = int(input("How many lemons do you want to put in your lemonade? "))
        makeRecipeSugar = int(input("How many grams of sugar do you want to put in your lemonade? "))
        makeRecipeIce = int(input("How many cups of ice do you want to put in your lemonade? "))
        if makeRecipeLemon >= inventoryD['lemons']:
            if makeRecipeSugar >= inventoryD['gramsOfSugar']:
                if makeRecipeIce >= inventoryD['cupsOfIce']:
                    cupsOfLemonadeClarify = input("Are you sure you want to make that many? It will cost $"+ str(1.5 * makeRecipeLemon + 0.75 * makeRecipeIce + 0.05 * makeRecipeSugar)+ " per cup. ")
                    inventoryD['lemons'] -= makeRecipeLemon * cupsOfLemonade
                    inventoryD['gramsOfSugar'] -= makeRecipeSugar * cupsOfLemonade
                    inventoryD['cupsOfIce'] -= makeRecipeIce * cupsOfLemonade
                    recipe['lemonRecipe'] += makeRecipeLemon
                    recipe['sugarRecipe'] += makeRecipeSugar
                    recipe['iceRecipe'] += makeRecipeIce
        else:
            print("Sorry, you don't have enough materials.")

print(" ")