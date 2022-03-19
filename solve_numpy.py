
import numpy

N: int = int(input())
A: list[list[float]] = [list(map(float, input().split())) for i in range(N)]
B: list[float] = list(map(float, input().split()))

print(*numpy.linalg.solve(A, B), sep="\n")