import random

def generateConsumables(rolls):
        for i in range(0, len(rolls)):
                if isinstance(rolls[i], int):
                        if rolls[i] == 1:
                                rolls[i] = generateConsumable() + " x1"
                        else:
                                rolls[i] = generateConsumable() + " x3"

        return rolls


def generateConsumable():
        options = ["First-Aid Med",
                "Flavor-specific food item",
                "Damaging item",
                "Specific status cure",
                "Full Heal",
                "Stat tonics",
                "Elemental oils",
                "Status tag",
                "Other",
                "Character-specific item",
                "Gem shard",
                "Ammunition",
                "Gremlin Bottle",
                "Potion of Vitrification",
                "Elixir",
                "PhoePhoe Down",
                "Fairy Bottle",
                "Coffee"]
        
        weights = [10, 8, 8, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 4, 4, 3, 2, 1]

        return random.choices(options, weights=weights)[0]                   

def singleRoll():
        options = ["Nightingale",
                   "Julia",
                   "Alternate costume",
                   "Rare item",
                   "Allied common monster",
                   "Furniture",
                   "Paint job",
                   1]
        
        weights = [1, 2, 5, 7, 10, 20, 25, 30]

        rolls = random.choices(options, weights=weights)

        generateConsumables(rolls)

        print(f"You rolled the gacha once! 6 GGs deducted!\nObtained: {rolls[0]}!")

def tenRoll():
        options = [1,
                "Materials x2",
                "Paint job",
                "Nothing",
                "Allied common monster",
                3,
                "Alt",
                "Furniture",
                "Rare item",
                "Small buff",
                "Julia x1",
                "Blueprints",
                "Nightingale",
                "Locale",
                "Strong buff",
                "A fucking rock",
                "Allied miniboss/boss"]
        
        weights = [14, 12, 11, 11, 10, 8, 6, 6, 5, 5, 3, 3, 2, 1, 1, 1, 1]

        rolls = random.choices(options, weights=weights, k=10)

        generateConsumables(rolls)

        print(f"You rolled the gacha ten times! 60 GGs deducted! Obtained:")
        print(*rolls,sep='\n')

random.seed()

multi = True

if multi:
        tenRoll()
else:
        singleRoll()
