# Script for a text-based roleplaying game system titled RPG Dungeon.
# The character in question, Lucina, has a number of chance-based effects on her attacks. Some come from her held items, while others are innate to her character.
# This script will, for an individual series of attacks, determine which of these effects trigger and on which attacks.
# Largely superseded by attackcina.py and recursioncina.py.

import random

SPD = 165 # Lucina's critical rate is determined by her speed stat.
ULT_ACTIVE = False # Toggles whether Lucina's ultimate ability is active.

onhits = {"Snake Tail": .05, "Taser": .07, "Tri-Tip Dagger": .15, "Ukulele": .25} # On-hit effects granted by items.

random.seed()

multiplier = 1

if ULT_ACTIVE: # When Lucina's ultimate ability is active, her chance of activating any of her chance-based effects increases by 50%.
    multiplier = 1.5
    for o in onhits:
        onhits[o] *= multiplier
        
onhits["crit"] = SPD/500

aether = False # Aether is a special two-hit combo attack that Lucina can trigger at a rate equal to her critical hit rate. Aether follow-up attacks can also trigger other on-hit effects.
atknum = 0

while atknum < 10:
    atk = "attack #%s (hit %.2f): " % (str(atknum + 1 + aether/2), random.random()) # The hit number is used for accuracy calculations if applicable.
    for o in onhits:
        if o == "crit" and aether: # Critical hits are calculated only once for Aether attacks, so skip the crit calculation on Aether follow-ups.
            continue
        if random.random() < onhits[o]: # Independently calculates the chance for each on-hit effect.
            atk += o
            atk += ", "
    if aether == False and random.random() < SPD * multiplier / 500: # If not already performing an Aether follow-up, checks to see if one is performed.
        aether = True
        atk += "Aether, "
    else: # Otherwise, move on to the next attack.
        aether = False
        atknum += 1 # This is in the if statement so that follow-ups can be given decimal numbers.
    print (atk[0:-2]) # Remove extraneous commas and colons.
