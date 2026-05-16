for hod in range(100, 334):  
    X = hod // 100
    O = (hod // 10) % 10
    D = hod % 10

    if X == O or X == D or O == D:
        continue

    mat = hod * 3
    if mat >= 1000:
        continue

    M = mat // 100
    A = (mat // 10) % 10
    T = mat % 10

    if M == A or M == T or A == T:
        continue

    # Проверка, что все 6 букв разные цифры
    if len({X, O, D, M, A, T}) == 6:
        print(f"{hod}+{hod}+{hod}={mat}")
