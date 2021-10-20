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


def test_numere_negative_nenule():
    assert numere_negative_nenule([23, 89, 4, 56]) == []
    assert numere_negative_nenule([-23, -5, 34, -9]) == [-23, -5, -9]
    assert numere_negative_nenule([-4, - 10, -56]) == [-4, -10, -56]


def este_prim(n):
    """
    Determina daca un numar este prim
    :param n: numarul
    :return: True, daca numarul este prim, False in caz contrar
    """
    if n < 2:
        return False
    for i in range(2, n // 2+ 1):
        if n % i == 0:
            return False
    return True


def test_este_prim():
    assert este_prim(3) is True
    assert este_prim(10) is False


def superprim(l):
    rezultat = []
    for i in l:
        j = i
        if j != 0:
            if este_prim(j):
                j = i % 10
    rezultat.append(i)
    return rezultat


def test_superprim():
    assert superprim([173, 239]) == [239]


def test_all():
    test_numere_negative_nenule()
    test_este_prim()
    test_superprim()


def main():
    # interfata de tip consola aici
    test_all()
    l = []
    while True:
        print("1. Citire lista")
        print("2. Afișarea tuturor numerelor negative nenule din listă")
        print("4. Afișarea tuturor numerelor din listă care sunt superprime.")
        print("a. Afisare lista")
        print("x. Iesire")
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            l = citire_lista(l)
        elif optiune == "2":
            print(numere_negative_nenule(l))
        elif optiune == "4":
            print(superprim(l))
        elif optiune.lower() == "a":
            print(l)
        elif optiune.lower() == "x":
            break
        else:
            print("Optiune gresita ! Reincercati...")


if __name__ == "__main__":
    main()