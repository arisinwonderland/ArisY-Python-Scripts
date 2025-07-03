import random

random.seed()

SPD = 165
ult = False

onhits = {"Snake Tail": .05, "Taser": .07, "Tri-Tip Dagger": .15, "Ukulele": .25}
onhits["crit"] = SPD/500

if ult:
    for o in onhits:
        onhits[o] *= 1.5


aether = False
i = 0

while i < 10:
    atk = "attack #%s (hit %.2f): " % (str(i + 1 + aether/2), random.random())
    for o in onhits:
        if o == "crit" and aether:
            continue
        if random.random() < onhits[o]:
            atk += o
            atk += ", "
    if aether == False and random.random() < SPD/500:
        aether = True
        atk += "Aether, "
    else:
        aether = False
        i += 1
    print (atk[0:-2])
