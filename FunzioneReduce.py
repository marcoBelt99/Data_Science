""" 
La funzione reduce() applica una funzione itarativamente a tutti i membri di una collezione
di dati, accumulando il risultato che, al termine della scansione, viene restituito da reduce(f, collezione)
"""

from functools import reduce

def somma(x, y):
    return x+y

lista = [1, 5, 6, 7, 12]

print(lista)

print("La somma di tutti gli elementi con la funzione REDUCE e': " + str(reduce(somma, lista)))

sum = 0
for elemento in lista:
    sum += elemento

print("somma degli elementi con classico ciclo for: " + str(sum))
