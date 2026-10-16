import time
import numpy as np
import matplotlib.pyplot as plt

def substituicao_direta(L, b, diag_unitaria=False):
    
    n = len(b)
    y = np.zeros(n, dtype=float)
    for i in range(n):
        soma = np.dot(L[i, :i], y[:i])
        if diag_unitaria:
            y[i] = b[i] - soma
        else:
            y[i] = (b[i] - soma) / L[i, i]
    return y


def substituicao_reversa(U, y):

    n = len(y)
    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        soma = np.dot(U[i, i + 1 :], x[i + 1 :])
        x[i] = (y[i] - soma) / U[i, i]
    return x

# ELIMINAÇÃO GAUSSIANA COM PIVOTAGEM PARCIAL COM ESCALA
def eliminacao_gaussiana_escala(A, b):
    
    n = len(b)
    M = A.astype(float).copy()
    b_mod = b.astype(float).copy()

    # Fatores de escala (máximo valor absoluto de cada linha)
    s = np.max(np.abs(M), axis=1)

    for k in range(n - 1):
        # Escolha da linha pivô com base na razão escalada
        razoes = np.abs(M[k:n, k]) / s[k:n]
        p = k + np.argmax(razoes)

        # Troca de linhas na matriz, no vetor independente e no vetor de escala
        if p != k:
            M[[k, p], :] = M[[p, k], :]
            b_mod[[k, p]] = b_mod[[p, k]]
            s[[k, p]] = s[[p, k]]

        # Eliminação (vetorizada por linha para melhor desempenho)
        fatores = M[k + 1 : n, k] / M[k, k]
        M[k + 1 : n, k:] -= np.outer(fatores, M[k, k:])
        b_mod[k + 1 : n] -= fatores * b_mod[k]

    return substituicao_reversa(M, b_mod)


# DECOMPOSIÇÃO P^t L U
def decomposicao_PtLU(A):
    
    n = A.shape[0]
    U = A.astype(float).copy()
    L = np.eye(n, dtype=float)
    perm = np.arange(n)

    for k in range(n - 1):
        # Pivotagem parcial padrão
        p = k + np.argmax(np.abs(U[k:n, k]))

        if p != k:
            U[[k, p], :] = U[[p, k], :]
            perm[[k, p]] = perm[[p, k]]
            if k > 0:
                L[[k, p], :k] = L[[p, k], :k]

        fatores = U[k + 1 : n, k] / U[k, k]
        L[k + 1 : n, k] = fatores
        U[k + 1 : n, k:] -= np.outer(fatores, U[k, k:])

    return perm, L, U


def resolver_PtLU(A, b):
    
    perm, L, U = decomposicao_PtLU(A)
    # Como P^t L U x = b <=> L U x = P b
    b_permutado = b[perm]
    y = substituicao_direta(L, b_permutado, diag_unitaria=True)
    x = substituicao_reversa(U, y)
    return x

# DECOMPOSIÇÃO DE CHOLESKY
def decomposicao_cholesky(A):

    n = A.shape[0]
    G = np.zeros((n, n), dtype=float)

    for i in range(n):
        # Elemento da diagonal
        soma_diag = np.dot(G[i, :i], G[i, :i])
        G[i, i] = np.sqrt(A[i, i] - soma_diag)

        # Elementos abaixo da diagonal na coluna i
        if i + 1 < n:
            soma_col = G[i + 1 : n, :i] @ G[i, :i]
            G[i + 1 : n, i] = (A[i + 1 : n, i] - soma_col) / G[i, i]

    return G


def resolver_cholesky(A, b):

    G = decomposicao_cholesky(A)
    y = substituicao_direta(G, b, diag_unitaria=False)
    x = substituicao_reversa(G.T, y)
    return x


# GERAÇÃO DE DADOS E EXPERIÊNCIA
def gerar_matriz_positiva_definida(n):
 
    M = np.random.uniform(-5, 5, size=(n, n))
    # M^T * M é semidefinida positiva; somar n*I garante que seja estritamente definida positiva
    return M.T @ M + n * np.eye(n)


def gerar_vetor_b(n):
    
    b = np.random.uniform(-10, 10, size=n)
    while np.all(b == 0):
        b = np.random.uniform(-10, 10, size=n)
    return b


def executar_experimento():
    valores_n = [100, 200, 300, 400, 500]
    num_matrizes = 10

    # Dicionário para guardar os tempos totais de execução
    tempos = {
        n: {"Gauss_Escala": 0.0, "PtLU": 0.0, "Cholesky": 0.0}
        for n in valores_n
    }

    print(
        f"{'n':>5} | {'Gauss c/ Escala (s)':>20} | {'Decomp. P^tLU (s)':>20} | {'Cholesky (s)':>15}"
    )
    print("-" * 70)

    for n in valores_n:
        # Gera os 10 sistemas previamente para medir apenas o tempo dos métodos
        sistemas = [
            (gerar_matriz_positiva_definida(n), gerar_vetor_b(n))
            for _ in range(num_matrizes)
        ]

        # Eliminação Gaussiana com pivotagem parcial com escala
        inicio = time.perf_counter()
        for A, b in sistemas:
            _ = eliminacao_gaussiana_escala(A, b)
        tempos[n]["Gauss_Escala"] = time.perf_counter() - inicio

        # Decomposição P^t L U
        inicio = time.perf_counter()
        for A, b in sistemas:
            _ = resolver_PtLU(A, b)
        tempos[n]["PtLU"] = time.perf_counter() - inicio

        #  Decomposição de Cholesky
        inicio = time.perf_counter()
        for A, b in sistemas:
            _ = resolver_cholesky(A, b)
        tempos[n]["Cholesky"] = time.perf_counter() - inicio

        print(
            f"{n:>5} | {tempos[n]['Gauss_Escala']:>20.6f} | {tempos[n]['PtLU']:>20.6f} | {tempos[n]['Cholesky']:>15.6f}"
        )

    return tempos

def executar_experimento_b():
    valores_n = [100, 200, 300, 400, 500]
    num_vetores = 10
    tempos_b = {
        n: {"Gauss_Escala": 0.0, "PtLU": 0.0, "Cholesky": 0.0}
        for n in valores_n
    }

    print(
        f"{'n':>5} | {'Gauss c/ Escala (s)':>20} | {'Decomp. P^tLU (s)':>20} | {'Cholesky (s)':>15}"
    )
    print("-" * 70)

    for n in valores_n:
        # Gera 1 única matriz positiva definida A e 10 vetores b != 0
        A = gerar_matriz_positiva_definida(n)
        vetores_b = [gerar_vetor_b(n) for _ in range(num_vetores)]

        # -----------------------------------------------------------------
        # Eliminação Gaussiana com pivotagem parcial com escala (Não reaproveita decomposição: recalcula o escalonamento 10 vezes)
        inicio = time.perf_counter()
        for b in vetores_b:
            _ = eliminacao_gaussiana_escala(A, b)
        tempos_b[n]["Gauss_Escala"] = time.perf_counter() - inicio

        # Decomposição P^t L U (Calcula a fatoração apenas 1 vez e resolve para os 10 vetores b)
        inicio = time.perf_counter()
        perm, L, U = decomposicao_PtLU(A)  # Feito apenas 1 vez para a matriz A
        for b in vetores_b:
            b_permutado = b[perm]
            y = substituicao_direta(L, b_permutado, diag_unitaria=True)
            _ = substituicao_reversa(U, y)
        tempos_b[n]["PtLU"] = time.perf_counter() - inicio

        # 3. Decomposição de Cholesky (Calcula a fatoração apenas 1 vez e resolve para os 10 vetores b)
        inicio = time.perf_counter()
        G = decomposicao_cholesky(A)  # Feito apenas 1 vez para a matriz A
        G_t = G.T
        for b in vetores_b:
            y = substituicao_direta(G, b, diag_unitaria=False)
            _ = substituicao_reversa(G_t, y)
        tempos_b[n]["Cholesky"] = time.perf_counter() - inicio

        print(
            f"{n:>5} | {tempos_b[n]['Gauss_Escala']:>20.6f} | {tempos_b[n]['PtLU']:>20.6f} | {tempos_b[n]['Cholesky']:>15.6f}"
        )

    return tempos_b


def plotar_comparacao(tempos_a, tempos_b):
    valores_n = [100, 200, 300, 400, 500]

    # Extração das listas de tempos para a letra a
    gauss_a = [tempos_a[n]["Gauss_Escala"] for n in valores_n]
    ptlu_a = [tempos_a[n]["PtLU"] for n in valores_n]
    chol_a = [tempos_a[n]["Cholesky"] for n in valores_n]

    # Extração das listas de tempos para a lera b
    gauss_b = [tempos_b[n]["Gauss_Escala"] for n in valores_n]
    ptlu_b = [tempos_b[n]["PtLU"] for n in valores_n]
    chol_b = [tempos_b[n]["Cholesky"] for n in valores_n]

    # Criação de uma única figura contendo as 6 curvas
    plt.figure(figsize=(10, 6))

    # Curvas da a - Linhas contínuas
    plt.plot(
        valores_n,
        gauss_a,
        "r-o",
        label="(a) Eliminação Gaussiana c/ Escala",
        linewidth=2,
    )
    plt.plot(
        valores_n, ptlu_a, "b-s", label="(a) Decomposição P^tLU", linewidth=2
    )
    plt.plot(
        valores_n,
        chol_a,
        "g-^",
        label="(a) Decomposição de Cholesky",
        linewidth=2,
    )

    # Curvas da b - Linhas tracejadas
    plt.plot(
        valores_n,
        gauss_b,
        "m--o",
        label="(b) Eliminação Gaussiana c/ Escala",
        linewidth=2,
    )
    plt.plot(
        valores_n, ptlu_b, "c--s", label="(b) Decomposição P^tLU", linewidth=2
    )
    plt.plot(
        valores_n,
        chol_b,
        "y--^",
        label="(b) Decomposição de Cholesky",
        linewidth=2,
    )

    # Configuração dos eixos, título e legenda
    plt.title(
        "Comparação de Tempo de Execução: a vs b", fontsize=14
    )
    plt.xlabel("Tamanho da matriz (n)", fontsize=12)
    plt.ylabel("Tempo de execução total (segundos)", fontsize=12)
    plt.xticks(valores_n)
    plt.grid(True, linestyle=":", alpha=0.7)
    plt.legend(loc="upper left", fontsize=10)
    plt.tight_layout()

    # Guarda e exibe o gráfico
    plt.savefig("comparacao_6_curvas.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    print("Executando Experimento a")
    tempos_a = executar_experimento()

    print()
    print("Executando Experimento b")
    tempos_b = executar_experimento_b()

    # Plota o gráfico unificado e responde às perguntas no terminal
    plotar_comparacao(tempos_a, tempos_b)

    # Verificação automática do método mais rápido para n = 500
    melhor_a = min(tempos_a[500], key=tempos_a[500].get)
    melhor_b = min(tempos_b[500], key=tempos_b[500].get)
    print(f"\nMenor tempo em a (n=500): {melhor_a}")
    print(f"Menor tempo em b (n=500): {melhor_b}")