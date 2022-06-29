N = int(input('N= '))  #variavel N para armazenar a quantidade de nomes que vão ser  inseridos
nomes_gerais = []    #essa variavel eu criei pra ir adicionando todos os nomes, sem formatação nem nada
nomes_divididos= []  #nessa outra lista, coloquei os nomes já dividos entre nome e sobrenome, ou seja, não eram mais uma unica string
sobrenomes = []  #essa lista criei para guardar os sobrenomes e facilitar no momento de chamar apenas os mesmos
nome = []      #essa foi a lista que recebeu os primeiros nomes

for c in range(N): #loop for para a inserção dos nomes
    x = input('Digite um nome e sobrenome: ') #variavel x recebe os nomes
    if x.count(' ') > 1: #comando if e count pra caso o usuario use o carcetere espaço mais de uma vez(com a intenção de colocar mais um sobrenome), a maquina entender isso como um erro, e refazer o pedido de nome
        print('Por favor, digite apenas nome e sobrenome!!') #print com mensagem de erro
        x = input('Digite um nome e sobrenome: ') # x novamente pedindo o nome, já que o anterior foi considerado invalído
    
    else: #else, para que se o erro acima não ocorrer, o programa dividir a string
        nomes_gerais.append(x)   #lista recebendo os nomes sem formatação alguma

for i in range(N): #loop for para fazer a separação dos nomes e sobrenomes e depois inserir  cada um em sua devida lista
    nomes_divididos.append(nomes_gerais[i].split()) #lista recebendo os nomes já divididos pela função split()
    sobrenomes.append(nomes_divididos[i][1]) #inserção dos sobrenomes em sua lista especifica
    nome.append(nomes_divididos[i][0]) #inserção dos primeiros nomes em sua respectiva lista 

#função sort() sendo aplicada nas duas variaveis para efetuar o ordenamento alfabetico em cada uma
nome.sort()
sobrenomes.sort()

for j in range(N): #ultimo loop, feito para imprimir o nome e sobrenome já em ordem alfabetica
    print(f'{nome[j]} {sobrenomes[j]}'.title()) #formatação através do método de "f strings" e comando title() para as letras iniciais de cada palavra saírem em caixa alta
