# Questão 1 - Lista 3 - Métodos Numéricos
# Sistema de molas resolvido por Gauss-Seidel 

k1, k2, k3, k4 = 200.0, 100.0, 100.0, 200.0
A = [[k1 + k2, -k2, 0.0],
     [-k2, k2 + k3, -k3],
     [0.0, -k3, k3 + k4]]
b = [10.0, 20.0, 10.0]
n = 3


def gauss_seidel(A, b, x0, tol=1e-5, max_iter=1000):
    n = len(b)
    x = x0[:]
    for k in range(1, max_iter + 1):
        x_old = x[:]
        for i in range(n):
            soma = 0.0
            for j in range(n):
                if j != i:
                    soma += A[i][j] * x[j]  # usa x já atualizado (j < i)
            x[i] = (b[i] - soma) / A[i][i]
        erro = max(abs(x[i] - x_old[i]) for i in range(n))
        print(f"k={k:3d}  x=({x[0]:.8f}, {x[1]:.8f}, {x[2]:.8f})  erro_inf={erro:.3e}")
        if erro < tol:
            return x, k, True
    return x, max_iter, False


# Solução exata por eliminação gaussiana (apenas para conferência)
def eliminacao(A, b):
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= f * M[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x


# Matriz de iteração T = -(D+L)^-1 U e c = (D+L)^-1 b
def matriz_T_c(A, b):
    n = len(b)
    # resolve (D+L) y = coluna, por substituição direta
    def sub_direta(col):
        y = [0.0] * n
        for i in range(n):
            y[i] = (col[i] - sum(A[i][j] * y[j] for j in range(i))) / A[i][i]
        return y
    U = [[A[i][j] if j > i else 0.0 for j in range(n)] for i in range(n)]
    cols = [sub_direta([-U[i][j] for i in range(n)]) for j in range(n)]
    T = [[cols[j][i] for j in range(n)] for i in range(n)]
    c = sub_direta(b)
    return T, c


if __name__ == "__main__":
    print("=== Gauss-Seidel ===")
    x, k, ok = gauss_seidel(A, b, [0.0, 0.0, 0.0])
    if ok:
        print(f"\nConvergiu em {k} iterações")
    else:
        print("\nCRITÉRIO DE PARADA NÃO ATINGIDO em 1000 iterações")
    print("x (Gauss-Seidel) =", x)
    print("x (eliminação)   =", eliminacao(A, b))
    T, c = matriz_T_c(A, b)
    print("\nT =")
    for l in T:
        print(["%.6f" % v for v in l])
    print("c =", ["%.6f" % v for v in c])
    print("||T||_inf =", max(sum(abs(v) for v in l) for l in T))