"""
Integrantes do grupo:
Augusto de Paula Freitas	8937191
Giovane Cunha Mocelin		8778382
Lucas Kassouf Crocomo		8937420
"""

import math
#retorna valor na função
def f(x):
	return 42*pow(x,4) - 23*pow(x,3) + 163*pow(x,2) - 92*x - 20
#retorna valor na f'
def fPrime(x):
	return 168*pow(x,3) - 69*pow(x,2) + 326*x -92

def newton(a, b, tol, maxiter):
	#inicializo string para escrevermos no arquivo de saída
	retString = 'k\txk\tf(xk)\tf\'(xk)\tek\n'
	
	#se a for raíz,
	if f(a) == 0:
		#appendamos os valores de k, xk, f(xk), f'(xk), e ek na string de saída
		retString += '0\t' + '%.10f'%(a) + '\t' + '%.10f'%(0) + '\t' + '%.10f'%(0) + '\n'
		return retString
	#senão, se b for raíz
	elif f(b) == 0:
		#appendamos os valores de k, xk, f(xk), f'(xk), e ek na string de saída e retornamos
		retString += '0\t' + '%.10f'%(b) + '\t' + '%.10f'%(0) + '\t' + '%.10f'%(0) + '\n'
		return retString
	#se f(a)*f(b) >0, não há raíz no intervalo
	if f(a)*f(b) > 0:
		#appendamos erro na string de saída e retornamos 
		retString = 'Não há raiz no intervalo [' + str(a) + ', ' + str(b) + '].\n'
		return retString
	#inicializamos iterador como 0 e erro como infinito
	k = 0
	err = math.inf

	#no intervalo [-1,0], a raíz da função (xbarra) é -1/6
	if ((a == -1) & (b == 0)):
		xbarra = -1/6
	else:
	#no outro intervalo especificado, a raíz da função é 5/7
		xbarra = 5/7


	x0 = a
	x = a
	
	#enquanto erro for maior que a tolerância (10^-6) e k menor que número máximo de iterações, fazer
	while ((err > tol) & (k < maxiter)):
		#appendamos os valores de k, xk, f(xk), f'(xk), e ek na string de saída
		retString += str(k) +'\t' + '%.10f'%(x0) + '\t' + '%.10f'%(f(x0)) + '\t' + '%.10f'%(fPrime(x0)) + '\t' + '%.10f'%(abs(x-xbarra)) + '\n'
		#se xk assumir valor fora do intervalo, appendamos erro na string de saída e retornamos
		if((x < a) | (x > b)):
			retString += 'Erro: Não foi possivel executar o método de newton, xk assume valor fora do intervalo [' + str(a) + ', ' + str(b) + '].\n'
			return retString
		#senão, se f'(xk) = 0, appendamos erro na string de saída e retornamos
		elif((fPrime(x) == 0)):
			retString += retString += 'Erro: Não foi possivel executar o método regula falsi, f\'(xk) asusme zero.\n'

		#calculamos xk
		x = x0 - f(x0)/fPrime(x0)
		#atualizamos o erro
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