
name = input("Enter your name: ")

print("\nWelcome to the Adventure Game, " + name + "!")
print("You are in the lost forest of the Dark Woods.")
print("Choose wisely. One wrong move could cost you your life!")

decision = input(
    "\nChoose your path: Strange Path of Lost City "
    "or Cave of Dragons: "
).lower().strip()

score = 0
lives = 3

if decision == "strange path of lost city":
    print("\nYou have entered the Lost City.")
    print("Two paths lie ahead.")

    decision = input("Choose left or right: ").lower().strip()

    if decision == "left":
        print("\nYou enter a dark alley.")
        decision = input("Go straight or turn back? ").lower().strip()

        if decision == "straight":
            print("\nYou discover a mysterious door!")
            decision = input("Open the door? ").lower().strip()

            if decision == "yes":
                print("\nYou discover a hidden treasure!")
                score += 1
                print("Congratulations, you win!")
            else:
                print("\nYou turn back and escape the city.")
                print("Adventure ended.")

        elif decision == "turn back":
            print("\nYou safely return to the forest.")
        else:
            print("\nInvalid choice. You are lost!")

    elif decision == "right":
        print("\nYou reach a broken stone bridge.")
        decision = input("Cross the bridge? ").lower().strip()

        if decision == "yes":
            print("\nThe bridge collapses!")
            lives -= 1
            print("You lose a life. Lives remaining:", lives)
            print("You barely escape the ruins.")
        else:
            print("\nYou avoid danger and return to the forest.")

    else:
        print("\nInvalid choice. The city gates close!")

elif decision == "cave of dragons":
    print("\nYou enter the Cave of Dragons.")
    print("A giant dragon blocks your way.")
    print('"Answer my riddles with YES or NO!"')

    ready = input(
        "\nDragon: Human, are you ready to play? "
    ).lower().strip()

    if ready == "yes" or ready == "y":
        print("\nDragon: Answer correctly to escape!")

        # Question 1
        answer1 = input(
            "\nQ1: Does the Moon produce its own light? "
        ).lower().strip()

        if answer1 == "no" or answer1 == "n":
            print("Correct! The Moon reflects sunlight.")
            score += 1

            # Question 2
            answer2 = input(
                "\nQ2: Is zero an even number? "
            ).lower().strip()

            if answer2 == "yes" or answer2 == "y":
                print("Correct! Zero is an even number.")
                score += 1

                print("\nThe dragon steps aside.")
                print("You have escaped the cave!")
                print("You win, " + name + "!")

            else:
                print("\nWrong answer!")
                lives -= 1
                print("The dragon refuses to let you pass.")

        else:
            print("\nWrong answer!")
            lives -= 1
            print("The dragon roars and blocks your escape.")

    else:
        print("\nYou refuse the challenge.")
        print("The dragon sends you back to the forest.")

else:
    print("\nInvalid path! Please choose one of the given options.")

print("\n========== GAME SUMMARY ==========")
print("Player:", name)
print("Score:", score)
print("Lives remaining:", lives)
print("Thanks for playing!")
