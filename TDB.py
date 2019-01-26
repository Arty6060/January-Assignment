##Variables
partOne=True
partTwo=True
partThree=True
partFour=True
partFive=True
partSix=True
abilities = {"Nova Bomb": 1, "Axion Bolt": 2}
inventory = {"MIDA": False, "LDR": False}
Thrall=5
battleTwoEnemies = {"AcolyteOne": 2, "AcolyteTwo": 2, "Knight": 5}
Ogre=15
battleOne=6
battleTwo=4
cover=False
midaHit=0
ldrHit=0
import random

##Intro
print("---The Dark Below: A Destiny Text Adventure---")

print("You land just outside a Hive tomb. Confronted by a construct of chitin and stone, you see a rune locking the doors leading to the tomb. You take pause to weigh your options.")

##Part One (Beginning of the game)
while partOne:
    print("You can:")
    print("-Check Equipment-")
    print("-Check your Ghost-")
    print("-Approach the door-")
    inputOne=input("What will you do? >>> ").lower()
            ##Equipment check
    if inputOne in ["check equipment", "equipment", "look equipment", "inspect equipment"]:
        print("You are armed with a MIDA Multi-Tool Scout Rifle and a LDR-5001 Sniper Rifle. Your Ghost is also with you. He can answer any questions you may have.")
            ##Ghost check
    elif inputOne in ["check ghost", "ghost", "look ghost", "inspect ghost"]:
        print("Your ghost is... unsurprisingly chatty. He makes you aware of your current alignment: The Voidwalker. A Voidwalker Warlock can throw Axion Bolts, unique grenades that spawn two bolts which seek out hostiles. You can also create what's colloquially known as a 'Nova Bomb', a large ball of Void energy that explodes once thrown.")
            ##Door check
    elif inputOne in ["approach door", "go to door", "door", "check door", "look door", "inspect door"]:
        print("You approach the door, the rune humming to you as you close in. You're not as versed on Hive magic as you should be, but your Ghost could possibly decipher the rune...")
        partOne=False

    else:
        print("-Invalid action, please try again-")

##Part Two (Investigating the door)
while partTwo:
    print("You can:")
    print("-Let your Ghost check the Rune-")
    print("-Check equipment-")
    print("-Ready weapon-")
    inputTwo=input("What will you do? >>> ").lower()

            ##Equipment
    if inputTwo in ["check equipment", "equipment", "look equipment", "inspect equipment"]:
        print("You are armed with a MIDA Multi-Tool Scout Rifle and a LDR-5001 Sniper Rifle. Your Ghost is also with you. He can answer any questions you may have.")

            ##Ready Weapon tree
    elif inputTwo in ["ready weapon","ready", "weapon", "equip weapon"]:
        inputWeapon=input("Which weapon do you equip? >>> ").lower()
        if inputWeapon in ["mida", "multi-tool", "mida multi-tool", "scout rifle"]:
            print("MIDA Multi-Tool equipped.")
            inventory["MIDA"] = True
            inventory["LDR"] = False
        elif inputWeapon in ["ldr", "ldr-5001", "sniper rifle"]:
            print("LDR-5001 equipped.")
            inventory["MIDA"] = False
            inventory["LDR"] = True
        else:
            print("No weapon equipped.")

            ##Ghost Rune
    elif inputTwo in ["ghost rune", "check rune", "rune", "inspect rune", "look rune"]:
        partTwo=False

    else:
        print("-Invalid action, please try again-")

print("Your Ghost begins deciphering the rune. He estimates it'll take a minute. Halfway through you begin to feel eyes gazing from the shadows. A Thrall blindly screeches at you, piercing your ears. Four more jump out alongside it and dash towards you.")
#Part Three (Thrall ambush)
while partThree:

    if Thrall <= 0:
        print("You've eliminated all the Thrall, and your Ghost has finished dismantling the rune. The chamber door creeks open. You pass through.")
        partThree=False

    elif battleOne != 0:
        print("You can:")
        print("-Ready weapon (if not already ready)-")
        print("-Fire equipped weapon-")
        print("-Use a Void ability-")
        print("Thrall left: " , Thrall)


        inputThree=input("What will you do? >>> ").lower()
                ##Ready Weapon tree
        if inputThree in ["ready weapon", "equip weapon", "ready"]:
            inputWeapon=input("Which weapon do you equip? >>> ").lower()
            if inputWeapon in ["mida", "multi-tool", "mida multi-tool", "scout rifle"]:
                print("MIDA Multi-Tool equipped.")
                inventory["MIDA"] = True
                inventory["LDR"] = False
                battleOne-=1
            elif inputWeapon in ["ldr", "ldr-5001", "sniper rifle"]:
                print("LDR-5001 equipped.")
                inventory["MIDA"] = False
                inventory["LDR"] = True
                battleOne-=1
            else:
                print("No weapon equipped.")

                ##Void Ability tree
        elif inputThree in ["use void", "void", "use void ability", "use ability"]:
            inputVoid=input("Which ability do you use? >>> ").lower()
            if inputVoid in ["axion bolt", "bolt", "grenade"]:
                if abilities["Axion Bolt"]!=0:
                    if Thrall != 1:
                        print("Your Axion Bolt is flung in front of you, roughly in the direction of the incoming Thrall. 2 bolts spawn in the radius and seek out two of the Thrall. They erupt in a void explosion.")
                        Thrall -= 2
                        battleOne -= 2
                        abilities["Axion Bolt"] -= 1
                        print(abilities)
                        continue
                    elif Thrall == 1:
                        print ("Your Axion Bolt is flung in front of you, in the direction of the last Thrall. It stumbles at the sight of your grenade, aware of its power. The bolt promptly consumes the creature, killing it.")
                        Thrall -= 1
                        abilities["Axion Bolt"] -= 1
                        print(abilities)
                        continue
                elif abilities["Axion Bolt"]==0:
                    print("Your Axion Bolt charges are depleted")
            elif inputVoid in ["nova bomb", "nova", "bomb", "void bomb", "one round purple boi"]:
                print("You jump up and summon an intense orb of Void energy between your palms, proppelling it towards the incoming Thrall. They don't stand a chance. The bomb decimates them, leaving no trace.")
                Thrall -= 5
                abilities["Nova Bomb"]-=1
            else:
                print("-Invalid action, please try again-")

                    ##Fire Weapon tree
        elif inputThree in ["fire weapon", "fire", "use weapon"]:
            if inventory["MIDA"] == True:
                if Thrall >= 3:
                    midaHit = random.randint(1, 3)
                    print("You fire off a volley of shots, killing " , midaHit , " Thrall. Their heads explode in a fountain of inky darkness.")
                    Thrall -= midaHit
                    battleOne -= 1
                    continue
                elif Thrall == 2:
                    midaHit = random.randint(1, 2)
                    print("You fire off a volley of shots, killing " , midaHit , " Thrall. Their heads explode in a fountain of inky darkness.")
                    Thrall -= midaHit
                    battleOne -= 1
                    continue
                elif Thrall == 1:
                    print("The last Thrall scuttles towards you, and with a well placed shot, you pop off its head. You reload your clip.")
                    Thrall -= 1
                    continue
            elif inventory["LDR"] == True:
                if Thrall != 1:
                    print("You nail one of the Thrall in the head with a clean shot. Dark essence pours out as it dissolves from reality.")
                    Thrall -= 1
                    battleOne -= 1
                    continue
                elif Thrall == 1:
                    print("The last Thrall charges towards you, and without scoping in, you take a point blank shot at its head. Your bullet rings loudly through the valley. You reload your clip.")
                    Thrall -= 1
                    continue

            else:
                print("-You have no weapon equipped-")

        else:
            print("-Invalid action, please try again-")

    else:
        print("The Thrall close in and incapacitate you, leaving your corpse mauled and tattered after feasting on your light.")
        print("-THE DARKNESS CONSUMED YOU-")
        battleOne = 6
        Thrall = 5
        abilities["Axion Bolt"] = 2
        abilities["Nova Bomb"] = 1
        continue

print("You move slowly through the tomb, past the chamber. All of a sudden you see two blaster shots from opposite directions coming towards you. You dodge out of the way, and get a glimpse at your foes. Two Hive Acolytes and a Knight.")
##Part Four (Acolyte battle)
while partFour:
    if battleTwoEnemies["Knight"]<=0 and battleTwoEnemies["AcolyteOne"]<=0 and battleTwoEnemies["AcolyteTwo"]<=0:
            print("You've cleared the wave of enemies. You make your way deeper into the tomb.")
            partFour=False

    elif battleTwo == 0:
        print("Your adverisaries overwhelm you, and your light fades.")
        print("-THE DARKNESS CONSUMED YOU-")
        battleTwo=3
        cover=False
        battleTwoEnemies["Knight"]=5
        battleTwoEnemies["AcolyteOne"]=2
        battleTwoEnemies["AcolyteTwo"]=2
        abilities["Axion Bolt"] = 2
        abilities["Nova Bomb"] = 1
        continue


    elif battleTwo != 0:
        print("You can:")
        print("-Ready Weapon-")
        print("-Fire Weapon-")
        print("-Use Void Ability-")
        print("-Talk to your Ghost-")
        print("-Take Cover-")
        battleTwo-=1
        inputFour = input("What will you do? >>> ").lower()

        if inputFour in ["ghost", "talk ghost", "talk to ghost", "inspect ghost", "examine ghost"]:
            if cover==False:
                print("Your Ghost quickly assesses the situation. It suggests you take cover to give you more time to plan a counter-attack.")
                continue
            else:
                print("Your Ghost thinks taking down the Knight will be challenging, and suggests focusing your fire on it with a powerful weapon or ability.")
                continue


            ##Ready Weapon tree
        if inputFour in ["ready weapon", "equip weapon", "ready"]:
            inputWeapon=input("Which weapon do you equip? >>> ").lower()
            if inputWeapon in ["mida", "multi-tool", "mida multi-tool", "scout rifle"]:
                print("MIDA Multi-Tool equipped.")
                inventory["MIDA"] = True
                inventory["LDR"] = False
            elif inputWeapon in ["ldr", "ldr-5001", "sniper rifle"]:
                print("LDR-5001 equipped.")
                inventory["MIDA"] = False
                inventory["LDR"] = True
            else:
                print("No weapon equipped.")

                ##Cover tree
        elif inputFour in ["cover", "take cover", "get into cover", "go to cover"]:
            if cover==False:
                print("You hover towards a pillar to your right. It looks thick enough to absorb a lot of damage from enemy fire.")
                battleTwo += 3
                cover=True
            else:
                print("You're already in cover.")

                ##Void Ability tree
        elif inputFour in ["use void", "void", "use void ability", "use ability"]:
            inputVoid=input("Which ability do you use? >>> ").lower()
            if inputVoid in ["axion bolt", "bolt", "grenade"]:
                if abilities["Axion Bolt"]!=0:
                    inputTarget=input("Do you target the Acolytes or the Knight? >>> ").lower()
                    if inputTarget in ["acolytes"]:
                        if battleTwoEnemies["AcolyteOne"]<=0 and battleTwoEnemies["AcolyteTwo"]<=2:
                            print("Your Axion Bolt hits the remaining Acolyte. They explode with Void energy.")
                            battleTwoEnemies["AcolyteTwo"]-=2
                            abilities["Axion Bolt"]-=1
                            continue
                        elif battleTwoEnemies["AcolyteOne"]<=2 and battleTwoEnemies["AcolyteTwo"]<=0:
                            print("Your Axion Bolt hits the remaining Acolyte. They explode with Void energy.")
                            battleTwoEnemies["AcolyteOne"]-=2
                            abilities["Axion Bolt"]-=1
                            continue
                        elif battleTwoEnemies["AcolyteOne"]<=2 and battleTwoEnemies["AcolyteTwo"]<=2:
                            if battleTwoEnemies["Knight"]>=4:
                                print ("Your Axion Bolt hits both Acolytes. It's just enough to kill them. The void explosion shrapnels towards the Knight, scraping its armour")
                                battleTwoEnemies["AcolyteOne"]-=2
                                battleTwoEnemies["AcolyteTwo"]-=2
                                battleTwoEnemies["Knight"]-=1
                                abilities["Axion Bolt"]-=1
                                continue
                            elif battleTwoEnemies["Knight"]<=3:
                                print ("Your Axion Bolt hits both Acolytes. It's just enough to kill them. They explode with void energy.")
                                battleTwoEnemies["AcolyteOne"]-=2
                                battleTwoEnemies["AcolyteTwo"]-=2
                                abilities["Axion Bolt"]-=1
                                continue
                        elif battleTwoEnemies["AcolyteOne"]<=0 and battleTwoEnemies["AcolyteTwo"]<=0:
                            print("There are no Acolytes left.")
                            continue
                    elif inputTarget in ["knight"]:
                        if battleTwoEnemies["Knight"]>=3:
                            print("The Axion Bolt lets out one charge, targeted at the Knight. It makes contact, but only staggers the Knight. It boasts by swinging its sword.")
                            battleTwoEnemies["Knight"]-=2
                            abilities["Axion Bolt"]-=1
                            continue
                        if battleTwoEnemies["Knight"]<=2:
                            print("The Axion Bolt lets out on charge, targeted at the Knight. The creature explodes with Void energy and no trace is left of it")
                            battleTwoEnemies["Knight"]-=2
                            abilities["Axion Bolt"]-=1
                elif abilities["Axion Bolt"]==0:
                    print("Your Axion Bolt charges are depleted.")
            elif inputVoid in ["nova bomb", "nova", "bomb", "void bomb", "one round purple boi"]:
                if abilities["Nova Bomb"]!=0:
                    if battleTwoEnemies["Knight"]>=4 and battleTwoEnemies["AcolyteOne"]>=1 and battleTwoEnemies["AcolyteTwo"]>=1:
                        print("You summon a sphere of pure void energy, and launch it towards your foes. The Acolytes are evicerated, and the Knight is also badly wounded, but is still able to fight.")
                        battleTwoEnemies["Knight"]-=3
                        battleTwoEnemies["AcolyteOne"]-=2
                        battleTwoEnemies["AcolyteTwo"]-=2
                        abilities["Nova Bomb"]-=1
                        continue
                    if battleTwoEnemies["Knight"]>=4 and battleTwoEnemies["AcolyteOne"]<=0 and battleTwoEnemies["AcolyteTwo"]<=0:
                        print("You summon a sphere of pure void energy, and launch it towards your foe. The Knight takes the full force of your Nova Bomb, but is still just strong enough to keep fighting.")
                        battleTwoEnemies["Knight"]-=3
                        continue
                    if battleTwoEnemies["Knight"]<=3 and battleTwoEnemies["AcolyteOne"]>=1 and battleTwoEnemies["AcolyteTwo"]>=1:
                        print("You summon a sphere of pure void energy, and launch it towards your foes. It obliterates them completely, consuming them within a purple dome of light.")
                        battleTwoEnemies["Knight"]-=3
                        battleTwoEnemies["AcolyteOne"]-=2
                        battleTwoEnemies["AcolyteTwo"]-=2
                        abilities["Nova Bomb"]-=1
                        continue
                    if battleTwoEnemies["Knight"]<=3 and battleTwoEnemies["AcolyteOne"]<=0 and battleTwoEnemies["AcolyteTwo"]<=0:
                        print("You summon a sphere of pure void energy, and launch it towards your foe. The Knight is consumed by your Nova Bomb completely, and explodes into nothing.")
                        battleTwoEnemies["Knight"]-=3
                        abilities["Nova Bomb"]-=1
                        continue
                    if battleTwoEnemies["Knight"]<=0 and battleTwoEnemies["AcolyteOne"]>=1 and battleTwoEnemies["AcolyteTwo"]>=1:
                        print("You summon a sphere of pure void energy, and launch it towards your foes. The remaining Acolytes are evicerated with no trace left.")
                        battleTwoEnemies["AcolyteOne"]-=2
                        battleTwoEnemies["AcolyteTwo"]-=2
                        abilities["Nova Bomb"]-=1
                        continue

                ##Fire Weapon tree
        elif inputFour in ["fire weapon", "fire", "use weapon", "weapon"]:
            if inventory["MIDA"] == True:
                print("Enemies remaining: ")
                if battleTwoEnemies["Knight"]>=1:
                    print("Knight")
                if battleTwoEnemies["AcolyteOne"]>=1:
                    print("Acolyte One")
                if battleTwoEnemies["AcolyteTwo"]>=1:
                    print("Acolyte Two")
                inputTarget=input("Who do you target? >>> ").lower()
                if inputTarget in ["knight"]:
                    midaHit=random.randint(1,3)
                    battleTwoEnemies["Knight"]-=midaHit
                    if battleTwoEnemies["Knight"]>=1:
                        print("You batter the Knight with a barrage of shots from your MIDA, but it's still standing.")
                        continue
                    elif battleTwoEnemies["Knight"]<=0:
                        print("You batter the Knight with a barrage of shots from your MIDA, and it collapses. You reload your clip.")
                        continue
                elif inputTarget in ["acolyte one", "acolyteone", "acolyte1", "acolyte 1", "one", "1", "thing 1"]:
                    midaHit=random.randint(1,3)
                    battleTwoEnemies["AcolyteOne"]-=midaHit
                    if battleTwoEnemies["AcolyteOne"]>=1:
                        print("You batter the Acolyte with a barrage of shots from your MIDA, but it's still standing.")
                        continue
                    elif battleTwoEnemies["AcolyteOne"]<=0:
                        print("You batter the Acolyte with a barrage of shots from your MIDA, and it collapses. You reload your clip.")
                        continue
                elif inputTarget in ["acolyte two", "acolytetwo", "acolyte2", "acolyte 2", "two", "2", "thing 2"]:
                    midaHit=random.randint(1,3)
                    battleTwoEnemies["AcolyteTwo"]-=midaHit
                    if battleTwoEnemies["AcolyteTwo"]>=1:
                        print("You batter the Acolyte with a barrage of shots from your MIDA, but it's still standing.")
                        continue
                    elif battleTwoEnemies["AcolyteTwo"]<=0:
                        print("You batter the Acolyte with a barrage of shots from your MIDA, and it collapses. You reload your clip.")
                        continue
                else:
                    print("-Invalid action-")
                    continue
            elif inventory["LDR"] == True:
                print("Enemies remaining: ")
                if battleTwoEnemies["Knight"]>=1:
                    print("Knight")
                if battleTwoEnemies["AcolyteOne"]>=1:
                    print("Acolyte One")
                if battleTwoEnemies["AcolyteTwo"]>=1:
                    print("Acolyte Two")
                inputTarget=input("Who do you target? >>> ").lower()
                if inputTarget in ["knight"]:
                    if battleTwoEnemies["Knight"]>=4:
                        battleTwoEnemies["Knight"]-=3
                        print("You nail the Knight in the head with a clean shot, but it's still standing.")
                        continue
                    elif battleTwoEnemies["Knight"]<=3:
                        battleTwoEnemies["Knight"]-=3
                        print("You nail the Knight in the head with a clean shot, and it collapses in a pool of darkness.")
                        continue
                elif inputTarget in ["acolyte one", "acolyteone", "acolyte1", "acolyte 1", "one", "1", "thing 1"]:
                    if battleTwoEnemies["AcolyteOne"]>=1:
                        battleTwoEnemies["AcolyteOne"]-=2
                        print("You scope in and hit the Acolyte, and it succumbs to its injury.")
                        continue
                elif inputTarget in ["acolyte two", "acolytetwo", "acolyte2", "acolyte 2", "two", "2", "thing 2"]:
                    if battleTwoEnemies["AcolyteTwo"]>=1:
                        battleTwoEnemies["AcolyteOne"]-=2
                        print("You scope in and hit the Acolyte, and it succumbs to its injury.")
                        continue

                else:
                    print("-Invalid action-")
                    continue
            else:
                print("-You have no weapon equipped-")
        else:
            print("-Invalid action, please try again-")


print("You arrive inside the tomb's Throne Room. There you see a locked chest, with four shapes portruding from it. It looks like they function as the keys to this chest, but you aren't certain.")
print("-All abilites have been regenerated-")
abilities["Axion Bolt"]=2
abilities["Nova Bomb"]=1
print(abilities)
