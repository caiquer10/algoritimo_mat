#148 Definir as regiões e os preços
regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
precos = [350, 400, 450, 500, 550]

# Criar uma função para calcular o preço da passagem
def calcular_preco(origem, destino):
  # Verificar se a origem e o destino são válidos
  if origem not in regioes or destino not in regioes:
    return "Região inválida"
  # Verificar se a origem e o destino são iguais
  if origem == destino:
    return "Origem e destino iguais"
  # Obter os índices da origem e do destino na lista de regiões
  indice_origem = regioes.index(origem)
  indice_destino = regioes.index(destino)
  # Calcular a diferença entre os índices
  diferenca = abs(indice_origem - indice_destino)
  # Obter o preço base da origem
  preco_base = precos[indice_origem]
  # Multiplicar a diferença pelo fator de 50 reais
  preco_final = preco_base + diferenca * 50
  # Retornar o preço final
  return f"O preço da passagem de {origem} para {destino} é R${preco_final}.00"