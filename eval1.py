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
    return ys[:n]


def retireAccent(texte):
    """
        paramètre texte : (str) Le texte dont on veut retirer les accents
        valeur renvoyée : (str) Le texte sans les accents

    >>> retireAccent('Éternel été, être où ça à')
    'Eternel ete, etre ou ca a'
    >>> retireAccent("à noël mon aïeul entendit précisément la grêle fouetter la tôle près de la façade du gîte où trônait un fût. Quel capharnaüm !")
    'a noel mon aieul entendit precisement la grele fouetter la tole pres de la facade du gite ou tronait un fut. Quel capharnaum !'
    """
    import unicodedata as ud
    # mettre le texte en forme décomposée
    forme_kd = ud.normalize('NFKD', texte)
    # renvoyer la chaîne constituée des caractères non "combinant" du texte
    return ''.join(c for c in forme_kd if not ud.combining(c))


def enMajuscule(texte):
    """
        paramètre texte : (str) Le texte sans accent qu'on veut mettre en majuscule
        valeur renvoyée : (str) Le texte en majuscule

    >>> enMajuscule('Ceci est un test.')
    'CECI EST UN TEST.'
    """
    sortie = ""
    for c in texte:
        if 'a' <= c <= 'z':
            c = chr(ord(c) + ord('A')-ord('a'))
        sortie += c
    return sortie


def retireDoublon(texte):
    """
        paramètre texte : (str) 
        valeur renvoyée : (str) Le texte où les lettres identiques consécutives ont été supprimées

    >>> retireDoublon('passionnant')
    'pasionant'
    >>> retireDoublon('cocorico')
    'cocorico'
    """
    sortie = texte[0]
    précédent = texte[0]
    for c in texte:
        if précédent != c:
            sortie += c
            précédent = c
    return sortie


# Construction du dictionnaire des valeurs par lettre
soundexValeurs = dict()
valeurs = {
    'AEHIOWY': 0,
    'BP': 1,
    'CKQ': 2,
    'DT': 3,
    'L': 4,
    'MN': 5,
    'R': 6,
    'GJ': 7,
    'XZS': 8,
    'FV': 9
}
for lettres in valeurs:
    val = valeurs[lettres]
    for c in lettres:
        soundexValeurs[c] = val


def codeSoundex(mot):
    """
        paramètre mot : (str) Le mot à coder en Soundex
        valeur renvoyée : (str) la version Soundex du mot

    >>> codeSoundex('SEIZE')
    'S800'
    >>> codeSoundex('CEZE')
    'C800'
    """
    mot = enMajuscule(retireAccent(mot))
    premiere = mot[0]
    traduction = ""
    for c in mot[1:]:
        if c in soundexValeurs:
            val = soundexValeurs[c]
            if val > 0:
                traduction += str(val)
        else:
            traduction += c
    traduction = retireDoublon(traduction)
    traduction = traduction + '000'
    return premiere + traduction[0:3]


def soundexParMot(texte):
    """
        paramètre texte : (str) Un texte non vide
        valeur renvoyée : (str) Chaque mot constitué de lettres est remplacé par son code SoundEx

    >>> soundexParMot('utf-8')
    'U390-8'
    >>> soundexParMot('seize, mots testés')
    'S800, M380 T838'
    """
    # on commence par découper le texte en une liste de parties
    # constituées alternativement de lettres et d'autres symboles
    parties = []
    mot = texte[0]
    etaitLettre = mot.isalpha()

    # pour chaque caractère du texte, s'il a le même status que le caractère précédent
    # on continue le "mot", sinon on ajoute le mot aux parties du texte et on commence
    # un nouveau mot
    for c in texte[1:]:
        estLettre = c.isalpha()
        if etaitLettre == estLettre:
            mot += c
        else:
            parties.append(mot)
            mot = c
            etaitLettre = estLettre
    # attention, le dernier mot n'est pas ajouté par la boucle
    parties.append(mot)

    # pour chaque mot, s'il est constitué de lettres, on le remplace par son code SoundEx
    for i in range(len(parties)):
        if parties[i][0].isalpha():
            parties[i] = codeSoundex(parties[i])

    return ''.join(parties)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
