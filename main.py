def is_prime(n):
    ok = 1
    for x in range(2, n, 1):
        if n % x == 0:
            ok = 0
    if ok == 1:
        return 1
    return 0


def size(n):
    nr = 0
    while n > 0:
        nr = nr + 1
        n = n // 10
    return nr + 1


def oglindit(n):
    r = 0
    while n > 0:
        r = r * 10 + (n % 10)
        n = n / 10
    return r


def is_superprime(n):
    """verifica daca sunt prime"""
    p = 1
    ok = 1
    for x in range(1, size(n), 1):
        if is_prime(n // p) == 0:
            ok = 0
        p = p * 10
    if ok == 1:
        return True
    return False


def test_is_superprime():
    """testeaza functia (verifica daca sunt prime)"""
    assert is_superprime(2) is True


def isprime(n):
    nr = 0
    for x in range(2, n, 1):
        if n % x == 0:
            nr = nr + 1
    if nr == 0:
        return True
    return False


def get_largest_prime_below(n):
    """returneaza ce mai mare numar prim mai mic decat n"""
    for x in range(n - 1, 2, -1):
        if isprime(x):
            return x
    return -1


def test_get_largest_prime_below():
    """testeaza functia (get_largest_prime_below)"""
    assert get_largest_prime_below(-1) == -1
    assert get_largest_prime_below(2) == -1


"""# LAB 2 - PROBLEMA 5"""


def is_palindrome(n):
    """
    verifica daca n este palindrom
    copiem valoarea lui n
    """
    c = n
    nr = 0
    while n > 0:
        nr = nr * 10 + (n % 10)
        n = n // 10
    if nr != c:
        return False
    return True


def test_is_palindrome():
    """testeaza functia (is_Palindrome)"""
    assert is_palindrome(12) == False
    assert is_palindrome(11) == True
    assert is_palindrome(1) == True


def menu():
    print("1.Citire date: ")
    print("2.Determina proprietatea 1")
    print("3.Determina proprietatea 2")
    print("4.Determina proprietatea 3 ")
    print("5.Iesire ")


def main():
    test_is_superprime()
    test_is_palindrome()
    test_get_largest_prime_below()
    while True:
        menu()
        optiune = input("Alege optiunea: ")

        if optiune == 1:
            n = int(input("Citeste n: "))
        elif optiune == 2:
            print(is_superprime)
        elif optiune == 3:
            print(get_largest_prime_below)
        elif optiune == 4:
            print(is_palindrome)
        elif optiune == 5:
            break


if __name__ == '__main__':
    main()
