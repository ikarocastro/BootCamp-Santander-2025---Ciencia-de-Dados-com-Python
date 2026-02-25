# A função input() é usada para receber dados do usuário.
nome = input("Digite seu nome: ")
# A função print() é usada para exibir dados na tela.
print("Olá,", nome + "!")

#========== EXIBINDO VALORES CO A FUÇÃO PRINT() ==========#

nome = "Guilherme"
sobrenome = "Carvalho"

print(nome, sobrenome)            # Exibe os valores separados por espaço
print(nome, sobrenome, end="...")  # Altera o final da linha para "..."
print(nome, sobrenome, sep="#")  # Altera o separador entre os valores para "#"

# Sera exibido:
# Guilherme Carvalho
# Guilherme Carvalho...
# Guilherme#Carvalho

