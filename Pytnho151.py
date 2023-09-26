#151 Entrar com o nome do paciente
nome = input("Digite o nome do paciente: ")

# Entrar com o peso do paciente em Kg
peso = float(input("Digite o peso do paciente em Kg: "))

# Entrar com a altura do paciente em metros
altura = float(input("Digite a altura do paciente em metros: "))

# Calcular o IMC do paciente
imc = peso / altura**2

# Classificar a faixa de risco do paciente de acordo com a tabela
if imc < 20:
    risco = "abaixo do peso"
elif imc <= 25:
    risco = "normal"
elif imc <= 30:
    risco = "excesso de peso"
elif imc <= 35:
    risco = "obesidade"
else:
    risco = "obesidade mórbida"

# Imprimir o nome do paciente e sua faixa de risco
print("O paciente", nome, "está na faixa de risco", risco)