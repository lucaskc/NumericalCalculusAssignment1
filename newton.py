"""
Integrantes do grupo:
Augusto de Paula Freitas	8937191
Giovane Cunha Mocelin		8778382
Lucas Kassouf Crocomo		8937420
"""

import math

def f(x):
	return 42*pow(x,4) - 23*pow(x,3) + 163*pow(x,2) - 92*x - 20

def fPrime(x):
	return 168*pow(x,3) - 69*pow(x,2) + 326*x -92

def newton(a, b, tol, maxiter):
	
	retString = 'k\txk\tf(xk)\tf\'(xk)\tek\n'

	if f(a) == 0:
		retString += '0\t' + '%.10f'%(a) + '\t' + '%.10f'%(0) + '\t' + '%.10f'%(0) + '\n'
		return retString
	elif f(b) == 0:
		retString += '0\t' + '%.10f'%(b) + '\t' + '%.10f'%(0) + '\t' + '%.10f'%(0) + '\n'
		return retString
	if f(a)*f(b) > 0:
		retString = 'Não há raiz no intervalo [' + str(a) + ', ' + str(b) + '].\n'
		return retString

	k = 0
	err = math.inf

	if ((a == -1) & (b == 0)):
		xbarra = -1/6
	else:
		xbarra = 5/7

	x0 = a
	x = a
	
	while ((err > tol) & (k < maxiter)):
		retString += str(k) +'\t' + '%.10f'%(x0) + '\t' + '%.10f'%(f(x0)) + '\t' + '%.10f'%(fPrime(x0)) + '\t' + '%.10f'%(abs(x-xbarra)) + '\n'
		if((x < a) | (x > b)):
			retString += 'Erro: Não foi possivel executar o método de newton, xk assume valor fora do intervalo [' + str(a) + ', ' + str(b) + '].\n'
			return retString
		x = x0 - f(x0)/fPrime(x0)
		err = abs(x-x0)/max(1,x)
		x0 = x
		k += 1

	return retString

def main():
	#Config do arquivo
	PATH = './saida_newton.xls'
	file = open(PATH, 'w+')

	tol = pow(10,-6)
	maxiter = 10000000	

	#Executa primeiro intervalo
	saida = newton(-1, 0, tol, maxiter)
	print(saida,'\n')
	file.write(saida)
	file.write('\n')

	#Executa segundo intervalo
	saida = newton(0, 1, tol, maxiter) #Erro
	print(saida, '\n')
	file.write(saida)
	file.write('\n')
	
	#Executa segundo intervalo corrigindo o intervalor para [0.5, 1]
	saida = newton(0.5, 1, tol, maxiter)
	print(saida)
	file.write(saida)

	file.close()
	
if __name__ == "__main__":
	main()