import math

def f(x):
	return 42*pow(x,4) - 23*pow(x,3) + 163*pow(x,2) - 92*x - 20

def bisection(a, b, tol, maxiter):
	if f(a) == 0:
		return a
	elif f(b) == 0:
		return b
	if f(a)*f(b) > 0:
		print ('error')

	k = 0
	err = math.inf
	x = (a+b)/2
	if ((a == -1) & (b == 0)):
		xbarra = -1/6
	elif ((a == 0) & (b == 1)):
		xbarra = 5/7
		
	#-pow((2/(3*(9 + pow(93,(1/2))))),(1/3)) + pow((1/2*(9 + pow(93,(1/2)))),(1/3))/pow(3,(2/3))

	print('k', ' \ta', ' \tb', ' \txk', ' \tek')

	while ((err > tol) & (k < maxiter)):
		print(k, '\t', a, '\t', b, '\t', x, '\t', abs(x-xbarra))
		if f(a)*f(x) < 0:
			b = x
		else:
			a = x
		x0 = x
		x = (a+b)/2
		err = abs(x-x0)/max(1,x)
		k += 1
	return x

def main():

	tol = pow(10,-6)
	maxiter = 10000000	
	bisection(-1, 0, tol, maxiter)
	print('\n\n\n')
	bisection(0, 1, tol, maxiter)

if __name__ == "__main__":
	main()