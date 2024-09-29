faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())

def calcular_porcentagem(quantiaEstado):
    return (quantiaEstado/faturamento_total)

for estado, quantiaEstado in faturamento_estados.items():
    percentual = calcular_porcentagem(quantiaEstado)
    print(f"{estado}: {percentual:.2f}% do total")

print(f"Faturamento total: {faturamento_total:.2f}")
