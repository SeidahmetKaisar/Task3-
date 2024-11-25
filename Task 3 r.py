x=1
z = int(input("Қай санға дейінгі кесте керек?"))
while x<10 :
    y=1
    while y<10:
        print(x,"*",y,"=",x*y)
        y=y+1
    print("")
    if x==z:
        break
    x = x + 1