'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

variaveis = {}

print("Bem-vindo ao cadastro de variaveis!")
print("Você pode cadastrar quantas variaveis quiser. Digite 'sair' para finalizar.")

while True: 
    # Pedimos ao usuário para inserir o nome da variável
    nome - input("Digite o nome da variável: ")
    
    # Se o usuário digitar 'sair', o loop é interrompido
    if nome.lower() == 'sair':
        break
    
    # Pedimos ao usuário para inserir o valor da variável
    valor = input(f"Digitar o valor para {nome}: ")
    
    # Salvamos a variável no dicionário
    variaveis[nome] = valor
    
# Exibimos todas as variáveis cadastradas
print("\nVariáveis cadastradas:")
for nome, valor in variaveis.items():
    print(f"{nome} = {valor}")
    
print("\nFim do programa! Obrigado por utilizar")
    # TODO: write code...
