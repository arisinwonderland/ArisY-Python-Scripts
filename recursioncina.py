import random

SPD = 115 * 1.28
critbonus = 5
showhit = True
ult = False

atks = ["SB", "DB1", "DB2", "DB3", "DB4", "PA1", "PA2"]
onhits = {"Snake Tail": .05, "Taser": .07, "Runald's Band": .08, "Kjaro's Band": .08, "Tri-Tip Dagger": .15}
extrahits = {"Ukulele": .25}
procs = {"Ukulele": .2}
coeffs = {} # dict of any proc coeffs that are != 1, in form index: coeff

def suffix(num):
    return chr(97+num)

def hitchance():
    if showhit:
        return "; hit %.2f" % random.random()
    else:
        return ""

def hitcalc(prefix, proc, hit): # triggered only from main, can aether
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
            
    if random.random() < critchance:
            atk += "crit, "
            crit = True
            
    print (atk[0:-2] + hitchance())

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
    
    print (atk[0:-2] + hitchance())

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

    print (atk[0:-2] + hitchance())
    
    subhit = 0
    for ex in extralist:
        subcalc(prefix + suffix(subhit), procs[ex], ex)
        subhit += 1

random.seed()
extrahits["Aether"] = SPD/500
critchance = (SPD/5 + critbonus)/100

if ult:
    for o in onhits:
        onhits[o] *= 1.5
    for e in extrahits:
        onhits[o] *= 1.5

hits = []

for atk in atks:
    hits.append((atk, 1.0))

current = 1

for hit in hits:
    if hit[0] in coeffs:
        hit[1] = coeffs[hit[0]]
    hitcalc(str(current), hit[1], hit[0])
    current += 1
