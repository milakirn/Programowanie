def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True
print(czy_pierwsza(13))
###############################################
#a = int(input("Podaj liczbę: "))
#
# Poprawiony
#
#while a != 0:
 #   if a == 2 or a == 3:
 #       print("Liczba jest pierwsza")
  #      break
   # elif a % 2 == 0 or a % 3 == 0:
    #    print("Liczba nie jest pierwsza")
     #   break
    #elif a % 1 == 0 and a % a == 0:
     #   print("Liczba jest pierwsza")
      #  break
    #else:
     #   print("Liczba nie jest pierwsza")
      #  break
#else:
 #   print("Liczba równa 0")