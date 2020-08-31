import numpy as np
import matplotlib.pyplot as plt

n = 20
p = np.zeros(n)
r = np.arange(0,4.0,0.005)
ra = np.arange(0,n,1)
on = np.ones(n);

for m in r:

	r = m
	p = np.zeros(n)
	p[0] = 0.2


	for i in range(0,n-1):

		p[i + 1] = r*p[i]*(1-p[i])

	ant = int((n/2)-1)
	dep = int(n-1)

	My_rango = p[ant:dep]
	my_set = set(My_rango)
	My_lista = list(my_set)

	R = r*np.ones(len(My_lista))

	plt.scatter(R,My_lista,s=1,c='b')

plt.grid()
plt.show()
