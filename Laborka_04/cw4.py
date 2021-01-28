cos = True
while cos:
    a = input("Podaj a: ")
    b = input("Podaj b: ")
    if a == 0 or b == 0:
        print("Jedna z liczb jest zerem")
        cos = False
    print((int(a) * int(b) / 2))
    #if type(a) or type(b) == str:
     #   print("Nie podałeś liczby")