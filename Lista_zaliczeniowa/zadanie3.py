from Question import Question

lista_pytan = [
    "Czy HTML to język programowania?\n TAK\n NIE\n\n",
    "Czy laptop obowiązkowo powinien posiadać napęd optyczny?\n TAK\n NIE\n\n",
    "Czy na Windowsie można zrobić Serwer?\n TAK\n NIE\n\n",
    "Czy jesteś pewien, że nauczysz się wszystkiego w programowaniu?\n TAK\n NIE\n\n",
    "Czy do komputera mogą być podpięte 3 dyski twarde ?\n TAK\n NIE\n\n",
    "RAM jest to pamięć stała?\n TAK\n NIE\n\n",
    "JavaScript to język programowania skryptów na strony internetowe?\n TAK\n NIE\n\n",
    "CD-ROM ma pojęmność 1.44 MB\n TAK\n NIE\n\n",
    "Teams jest najlepszym programem do nauki zdalnej\n TAK\n NIE\n\n",
    "Najlepsze przyjaciele dla programisty to StackOverfow oraz geeksforgeeks\n TAK\n NIE\n\n"
]

pytania = [
    Question(lista_pytan[0], "NIE"),
    Question(lista_pytan[1], "NIE"),
    Question(lista_pytan[2], "TAK"),
    Question(lista_pytan[3], "NIE"),
    Question(lista_pytan[4], "TAK"),
    Question(lista_pytan[5], "NIE"),
    Question(lista_pytan[6], "TAK"),
    Question(lista_pytan[7], "NIE"),
    Question(lista_pytan[8], "TAK"),
    Question(lista_pytan[9], "TAK")
]

def zacznij_test(test):
    punkty = 0
    ocena = 0
    for question in test:
        answer = input(question.prompt).upper()
        if answer == question.answer:
            punkty += 1
        if punkty >= 0 and punkty <= 2:
            ocena = 1
        elif punkty >= 3 and punkty <= 4:
            ocena = 2
        elif punkty >= 5 and punkty <= 6:
            ocena = 3
        elif punkty >= 7 and punkty <= 8:
            ocena = 4
        elif punkty >= 9 and punkty <= 10:
            ocena = 5

    print(f"Dostałeś {punkty} ilość punktów, twoja ocena to {ocena}")

if __name__ == "__main__":
    zacznij_test(pytania)