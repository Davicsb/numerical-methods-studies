# Função auxiliar exponencial sem usar bibliotecas externas (Série de Taylor)
def exponencial(x):
    soma = 1.0
    termo = 1.0
    n = 1
    # 30 termos são suficientes para alta precisão
    while n < 30:
        termo *= x / n
        soma += termo
        n += 1
    return soma

# a) Definição da função f(t) = 0
def f(t):
    return 63.0 * exponencial(-0.25 * t) - 13.0

# b) Implementação do Método da Bissecção
def bisseccao(func, a, b, tol=1e-6, max_iter=1000):
    if func(a) * func(b) >= 0:
        return None  # Não garante raiz no intervalo
    
    an = a
    bn = b
    raiz_anterior = an
    
    for _ in range(max_iter):
        cn = (an + bn) / 2.0
        
        # Critério de parada: diferença entre aproximações consecutivas ou valor exato
        if abs(cn - raiz_anterior) < tol or func(cn) == 0.0:
            return cn
            
        if func(an) * func(cn) < 0:
            bn = cn
        else:
            an = cn
            
        raiz_anterior = cn
        
    return cn

# c) Algoritmo para encontrar automaticamente subintervalos e aplicar a bissecção
def encontrar_raiz_por_subintervalos(func, a, b, C, tol=1e-6):
    # Divide o intervalo [a, b] em subintervalos de comprimento C
    intervalos = []
    inicio = a
    while inicio < b:
        fim = min(inicio + C, b)
        intervalos.append((inicio, fim))
        inicio = fim
        
    # Testa cada subintervalo
    for sub_a, sub_b in intervalos:
        # Verifica se há mudança de sinal (Teorema de Bolzano)
        if func(sub_a) * func(sub_b) < 0:
            # Chama o Método da Bissecção para o subintervalo encontrado
            return bisseccao(func, sub_a, sub_b, tol)
            
    return None  # Retorna nulo caso não encontre nenhuma raiz

# d) Execução para a letra d
a_val = 0.0
b_val = 30.0
C_val = 3.0

tempo_aproximado = encontrar_raiz_por_subintervalos(f, a_val, b_val, C_val)

print("RESULTADOS")
print(f"Intervalo de busca: [{a_val}, {b_val}] com comprimento C = {C_val}")
if tempo_aproximado is not None:
    print(f"Tempo aproximado em que a temperatura atinge 35°C: t = {tempo_aproximado:.6f} minutos")
    print(f"Verificação f(t) = {f(tempo_aproximado)}")
else:
    print("Nenhuma raiz encontrada no intervalo especificado.")