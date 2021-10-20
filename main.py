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


def ultima_cifra(x):
    """
    Determina ultima cifra a unui numar
    :param x: numarul
    :return: ultima sa cifra
    """
    return x % 10


def test_ultima_cifra():
    assert ultima_cifra(13) == 3
    assert ultima_cifra(458) == 8


def cel_mai_mic_numar(l, n):
    """
    Afiseaza cel mai mic numar din lista care are ultima cifra egala cu cifra citita de la tastatura
    :param l: lista de nr intregi
    :param n: numarul introdus
    :return: cel mai mic numar din lista care are ultima cifra egala cu cifra citita de la tastatura
    """
    lista_crescatoare = l[:]
    lista_crescatoare.sort()
    rezultat = 0
    for i in lista_crescatoare:
        if ultima_cifra(i) == n:
            rezultat = i
            return rezultat


def test_cel_mai_mic_numar():
    assert cel_mai_mic_numar([23, 678], 3) == 23
    assert cel_mai_mic_numar([1, 6, 34, 68, 40, 48, 20], 8) == 48


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
    """
    Afisarea tuturor numerelor din lista care sunt superprime
    :param l: lista de numere intregi
    :return: lista numerelor care sunt superprime
    """
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
    test_ultima_cifra()
    test_cel_mai_mic_numar()


def main():
    # interfata de tip consola aici
    test_all()
    l = []
    while True:
        print("1. Citire lista")
        print("2. Afișarea tuturor numerelor negative nenule din listă")
        print("3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
        print("4. Afișarea tuturor numerelor din listă care sunt superprime.")
        print("a. Afisare lista")
        print("x. Iesire")
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            l = citire_lista(l)
        elif optiune == "2":
            print(numere_negative_nenule(l))
        elif optiune == "3":
            n = int(input("Introduceti cifra: "))
            print(cel_mai_mic_numar(l, n))
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