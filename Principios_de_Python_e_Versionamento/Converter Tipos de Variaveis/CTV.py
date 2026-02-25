
#============= CONVERSÃO DE TIPOS DE VARIÁVEIS =============#

# Em alguns momentos é necessário converter tipos de variáveis em Python. para manipular de forma diferente. Por exemplo:
 
# Variáveis do tipo "string" , que armazenam números e precisamos fazer alguma operação matemática com esse valor

preco = 10
print(preco)

preco = float(preco)
print(preco)
# Nesse caso, converti a variável "preco" de inteiro (int) para ponto flutuante (float)

# uma outra forma de fazer essa conversão é utilizando a divisão por ponto flutuante

preco = 10 / 2
print(preco)
# Nesse caso, o Python já converteu automaticamente o valor para float

# Da mesma forma podemos converter do tipo float para inteiro

preco = 10.30
print(preco)
# Exibi 10.3

preco = int(preco)
print(preco)
# Exibi 10, ou seja, o Python descarta a parte decimal

#============= CONVERSÃO POR DIVISÃO =============#

# Vamos converter essa mesma operaração usando a divisão por inteiro

preco = 10 
print(preco)
# Exibi 10

print(preco / 2)
# Exibi 5.0, ou seja, o Python converteu automaticamente para float

print(preco // 2)
# Exibi 5, ou seja, o Python converteu automaticamente para int

#============= NUMERICO PARA STRING =============#

preco = 10.50
idade = 28

print(str(preco))
# Exibi '10.5'

print(str(idade))
# Exibi '28'
# Nesse caso, convertemos os valores numéricos para string

texto = f"idade {idade} preco {preco}"
print(texto)
# O "F" antes das aspas indica que é uma string formatada, ou seja, podemos inserir variáveis dentro da string

#Para concatenar passamos elas entre chaves {}

# Exibi 'idade 28 preco 10.5'

#============= STRING PARA NUMERICO =============#

valor = "10.50"
idade = "28"

print(float(valor))
# Exibi 10.5
# Estamos utilizando a função ou contrutor float() para converter a string em número de ponto flutuantes

print(int(idade))
# Exibi 28
# Nesse caso, convertemos os valores string para numéricos

#============= ERROS DE CONVERSAO =============#

# Nem sempre a conversão de tipos de variáveis é possível. Por exemplo:

preco = "python"
print(float(preco))
# Nesse caso, o Python retornará um erro do tipo ValueError, pois não é possível converter a string "python" em número de ponto flutuante