#!/usr/bin/python3
# -*- coding: utf-8 -*-
from eval1 import sélectionner

# ouverture du fichier
fsource = open('quizz-diu-eil.txt', 'r', encoding='utf-8')

# lecture des lignes dans une liste de
# p-uplets (question (str), réponse (str), points (int))
questions = []
for ligne in fsource:
    try:
        q, r, p = ligne.strip().split(';')
        questions.append((q, r, int(p)))
    except:
        pass

fsource.close()

# Sélection du nombre de questions souhaité
nb_questions = int(input('Combien de questions souhaitez-vous ? '))
assert nb_questions <= len(questions),\
    f"Trop de questions demandées, seules {len(questions)} sont disponibles."
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
