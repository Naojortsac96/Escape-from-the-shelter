
import random
from os import access

access_card=False
especial_number=random.randint(1,100)

texto="Welcome to escape from the shelter"
print(texto)
print("*"*len(texto))

print("\nYour name is Kain, a street cat who has been locked in an animal shelter waiting to be euthanized.\n"
      "Today, the guard left the cage open by mistake; this is your last chance of survival.\n"
      "After leaving the cage, you see two escape routes:\n"
      "\n"
      "a dark pathway and a hole on the wall that you don't know where it goes. what route you should go?\n")

question=input("[A- Dark pathway]|[B- Hole on the wall]: ").upper()

if question=="A":
    print("you walk along the dark pathway. Because you are a cat, you can see in the darkness.\n"
          "A guard with a flashlight notices you.\n"
          "what's your next move?\n")
    question1=input("[A- get close to the guard and rub his leg]|[B- Scratch his face]: ").upper()

    if question1=="A":
        print("the guard doesn't have emotions and put you back in the cage where you are euthanized moments later\n"
              "GAME OVER")

    elif question1=="B":
        print("The guard tries to stop you from scratching his face,\n"
              "but he can't see and ends up hitting his head against a wall. He is now unconscious.\n"
              "you see the guard has a key. Take the key?\n")

        question2=input("[A-Yes] | [B- No]: ").upper()
        if question2=="A":
            print("you've got the key and use it to free a cat that was locked nearby.\n"
                  "The cat thanks you and tells you her name is Maebe.\n"
                  "After the introduction, the two of you run until the path splits in two.\n"
                  "Maebe says there is an exit on the right. Where should you go?")
            
            question3=input("[A-Left]|[B-right]: ").upper()

            if question3=="A":
                print("you ignore Maebe's suggestion and keep running until you reach the dog zone.\n"
                      "The dogs are in their cages,\n"
                      "but they bark as soon as they see you.\n"
                      "Alerting the guards. The guards put both of you inside the cage of\n"
                      "an aggressive dog,which bites you to death\n"
                      "GAME OVER")

            elif question3=="B":
                print("you go right and run along the pathway until you see a window.\n"
                      "Maebe tells you that one of the windows can be opened\n"
                      "Both of you jump out of the window and there it is,\n "
                      "your ticket to freedom. Both of you leave that evil shelter behind.\n"
                      "Congratulations! you are finally free!\n"
                      "\n"
                      "THE END")
            elif question3 not in ("A", "B"):
                print("you are thinking too much and the guard captures you...\n GAME OVER")
                exit()



        elif question2=="B":
            print("You leave the key and run like if it was lunch time. The path splits in two\n"
                  "where should we go?")

            question4= input("[A - Left]|[B - Right]: ").upper()
            if question4=="A":
                print("you reach the dog zone. dogs are in their cages,\n"
                      "but they bark when they see you. Alerting the guards. The guards put you inside the cage of\n"
                      "an aggressive dog, which bites you to death\n"
                      "GAME OVER")

            elif question4=="B":
                print("You reach a pathway without an exit\n"
                      "you try to go back but a guard catches you\n"
                      "GAME OVER")

            elif question4 not in ("A", "B"):
                print("you are thinking too much and the guard captures you...\n"
                      "GAME OVER")
                exit()

        elif question2 not in ("A","B"):
            print("you are thinking too much and the guard captures you...\n"
                  "GAME OVER")
            exit()

    elif question1 not in ("A","B"):
        print("you are thinking too much and the guard captures you...\n"
              "GAME OVER")
        exit()


elif question=="B":
    print("You are in the ventilation ducts area and you find an employee's card.\n"
          "Will you take the card?\n")

    question5=input("[A-yes]|[B-No]: ").upper()
    if question5=="A":
        print("You pick up the card and keep moving forward\n"
              "until you manage to exit through an opening that leads to a hallway with a door at the end.\n"
              "Next to the door, there is a chair that lets you access a terminal used to open it,\n"
              "but you need a card. What do you do?\n")
        access_card=True

    elif question5=="B":
        print("You leave the card on the floor. You keep moving forward until you manage to exit\n"
              "through an opening that leads to a hallway with a door at the end.\n"
              "Next to the door, there is a chair that lets you access a terminal used to open it,\n"
              "but you need a card. What do you do?")

    elif question5 not in ("A","B"):
        print("you are thinking too much and the guard captures you...\n"
              "GAME OVER")
        exit()


    question6 = input("[A - Find another route]|[B - Open door]: ").upper()

    if question6 =="A":
        print("you try to find another route but one of the guards notice you and put you back in the cage\n"
              "GAME OVER")



    elif question6=="B" and access_card== False:
        print("Access denied... The door doesn't open. You look for another route, but a guard arrests you\n"
              "GAME OVER")

    elif question6=="B" and access_card== True:
        print("You use the employee's card to access the terminal. Now the terminal asks you what is 17*{}".format(especial_number))
        question7= float(input("Please, introduce your answer: "))

        if question7 == 17*especial_number:
            print("You can read a comment on the terminal that says: 'How clever you are!.'\n"
                  "Immediately after, the door that leads to the street opens.\n"
                  "You are finally free! Congratulations, you have earned your freedom, but you did not save Maebe.\n"
                  "THE END")

        elif question7 !=17*especial_number:
            print("You can read a comment on the terminal that says: 'Either you are a cat or you are very stupid.'\n"
                  "The system locks the door and alerts the guards, who finds you and take you back to your cage.\n"
                  "GAME OVER.")

        elif question7 not in ("A", "B"):
            print("you are thinking too much and the guard captures you...\n"
                  "GAME OVER")
            exit()

    elif question6 not in ("A", "B"):
        print("you are thinking too much and the guard captures you...\n"
              "GAME OVER")
        exit()



elif question not in ("A","B"):
    print("you are thinking too much and the guard captures you...\n"
          "GAME OVER")
    exit()




