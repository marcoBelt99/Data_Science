import numpy as np


def funzione01():
    """
    Esempio più semplice possibile: se memorizzassimo i nostri dati in liste Python (o
    liste di liste), la somma o la moltiplicazione delle liste elemento per
    elemento usando una sintassi normale non funzionerebbe, mentre
    funziona per ndarray: 
    """

    print("Operazioni sulle liste di Python")

    a = [1, 2, 3]
    b = [4, 5, 6]

    print("a+b", a+b)

    try:
        print(a*b)
    except TypeError:
        print("a*b non ha alcun significato per le liste di Python")
    print()
    print("Operazioni su matrici di numpy")
    a = np.array([1, 2, 3])  # creo un array con np.array()
    b = np.array([4, 5, 6])
    print("a+b", a+b)
    print("a*b", a*b)


def funzione02():
    """
    Funzioni lungo gli assi: somma degli elementi di una matrice
    """
    a = np.array([[1, 2], [3,4]]) 
    print("Matrice A: ", a)



def main():
    # funzione01()
    funzione02()


main()
