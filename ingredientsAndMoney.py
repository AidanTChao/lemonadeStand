# Variables

print(" ")

money = 50
lemons = 0
cupsOfIce = 0
gramsOfSugar = 0

def decision(): 
    return int(input("What do you want to do? See Inventory - 1 | Go To Shop - 2"))
def inventory():
    return "You have", str(lemons), "lemons,", str(cupsOfIce), "cups of ice,", str(gramsOfSugar), "grams of sugar, and $"+ str(money)
def shopF(): 
    return int(input("What do you want to buy? Lemons - 1 | Cups Of Ice - 2 | Grams of Sugar - 3: "))

val = decision()
if val == 2:
    shop = shopF()
    if shop == 1:
        howManyLemons = int(input("How many lemons do you want to buy? "))
        if howManyLemons <= money:
            howManyLemonsClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManyLemons) * 1+ ". ")
            if howManyLemonsClarify == "yes":
                lemons += howManyLemons
                money -= howManyLemons
    elif shop == 2:
        cupsOfIce = int(input("How many cups of ice do you want to buy? "))
        if howManyIce <= money:
            howManyIceClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManyIce) * 1+ ". ")
            if howManyIceClarify == "yes":
                cupsOfIce += howManyIce
                money -= howManyIce
        elif shop == 2:
        gramsOfSugar = int(input("How many grams of sugar do you want to buy? "))
        if howManyIce <= money:
            howManySugarClarify = input("Are you sure you want to buy that many? It will cost $"+ str(howManySugar) * 1+ ". ")
            if howManySugarClarify == "yes":
                gramsOfSugar += howManySugar
                money -= howManySugar
        else:
            print("Sorry, you don't have enough money.")
            decision()
elif val == 1:
    print(*inventory())
