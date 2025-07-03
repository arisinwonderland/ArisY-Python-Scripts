import random

def genitem(type):
        common = ["Armor-Piercing Rounds", "Backup Magazine", "Crowbar", "Focus Crystal", "Gasoline", "Lens-Maker’s Glasses", "Meat Nugget", "Medkit", "Monster Tooth", "Paul’s Goat Hoof", "Soldier’s Syringe", "Sticky Bomb", "Stun Grenade", "Taser", "Topaz Brooch", "Tougher Times", "Tri-Tip Dagger"]
        uncommon = ["Arms Race", "AtG Missile Launcher Mk. 1", "Bandolier", "Berserker’s Pauldron", "Boxing Gloves", "Chronobauble", "Dead Man’s Foot", "Death Mark", "Fuel Cell", "Golden Gun", "Harvester’s Scythe", "Hopoo Feather", "Infusion", "Kjaro’s Band", "Runald’s Band", "Leeching Seed", "Old Guillotine", "Predatory Instincts", "Red Whip", "Time Keeper’s Secret", "Ukulele", "Will-o’-the-Wisp"]
        legendary = ["57 Leaf Clover", "Aegis", "Alien Head", "Brilliant Behemoth", "Ceremonial Dagger", "Dio’s Best Friend", "Happiest Mask", "Hardlight Afterburner", "Heaven Cracker", "Interstellar Desk Plant", "Old Jack-In-The-Box", "Permafrost", "Rejuvenation Rack", "Shattering Justice (Light)", "Soulbound Catalyst", "Thallium", "Unstable Tesla Coil", "Wake of Vultures"]
        equipment = ["Blast Shower", "Crudely Drawn Buddy", "Disposable Missile Launcher", "Foreign Fruit", "Glowing Meteorite", "Jade Elephant", "Ocular HUD", "Rotten Brain", "Sawmerang", "Snowglobe", "The Back-up"]
        types = [common, uncommon, legendary, equipment]

        return random.choice(types[type])

def genset():
    items = {}
    for i in range (0,10):
                r = random.random()
                if r < .63:
                        item = genitem(0)
                        if item in items:
                                items[item] += 1
                        else:
                                items[item] = 1
                elif r < .9:
                        item = genitem(1)
                        if item in items:
                                items[item] += 1
                        else:
                                items[item] = 1
                elif r < .99:
                        item = genitem(3)
                        if item in items:
                                items[item] += 1
                        else:
                                items[item] = 1
                else:
                        item = genitem(2)
                        if item in items:
                                items[item] += 1
                        else:
                                items[item] = 1
    for i in items:
                print(i + ": " + str(items[i]))
    print()
    
random.seed()
party = ["Lucina", "Hilda", "Hope", "Khith", "Beelzebub"]

for char in party:
    print(char)
    genset()
