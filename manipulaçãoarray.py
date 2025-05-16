nomes = [] #cria a lista [] n esquecer  o =

for i in range(5):      #Um laço de repetição que roda 5 vezes (i vai de 0 até 4) n esquecer o :
    nome = input(f'Digite o {i+1}nome:')    #Usa input() para pedir ao usuário um nome. O f"" é uma f-string, usada para formatar o texto com o número atual (i+1)com a bolinha de numero, deixando a mensagem mais bonita.
    nomes.append(nome)      #Adiciona o nome digitado na lista nomes usando o método .append().

print('\nNomes em ordem alfabetica:')
nomes.sort()    #Organiza a lista nomes em ordem alfabética com .sort().
print(nomes) 

if'Lucas' in nomes: 

    print('Lucas esta na lista')

else:
   print ('Lucas nao esta na lista')
    
print(f'Total de nomes digitados: {len(nomes)}')  #Exibe quantos nomes foram digitados usando len(), que retorna o tamanho da lista.


