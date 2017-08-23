import math

def f(x):
	return 42*pow(x,4) - 23*pow(x,3) + 163*pow(x,2) - 92*x - 20

def bisection(a, b, tol, maxiter):
	
	if f(a) == 0:
		retString += '0\t' + '%.10f'%(a) + '\t' + '%.10f'%(0) + '\t' + '%.10f'%(0) + '\n'
		return retString
	elif f(b) == 0:
		retString += '0\t' + '%.10f'%(b) + '\t' + '%.10f'%(0) + '\t' + '%.10f'%(0) + '\n'
		return retString
	if f(a)*f(b) > 0:
		retString = 'Não há raiz no intervalo [' + str(a) + ', ' + str(b) + '].\n'
		return retString

	retString = 'k\ta\tb\txk\tek\n'

	k = 0
	err = math.inf

	x = (a+b)/2
	if ((a == -1) & (b == 0)):
		xbarra = -1/6
	elif ((a == 0) & (b == 1)):
		xbarra = 5/7

	while ((err > tol) & (k < maxiter)):
		retString += str(k) + '\t' + '%.10f'%(a) + '\t' + '%.10f'%(b) + '\t' + '%.10f'%(x) + '\t' + '%.10f'%(abs(x-xbarra)) + '\n'
		if f(a)*f(x) < 0:
			b = x
		else:
			a = x
		x0 = x
		x = (a+b)/2
		err = abs(x-x0)/max(1,x)
		k += 1

	return retString

def main():
	#Config do arquivo
	PATH = './saida_bisseccao.xls'
	file = open(PATH, 'w+')

	tol = pow(10,-6)
	maxiter = 10000000

	#Executa primeiro intervalo
	saida = bisection(-1, 0, tol, maxiter)
	print(saida, '\n')
	file.write(saida)
	file.write('\n')
	
	#Executa segundo intervalo
	saida = bisection(0, 1, tol, maxiter)
	print(saida)
	file.write(saida)

	file.close()

if __name__ == "__main__":
	main()