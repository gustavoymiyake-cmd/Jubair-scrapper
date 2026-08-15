import json
from datetime import datetime, timedelta

# Simulação da função que busca dados (Na prática, você usaria uma API ou Scraper aqui)
def buscar_ocupacao_airbnb(id_imovel):
    # O Airbnb usa uma API GraphQL oculta para buscar os calendários.
    # Por proteção, simularemos o retorno: 40 dias ocupados de 84 possíveis.
    return {"dias_ocupados_12_semanas": 40, "total_dias": 84}

# 1. Carregar a lista de imóveis que você quer monitorar
with open('imoveis.json', 'r') as f:
    config = json.load(f)

resultados = {
    "ultima_atualizacao": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "imoveis": []
}

# 2. Processar cada imóvel
for imovel in config['lista']:
    dados_ocupacao = buscar_ocupacao_airbnb(imovel['id_airbnb'])
    
    taxa = (dados_ocupacao['dias_ocupados_12_semanas'] / 84) * 100
    
    resultados['imoveis'].append({
        "nome": imovel['nome'],
        "id": imovel['id_airbnb'],
        "dias_reservados": dados_ocupacao['dias_ocupados_12_semanas'],
        "taxa_ocupacao": round(taxa, 1)
    })

# 3. Salvar o resultado consolidado para o site HTML ler
with open('dados_consolidados.json', 'w') as f:
    json.dump(resultados, f, indent=4)
    
print("Atualização concluída e salva com sucesso!")
