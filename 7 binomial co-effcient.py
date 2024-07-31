def binomialCoeff_BF(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomialCoeff_BF(n - 1, k - 1) + binomialCoeff_BF(n - 1, k)

def binomialCoef_DC(n, k):
    C = [[0 for x in range(k + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]

n = int(input("Enter n: "))
k = int(input("Enter k: "))
print("Brute Force method C(n, k):", binomialCoeff_BF(n, k))
print("Divide and Conquer C(n, k):", binomialCoef_DC(n, k))
