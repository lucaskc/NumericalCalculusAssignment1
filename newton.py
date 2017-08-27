"""
Integrantes do grupo:
Augusto de Paula Freitas	8937191
Giovane Cunha Mocelin		8778382
Lucas Kassouf Crocomo		8937420
"""

import numpy as np

#retorna valor na função
def f(x):
	return 42*np.power(x,4) - 23*np.power(x,3) + 163*np.power(x,2) - 92*x - 20
#retorna valor na f'
def fPrime(x):
	return 168*np.power(x,3) - 69*np.power(x,2) + 326*x -92

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
	err = np.float64('inf')

	#no intervalo [-1,0], a raíz da função (xbarra) é -1/6
	if ((a == -1) & (b == 0)):
		xbarra = np.float64(-1/6)
	else:
	#no outro intervalo especificado, a raíz da função é 5/7
		xbarra = np.float64(5/7)


	x0 = a
	x = a
	
	#enquanto erro for maior que a tolerância (10^-6) e k menor que número máximo de iterações, fazer
	while ((err > tol) & (k < maxiter)):
		#appendamos os valores de k, xk, f(xk), f'(xk), e ek na string de saída
		retString += str(k) +'\t' + '%.10f'%(x0) + '\t' + '%.10f'%(f(x0)) + '\t' + '%.10f'%(fPrime(x0)) + '\t' + '%.10f'%(np.absolute(x-xbarra)) + '\n'
		#se xk assumir valor fora do intervalo, appendamos erro na string de saída e retornamos
		if((x < a) | (x > b)):
			retString += 'Erro: Não foi possivel executar o método de newton, xk assume valor fora do intervalo [' + str(a) + ', ' + str(b) + '].\n'
			return retString
		#senão, se f'(xk) = 0, appendamos erro na string de saída e retornamos
		elif((fPrime(x) == 0)):
			retString += 'Erro: Não foi possivel executar o método regula falsi, f\'(xk) asusme zero.\n'

		#calculamos xk
		x = x0 - f(x0)/fPrime(x0)
		#atualizamos o erro
		err = np.absolute(x-x0)/np.maximum(1,x)
		x0 = x
		k += 1

	return retString

def main():
	#Config do arquivo
	PATH = './newton_saida.xls'
	file = open(PATH, 'w+')

	tol = np.float64(np.power(10.0,-6))
	maxiter = 10000000	

	#Executa primeiro intervalo
	saida = newton(np.float64(-1), np.float64(0), tol, maxiter)
	print(saida,'\n')
	file.write(saida)
	file.write('\n')

	#Executa segundo intervalo
	saida = newton(np.float64(0), np.float64(1), tol, maxiter) #Erro
	print(saida, '\n')
	file.write(saida)
	file.write('\n')
	
	#Executa segundo intervalo corrigindo o intervalor para [0.5, 1]
	saida = newton(np.float64(0.5), np.float64(1), tol, maxiter)
	print("Executando para intervalo [0.5, 1]")
	print(saida)
	file.write(saida)

	file.close()
	
if __name__ == "__main__":
	main()