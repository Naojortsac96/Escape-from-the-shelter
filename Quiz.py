title= "\nWelcome to the cheese test"
print(title+"\n"+"-"*len(title)+"\n")


points = 0

option= input("Question 1: What do you do when you see cheese on a table?\n"
              "A - I ran away\n"
              "B - I taste one cheese or two\n"
              "C - I eat all of them\n").upper()

if option == "A":
    points += 0

elif option == "B":
    points +=5

elif option == "C":
    points +=10

else:
    print("Options available are A,B y C")
    exit()

option= input("Question 2: How do you like burgers?\n"
              "A - Without cheese\n"
              "B - With cheese\n"
              "C - With Bread and cheese\n").upper()

if option == "A":
    points += 0

elif option == "B":
    points +=5

elif option == "C":
    points +=10

else:
    print("Options available are A,B y C")
    exit()


option= input("Question 3: Are you lactose tolerant?\n"
              "A - Yes\n"
              "B - Sometimes\n"
              "C - No\n").upper()

if option == "A":
    points += 0

elif option == "B":
    points +=5

elif option == "C":
    points +=10

else:
    print("Options available are A,B y C")
    exit()

print(points)

if points >= 25:
    print("Result: You are a cheese fan")

elif points>= 15:
    print("Result: Congratulations!, you are a person who likes cheese")

else:
    print("Result: It seems you don't like cheese")
    exit()

