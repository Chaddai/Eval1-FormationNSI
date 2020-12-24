#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tableau import sélectionner, mélanger, appartient
from chaine import enMajuscule, demanderEntierEntre
from eval1 import importerQuestions


toutesQuestions = importerQuestions("quizz-diu-eil.txt")

# Création du dictionnaire de listes de questions
# indexées par le nombre de points rapportés.
parPoints = dict()
for question in toutesQuestions:
    _, _, p = question
    # Si ce nombre de point n'a pas précédemment été rencontré, on crée une liste vide pour
    # cette clé
    if p not in parPoints:
        parPoints[p] = []
    # On ajoute cette question à la liste des questions rapportant p points
    parPoints[p].append(question)


questions = []
mode = input("Souhaitez vous sélectionner vos questions par nombre de points [O/n] ? ")
if appartient(enMajuscule(mode), ['N', 'NO', 'NON']):
    nb_questions = demanderEntierEntre(0, len(questions), 'Combien de questions souhaitez-vous ? ')
    questions = sélectionner(nb_questions, toutesQuestions)
else:
    for p in parPoints.keys():
        nb_questions = demanderEntierEntre(0, len(parPoints[p]),
                                           f'Combien de questions à {p} points souhaitez-vous ? ')
        questions.extend(sélectionner(nb_questions, parPoints[p]))
    # mélange final pour éviter les successions de questions par points
    mélanger(questions)


score = 0
total = 0
for (question, réponse, points) in questions:
    print(question)
    rep = input("Votre réponse : ")
    if rep == réponse:
        score += points
    total += points

print("Vous avez obtenu", score, "points sur un total possible de", total)
