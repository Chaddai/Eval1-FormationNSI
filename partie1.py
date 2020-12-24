#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tableau import sélectionner
from chaine import demanderEntierEntre


# ouverture du fichier
fsource = open('quizz-diu-eil.txt', 'r', encoding='utf-8')

# lecture des lignes dans une liste de
# p-uplets (question (str), réponse (str), points (int))
questions = []
for ligne in fsource:
    q, r, p = ligne.strip().split(';')
    questions.append((q, r, int(p)))

fsource.close()


# Sélection du nombre de questions souhaité
nb_questions = demanderEntierEntre(0, len(questions), 'Combien de questions souhaitez-vous ? ')
# Sélection aléatoire des questions
questions = sélectionner(nb_questions, questions)


score = 0
for (question, réponse, points) in questions:
    print(question)
    rep = input("Votre réponse : ")
    if rep == réponse:
        score += points

# calcul du score total possible par somme des points de toutes les questions
total = sum(p for _, _, p in questions)
print("Vous avez obtenu", score, "points sur un total possible de", total)
