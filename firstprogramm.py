a=int(input("Introduzca su primer número: "))
b=int(input("Introduzca su segundo numero: "))
c= int(input("Introduzca su tercer numero: "))

d=(a,b,c)

print("El número más grande entre {},{},{} es:{}, y el más pequeno es:{}".format(a,b,c,
                                                                                 max(a,b,c),
                                                                                 min(a,b,c)))
