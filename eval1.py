#!/usr/bin/python3
# -*- coding: utf-8
"""
Ce module contient les fonctions spécifiques à l'évaluation 1 du bloc 1
"""
from chaine import sousChaine, enMajuscule, retireAccent, retireDoublon


def importerQuestions(nomFichier):
    """
    Importe les questions depuis le fichier dont le nom est passé en paramètre
    """
    # ouverture du fichier
    fsource = open(nomFichier, 'r', encoding='utf-8')

    # lecture des lignes dans une liste de
    # p-uplets (question (str), réponse (str), points (int))
    questions = []
    for ligne in fsource:
        q, r, p = ligne.strip().split(';')
        questions.append((q, r, int(p)))

    fsource.close()

    return questions


# Construction du dictionnaire des valeurs par lettre (0 pour les lettres à supprimer)
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
    Calcule le code Soundex d'un mot (alphabétique)
        paramètre mot : (str) Le mot à coder (ne doit contenir que des caractères alphabétiques)
        valeur renvoyée : (str) la version Soundex du mot

    >>> codeSoundex('SEIZE')
    'S800'
    >>> codeSoundex('CEZE')
    'C800'
    """
    mot = enMajuscule(retireAccent(mot))
    premiere = mot[0]
    traduction = ''
    for c in sousChaine(mot, 1, len(mot)-1):
        if c in soundexValeurs:
            val = soundexValeurs[c]
            # Une valeur de 0 indique qu'on doit négliger la lettre
            if val > 0:
                traduction += str(val)
    traduction = retireDoublon(traduction)
    traduction = traduction + '000'
    return premiere + sousChaine(traduction, 0, 3)


def soundexParMot(texte):
    """
    Applique le codage Soundex à tous les mots (alphabétique) d'un texte
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
    for c in sousChaine(texte, 1, len(texte)-1):
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

    # recollons les morceaux
    sortie = ''
    for partie in parties:
        sortie += partie

    return sortie


if __name__ == "__main__":
    import doctest
    doctest.testmod()
