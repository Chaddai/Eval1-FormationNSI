#!/usr/bin/python3
# -*- coding: utf-8
"""
Ce module contient les fonctions communes sur les chaînes de caractères, 
écrites au fur et à mesure de l'année.
"""


def sousChaine(texte, début, taille):
    """
    Extrait une chaîne formée des caractères de texte depuis l'indice début de la taille indiquée
        paramètre texte : (str) Une chaîne de caractères
        paramètre début : (int) l'indice où débute l'extraction (inclus)
        paramètre taille : (int) la taille de la chaîne à extraire
        valeur renvoyée : (str) Une chaîne de caractère extraite de texte
    On doit avoir 0 <= début < len(texte) et 0 <= taille <= len(texte) - début

    >>> sousChaine('Bonjour tout le monde !', 0, 7)
    'Bonjour'
    """
    assert 0 <= début < len(texte), "L'indice de début doit être valide"
    assert 0 <= taille <= len(texte) - début, "Vous ne pouvez extraire autant de caractères"
    extrait = ''
    for i in range(début, début+taille):
        extrait += texte[i]
    return extrait


# Construction d'un dictionnaire des lettres accentuées vers leur version sans accent
sansAccent = dict()
accents = {
    'àâä': 'a',
    'æ': 'ae',
    'ç': 'c',
    'éèêë': 'e',
    'ïî': 'i',
    'ôö': 'o',
    'œ': 'oe',
    'ûùü': 'u',
    'ÿ': 'y',
    'ÀÂÄ': 'A',
    'Æ': 'AE',
    'Ç': 'C',
    'ÉÈÊË': 'E',
    'ÏÎ': 'I',
    'ÔÖ': 'O',
    'Œ': 'OE',
    'ÛÙÜ': 'U',
    'Ÿ': 'Y',
}
for typeAccent in accents:
    for lettre in typeAccent:
        sansAccent[lettre] = accents[typeAccent]


def retireAccent(texte):
    """
    Construit une version de texte sans accents (texte français).
        paramètre texte : (str) Le texte dont on veut retirer les accents
        valeur renvoyée : (str) Le texte sans les accents

    >>> retireAccent('Éternel été, être où ça à')
    'Eternel ete, etre ou ca a'
    >>> retireAccent("à noël mon aïeul entendit précisément la grêle fouetter la tôle près de la façade du gîte où trônait un fût. Quel capharnaüm !")
    'a noel mon aieul entendit precisement la grele fouetter la tole pres de la facade du gite ou tronait un fut. Quel capharnaum !'
    """
    sortie = ''
    for c in texte:
        if c in sansAccent:
            sortie += sansAccent[c]
        else:
            sortie += c
    return sortie


def retireAccentUnicode(texte):
    """
    Construit une version de texte sans accents.
        paramètre texte : (str) Le texte dont on veut retirer les accents
        valeur renvoyée : (str) Le texte sans les accents

    >>> retireAccentUnicode('Éternel été, être où ça à')
    'Eternel ete, etre ou ca a'
    >>> retireAccentUnicode("à noël mon aïeul entendit précisément la grêle fouetter la tôle près de la façade du gîte où trônait un fût. Quel capharnaüm !")
    'a noel mon aieul entendit precisement la grele fouetter la tole pres de la facade du gite ou tronait un fut. Quel capharnaum !'
    """
    import unicodedata as ud
    # mettre le texte en forme décomposée
    forme_kd = ud.normalize('NFKD', texte)
    # renvoyer la chaîne constituée des caractères non "combinant" du texte
    sortie = ''
    for c in forme_kd:
        if not ud.combining(c):
            sortie += c
    return sortie


def enMajuscule(texte):
    """
    Met en majuscule un texte sans accents
        paramètre texte : (str) Le texte sans accents qu'on veut mettre en majuscule
        valeur renvoyée : (str) Le texte en majuscule

    >>> enMajuscule('Ceci est un test.')
    'CECI EST UN TEST.'
    """
    sortie = ''
    for c in texte:
        if 'a' <= c <= 'z':
            c = chr(ord(c) + ord('A')-ord('a'))
        sortie += c
    return sortie


def retireDoublon(texte):
    """
    Retire les lettres consécutives identiques
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


def demanderEntierEntre(a, b, demande):
    """
    Demande un entier entre a et b et répète la demande tant que la réponse n'est pas satisfaisante
        paramètre a : (int)
        paramètre b : (int)
        paramètre demande : (str) La question à poser
    """
    while True:
        try:  # nécessaire pour traiter le cas où l'utilisateur n'entre pas un entier
            n = int(input(demande))
            if a <= n <= b:
                return n
        except:
            pass
        print('Vous devez entrer un entier entre', a, 'et', b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
