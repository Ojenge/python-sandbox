from math import *

def polysum(n, s):
	
	area_poly = ((0.25 * n * (s**2))/(tan(pi/n)))
	
	peri_poly = (n * s)**2
	
	sum_poly = area_poly + peri_poly
	
	
	
	return round(sum_poly, 4)	
	
	