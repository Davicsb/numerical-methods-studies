import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def montar_sistema():
    """Monta M, b e A = I - M a partir da propriedade do valor medio."""
    M = [
        [0.0, 0.25, 0.25, 0.0],
        [0.25, 0.0, 0.0, 0.25],
        [0.25, 0.0, 0.0, 0.25],
        [0.0, 0.25, 0.25, 0.0],
    ]
    b = [0.0, 0.5, 0.0, 0.5]
    n = len(b)
    A = [[(1.0 if i == j else 0.0) - M[i][j] for j in range(n)] for i in range(n)]
    return M, b, A

def substituicao_direta(L, b, diag_unitaria=False):
    n = len(b)
    y = [0.0] * n
    for i in range(n):
        soma = sum(L[i][k] * y[k] for k in range(i))
        if diag_unitaria:
            y[i] = b[i] - soma
        else:
            y[i] = (b[i] - soma) / L[i][i]
    return y

def substituicao_reversa(U, y):
    n = len(y)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(U[i][k] * x[k] for k in range(i + 1, n))
        x[i] = (y[i] - soma) / U[i][i]
    return x

def cholesky_com_teste(A, tol=1e-12):
    """Decomposicao de Cholesky A = G G^T que tambem testa se A e positiva definida.

    Retorna (G, True) se A for positiva definida e (None, False) caso contrario.
    Se algum valor dentro da raiz quadrada for <= 0, A nao e positiva definida.
    """
    n = len(A)

    # Cholesky so se aplica a matrizes simetricas
    for i in range(n):
        for j in range(i):
            if abs(A[i][j] - A[j][i]) > tol:
                return None, False

    G = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            soma = sum(G[i][k] * G[j][k] for k in range(j))
            if i == j:
                valor = A[i][i] - soma
                if valor <= tol:
                    return None, False
                G[i][i] = math.sqrt(valor)
            else:
                G[i][j] = (A[i][j] - soma) / G[j][j]
    return G, True

def resolver_cholesky(G, b):
    n = len(G)
    Gt = [[G[j][i] for j in range(n)] for i in range(n)]
    y = substituicao_direta(G, b)
    return substituicao_reversa(Gt, y)

def decomposicao_PtLU(A):
    """Decomposicao P^t L U com pivoteamento parcial: A = P^t L U."""
    n = len(A)
    U = [linha[:] for linha in A]
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    perm = list(range(n))

    for k in range(n - 1):
        p = max(range(k, n), key=lambda i: abs(U[i][k]))
        if p != k:
            U[k], U[p] = U[p], U[k]
            perm[k], perm[p] = perm[p], perm[k]
            for j in range(k):
                L[k][j], L[p][j] = L[p][j], L[k][j]
        for i in range(k + 1, n):
            fator = U[i][k] / U[k][k]
            L[i][k] = fator
            for j in range(k, n):
                U[i][j] -= fator * U[k][j]

    return perm, L, U

def resolver_PtLU(A, b):
    perm, L, U = decomposicao_PtLU(A)
    b_perm = [b[perm[i]] for i in range(len(b))]
    y = substituicao_direta(L, b_perm, diag_unitaria=True)
    return substituicao_reversa(U, y)

def resolver_sistema(A, b):
    """Usa Cholesky se A for positiva definida; caso contrario, P^t L U."""
    G, eh_pd = cholesky_com_teste(A)
    if eh_pd:
        return resolver_cholesky(G, b), "Cholesky"
    return resolver_PtLU(A, b), "P^t L U"

def residuo_maximo(A, x, b):
    n = len(b)
    return max(abs(sum(A[i][j] * x[j] for j in range(n)) - b[i]) for i in range(n))

def plotar_placa(t):
    """Reproduz a figura da placa: pontos da malha coloridos pela temperatura."""
    c = 0.5                     # coordenada dos pontos interiores: x, y em {-c, c}
    s = math.sqrt(1 - c * c)    # coordenada dos pontos de contorno sobre o circulo
    mapa = plt.get_cmap("coolwarm")

    fig, ax = plt.subplots(figsize=(6.5, 6))
    ax.add_patch(Circle((0, 0), 1.0, facecolor="#eeeeee", edgecolor="black", zorder=0))

    # Linhas da malha
    for v in (-c, c):
        ax.plot([v, v], [-s, s], color="tab:blue", linewidth=1, zorder=1)
        ax.plot([-s, s], [v, v], color="tab:blue", linewidth=1, zorder=1)

    # Pontos de contorno: 0 na metade esquerda, 1 na metade direita
    contorno = [
        (-c, s, 0), (c, s, 1),      # em cima
        (-c, -s, 0), (c, -s, 1),    # embaixo
        (-s, c, 0), (s, c, 1),      # esquerda e direita (linha de cima)
        (-s, -c, 0), (s, -c, 1),    # esquerda e direita (linha de baixo)
    ]
    for x, y, temp in contorno:
        ax.scatter(x, y, s=120, color=mapa(float(temp)), edgecolors="black", zorder=3)
        ax.annotate(f"{temp}", (x, y), textcoords="offset points", xytext=(0, 11),
                    ha="center", fontsize=9)

    # Pontos interiores t1, t2, t3, t4
    interiores = [(-c, c), (c, c), (-c, -c), (c, -c)]
    for i, ((x, y), temp) in enumerate(zip(interiores, t), start=1):
        ax.scatter(x, y, s=700, color=mapa(temp), edgecolors="black", zorder=4)
        ax.annotate(f"t{i}\n{temp:.2f}", (x, y), ha="center", va="center",
                    fontsize=9, zorder=5)

    barra = plt.cm.ScalarMappable(cmap=mapa, norm=plt.Normalize(0, 1))
    fig.colorbar(barra, ax=ax, label="Temperatura", shrink=0.8)

    ax.set_aspect("equal")
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.set_title("Temperaturas de equilibrio na placa circular")
    ax.axis("off")
    plt.tight_layout()
    plt.savefig("questao3c_placa.png", dpi=200)
    plt.show()

if __name__ == "__main__":
    M, b, A = montar_sistema()

    print("Matriz M:")
    for linha in M:
        print("  ", linha)
    print("Vetor b:", b)
    print("Matriz A = I - M:")
    for linha in A:
        print("  ", linha)

    G, eh_pd = cholesky_com_teste(A)
    print(f"\nA e positiva definida? {eh_pd}")

    t, metodo = resolver_sistema(A, b)
    print(f"Metodo utilizado: {metodo}")
    print("\nTemperaturas nos pontos interiores:")
    for i, valor in enumerate(t, start=1):
        print(f"  t{i} = {valor:.6f}")
    print(f"\nResiduo maximo |At - b| = {residuo_maximo(A, t, b):.2e}")

    # Item (c): figura da placa
    plotar_placa(t)

    # Teste do desvio: matriz simetrica que NAO e positiva definida
    B = [[1.0, 2.0], [2.0, 1.0]]
    _, pd_B = cholesky_com_teste(B)
    print(f"\nTeste com B = [[1, 2], [2, 1]]: positiva definida? {pd_B}")
    xB, metodo_B = resolver_sistema(B, [3.0, 3.0])
    print(f"Metodo usado: {metodo_B}, solucao = {xB}")