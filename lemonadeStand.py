from recipeAndPricing import recipeFunction
from lemonadeShop import shopFunction
from startDay import dayFunction

print("Resident Evil 30289732 just came out! But with $50 to your name, you don't have enough to buy it.")
print("As the number of games went up, the price did too. It is $300. Guess you'll have to work for it.")
print("Dog walking? No, you're allergic. Mowing lawns? No, the lawn mower would be more expensive than the game.")
print("Then it dawns on you. You'll open a lemonade stand.")

while True:
    try:
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
        price = 0
        val = 0
        day = 0

        print(" ")

        def decision(): 
            return int(input("What do you want to do? See Inventory - 1 | Go To Shop - 2 | Edit Recipe - 3 | Start Day - 4 | Quit - 5: "))
        def inventory(): 
            return "You have", str(inventoryD['lemons']), "lemons,", str(inventoryD['cupsOfIce']), "cups of ice,", str(inventoryD['gramsOfSugar']), "grams of sugar, and $"+ str(inventoryD['money'])
        def shopF(): 
            return int(input("What do you want to buy? Lemons - 1 | Cups Of Ice - 2 | Grams of Sugar - 3: "))

        while inventoryD['money'] <= 0:
            print("All of that work... for what? You didn't get the game. It's okay, you can try again next week.")
            break

        while val != 5:
            if inventoryD["money"] >= 5:
                val = decision()
                if val == 1:
                    print(" ")
                    print("--------------- INVENTORY ---------------")
                    print(*inventory())
                    print(" ")
                elif val == 2:
                    print(" ")
                    print("--------------- SHOP ---------------")
                    shopFunction(inventoryD, shopF)
                    print(" ")
                elif val == 3:
                    print(" ")
                    print("--------------- RECIPE ---------------")
                    price = recipeFunction(recipe, inventoryD)
                    print(" ")
                elif val == 12:
                    inventoryD["lemons"] += 50
                    inventoryD["cupsOfIce"] += 50
                    inventoryD["gramsOfSugar"] += 50
                    recipe["lemons"] = 1
                    recipe["sugar"] = 1
                    recipe["ice"] = 1
                    price = 4
                elif val == 4:
                    print(" ")
                    day = dayFunction(inventoryD, day, customers, price, recipe)
                    print(" ")
                    if  day == -1:
                        break
            else:
                print("All of that work... for what? You didn't get the game. It's okay, you can try again next week.")
                break

        print(" ")

        print("                    __________________")
        print("                   |     LEMONADE    |")
        print("  ___              |-----------------|")
        print("\\( ^^)/            |_________________|")
        print("  |_|              |                 |")
        print("  | |              |_________________|")

        print(" ")
    except ValueError, TypeError, ImportError:
        print("INVALID RESPONSE")
    else:
        break