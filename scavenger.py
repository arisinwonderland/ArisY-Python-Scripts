import random

def genitem(type):
        common = ["Armor-Piercing Rounds", "Backup Magazine", "Crowbar", "Focus Crystal", "Gasoline", "Lens-Maker’s Glasses", "Meat Nugget", "Medkit", "Monster Tooth", "Paul’s Goat Hoof", "Soldier’s Syringe", "Sticky Bomb", "Stun Grenade", "Taser", "Topaz Brooch", "Tougher Times", "Tri-Tip Dagger"]
        uncommon = ["Arms Race", "AtG Missile Launcher Mk. 1", "Bandolier", "Berserker’s Pauldron", "Boxing Gloves", "Chronobauble", "Dead Man’s Foot", "Death Mark", "Fuel Cell", "Golden Gun", "Harvester’s Scythe", "Hopoo Feather", "Infusion", "Kjaro’s Band", "Runald’s Band", "Leeching Seed", "Old Guillotine", "Predatory Instincts", "Red Whip", "Time Keeper’s Secret", "Ukulele", "Warbanner", "War Horn", "Will-o’-the-Wisp"]
        legendary = ["57 Leaf Clover", "Aegis", "Alien Head", "Brilliant Behemoth", "Ceremonial Dagger", "Dio’s Best Friend", "Happiest Mask", "Hardlight Afterburner", "Heaven Cracker", "Interstellar Desk Plant", "Old Jack-In-The-Box", "Permafrost", "Rejuvenation Rack", "Shattering Justice (Light)", "Soulbound Catalyst", "Thallium", "Unstable Tesla Coil", "Wake of Vultures"]
        equipment = ["Blast Shower", "Crudely Drawn Buddy", "Disposable Missile Launcher", "Foreign Fruit", "Glowing Meteorite", "Jade Elephant", "Ocular HUD", "Rotten Brain", "Sawmerang", "Snowglobe", "The Back-up"]
        types = [common, uncommon, legendary, equipment]

        return random.choice(types[type])

def genscav(items):
        blacklist = ["Armor-Piercing Rounds", "Bandolier", "Ceremonial Dagger", "Glowing Meteorite", "Hopoo Feather", "Old Guillotine", "Stun Grenade", "Wake of Vultures", ""]
        item = ""
        for i in range (0,3):
            while item in items or item in blacklist:
                    item = genitem(0)
            items[item] = 3

        for i in range (0,2):
            while item in items or item in blacklist:
                    item = genitem(1)
            items[item] = 2

        while item in items or item in blacklist:
             item = genitem(2)
        items[item] = 1
        
        while item in items or item in blacklist:
             item = genitem(3)
        items[item] = 1

def genbag(items):
        size = random.randint(8,12)
        print(size)
        for i in range (0,size):
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

random.seed()
items = {}
bag = True

if bag:
        genbag(items)
else:
        genscav(items)


for i in items:
    print(i + ": " + str(items[i]))
