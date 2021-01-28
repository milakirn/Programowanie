a = list(input("Podaj ciąg liczb: "))

tab_r = a[::-1]

if tab_r == a:
    print("Palindrom, ale i tak wypiszę rezultat: ", tab_r)
else:
    print("Odwrócona będzie wygłądać tak " , tab_r)