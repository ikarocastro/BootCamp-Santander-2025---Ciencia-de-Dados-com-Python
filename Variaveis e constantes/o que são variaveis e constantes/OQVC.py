age = 28
name = "Alice"
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade')

# A variável 'age' pode ser alterada para outro valor
age = 29
print(f'No próximo ano, eu terei {age} ano(s) de idade')
# A variável 'name' também pode ser alterada
name = "Bob"
print(f'Meu nome agora é {name}')

# A variável 'name' pode ser alterada para outro valor
name = "Charlie"
print(f'Meu nome agora é {name}')
# Variáveis são usadas para armazenar dados que podem mudar ao longo do tempo
print(f'Olá, meu nome é {name} e eu tenho {age} anos.')

# Constantes
PI = 3.14159
print(f'PI vale {PI}')
# A constante 'PI' não deve ser alterada
# PI = 3.14  # Isso não é recomendado
# Constantes são usadas para valores que não mudam
print(f'O valor de PI é sempre {PI}')   

STATES = ['SP', 'RJ', 'MG']
print(f'Estados brasileiros: {STATES}')


# Tipos de dados
# int - inteiro
# float - ponto flutuante
# str - string
# bool - booleano

height = 1.75  # float
is_student = True  # bool
print(f'Altura: {height} metros')
print(f'É estudante: {is_student}')
# Exemplo de uso de variáveis e constantes em um programa simples
print(f'Nome: {name}, Idade: {age}, Altura: {height}, Estudante: {is_student}, PI: {PI}')


#OBSERVAÇÕES:

# Em python, não existe uma sintaxe específica para definir constantes.
# Por convenção, usamos letras maiúsculas para indicar que uma variável é uma constante.
# Para fazer isso , basta nomear a variável com todas as letras maiúsculas, como no exemplo acima com 'PI'.
# Ou seja se eu observo no meu código uma variável com todas as letras maiúsculas, eu sei que ela é uma constante e não deve ser alterada.

# BOAS PRÁTICAS:

# O padrão de nomes para variáveis em Python é o snake_case, onde as palavras são separadas por underscores (_).
# Exemplo: minha_variavel, idade_usuario, nome_completo.

# O padrão de nomes para constantes em Python é o UPPER_SNAKE_CASE, onde todas as letras são maiúsculas e as palavras são separadas por underscores (_).
# Exemplo: MINHA_CONSTANTE, VALOR_MAXIMO, TAXA_DE_JUROS.

# Escolhers nomes sugestivos ou seja nomes que façam sentido para o contexto do programa.

# Nome de constantes devem ser escritos em letras maiúsculas para indicar que são valores que não devem ser alterados.

# É muito importante seguir essas convenções para manter a legibilidade e a manutenção do código.