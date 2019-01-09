##Variables
Super=1
Grenade=2
Thrall=5
Ogre=10

##Intro
print("---The Dark Below: A Destiny Text Adventure---")

print("You land just outside a Hive tomb. Confronted by a construct of chitin and stone, you see a rune locking the doors leading to the tomb. You take pause to weigh your options.")

##Start of Loop (Beginning of the game)
while True:
    print("You can:")
    print("-Check Equipment-")
    print("-Check your Ghost-")
    print("-Approach the door-")
    inputOne=input("What will you do? >>> ").lower()
    if inputOne in ["check equipment", "equipment", "look equipment", "inspect equipment"]:
        print("You are armed with a MIDA Multi-Tool Scout Rifle and a LDR-5001 Sniper Rifle. Your Ghost is also with you. He can answer any questions you may have.")

    elif inputOne in ["check ghost", "ghost", "look ghost", "inspect ghost"]:
        print("Your ghost is... unsurprisingly chatty. He makes you aware of your current alignment: The Voidwalker. A Voidwalker Warlock can throw Axion Bolt Grenades, as well as a large ball of concentrated Void energy, more colloquially referred to as the 'Nova Bomb'.")

    elif inputOne in ["approach door", "go to door", "door", "check door", "look door", "inspect door"]:
        print("You approach the door, the rune humming to you as you close in. You're not as versed on Hive magic as you should be, but your Ghost could possibly decipher the rune...")
        ##Loop Two (Investigating the door)
        print("You can:")
        print("-Let your Ghost check the Rune-")
        print("-Check Equipment-")
        print("-Ready weapon-")
        inputTwo=input("What will you do? >>> ").lower()
        if inputTwo in ["check equipment", "equipment", "look equipment", "inspect equipment"]:
            print("You are armed with a MIDA Multi-Tool Scout Rifle and a LDR-5001 Sniper Rifle. Your Ghost is also with you. He can answer any questions you may have.")

        else:
            print("-Invalid action, please try again-")

    else:
        print("-Invalid action, please try again-")
