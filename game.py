
day = 1
health = 100
radiation = 0
ammo = 10
caps = 50


ammo_spent = 3
radiation_increase = 15
health_damage = 30
day_increase = 1
passive_radiation_increase = 5
caps_increase = 20


while health > 0 and radiation < 100 and day <= 7:
    print("-" * 50)
    print(
        f"DAY: {day} | HP: {health} | RAD: {radiation}% | AMMO: {ammo} | CAPS: {caps}")
    print("-" * 50)

    choice = input("What do you want to do today?\nA - Enter the Ruins (Dangerous Loot)\nB - Go to Merchant Camp (Trade)\nC - Sleep in Safehouse (Rest)\n> ").lower().strip()

    while choice not in ["a", "b", "c"]:
        choice = input(
            "Please make a valid choice (A, B, C): ").lower().strip()

    if choice == "a":

        if ammo >= ammo_spent:
            ammo -= ammo_spent
            radiation += radiation_increase
            caps += caps_increase
            print("Action: You looted the ruins, but gained some radiation.")
        else:
            health -= health_damage
            print("Action: You ran out of ammo during a fight and took heavy damage!")

    elif choice == "b":
        items = input(
            "1. Buy Stimpack (30 Caps = +40 HP)\n2. Buy Rad-Away (40 Caps = -30 Rads)\n3. Buy Both\n> ").strip()

        if items == "1" and caps >= 30:
            health += 40
            caps -= 30
            if health > 100:
                health = 100
            print("Action: Bought Stimpack.")
        elif items == "2" and caps >= 40:
            radiation -= 30
            caps -= 40
            if radiation < 0:
                radiation = 0
            print("Action: Bought Rad-Away.")
        elif items == "3" and caps >= 70:
            health += 40
            radiation -= 30
            caps -= 70
            if health > 100:
                health = 100
            if radiation < 0:
                radiation = 0
            print("Action: Bought Both.")
        else:

            print(
                "Action: Not enough caps or invalid choice! The merchant kicks you out.")

    elif choice == "c":

        health += 20
        if health > 100:
            health = 100
        print("Action: You rested well and recovered some health.")

    day += day_increase
    radiation += passive_radiation_increase


print("\n" + "=" * 50)
if health <= 0:
    print("GAME OVER: You became mutant food in the wasteland...")
elif radiation >= 100:
    print("GAME OVER: You mutated and lost your mind...")
elif day > 7:
    print("VICTORY: Congratulations, you reached the extraction chopper!")
print("=" * 50)
