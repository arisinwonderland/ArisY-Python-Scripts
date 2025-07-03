# Created 2020-07-26
# Script for a text-based roleplaying game system titled RPG Dungeon.
# The character in question, Lucina, has a number of chance-based effects on her attacks. Some come from her held items, while others are innate to her character.
# This script will, for an individual series of attacks, determine when these effects trigger and how many times she hits.
# As an evolution of lucina.py, this version accounts for some of the specific properties of the attacks she uses.
# However, it's messier in execution than recursioncina.py due to its attempt to account for the unique properties of all abilities and my own being rusty with code at the time.
# Note also the use of the "proc coefficient" mechanic from Risk of Rain 2, which has been ported to this system. It's a little hard to explain, so I recommend checking their wiki.
# Also, contrary to what the file names might suggest, this still does have recursion. Not sure where that came from.

import random

SPD = 115 * 1.28
ULT_ACTIVE = False # Toggles whether Lucina's ultimate ability is active.
CRIT_BONUS = 5 # Flat bonus to critical hit rate.

atks = ["SB", "DB", "DB", "Disposable Missile Launcher"] # List of abilities used. Names abbreviated for convenience.
coeffs = {"Disposable Missile Launcher": 1.0} # Proc coefficients for any abnormal attacks. Formatted as a dict, where the key is the identifier of the affected attack and the value is the proc coefficient as a float.
onhits = {"Snake Tail": .05, "Taser": .07, "Runald's Band": .08, "Kjaro's Band": .08, "Tri-Tip Dagger": .15}
extrahits = {"Ukulele": .25} # Unlike the above chance-based effects, these effects trigger a new bonus hit when successful. These bonus hits can then themselves trigger the effects above.
procs = {"Ukulele": .2} # More proc coefficients. Also a dict, but the key is the name of the bonus hit effect this time, since all bonus hits from the same source share a proc coefficient.

def suffix(num): # Now that more than one follow-up attack can occur, using .5 no longer works, so follow-ups are labeled with letters added on to the numbers instead.
    return chr(97 + num) # Theoretically this breaks if there are more than 26 follow-ups on the same attack, but that's so vanishingly unlikely I didn't think it was worth the trouble to account for.

def hitcheck(atknum, proc, hit):
    hitname = ""
    
    if hit == "DB": # This elif statement differentiates between ability hits and bonus (follow-up) attacks.
        hitname = "DB1"
    elif hit in ["DB", "SB", "SS", "BS", "PA", "NPA"]: # These are all innate abilities with predefined behavior.
        hitname = hit
    
    if hitname != "":
        normalhitcalc(str(atknum), proc, hitname)
        if hit == "DB": # DB, or Dancing Blade, is an attack that hits up to four times.
            dbcount = 1 # Number of total hits per DB use.
            while dbcount < 4 and random.random() < .8: # Each follow-up has an 80% chance of occurring, up to four total hits.
                atknum += 1
                dbcount += 1
                normalhitcalc(str(atknum), proc, "DB%d" % dbcount)
    else: # If the hit came from a source other than an innate ability, such as an activated item, skip per-ability conditions and check accuracy.
        otherhitcalc(str(atknum), proc, hit)
    return atknum + 1 # Increment the attack counter after each attack hit.

def normalhitcalc(prefix, proc, hit):
    atk = "attack #%s (%s): " % (prefix, hit)
    extralist = []
    crit = False

    if hit == "SS":
        critchance = critrate * 1.5 # critchance differs from critrate in that it can receive per-attack modifiers.
    else:
        critchance = critrate
    
    for o in onhits:
        if random.random() < onhits[o] * proc:
            atk += o
            atk += ", "
            
    for e in extrahits:
        if random.random() < extrahits[e]:
            atk += e
            atk += ", "
            extralist.append(e) # Make a list of all extra hit procs for later use.

    if random.random() < critchance:
            atk += "crit, "
            crit = True
            
    print (atk[0:-2])

    subhit = 0
    for ex in extralist: # Run one of the two functions depending on which type of extra hit proc it was.
        if ex == "Aether": # Aether can proc other extra hit effects but not itself.
            aethercalc(prefix + suffix(subhit), crit)
        else: # Other extra hits can't proc Aether or themselves.
            subcalc(prefix + suffix(subhit), procs[ex], ex)
        subhit += 1

def otherhitcalc(prefix, proc, hit):
    atk = "attack #%s (%s): " % (prefix, hit)
    extralist = []
    crit = False
    
    for o in onhits:
        if random.random() < onhits[o] * proc:
            atk += o
            atk += ", "
            
    for e in extrahits:
        if random.random() < extrahits[e]:
            atk += e
            atk += ", "
            extralist.append(e)

    if random.random() < critrate:
            atk += "crit, "
            crit = True
            
    print (atk[0:-2] + "; hit %.2f" % random.random()) # Since hit rate doesn't really interact with anything, this just prints a float without further calculation.

    subhit = 0
    for ex in extralist:
        if ex == "Aether":
            aethercalc(prefix + suffix(subhit), crit)
        else:
            subcalc(prefix + suffix(subhit), procs[ex], ex)
        subhit += 1

def aethercalc(prefix, crit): # Called only by hitcalc(). Indicates specifically the second hit of an Aether attack.
    atk = "attack #%s (Aether): " % prefix
    extralist = []
    
    for o in onhits:
        if random.random() < onhits[o]:
            atk += o
            atk += ", "
        
    for e in extrahits:
        if e == "Aether":
            continue
        if random.random() < extrahits[e]:
            atk += e
            atk += ", "
            extralist.append(e)

    if crit:
        atk += "crit, "
    
    print(atk[0:-2])

    subhit = 0
    for ex in extralist:
        subcalc(prefix + suffix(subhit), procs[ex], ex)
        subhit += 1

def subcalc(prefix, proc, hit): # Called by either of the above two functions. Cannot Aether or repeat the same type of extra hit.
    atk = "attack #%s (%s): " % (prefix, hit)
    extralist = []
    
    for o in onhits:
        if random.random() < onhits[o] * proc:
            atk += o
            atk += ", "
        
    for e in extrahits:
        if e == "Aether" or e == hit:
            continue
        if random.random() < extrahits[e]:
            atk += e
            atk += ", "
            extralist.append(e)

    if random.random() < critrate:
        atk += "crit, "
                
    print (atk[0:-2] + "; hit %.2f" % random.random())
    
    subhit = 0
    for ex in extralist:
        subcalc(prefix + suffix(subhit), procs[ex], ex)
        subhit += 1

random.seed()

extrahits["Aether"] = SPD / 500
critrate = (SPD / 5 + CRIT_BONUS) / 100

if ULT_ACTIVE: # When Lucina's ultimate ability is active, her chance of activating any of her chance-based effects increases by 50%.
    multiplier = 1.5
    for o in onhits:
        onhits[o] *= multiplier
    for e in extrahits:
        onhits[o] *= multiplier

print ("crit rate = %.2f, ult = %s" % (critrate, ULT_ACTIVE))

atknum = 1

for atk in atks:
    proc = 1.0
    
    if atk in coeffs:
        proc = coeffs[atk]
        
    atknum = hitcheck(atknum, proc, atk)
