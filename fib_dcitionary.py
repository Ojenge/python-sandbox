def fib_efficient(n. d):
	if n in d:
		return d[n]
	else:
		ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
		d[n] = ans
		return ans
		
#base cases for the fibonacci sequence
d = {1:1, 2:2}