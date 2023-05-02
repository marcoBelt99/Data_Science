import numpy as np
from typing import Callable

def fun01():
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


def fun02():
    """
    Funzioni lungo gli assi: somma degli elementi di una matrice lungo gli assi.
    Essenzialmente 'comprime la matrice' lungo l'asse 0 (righe) oppure 1 (colonne)
    e restituisce una matrice che ha una dimensione in meno rispetto a quella originale
    """
    a = np.array([[1, 2], [3,4]]) # creo una matrice
    print("Matrice A: ", a)
    # Somma lungo l'asse 0 (lungo le righe)
    print("Somma asse 0 (righe): ", a.sum(axis=0))
    # Somma lungo l'asse 1 (lungo le colonne)
    print("Somma asse 1 (colonne): ", a.sum(axis=1))


def fun03():
    """
    ndarray NumPy supporta la somma di una matrice 1D sull'ultimo asse.
    Es se a e' una matrice di R righe e C colonne, allora posso sommare ad a una 
    matrice 1D b di lunghezza C e NumPy calcolera' la somma in modo intuitivo, 
    aggiungendo gli elementi ad ogni riga di a
    """
    a = np.array([  [1,2,3],
                    [4,5,6]])
    b = np.array([10,20,30])
    print("a+b\n", a+b)
    
def square(x: np.ndarray) -> np.ndarray:
    """
    Calcola il quadrato di ogni elemento della ndarray in input

    Args:
        x (np.ndarray): array di input

    Returns:
        np.ndarray: quadrato di x
    """
    return np.power(x,2)

def leaky_relu(x: np.ndarray) -> np.ndarray:
    """
    Applica la funzione 'Leaky ReLU' a ogni elemento del ndarray

    Args:
        x (np.ndarray): input

    Returns:
        np.ndarray: output
    """
    return np.maximum(0.2 * x, x)


def deriv(func: Callable[[np.ndarray], np.ndarray],
            input_: np.ndarray,
            delta: float = 0.001 ) -> np.ndarray:
    """
    Calcolo della derivata di una funzione "func" per ogni elemento della matrice "input"

    Args:
        func (Callable[[np.ndarray], np.ndarray]): funzione da derivare
        input_ (np.ndarray): matrice
        delta (float, optional): _description_. Defaults to 0.001.

    Returns:
        np.ndarray: _description_
    """
    return (func(input_ + delta) - func(input-delta)) / (2*delta)



def main():
    # fun01()
    # fun02()
    # fun03()

    # Test delle funzioni
    x = np.array([3,-2,5])
    print(x)
    print("Quadrato di x: ", square(x))
    
    print("ReLU di x: ", leaky_relu(x))
    
    

    
main()
