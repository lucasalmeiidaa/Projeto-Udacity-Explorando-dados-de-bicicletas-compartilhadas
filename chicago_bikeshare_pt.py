# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
data_list_20 = data_list[1:21]
for i, data in enumerate(data_list_20):
    print((i+1),":", data) #R: Imprime as 20 linhas com seus respectivos números.

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for data in data_list[0:21]:
    print(data[-2])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
        Função para criar uma lista a partir de uma coluna.
        Argumentos:
            data: Arquivo que será lido.
            index: Índice do cabecalho que deseja-se criar uma lista (Ex.: 2 -> Trip Duration).
         Retorna:
            Uma lista de strings.

    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for lines in data:
        column_list.append(lines[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0

for line in data_list: #R: Loop criado para iterar cada índice [-2] da linha.
    if line[-2] == "Male": #R: Se a string contida no -2 for "Male", soma-se 1 em male.
        male += 1
    elif line[-2] == "Female": #R: Se a string contida no -2 for "Female", soma-se 1 em female.
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
        Função para contar os gêneros.
        Argumentos:
            data_list: Arquivo lido.
        Retorna:
            Valores na forma [número de homens, número de mulheres].

    """
    male = 0
    female = 0
    genders = column_to_list(data_list, -2)
    for gender in genders:
        if gender == "Male":
            male = male + 1
        elif gender == "Female":
            female = female + 1
        else:
            continue
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
        Função para definir o gênero mais popular.
        Argumentos:
            data_list: Arquivo lido.
        Retorna:
            Uma string como resposta.

    """
    answer = ""
    genders = column_to_list(data_list, -2)
    count_genero = count_gender(data_list) #R: Utiliza-se a função 'count_gender' criada anteriormente
    if count_genero[0] > count_genero[1]:  #que retorna valore [male, female]. Com isso, pode-se comparar
        answer = answer + "Male"           #os valores desta lista retornada.
    elif count_genero[0] < count_genero[1]:
        answer = answer + "Female"
    else:
        answer = answer + "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_user_types(data_list): #R: Primeiramente, vamos definir uma função que conta user types.
    """
     Função para contar 'User Types'.
     Argumentos:
         data_list: Arquivo a ser lido.
     Retorna:
         Valores na forma [número de customers, número de subscriber].

    """
    customer = 0
    subscriber = 0
    types = column_to_list(data_list, -3) #R: 'column_to_list' é uma função definida anteriormente para criar
    for type in types:                    #uma lista a partir de uma coluna (index).
        if type == "Subscriber":
            subscriber = subscriber + 1
        elif type == "Customer":
            customer = customer + 1
        else:
            continue
    return [customer, subscriber]

types = column_to_list(data_list, -3) #R: (Questão extra -> Descobrir qual o outro consumidor.)
other_types = []
for type in types: #R: Cria-se um loop com types e avalia se é 'Subscriber' ou 'Customer'.
    if (type != "Subscriber") and (type != "Customer"):
        other_types.append(type) #R: Caso não seja nenhum, adiciona o mesmo em uma lista.
other_types = set(other_types) #R: Retira mais de uma string igual, deixando só uma de cada tipo.
print("R: O outro tipo de consumidor sem ser 'customer' e 'subscriber' é: ", other_types)

print("R: Primeiramente, o número de User Types [Customer, Subscriber] é:", count_user_types(data_list))
print("R: Gráfico gerado.")

user_types_list = column_to_list(data_list, -3) #R: Agora geramos o gráfico.
types = ["Customer", "Subscribe"]
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User type')
plt.xticks(y_pos, types)
plt.title('Quantidade por \'User Type\'')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Pois existem alguns dados de \'gender\' que não foram preenchidos, ficando em branco."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

trip_duration_list = sorted(list(map(int, trip_duration_list))) #R: Itera cada elemento da lista como int.
min_trip = trip_duration_list[0] #R: Busca o primeiro elemento de uma lista organizada crescente.
max_trip = trip_duration_list[-1] #R: Busca o último elemento de uma lista organizada cerscente.


def mean(trip_duration_list): #R: Cria-se a função mean para que faça media.
    """
     Função para calcular a média.
     Argumentos:
         trip_duration_list: Lista contendo a duração de cada viagem como int.
     Retorna:
         A média da lista de números inteiros 'trip_duration_list'.

    """
    soma = 0
    for duration in trip_duration_list: #R: Loop criado para somar todos os números int da lista.
        soma = soma + duration
    return (float(soma / len(trip_duration_list))) #R: Retorna a média.
mean_trip = mean(trip_duration_list)

if len(trip_duration_list) % 2 == 0:    #R:Verifica se é par ou não para assim tirar a mediana.
    lst_1 = trip_duration_list[0:((len(trip_duration_list) // 2) + 1)] #R:Cria uma lista cortada até a metade.
    lst_2 = trip_duration_list[((len(trip_duration_list) // 2)):] #R: Cria uma lista da metade pra frente.
    median_trip = (lst_1[-1] + lst_2[0]) // 2 #R: Calcula a mediana com base nos dois números do meio.

else:
    median_trip = trip_duration_list[(len(trip_duration_list)) // 2] #R: Obtém o número exatamente na metade da lista.

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

start_stations = set(column_to_list(data_list, 3)) #R: Aqui, usa-se o método set() para a função
                                                   #'column_to_list' criada anteriormente.
print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """
     Função para contar tipos de usuários.
     Argumentos:
         column_list: Arquivo a ser lido.
     Retorna:
         Types na forma [X, ..., Xn] e Counts na forma [Y, ..., Yn].

    """
    types = list(set(column_list))  #R: Retira as strings repetidas, deixando uma de cada.
    counts = [0]*len(types) #R: Multiplica a lista com valor 0 pela qtd de tipos.
    for index, item in enumerate(types): #R: Para cada índice, ítem na lista enumerada de tipos:
        for i in column_list: #R: Para a string na column_list:
            if i == item: #R: Se essa string for igual a um type já existente.
                counts[index] += 1 #R: Soma +1 no índice que representa esse tipo.
            else: #R: Se não:
                continue #R: Continua o loop.
    return types, counts #R: Retorna types e counts. CÓDIGO FEITO COM AUXÍLIO DO FÓRUM.

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------

print("\n \n O número de linha total desse arquivo é:", len(data_list))
print("\n \n FIM DO PRIMEIRO PROJETO! :)")
