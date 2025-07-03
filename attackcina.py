import random

SPD = 115 * 1.28
critbonus = 5
ult = False

atks = ["DB", "DB", "DB"]
coeffs = {} # dict of any proc coeffs on the initial attacks that are != 1, form "index: coeff"
onhits = {"Snake Tail": .05, "Taser": .07, "Runald's Band": .08, "Kjaro's Band": .08, "Tri-Tip Dagger": .15}
extrahits = {"Ukulele": .25}
procs = {"Ukulele": .2}

def suffix(num):
    return chr(97+num)

def hitcheck(current, proc, hit):
    hitname = ""
    
    if hit == "DB":
        hitname = "DB1"
    elif hit in ["DB", "SB", "SS", "BS", "PA", "NPA"]:
        hitname = hit
    
    if hitname != "":
        normalhitcalc(str(current), proc, hitname)
        if hit == "DB":
            dbcount = 1
            while dbcount < 4 and random.random() < .8:
                current += 1
                dbcount += 1
                normalhitcalc(str(current), proc, "DB%d" % dbcount)
    else:
        otherhitcalc(str(current), proc, hit)
    return current + 1

def normalhitcalc(prefix, proc, hit):
    atk = "attack #%s (%s): " % (prefix, hit)
    extralist = []
    crit = False

    if hit == "SS":
        critchance = critrate * 1.5 # critchance is for the specific attack
    else:
        critchance = critrate # critrate is lucina's general purpose crit rate
    
    for o in onhits:
        if random.random() < onhits[o] * proc:
            atk += o
            atk += ", "
            
    for e in extrahits:
        if random.random() < extrahits[e]:
            atk += e
            atk += ", "
            extralist.append(e) #make list of all extra hit procs

    if random.random() < critchance:
            atk += "crit, "
            crit = True
            
    print (atk[0:-2])

    subhit = 0
    for ex in extralist: #run one of the two functions depending on which proc
        if ex == "Aether":
            aethercalc(prefix + suffix(subhit), crit)
        else:
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
            extralist.append(e) #make list of all extra hit procs

    if random.random() < critrate:
            atk += "crit, "
            crit = True
            
    print (atk[0:-2] + "; hit %.2f" % random.random())

    subhit = 0
    for ex in extralist: #run one of the two functions depending on which proc
        if ex == "Aether":
            aethercalc(prefix + suffix(subhit), crit)
        else:
            subcalc(prefix + suffix(subhit), procs[ex], ex)
        subhit += 1

def aethercalc(prefix, crit): # triggered only from hitcalc, can only be hit 2 of aether
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

def subcalc(prefix, proc, hit): # triggered from above two, cannot aether
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
extrahits["Aether"] = SPD/500
critrate = (SPD/5 + critbonus)/100

if ult:
    for o in onhits:
        onhits[o] *= 1.5
    for e in extrahits:
        onhits[o] *= 1.5

print ("crit rate = %.2f, ult = %s" % (critrate, ult))

current = 1

for atk in atks:
    proc = 1.0
    
    if atk in coeffs:
        proc = coeffs[atk]
        
    current = hitcheck(current, proc, atk)
