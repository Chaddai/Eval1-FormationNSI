#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tableau import sélectionner, mélanger, appartient
from chaine import enMajuscule, demanderEntierEntre


# ouverture du fichier
fsource = open('quizz-diu-eil.txt', 'r', encoding='utf-8')

# lecture des lignes dans un dictionnaire de listes de
# p-uplets (question (str), réponse (str), points (int))
# indexées par le nombre de points rapportés et dans une
# liste de questions
parPoints = dict()
toutesQuestions = []
for ligne in fsource:
    q, r, p = ligne.strip().split(';')

    # Si ce nombre de point n'a pas précédemment été rencontré, on crée une liste vide pour
    # cette clé
    if p not in parPoints:
        parPoints[p] = []

    # On crée un p-uplet caractérisant cette question
    question = (q, r, int(p))
    # On ajoute cette question à la liste des questions rapportant p points
    parPoints[p].append(question)
    # Et à la liste de toutes les questions
    toutesQuestions.append(question)

fsource.close()


questions = []
mode = input("Souhaitez vous sélectionner vos questions par nombre de points [O/n] ? ")
if appartient(enMajuscule(mode), ['N', 'NO', 'NON']):
    nb_questions = demanderEntierEntre(0, len(questions), 'Combien de questions souhaitez-vous ? ')
    # Sélection aléatoire des questions
    questions = sélectionner(nb_questions, toutesQuestions)
else:
    for p in parPoints.keys():
        # Sélection du nombre de questions souhaité
        nb_questions = demanderEntierEntre(0, len(parPoints[p]),
                                           f'Combien de questions à {p} points souhaitez-vous ? ')
        # Sélection aléatoire des questions
        questions.extend(sélectionner(nb_questions, parPoints[p]))
    # mélange final pour éviter les successions de questions par points
    mélanger(questions)


score = 0
for (question, réponse, points) in questions:
    print(question)
    rep = input("Votre réponse : ")
    if rep == réponse:
        score += points

# calcul du score total possible par somme des points de toutes les questions
total = sum(p for _, _, p in questions)
print("Vous avez obtenu", score, "points sur un total possible de", total)
