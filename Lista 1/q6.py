def newton(f, df, x0, tol=1e-6, nmax=100):
    x = x0
    for i in range(1, nmax + 1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            return None, i
        x_novo = x - fx / dfx
        if abs(x_novo - x) < tol:
            return x_novo, i
        x = x_novo
    return None, nmax

def bissecao(f, a, b, tol=1e-6, nmax=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        return None, 0

    p_ant = a
    for i in range(1, nmax + 1):
        p = (a + b) / 2
        fp = f(p)
        if fp == 0 or abs(p - p_ant) < tol:
            return p, i
        if fa * fp < 0:
            b = p
        else:
            a, fa = p, fp
        p_ant = p
    return p, nmax

def f6(x):
    return x ** 3 - 2 * x - 5

def df6(x):
    return 3 * x ** 2 - 2

# Execucao
print("RESULTADOS DA QUESTAO 6 (a)")
print("Metodo de Newton implementado (funcao newton(f, df, x0, tol, nmax)).")

print("\nRESULTADOS DA QUESTAO 6 (b)")
raiz_newton, it_newton = newton(f6, df6, x0=2, tol=1e-6, nmax=100)
print(f"Raiz (Newton):        {raiz_newton}")
print(f"Iteracoes (Newton):   {it_newton}")

print("\nRESULTADOS DA QUESTAO 6 (c)")
raiz_bissec, it_bissec = bissecao(f6, 2, 3, tol=1e-6, nmax=100)
print(f"Raiz (Bissecao):      {raiz_bissec}")
print(f"Iteracoes (Bissecao): {it_bissec}")

print("\nRESULTADOS DA QUESTAO 6 (d)")
print(f"{'Metodo':<12}{'Raiz':<22}{'Iteracoes'}")
print(f"{'Newton':<12}{raiz_newton:<22}{it_newton}")
print(f"{'Bissecao':<12}{raiz_bissec:<22}{it_bissec}")
print()
print(f"Diferenca entre as raizes: {abs(raiz_newton - raiz_bissec):.2e}")
print()
print("Conclusao: os dois metodos convergem para a mesma raiz (dentro da")
print("tolerancia 1e-6), aproximadamente x = 2.0946. O Metodo de Newton")
print("converge com muito menos iteracoes porque sua convergencia e")
print("quadratica (o numero de digitos corretos aproximadamente dobra a")
print("cada iteracao), enquanto a Bissecao converge linearmente, reduzindo")
print("o intervalo pela metade a cada passo -- por isso precisa de bem")
print("mais iteracoes para atingir a mesma tolerancia.")