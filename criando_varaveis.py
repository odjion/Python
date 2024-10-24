# ----------------------------
# VARIÁVEIS
# ----------------------------
# Variáveis são usadas para armazenar informações que podem ser usadas mais tarde.
# Exemplo de variável:
nome = "João"

# A variável 'nome' armazena uma string com o valor "João".

# ----------------------------
# ENTRADA DE DADOS
# ----------------------------
# Podemos usar a função input() para obter dados do usuário.
nome = input("Qual é o seu nome? ")

# A função input() sempre retorna uma string, mesmo que o usuário digite um número.
# Para converter para outros tipos, usamos funções como int(), float(), etc.
idade = int(input("Qual é a sua idade? "))

# ----------------------------
# SAÍDA DE DADOS
# ----------------------------
# Usamos a função print() para exibir valores no console.
print(f"Olá, {nome}!")
print(f"Você tem {idade} anos!")

# f-string é uma forma de concatenar strings com variáveis, facilitando a leitura.
# É mais moderno e eficiente do que usar + para concatenar strings.

# ----------------------------
# MAIS EXEMPLOS DE VARIÁVEIS
# ----------------------------
# Variáveis podem armazenar diferentes tipos de valores:
altura = 1.75  # número decimal (float)
job = "Software Engineer"  # string

# Exibindo as variáveis:
print(f"Sua altura é {altura} metros.")
print(job)  # exibe "Software Engineer" no console.

# ----------------------------
# EXEMPLO DE CÓDIGO SIMPLES
# ----------------------------
# Este código exibe uma mensagem simples no console.
print("Hello, World!")
