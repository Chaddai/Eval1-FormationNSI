#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tableau import sélectionner
from chaine import demanderEntierEntre
from eval1 import importerQuestions


questions = importerQuestions("quizz-diu-eil.txt")


# Sélection du nombre de questions souhaité
nb_questions = demanderEntierEntre(0, len(questions), 'Combien de questions souhaitez-vous ? ')
# Sélection aléatoire des questions
questions = sélectionner(nb_questions, questions)


score = 0
total = 0
for (question, réponse, points) in questions:
    print(question)
    rep = input("Votre réponse : ")
    if rep == réponse:
        score += points
    total += points

print("Vous avez obtenu", score, "points sur un total possible de", total)
