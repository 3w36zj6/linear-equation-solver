print_matrix = lambda matrix: print(*matrix, sep="\n")


def lu_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    L: list[list[float]] = [[1.0 if i == j else 0.0 for j in range(N)] for i in range(N)]
    U: list[list[float]] = [[0.0 for j in range(N)] for i in range(N)]

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

    return L, U


if __name__ == "__main__":
    N: int = int(input())
    A: list[list[float]] = [list(map(float, input().split())) for i in range(N)]
    B: list[float] = list(map(float, input().split()))

    L, U = lu_decomposition(A)
