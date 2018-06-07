#!/usr/bin/python
from item import Item
from Knapsack import Knapsack
from pylab import *
from random import *
from numpy import *  


def calcKnapsack(arrayDeItens, Knapsack):
	#for xx in range(0, size(array)):
	#	print array[xx].peso, array[xx].valor
	m = Knapsack.cap
	n = Knapsack.itensAmount
	matriz = np.zeros((m+1, n+1), dtype=np.int)
	#matrix = cria_matriz((n+(1)), (m+(1)), 0)
	for x in range(0,m+1):
		for i in range(1,n):
			a = matrix[i-1][x]
			if ((x-arrayDeItens[i].peso) >= 0):
				b = arrayDeItens[i].valor + matrix[i-1][x-arrayDeItens[i].peso]
 				if (a<b):
 					a = b
 			matrix[i][x] = a
 	return matrix[n][m]

def calcKnapsackAlternativo(array, Knapsack):
	x = 0
	i = 1
	m = Knapsack.cap
	n= Knapsack.itensAmount
	matrix = cria_matriz(n+1, m+1, 0)
	while x <= m:
		a = matrix[i][x]
		if x-array[i].peso >= 0:
			b = array[i].peso + matrix[i-1][x-array[i].peso]
			if a<b:
				a = b
		matrix[i][x] = a
		i = i + 1
		if i == n+1:
			i = 1
			x = x + 1
	j = matrix[n][m]
	return j
				
def cria_matriz(n_lines, n_columns, value):
    matriz = [] 
    for i in range(n_lines):
        line = []
        for j in range(n_columns):
        	line.append(value)
		matriz.append(line)
    return matriz	

def readFile(nome):
	f = open(""+nome+".txt","r")
	array = []
	cont = 0
	for linha in f:
		if (cont != 0):
			valores = linha.split()
			item = Item(int(valores[1]), int(valores[0]))
			array.append(item)
		else:
			valores = linha.split()
			array.append(Knapsack(int(valores[1]), int(valores[0])))
			cont = cont + 1 
	f.close()
	return array

############################################################################
a = 0
while a<1 or a>3 :
	a = input("Knapsack number: ")
else: 
	array = readFile("Knapsack"+str(a))
	Knapsack = Knapsack(int(array[0].itensAmount), int(array[0].cap))
	array.pop(0)
	print calcKnapsack(array, Knapsack)
