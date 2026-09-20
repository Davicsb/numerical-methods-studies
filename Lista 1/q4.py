import math
import matplotlib.pyplot as plt

def plot_function(f, a, b, n, ax=None, label=None, **kwargs):
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 4))

    passo = (b - a) / (n - 1)
    xs = [a + i * passo for i in range(n)]
    ys = [f(x) for x in xs]

    ax.plot(xs, ys, '-', label=label, **kwargs)
    ax.axhline(0, color='gray', linewidth=0.7)
    ax.grid(True, alpha=0.3)
    return ax

def bissecao_sequencia(f, a, b, tol=1e-6, nmax=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        return None

    pontos = []
    p_ant = a
    for _ in range(nmax):
        p = (a + b) / 2
        pontos.append(p)
        fp = f(p)
        if fp == 0 or abs(p - p_ant) < tol:
            return pontos
        if fa * fp < 0:
            b = p
        else:
            a, fa = p, fp
        p_ant = p
    return pontos

def f_questao4(x):
    """f(x) = ln(x) - 2^x + x^2 - 1"""
    return math.log(x) - 2 ** x + x ** 2 - 1

# Execucao
print("RESULTADOS DA QUESTAO 4 (a)")
print("Validando plot_function com f(x) = sin(x) em [0, 2*pi], n=60")
ax1 = plot_function(math.sin, 0, 2 * math.pi, 60, label="sin(x)")
ax1.set_title("Validacao de plot_function: f(x) = sin(x)")
ax1.legend()
plt.savefig("questao4a_validacao.png", dpi=150, bbox_inches="tight")
print("Grafico salvo em questao4a_validacao.png")
plt.show()

print("\nRESULTADOS DA QUESTAO 4 (b)")
pontos = bissecao_sequencia(f_questao4, 3, 5, tol=1e-6, nmax=100)
print(f"Numero de iteracoes: {len(pontos)}")
print(f"Raiz aproximada:     {pontos[-1]}")

ax2 = plot_function(f_questao4, 3, 5, 200, label="f(x) = ln(x) - 2^x + x^2 - 1")
xs_p = pontos
ys_p = [f_questao4(p) for p in xs_p]
ax2.plot(xs_p, ys_p, 'o', color='red', markersize=4, label="sequencia p_n (bissecao)")
ax2.set_title("Bissecao: sequencia de aproximacoes sobre o grafico de f")
ax2.legend()
plt.savefig("questao4b_bissecao.png", dpi=150, bbox_inches="tight")
print("Grafico salvo em questao4b_bissecao.png")
plt.show()