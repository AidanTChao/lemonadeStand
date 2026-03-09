def recipeFunction(recipe, inventoryD):
    while True:
        try:
            print("Your current recipe is", str(recipe))
            makeRecipeLemon = int(input("How many lemons do you want to put in your lemonade? "))
            makeRecipeSugar = int(input("How many grams of sugar do you want to put in your lemonade? "))
            makeRecipeIce = int(input("How many cups of ice do you want to put in your lemonade? "))
            lemonadePrice = int(input("How much do you want your lemonade to cost? It costs you $"+ str(round(1.5 * makeRecipeLemon + 0.75 * makeRecipeIce + 0.05 * makeRecipeSugar))+ " to make one cup. "))
            if makeRecipeLemon <= inventoryD['lemons']:
                if makeRecipeSugar <= inventoryD['gramsOfSugar']:
                    if makeRecipeIce <= inventoryD['cupsOfIce']:
                        totalRecipe = 1.5 * makeRecipeLemon + 0.75 * makeRecipeIce + 0.05 * makeRecipeSugar
                        lemonadePriceClarify = input("Are you sure you want that price? It will cost $"+ str(totalRecipe)+ " per cup and you will be making $"+ str(round(lemonadePrice - totalRecipe, 2))+ ". ")
                        inventoryD['lemons'] -= round(makeRecipeLemon * lemonadePrice)
                        inventoryD['gramsOfSugar'] -= makeRecipeSugar * lemonadePrice
                        inventoryD['cupsOfIce'] -= makeRecipeIce * lemonadePrice
                        recipe['lemons'] = makeRecipeLemon
                        recipe['sugar'] = makeRecipeSugar
                        recipe['ice'] = makeRecipeIce
                        if lemonadePriceClarify == "no":
                            recipe["lemons"] = 0
                            recipe["sugar"] = 0
                            recipe["ice"] = 0
                            lemonadePrice = 0
                        return lemonadePrice
            else:
                print("Sorry, you don't have enough materials.")
                return 0
        except ValueError, TypeError, ImportError:
            print("INVALID RESPONSE")
        else:
            break