##Variables
partOne=True
partTwo=True
partThree=True
abilities = {"Nova Bomb": 1, "Axion Bolt": 2}
inventory = {"MIDA": False, "LDR": False}
Thrall=5
thrallTimer=5
Ogre=10
midaHit=0
ldrHit=0

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
    if inputOne in ["check equipment", "equipment", "look equipment", "inspect equipment"]:
        print("You are armed with a MIDA Multi-Tool Scout Rifle and a LDR-5001 Sniper Rifle. Your Ghost is also with you. He can answer any questions you may have.")

    elif inputOne in ["check ghost", "ghost", "look ghost", "inspect ghost"]:
        print("Your ghost is... unsurprisingly chatty. He makes you aware of your current alignment: The Voidwalker. A Voidwalker Warlock can throw Axion Bolts, unique grenades that spawn two bolts which seek out hostiles. You can also create what's colloquially known as a 'Nova Bomb', a large ball of Void energy that explodes once thrown.")

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
    if inputTwo in ["check equipment", "equipment", "look equipment", "inspect equipment"]:
        print("You are armed with a MIDA Multi-Tool Scout Rifle and a LDR-5001 Sniper Rifle. Your Ghost is also with you. He can answer any questions you may have.")

    elif inputTwo in ["ready weapon", "weapon", "equip weapon"]:
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

    elif inputTwo in ["ghost rune", "check rune", "rune", "inspect rune", "look rune"]:
        partTwo=False

    else:
        print("-Invalid action, please try again-")

print("Your Ghost begins deciphering the rune. He estimates it'll take a minute. Halfway through you begin to feel eyes gazing from the shadows. A Thrall blindly screeches at you, piercing your ears. Three more jump out alongside it and dash towards you.")
#Part Three (Thrall ambush)
while partThree:
    if thrallTimer != 0:
        print("You can:")
        print("-Ready weapon (if not already ready)-")
        print("-Fire equipped weapon-")
        print("-Use a Void ability-")
        print("Thrall left: " , Thrall)

        inputThree=input("What will you do? >>> ").lower()
        if inputThree in ["ready weapon", "equip weapon"]:
            inputWeapon=input("Which weapon do you equip? >>> ").lower()
            if inputWeapon in ["mida", "multi-tool", "mida multi-tool", "scout rifle"]:
                print("MIDA Multi-Tool equipped.")
                inventory["MIDA"] = True
                inventory["LDR"] = False
                thrallTimer -= 1

            elif inputWeapon in ["ldr", "ldr-5001", "sniper rifle"]:
                print("LDR-5001 equipped.")
                inventory["MIDA"] = False
                inventory["LDR"] = True
                thrallTimer -= 1

            else:
                print("No weapon equipped.")

        elif inputThree in ["use void", "void", "use void ability", "use ability"]:
            inputVoid=input("Which ability do you use? >>> ").lower()
            if inputVoid in ["axion bolt", "bolt", "grenade"]:
                if Thrall != 1:
                    print("Your Axion Bolt is flung in front of you, roughly in the direction of the incoming Thrall. 2 bolts spawn in the radius and seek out two of the Thrall. They erupt in a void explosion.")
                    Thrall -= 2
                    print(Thrall)
                    thrallTimer -= 2
                    abilities["Axion Bolt"] -= 1
                    print(abilities)

                if Thrall == 1:
                    print ("Your Axion Bolt is flung in front of you, in the direction of the last Thrall. It stumbles at the sight of your grenade, aware of its power. The bolt promptly consumes the creature, killing it.")
                    Thrall -= 1
                    abilities["Axion Bolt"] -= 1
                    print(abilities)


        elif inputThree in ["fire weapon", "fire", "use weapon"]:
            if inventory["MIDA"] == True:
                if Thrall >= 3:
                    midaHit.randint(1,3)
                    print("You fire off a volley of shots, killing " , midaHit , " Thrall. Their heads explode in a fountain of inky darkness.")
                    Thrall -= midaHit
                    thrallTimer -= 1
                if Thrall == 2:
                    midaHit.randint(1,2)
                    print("You fire off a volley of shots, killing " , midaHit , " Thrall. Their heads explode in a fountain of inky darkness.")
                    Thrall -= midaHit
                    thrallTimer -= 1
                if Thrall == 1:
                    midaHit = 1
                    print("The last Thrall scuttles towards you, and with a well placed shot, you pop off its head. You reload your clip")



        else:
            print("-Invalid action, please try again-")

    else:
        print("The Thrall close in and incapacitate you, leaving your corpse mauled and tattered after feasting on your light.")
        print("THE DARKNESS CONSUMED YOU")
        thrallTimer = 5
        continue
