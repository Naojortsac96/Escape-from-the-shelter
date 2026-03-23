age= int(input("What is your age?: "))
type_of_card=input("tell me what type of card you have (S for student, P pensioner, F big family, N nada): ").upper()

if (25<=age<=35 and type_of_card == "S") or age<=10 or (age>65 and type_of_card=="P") or (type_of_card == "F"):
            print("discount applied!")
else:
    print("you don't qualify for a discount")