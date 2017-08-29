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

def bisection(a, b, tol, maxiter):

	#inicializo string para escrevermos no arquivo de saída
	retString = 'k\ta\tb\txk\tek\n'

	if f(a) == 0: #se a for raíz,
		#concatenamos os valores de k, a, b, f(xk), e ek na string de saída e retornamos
		retString += '0\t' + '%.10f'%(a) + '\t' + '%.10f'%(0) + '\t' + '%.10f'%(0) + '\n' 
		return retString
	elif f(b) == 0: #senão, se b for raíz
		#concatenamos os valores de k, a, b, f(xk), e ek na string de saída e retornamos
		retString += '0\t' + '%.10f'%(b) + '\t' + '%.10f'%(0) + '\t' + '%.10f'%(0) + '\n' 
		return retString

	if f(a)*f(b) > 0: #se f(a)*f(b) >0, não há raíz no intervalo
		#concatenamos erro na string de saída e retornamos
		retString = 'Não há raiz no intervalo [' + str(a) + ', ' + str(b) + '].\n'  
		return retString

	#inicializamos iterador como 0 e erro como infinito
	k = 0
	err = np.float64('inf')

	if ((a == -1) & (b == 0)): #no intervalo [-1,0], a raíz da função (xbarra) é -1/6
		xbarra = np.float64(-1/6)
	else:
		xbarra = np.float64(5/7) #no outro intervalo especificado, a raíz da função é 5/7

	x = np.float64((a+b)/2)

	#enquanto erro for maior que a tolerância (10^-6) e k menor que número máximo de iterações, fazer
	while ((err > tol) & (k < maxiter)):
		#concatenamos os valores de k, a, b, f(xk), e ek na string de saída
		retString += str(k) + '\t' + '%.10f'%(a) + '\t' + '%.10f'%(b) + '\t' + '%.10f'%(x) + '\t' + '%.10f'%(np.absolute(x-xbarra)) + '\n'
		if f(a)*f(x) < 0: #se f(a)*f(x) < 0 a proxima iteracao será realizada no intervalo [a, x] ou o da esquerda
			b = x
		else: #senao a proxima iteracao será realizada no intervalo [x, b] ou o da direita
			a = x
		x0 = x
		#calculamos xk
		x = (a+b)/2
		#atualizamos o erro
		err = np.absolute(x-x0)/np.maximum(1,x)
		k += 1
	return retString

def main():
	#Config do arquivo
	PATH = './bisseccao_saida.xls'
	file = open(PATH, 'w+')

	tol = np.float64(np.power(10.0,-6))
	maxiter = 10000000

	#Executa primeiro intervalo
	saida = bisection(np.float64(-1), np.float64(0), tol, maxiter)
	print(saida, '\n')
	file.write(saida)
	file.write('\n')

	
	#Executa segundo intervalo
	saida = bisection(np.float64(0), np.float64(1), tol, maxiter)
	print(saida)
	file.write(saida)

	file.close()

if __name__ == "__main__":
	main()