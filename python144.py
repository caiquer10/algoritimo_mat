#144 Definir uma função para calcular o crédito especial
def calcular_credito(saldo_medio):
  # Verificar o saldo médio e aplicar o percentual correspondente
  if saldo_medio <= 500:
    credito = 0
  elif saldo_medio <= 1000:
    credito = saldo_medio * 0.3
  elif saldo_medio <= 3000:
    credito = saldo_medio * 0.4
  else:
    credito = saldo_medio * 0.5
  # Retornar o crédito calculado
  return credito

# Ler o saldo médio do usuário
saldo_medio = float(input("Digite o saldo médio: "))

# Chamar a função para calcular o crédito especial
credito = calcular_credito(saldo_medio)

# Imprimir uma mensagem informando o saldo médio e o valor do crédito
if credito > 0:
  print(f"Como seu saldo era de R${saldo_medio:.2f}, seu crédito será de R${credito:.2f}.")
else:
  print(f"Como seu saldo era de R${saldo_medio:.2f}, você não terá nenhum crédito.")