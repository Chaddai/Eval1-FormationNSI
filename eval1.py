#!/usr/bin/python3
# -*- coding: utf-8 
"""
Ce module contient les fonctions communes
pour réaliser l'évaluation 1 du bloc 1 comme
la fonction mélanger() et la fonction sélectionner()
"""

import random as rd

def mélanger(xs):
    """
    Paramètre xs : list La liste à mélanger sur place
    Sortie None

    >>> L = [1,2,3]; mélanger(L); set(L) == set([1,2,3])
    True
    >>> L = [1,1,2,3]; mélanger(L); len(L) == 4
    True
    """
    for i in range(len(xs)-1, 0, -1):
        j = rd.randint(0,i)
        (xs[j], xs[i]) = (xs[i], xs[j]) 

def sélectionner(n, xs):
    """
    Paramètre n : int Le nombre d'éléments à sélectionner au hasard
    Paramètre xs : list La liste dans laquelle les éléments sont sélectionnés

    >>> len(sélectionner(2, [1,2,3,4])) == 2
    True
    >>> set(sélectionner(2, [1,2,3,4])).issubset(set([1,2,3,4]))
    True
    """
    assert n <= len(xs), "Liste trop courte pour sélectionner "+str(n)+" éléments."
    ys = list(xs)
    mélanger(ys)
    return ys[:n]



if __name__ == "__main__":
    import doctest
    doctest.testmod()