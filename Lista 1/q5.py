# b) Implementação do Método da Iteração de Ponto Fixo
def ponto_fixo(g, x0, tol=1e-6, max_iter=100):
    xn = x0
    for n in range(max_iter):
        x_novo = g(xn)
        
        # Critério de parada
        if abs(x_novo - xn) < tol:
            return x_novo, n + 1
            
        xn = x_novo
        
    return None, max_iter  # Retorna nulo/None caso não haja convergência após N_max

# c) Definição das funções g1 e g2
def g1(x):
    return 1.0 / (1.0 + x)

def g2(x):
    return (1.0 / x) - 1.0

# Parâmetros solicitados na letra c
x0 = 0.5
tol = 1e-6
max_iter = 100

print("RESULTADOS DA QUESTÃO 5 (c)")

# Testando g1
raiz_g1, iter_g1 = ponto_fixo(g1, x0, tol, max_iter)
if raiz_g1 is not None:
    print(f"Função g1(x): Convergiu para x = {raiz_g1:.6f} em {iter_g1} iterações.")
else:
    print(f"Função g1(x): Não convergiu após {max_iter} iterações.")

# Testando g2
raiz_g2, iter_g2 = ponto_fixo(g2, x0, tol, max_iter)
if raiz_g2 is not None:
    print(f"Função g2(x): Convergiu para x = {raiz_g2:.6f} em {iter_g2} iteracoes.")
else:
    print(f"Função g2(x): Não convergiu (retornou nulo) após {max_iter} iterações.")