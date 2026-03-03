from customer_class import Customer

print(" ")

recipe = {'lemons': 0,
          'sugar': 0,
          'ice': 0}
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
customers = []
makeRecipePrice = 0
val = 0
day = 0

def decision(): 
    return int(input("What do you want to do? See Inventory - 1 | Go To Shop - 2 | Edit Recipe - 3 | Start Day - 4 | Quit - 5: "))
def inventory(): 
    return "You have", str(inventoryD['lemons']), "lemons,", str(inventoryD['cupsOfIce']), "cups of ice,", str(inventoryD['gramsOfSugar']), "grams of sugar, and $"+ str(inventoryD['money'])
def shopF(): 
    return int(input("What do you want to buy? Lemons - 1 | Cups Of Ice - 2 | Grams of Sugar - 3: "))

while val != 5:
    val = decision()
    if val == 2:
        shop = shopF()
        if shop == 1:
            howManyLemons = int(input("How many lemons do you want to buy? "))
            if howManyLemons <= inventoryD['money']:
                howManyLemonsClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManyLemons * 1.5)+ ". ")
                if howManyLemonsClarify.lower() == "yes":
                    inventoryD['lemons'] += howManyLemons
                    inventoryD['money'] -= howManyLemons * 1.5
                else:
                    inventoryD["lemons"] = inventoryD["lemons"]
                    inventoryD["money"] = inventoryD["money"]
                    
        elif shop == 2:
            howManyIce = int(input("How many cups of ice do you want to buy? "))
            if howManyIce <= inventoryD['money']:
                howManyIceClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManyIce * 0.75)+ ". ")
                if howManyIceClarify.lower() == "yes":
                    inventoryD['cupsOfIce'] += howManyIce
                    inventoryD['money'] -= howManyIce * 0.75
                else:
                   inventoryD["cupsOfIce"] = inventoryD["cupsOfIce"]
                   inventoryD["money"] = inventoryD["money"]

        elif shop == 3:
            howManySugar = int(input("How many grams of sugar do you want to buy? "))
            if howManySugar <= inventoryD['money']:
                howManySugarClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManySugar * 0.05)+ ". ")
                if howManySugarClarify.lower() == "yes":
                    inventoryD['gramsOfSugar'] += howManySugar
                    inventoryD['money'] -= howManySugar * 0.05
                else:
                   inventoryD["lemons"] = inventoryD["lemons"]
                   inventoryD["money"] = inventoryD["money"]
        else:
            print("Sorry, you don't have enough money.")
    elif val == 1:
        print(*inventory())
    elif val == 3:
        print("Your current recipe is", str(recipe))
        makeRecipeLemon = int(input("How many lemons do you want to put in your lemonade? "))
        makeRecipeSugar = int(input("How many grams of sugar do you want to put in your lemonade? "))
        makeRecipeIce = int(input("How many cups of ice do you want to put in your lemonade? "))
        lemonadePrice = int(input("How much do you want your lemonade to cost? It costs you $"+ str(1.5 * makeRecipeLemon + 0.75 * makeRecipeIce + 0.05 * makeRecipeSugar)+ " to make one cup. "))
        if makeRecipeLemon <= inventoryD['lemons']:
            if makeRecipeSugar <= inventoryD['gramsOfSugar']:
                if makeRecipeIce <= inventoryD['cupsOfIce']:
                    totalRecipe = 1.5 * makeRecipeLemon + 0.75 * makeRecipeIce + 0.05 * makeRecipeSugar
                    lemonadePriceClarify = input("Are you sure you want that price? It will cost $"+ str(totalRecipe)+ " per cup and you will be making $"+ str(round(lemonadePrice - totalRecipe, 2))+ ". ")
                    inventoryD['lemons'] -= makeRecipeLemon * lemonadePrice
                    inventoryD['gramsOfSugar'] -= makeRecipeSugar * lemonadePrice
                    inventoryD['cupsOfIce'] -= makeRecipeIce * lemonadePrice
                    recipe['lemons'] = makeRecipeLemon
                    recipe['sugar'] = makeRecipeSugar
                    recipe['ice'] = makeRecipeIce
                    if lemonadePriceClarify == "no":
                        recipe["lemons"] = 0
                        recipe["sugar"] = 0
                        recipe["ice"] = 0
                        makeRecipePrice = 0
        else:
            print("Sorry, you don't have enough materials.")
    elif val == 12:
        inventoryD["lemons"] += 50
        inventoryD["cupsOfIce"] += 50
        inventoryD["gramsOfSugar"] += 50
    elif val == 4:
        if day < 7:
            day += 1
        else:
            if inventoryD["money"] >= 100:
                print(f"Excelent job! you ended with: {inventoryD}")
                break
            else:
                print("All of that work... for what? You didn't pay off your debts. It's okay, you can try again next week.")
                break
        print(f"--------------- DAY {day} ---------------")
        for x in range(10):
            customers.append(Customer())
        for customer in customers:
            attributes = customer.get_customer_attributes()
            customersBought = 0
            if attributes["price"] <= lemonadePrice:
                if attributes["sweetness"] == makeRecipeSugar and makeRecipeLemon or attributes["ice"] == makeRecipeIce:
                    print("You got a sale!")
                    customersBought += 1
                    cupsOfLemonade -= 1
                    inventoryD["money"] += lemonadePrice
                    print(f"You made ${customersBought * lemonadePrice}")
        inventoryD["lemons"] = round(inventoryD["lemons"] / 2)
        inventoryD["cupsOfIce"] = round(inventoryD["cupsOfIce"] / 2)
        inventoryD["gramsOfSugar"] = round(inventoryD["gramsOfSugar"] / 2)              
                
print(" ")