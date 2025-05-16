numeros = [10, 20 ,30 ,40 ,50]
print('lista original:', numeros)

print('Primeiro elemento:', numeros[0]) #acessa o primeiro elemento
print('Ultimo elemento: ', numeros[-1])  #acessa o segundo elemento Em Python, índices negativos começam do final.

numeros[2] = 99                             #altera o valor do indice 2 de 30 pra 90
print('Lista apos alteracao:', numeros)

numeros.append(60)  # adiciona 60 no final da lista.
numeros.insert(1, 15) #insere ele na posicao 1, deslocando os demais
print('Lista apos adicoes')

numeros.remove(40)  #remove o valor 40 da lista
removido = numeros.pop() #remove o ultimo elemento da lista e o retorna sendo o 60

print('Valor removido com pop():', removido) #Mostra o valor que foi retirado com pop().
print('Lista apos remocoes:', numeros)


print('Percorrendo com for:')
for numero in numeros:
    print(f'{numero}', end=' ')

print()  # para pular linha depois do for pq fiz antes e ficou tudo junto

numeros.sort()  #crescente
numeros.reverse()  #reverso(decrescente)

print('Lista invertida (decrescente):', numeros)
print()

if 99 in numeros:
    print('O valor 99 esta na lista.')
else:
    print('O valor 99 nao esta na lista.')
