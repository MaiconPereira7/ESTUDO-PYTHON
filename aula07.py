n1 = int (input ('Digite o primeiro numero:'))
n2 = int (input ('Digite o segundo numero:'))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

#print('A soma entre',numero1, 'e',numero2 ,'e de' , s)

print('A soma e {} , o produto e {} e a divisao e {} ' .format(s, m, d))
print('A divisao inteira {} e potencia e {}'.format (di, e ))
