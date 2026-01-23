# Variables

print(" ")

money = 50
lemons = 0
cupsOfIce = 0
gramsOfSugar = 0
inventory = "You have", str(lemons), "lemons,", str(cupsOfIce), "cups of ice,", str(gramsOfSugar), "grams of sugar, and $"+ str(money)
desision = int(input("What do you want to do? See Inventory - 1 | Go To Shop - 2"))
shop = int(input("What do you want to buy? Lemons - 1 | Cups Of Ice - 2 | Grams of Sugar - 3: "))

if desision == 1:
    print(inventory)
if desision == 2:
    if shop == 1:
        howManyLemons = int(input("How many lemons do you want to buy? "))
        if howManyLemons >= money:
            howManyLemonsClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManyLemons) * 1+ ". ")
            if howManyLemonsClarify == "yes":
                lemons += howManyLemons
                money -= howManyLemons
        else:
            print("Sorry, you don't have enough money.")
            desision = int(input("What do you want to do? See Inventory - 1 | Go To Shop - 2"))