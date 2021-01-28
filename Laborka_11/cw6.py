liczba = int(input("Podaj liczbę w systemie dziesiętnym: "))
binar = bin(liczba)
hexa = hex(liczba)
osemk = oct(liczba)
print(f"Liczba {liczba} na innych systemach: binarny - {binar},"
      f" szesnastkowy - {hexa}, osemkowy - {osemk}")