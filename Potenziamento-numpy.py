import numpy as np

# Matrice 3 righe e 2 colonne
print("Matrice 3 righe e 2 colonne")
M1 = np.array([[1,2],[3,4], [6, 7]])
print(M1)

print("\n")

# Matrice trasposta
print("Matrice Trasposta")
M1_trasposta = M1.T
print(M1_trasposta)
print("\n")

# Creazione vettore e mescolamento dei suoi elementi in maniera casuale
print("Creazione vettore e mescolamento dei suoi elementi in maniera casuale")
x = [3,4,5,10,15,1,0]
print(x)

print("Vettore mescolato")
np.random.shuffle(x)
print(x)

print("\n")
# Prodotto elemento per elemento di due vettori
x = np.array([2,2])
y = np.array([2,3])
print("Vettore x: " ,  x.T, "\t", "Vettore y:" , y.T)
print(x.dot(y.T))

