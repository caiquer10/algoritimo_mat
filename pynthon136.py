#136 Definir uma função para calcular o algoritmo 36
def algoritmo_36(num):
  # Inicializar as variáveis
  soma = 0
  cont = 0
  # Repetir enquanto o número não for zero
  while num != 0:
    # Obter o último dígito do número
    digito = num % 10
    # Somar o dígito ao acumulador
    soma = soma + digito
    # Incrementar o contador de dígitos
    cont = cont + 1
    # Remover o último dígito do número
    num = num // 10
  # Retornar a média aritmética dos dígitos
  return soma / cont

# Ler um número do usuário
num = int(input("Digite um número: "))

# Chamar a função para calcular o algoritmo 36
resultado = algoritmo_36(num)

# Imprimir o resultado
print(f"O resultado do algoritmo 36 é {resultado:.2f}")