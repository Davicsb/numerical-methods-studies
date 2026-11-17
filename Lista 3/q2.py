# Dados do problema (partilhados por todas as alíneas)
h = [0.0, 0.5, 1.0, 1.5, 2.0]
V = [0.0, 620.0, 1480.0, 2570.0, 4020.0]
h_alvo = 1.25

# a) Método dos Mínimos Quadrados (Grau 2)
def minimos_quadrados(x_vals, y_vals):
    n = len(x_vals)
    sum_x = sum(x_vals)
    sum_x2 = sum(x**2 for x in x_vals)
    sum_x3 = sum(x**3 for x in x_vals)
    sum_x4 = sum(x**4 for x in x_vals)

    sum_y = sum(y_vals)
    sum_xy = sum(x_vals[i] * y_vals[i] for i in range(n))
    sum_x2y = sum((x_vals[i]**2) * y_vals[i] for i in range(n))

    # Matriz A e Vetor B (A * a = B)
    A = [
        [n,      sum_x,  sum_x2],
        [sum_x,  sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4]
    ]
    B = [sum_y, sum_xy, sum_x2y]

    # Determinante de matriz 3x3
    def det3x3(M):
        return (M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1]) -
                M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0]) +
                M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]))

    # Substituição de coluna para a Regra de Cramer
    def replace_col(M, col_idx, V_col):
        M_copy = [row[:] for row in M]
        for i in range(3):
            M_copy[i][col_idx] = V_col[i]
        return M_copy

    # Resolução por Regra de Cramer
    det_A = det3x3(A)
    a0 = det3x3(replace_col(A, 0, B)) / det_A
    a1 = det3x3(replace_col(A, 1, B)) / det_A
    a2 = det3x3(replace_col(A, 2, B)) / det_A

    return a0, a1, a2

# b) Interpolação de Lagrange (Grau 4)
def lagrange_interpolation(x_vals, y_vals, x_target):
    n = len(x_vals)
    y_target = 0.0
    
    for i in range(n):
        L_i = 1.0
        for j in range(n):
            if i != j:
                L_i *= (x_target - x_vals[j]) / (x_vals[i] - x_vals[j])
        y_target += y_vals[i] * L_i
        
    return y_target

# c) Método de Neville
def neville_method(x_vals, y_vals, x_target):
    n = len(x_vals)
    P = [[0.0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        P[i][0] = y_vals[i]
        
    for j in range(1, n):
        for i in range(j, n):
            termo1 = (x_target - x_vals[i - j]) * P[i][j - 1]
            termo2 = (x_target - x_vals[i]) * P[i - 1][j - 1]
            denominador = x_vals[i] - x_vals[i - j]
            P[i][j] = (termo1 - termo2) / denominador
            
    return P


# Execução e Apresentação dos Resultados
print("a) MÉTODO DOS MÍNIMOS QUADRADOS")
a0, a1, a2 = minimos_quadrados(h, V)
print(f"Coeficientes encontrados: a0 = {a0:.2f}, a1 = {a1:.2f}, a2 = {a2:.2f}")
print(f"Polinómio: p2(h) = {a0:.2f} + {a1:.2f}h + {a2:.2f}h^2")
v_estimado_mq = a0 + a1*h_alvo + a2*(h_alvo**2)
print(f"Volume estimado na curva para h = {h_alvo}m: {v_estimado_mq:.2f} L")

print()
print("b) INTERPOLAÇÃO DE LAGRANGE")
vol_lagrange = lagrange_interpolation(h, V, h_alvo)
print(f"Volume interpolado para h = {h_alvo}m: {vol_lagrange:.5f} L")

print()
print("c) MÉTODO DE NEVILLE")
tabela_neville = neville_method(h, V, h_alvo)
n_pontos = len(h)

print(f"Tabela Triangular para h = {h_alvo}m:\n")
for i in range(n_pontos):
    linha = f"i={i} | h={h[i]:.1f} | "
    for j in range(i + 1):
        linha += f"{tabela_neville[i][j]:.3f} | "
    print(linha)

vol_neville = tabela_neville[n_pontos-1][n_pontos-1]
print(f"\nValor final estimado do Volume: {vol_neville:.5f} L")