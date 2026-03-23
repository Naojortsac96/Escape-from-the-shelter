

dollar_euro = 0.91
pound_euro = 1.18

currency= input("Which currency would you like to convert from?\n"
               "A- Dollar to Euros\n"
               "B- Euros to Dollars\n"
               "C- Pounds to Euros\n"
               "D- Euros to Pounds\n").upper()

user_text="Please, introduce the amount in {}: "

if currency == "A":
    dollar_euros=float(input(user_text.format("dollars")))
    print("{}$ = {}€".format(dollar_euros,dollar_euros*dollar_euro))

elif currency == "B":
    euros_dollar=float(input(user_text.format("euros")))
    print("{}€ = {}$".format(euros_dollar,euros_dollar/dollar_euro))

elif currency == "C":
    pounds_euros=float(input(user_text.format("pounds")))
    print("{}£ = {}€".format(pounds_euros,pounds_euros*pound_euro))

elif currency == "D":
    euros_pounds=float(input(user_text.format("euros")))
    print("{}€ = {}£".format(euros_pounds,euros_pounds/pound_euro))

else:
    print("La opcion no es valida")
    exit()
