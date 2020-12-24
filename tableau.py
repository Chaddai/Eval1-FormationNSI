#!/usr/bin/python3
# -*- coding: utf-8
"""
Ce module contient les fonctions communes sur les tableaux, écrites au fur et à mesure de l'année.
"""
import random as rd


def appartient(x, xs):
    """
    Vérifie si un élément x appartient au tableau xs
        paramètre x : (a) Une valeur du type des éléments du tableau
        paramètre xs : (list(a)) Un tableau
        valeur renvoyée : (bool) Si x est présent (égal ==) à un élément de xs

    >>> appartient(1, [1,2,3])
    True
    >>> appartient(1, [4,5,6])
    False
    >>> appartient(1, [])
    False
    """
    for val in xs:
        if x == val:
            return True
    return False


def extraction(xs, début, taille):
    """
    Extrait du tableau xs un nouveau tableau formé des éléments de xs depuis l'indice début
    et de la taille indiquée
        paramètre xs : (list(a)) Un tableau
        paramètre début : (int) l'indice où débute l'extraction (inclus)
        paramètre taille : (int) la taille du tableau à extraire
        valeur renvoyée : (list(a)) Un nouveau tableau extrait de xs
    On doit avoir 0 <= début < len(xs) et 0 <= taille <= len(xs) - début

    >>> extraction([0,1,2,3,4], 2, 2)
    [2, 3]
    """
    assert 0 <= début < len(xs), "L'indice de début doit être valide"
    assert 0 <= taille <= len(xs) - début, "Vous ne pouvez extraire d'éléments au-delà de la liste"
    extrait = []
    for i in range(début, début+taille):
        extrait.append(xs[i])
    return extrait


def mélanger(xs):
    """
    Mélange équiprobable du tableau xs à l'aide de l'algorithme de Fisher-Yates
        paramètre xs : (list) La liste à mélanger sur place
        valeur renvoyée : aucune

    >>> L = [1,2,3]; mélanger(L); set(L) == set([1,2,3])
    True
    >>> L = [1,1,2,3]; mélanger(L); len(L) == 4
    True
    """
    for i in range(len(xs)-1, 0, -1):
        j = rd.randint(0, i)
        (xs[j], xs[i]) = (xs[i], xs[j])


def sélectionner(n, xs):
    """
    Tirage aléatoire sans remise de n éléments de xs
        paramètre n : (int) Le nombre d'éléments à sélectionner au hasard (sans remise)
        paramètre xs : (list) La liste dans laquelle les éléments sont sélectionnés
        valeur renvoyée : (list) une liste de n éléments sélectionnés dans xs

    >>> len(sélectionner(2, [1,2,3,4])) == 2
    True
    >>> set(sélectionner(2, [1,2,3,4])).issubset(set([1,2,3,4]))
    True
    """
    assert n <= len(xs), "Liste trop courte pour sélectionner "+str(n)+" éléments."
    ys = list(xs)
    mélanger(ys)
    return extraction(ys, 0, n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
