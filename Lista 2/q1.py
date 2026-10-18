import random

def gerar_matriz_pd(n, limite=10.0):
    """Gera uma matriz n x n simetrica positiva definida.

    Ideia: pelo teorema, toda matriz simetrica, estritamente diagonal
    dominante e com diagonal nao-negativa e positiva definida.
    """
    A = [[0.0] * n for _ in range(n)]

    # Passo 1: sorteia a parte triangular superior e espelha (simetria)
    for i in range(n):
        for j in range(i + 1, n):
            valor = random.uniform(-limite, limite)
            A[i][j] = valor
            A[j][i] = valor

    # Passo 2: diagonal = soma dos modulos da linha + numero positivo
    for i in range(n):
        soma = sum(abs(A[i][j]) for j in range(n) if j != i)
        A[i][i] = soma + random.uniform(1.0, limite)

    return A

def eh_simetrica(A):
    n = len(A)
    return all(A[i][j] == A[j][i] for i in range(n) for j in range(i))

def diagonal_nao_negativa(A):
    return all(A[i][i] >= 0 for i in range(len(A)))

def eh_diag_dominante_estrita(A):
    n = len(A)
    for i in range(n):
        soma = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) <= soma:
            return False
    return True

def exibir_exemplo(A):
    n = len(A)
    print(f"Matriz {n}x{n}:")
    for linha in A:
        print("  [" + ", ".join(f"{v:8.3f}" for v in linha) + "]")

    print("Verificacao da dominancia diagonal estrita, linha a linha:")
    for i in range(n):
        soma = sum(abs(A[i][j]) for j in range(n) if j != i)
        print(f"  linha {i + 1}: |a{i + 1}{i + 1}| = {abs(A[i][i]):.3f} > {soma:.3f}  ->  {abs(A[i][i]) > soma}")

    print(f"Simetrica: {eh_simetrica(A)}")
    print(f"Diagonal nao-negativa: {diagonal_nao_negativa(A)}")
    print(f"Estritamente diagonal dominante: {eh_diag_dominante_estrita(A)}")
    print()

if __name__ == "__main__":
    random.seed(2026)  # semente fixa para os resultados serem reproduziveis

    for n in (3, 4, 5):
        print(f"=== Exemplo n = {n} ===")
        exibir_exemplo(gerar_matriz_pd(n))