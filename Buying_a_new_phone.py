print("\nWelcome\n")

print("Answer the questions to find out what phone you should get\n")

phone=input("What's your favourite operating system?\n"
            "A-Android\n"
            "B-IOS\n").upper()

if phone=="A":
    phone=input("Do you have money?\n"
                "A-Yes\n"
                "B-No\n").upper()

    if phone=="A":
        phone=input("Would you like a good camera?\n"
                    "A-Yes\n"
                    "B-No\n").upper()
        if phone=="A":
            print("You should get Samsung S25 Ultra ")

        elif phone=="B":
            print("You should get the Samsung S25")

        else:
            print("Incorrect answer, please start again")
            exit()

    elif phone=="B":
        print("You should buy a second hand Samsung")
    else:
        print("Incorrect answer, please start again")
        exit()




elif phone=="B":
    phone = input("Do you have money?\n"
                  "A-Yes\n"
                  "B-No\n").upper()

    print("you have selected:{}...".format(phone))
    if phone == "A":
        print("You should buy Iphone 17 Pro Max ")


    elif phone == "B":
        print("You should buy a second hand Iphone")

    else:
        print("Incorrect answer, please start again")
        exit()


else:
    print("Wrong answer, try again")
    exit()