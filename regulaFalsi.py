"""
Integrantes do grupo:
Augusto de Paula Freitas	8937191
Giovane Cunha Mocelin		8778382
Lucas Kassouf Crocomo		8937420
"""

import math

def f(x):
	return 42*pow(x,4) - 23*pow(x,3) + 163*pow(x,2) - 92*x - 20

def regulaFalsi(a, b, tol, maxiter):
	
	retString = 'k\txk\tf(xk)\tek\n'

	if f(a) == 0:
		retString += '0\t' + '%.10f'%(a) + '\t' + '%.10f'%(0) + '\t' + '%.10f'%(0) + '\n'
		return retString
	elif f(b) == 0:
		retString += '0\t' + '%.10f'%(b) + '\t' + '%.10f'%(0) + '\t' + '%.10f'%(0) + '\n'
		return retString
	if f(a)*f(b) > 0:
		retString = 'Erro: Não há raiz no intervalo [' + str(a) + ', ' + str(b) + '].\n'
		return retString

	k = 1
	err0 = math.inf
	err1 = math.inf

	if ((a == -1) & (b == 0)):
		xbarra = -1/6
	else:
		xbarra = 5/7

	x0 = a
	x1 = b
	x = a
	
	retString += str(0) + '\t' + '%.10f'%(x0) + '\t' + '%.10f'%(f(x0)) + '\t' + '%.10f'%(abs(x-xbarra)) + '\n'
	
	while ((err0 > tol) & (err1 > tol) & (k < maxiter)):
		
		retString += str(k) + '\t' + '%.10f'%(x1) + '\t' + '%.10f'%(f(x1)) + '\t' + '%.10f'%(abs(x-xbarra)) + '\n'
		if((x < a) | (x > b) | (f(x1)-f(x0) == 0)):
			retString += 'Erro: Não foi possivel executar o método regula falsi, pois no intervalo [' + str(a) + ', ' + str(b) + '] f\'(x) possui zero.\n'
			return retString
		elif((x < a) | (x > b)):
			retString += 'Erro: Não foi possivel executar o método regula falsi, xk assume valor fora do intervalo [' + str(a) + ', ' + str(b) + ']\n'
			return retString
		x = (f(x1)*x0-f(x0)*x1)/(f(x1)-f(x0))
		err0 = abs(x-x0)/max(1,x0)
		err1 = abs(x-x1)/max(1,x1)
		if (f(x)*f(x1) < 0):
			x0 = x1
		x1 = x
		
		k += 1

	return retString

def main():
	#Config do arquivo
	PATH = './saida_regula_falsi.xls'
	file = open(PATH, 'w+')

	tol = pow(10,-6)
	maxiter = 10000000

	#Executa primeiro intervalo
	saida = regulaFalsi(-1, 0, tol, maxiter)
	print(saida, '\n')
	file.write(saida)
	file.write('\n')

	#Executa segundo intervalo
	saida = regulaFalsi(0, 1, tol, maxiter)
	print(saida)
	file.write(saida)

	file.close()
	
if __name__ == "__main__":
	main()