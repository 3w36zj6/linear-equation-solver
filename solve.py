from decimal import Decimal

print_matrix = lambda matrix: print(*matrix, sep="\n")  # 行列表示用


def lu_decomposition(A: list[list[Decimal]]) -> tuple[list[list[Decimal]], list[list[Decimal]], list[list[Decimal]]]:
    """
    正方行列AをLU分解する。

    Parameters
    ----------
    A : list[list[Decimal]]
        LU分解する正方行列A。

    Returns
    -------
    L : list[list[Decimal]]
        下三角行列L。
    U : list[list[Decimal]]
        上三角行列U。
    P : list[list[Decimal]]
        ピボット選択の置換行列P。
    """

    L: list[list[Decimal]] = [[Decimal(1) if i == j else Decimal(0) for j in range(N)] for i in range(N)]  # 単位行列
    U: list[list[Decimal]] = [[Decimal(0) for j in range(N)] for i in range(N)]  # 零行列
    P: list[list[Decimal]] = [[Decimal(1) if i == j else Decimal(0) for j in range(N)] for i in range(N)]  # 単位行列

    # ピボット選択
    for k in range(N):
        abs_col: list[Decimal] = [abs(A[i][k]) for i in range(N)]
        max_index: int = abs_col.index(max(abs_col))  # 絶対値が最も大きい成分を探す

        # swap
        A[k], A[max_index] = A[max_index], A[k]
        P[k], P[max_index] = P[max_index], P[k]

    for k in range(N):
        # U
        for j in range(k, N):
            U[k][j] = A[k][j]
            for s in range(k):
                U[k][j] -= L[k][s] * U[s][j]

        # L
        for i in range(1 + k, N):
            L[i][k] = A[i][k]
            for s in range(k):
                L[i][k] -= L[i][s] * U[s][k]
            L[i][k] /= U[k][k]

    return L, U, P


def backward_substitution(A: list[list[Decimal]], B: list[Decimal]) -> list[Decimal]:
    """
    後退代入で方程式AX = Bを解く。

    Parameters
    ----------
    A : list[list[Decimal]]
        上三角行列A。
    B : list[Decimal]
        行列B。

    Returns
    -------
    X : list[Decimal]
        方程式の解。
    """
    X: list[Decimal] = [Decimal(0) for i in range(N)]
    for i in reversed(range(0, N)):
        X[i] = B[i]
        for k in range(i + 1, N):
            X[i] -= A[i][k] * X[k]
        X[i] /= A[i][i]

    return X


def multiply_permutation_matrix(P: list[list[Decimal]], B: list[Decimal]) -> list[Decimal]:
    """
    置換行列Pを行列Bに左からかける。

    Parameters
    ----------
    P : list[list[Decimal]]
        置換行列P。
    B : list[Decimal]
        行列B。

    Returns
    -------
    PB : list[Decimal]
        置換後の行列。
    """
    PB: list[Decimal] = [Decimal(0) for i in range(N)]
    for i in range(N):
        for j in range(N):
            PB[i] += P[i][j] * B[j]

    return PB


if __name__ == "__main__":
    # 標準入力
    N: int = int(input())
    A: list[list[Decimal]] = [list(map(Decimal, input().split())) for i in range(N)]
    B: list[Decimal] = list(map(Decimal, input().split()))

    # LU分解
    L: list[list[Decimal]]
    U: list[list[Decimal]]
    P: list[list[Decimal]]
    L, U, P = lu_decomposition(A)

    # LY = PBを解く
    L = [row[::-1] for row in L[:]][::-1]  # 後退代入と上下逆なので逆順に
    PB: list[Decimal] = multiply_permutation_matrix(P, B)[::-1]  # 置換行列をかけて後退代入と上下逆なので逆順に
    Y: list[Decimal] = backward_substitution(L, PB)[::-1]

    # UX = Yを解く
    X: list[Decimal] = backward_substitution(U, Y)

    # 標準出力
    print(*X, sep="\n")
