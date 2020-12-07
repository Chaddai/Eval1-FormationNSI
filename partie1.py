#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random as rd

def mélanger(xs):
    """
    Paramètre xs : list La liste à mélanger sur place
    Sortie None

    >>> set(mélanger([1,2,3])) == set(1,2,3)
    True
    >>> len(mélanger([1,1,2,3])) == 4
    True
    """
    for i in range(len(xs)-1, 0, -1):
        j = rd.randint(0,i)
        (xs[j], xs[i]) = (xs[i], xs[j]) 

# ouverture du fichier
fsource = open('quizz-diu-eil.txt','r')

# lecture des lignes dans une liste de
# p-uplets (question (str), réponse (str), points (int))
questions = []
for ligne in fsource:
    try:
        q, r, p = ligne.strip().split(';')
        questions.append([q,r,int(p)])
    except:
        pass

fsource.close()

# Sélection aléatoire du nombre de questions souhaité
nb_questions = int(input('Combien de questions souhaitez-vous ? '))
assert nb_questions <= len(questions), "Trop de questions demandées, seules "+str(len(questions))+" sont disponibles."
mélanger(questions)
questions = questions[0:nb_questions]

score = 0
for (question, réponse, points) in questions:
    print(question)
    rep = input("Votre réponse : ")
    if rep == réponse:
        score += points

print("Vous avez obtenu", score, "points sur un total possible de", sum(p for _,_,p in questions), ".")



