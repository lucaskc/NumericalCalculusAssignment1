import math

def f(x):
	return 42*pow(x,4) - 23*pow(x,3) + 163*pow(x,2) - 92*x - 20

def fPrime(x):
	return 168*pow(x,3) - 69*pow(x,2) + 326*x -92

def newton(a, b, tol, maxiter):
	k = 0
	err = math.inf

	print('k', '\txk', ' \tf(xk)', ' \tf\'(xk)', ' \tek')

	if ((a == -1) & (b == 0)):
		xbarra = -1/6
	else:
		xbarra = 5/7
	

	x0 = a
	x = 0
	
	while ((err > tol) & (k < maxiter)):
		print(k, '\t', x0, '\t', f(x0), '\t', fPrime(x0), '\t', abs(x-xbarra))
		x = x0 - f(x0)/fPrime(x0)
		err = abs(x-x0)/max(1,x)
		x0 = x
		k += 1
	return x

def main():

	tol = pow(10,-6)
	maxiter = 10000000	
	newton(-1, 0, tol, maxiter)
	print('\n\n\n')
	newton(0, 1, tol, maxiter)	#Da ruim
	print('\n\n\n')
	newton(0.5, 1, tol, maxiter)
	
if __name__ == "__main__":
	main()