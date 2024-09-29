import json

def calcular_faturamento(dados_faturamento):
    faturamentos_validos = [dia['valor'] for dia in dados_faturamento if dia['valor'] > 0]

    if not faturamentos_validos:
        return "Nenhum dia de faturamento válido encontrado."

    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)

    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

    dias_acima_da_media = sum(1 for valor in faturamentos_validos if valor > media_mensal)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

with open('faturamento.json', 'r') as arquivo:
    dados_faturamento = json.load(arquivo)

resultado = calcular_faturamento(dados_faturamento)

print(f"Menor faturamento: {resultado['menor_faturamento']}")
print(f"Maior faturamento: {resultado['maior_faturamento']}")
print(f"Número de dias acima da média: {resultado['dias_acima_da_media']}")
