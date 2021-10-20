def citire_lista(l):
    l = []
    numere = input("Introduceti numerele, separate prin vrigula: ")
    numere_ca_string = numere.split(",")
    for i in numere_ca_string:
        l.append(int(i))
    return l


def numere_negative_nenule(l):
    """
    Afișeaza toate numerele negative nenule din listă
    :param l: lista de numere intregi
    :return: lista cu toate numerele negative nenule din lista
    """
    rezultat = []
    for i in l:
        if i < 0:
            rezultat.append(i)
    return rezultat



def main():
    # interfata de tip consola aici
    l = []
    while True:
        print("1. Citire lista")
        print("2. Afișarea tuturor numerelor negative nenule din listă")
        print("a. Afisare lista")
        print("x. Iesire")
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            l = citire_lista(l)
        elif optiune == "2":
            print(numere_negative_nenule(l))
        elif optiune.lower() == "a":
            print(l)
        elif optiune.lower() == "x":
            break
        else:
            print("Optiune gresita ! Reincercati...")


if __name__ == "__main__":
    main()