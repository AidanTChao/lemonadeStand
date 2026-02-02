# Variables

print(" ")
from recipeAndPricing import ingredients
money = 50.00
lemons = 0
cupsOfIce = 0
gramsOfSugar = 0
howManyLemons = 0
howManyLemonsClarify = 0
howManyIce = 0
howManyIceClarify = 0
howManySugar = 0
howManySugarClarify = 0
cupsOfLemonade = 0
val = 0

def decision(): 
    return int(input("What do you want to do? See Inventory - 1 | Go To Shop - 2 | Recipe - 3 | Quit - 4: "))
def inventory(): 
    return "You have", str(lemons), "lemons,", str(cupsOfIce), "cups of ice,", str(gramsOfSugar), "grams of sugar, and $"+ str(money)
def shopF(): 
    return int(input("What do you want to buy? Lemons - 1 | Cups Of Ice - 2 | Grams of Sugar - 3: "))

while val != 4:
    val = decision()
    if val == 2:
        shop = shopF()
        if shop == 1:
            howManyLemons = int(input("How many lemons do you want to buy? "))
            if howManyLemons <= money:
                howManyLemonsClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManyLemons * 1.5)+ ". ")
                if howManyLemonsClarify == "yes":
                    lemons += howManyLemons
                    money -= howManyLemons
                    
        elif shop == 2:
            howManyIce = int(input("How many cups of ice do you want to buy? "))
            if howManyIce <= money:
                howManyIceClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManyIce * 0.75)+ ". ")
                if howManyIceClarify == "yes":
                    cupsOfIce += howManyIce
                    money -= howManyIce
        elif shop == 3:
            howManySugar = int(input("How many grams of sugar do you want to buy? "))
            if howManySugar <= money:
                howManySugarClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManySugar * 0.05)+ ". ")
                if howManySugarClarify == "yes":
                    gramsOfSugar += howManySugar
                    money -= howManySugar
        else:
            print("Sorry, you don't have enough money.")
    elif val == 1:
        print(*inventory())
    elif val == 3:
        print("Your current recipie is", str(ingredients))
        makeRecipeLemon = int(input("How many lemons do you want to put in your lemonade? "))
        makeRecipeSugar = int(input("How many grams of sugar do you want to put in your lemonade? "))
        makeRecipeIce = int(input("How many cups of ice do you want to put in your lemonade? "))
        if makeRecipeLemon >= lemons:
            if makeRecipeSugar >= gramsOfSugar:
                if makeRecipeIce >= cupsOfIce:
                    cupsOfLemonadeClarify = input("Are you sure you want to make that many? It will cost $"+ str(1.5 * makeRecipeLemon + 0.75 * makeRecipeIce + 0.05 * makeRecipeSugar)+ " per cup. ")
                    lemons -= makeRecipeLemon * cupsOfLemonade
                    gramsOfSugar -= makeRecipeSugar * cupsOfLemonade
                    makeRecipeIce -= makeRecipeIce * cupsOfLemonade
        else:
            print("Sorry, you don't have enough materials.")

print(" ")