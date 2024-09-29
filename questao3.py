def calcular_faturamento(faturamento):
    menorFaturamento = min(f for f in faturamento if f > 0)
    maiorFaturamento = max(faturamento)

    mediaFaturamento = (sum(faturamento)/len(faturamento))
    
    diasAcimaMedia = len([f for f in faturamento if f > mediaFaturamento])

    return menorFaturamento, maiorFaturamento, diasAcimaMedia


faturamento = [
    0, 100, 200, 300, 150, 0, 400, 250, 100, 50, 0, 500, 0, 350, 0, 
    600, 700, 100, 800, 0, 0, 900, 120, 130, 140, 0, 110, 50, 0, 160
]

menor, maior, dias_acima_media = calcular_faturamento(faturamento)

# Exibe os resultados
print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
