#!/usr/bin/python3
# -*- coding: utf-8 -*-
from eval1 import sélectionner, mélanger, codeSoundex

# ouverture du fichier
fsource = open('quizz-diu-eil.txt','r')

# lecture des lignes dans une liste de
# p-uplets (question (str), réponse (str), points (int))
parPoints = dict()
toutesQuestions = []
for ligne in fsource:
    try:
        q, r, p = ligne.strip().split(';')
        if p not in parPoints:
            parPoints[p] = []
        question = (q,r,int(p))
        parPoints[p].append(question)
        toutesQuestions.append(question)
    except:
        pass

fsource.close()

questions = []
mode = input("Souhaitez vous sélectionner vos questions par nombre de points [O/n] ? ")
if mode.lower() in ['n', 'no', 'non']:
    nb_questions = int(input('Combien de questions souhaitez-vous ? '))
    assert nb_questions <= len(toutesQuestions), "Trop de questions demandées, seules "+str(len(toutesQuestions))+" sont disponibles."
    # Sélection aléatoire des questions
    questions = sélectionner(nb_questions, toutesQuestions)
else :
    for p in parPoints.keys():
        # Sélection du nombre de questions souhaité
        nb_questions = int(input(f'Combien de questions à {p} points souhaitez-vous ? '))
        assert nb_questions <= len(parPoints[p]), "Trop de questions demandées, seules "+str(len(parPoints[p]))+" sont disponibles."
        # Sélection aléatoire des questions
        questions.extend(sélectionner(nb_questions, parPoints[p]))
    # mélange final pour éviter les successions de questions par points
    mélanger(questions)

score = 0
for (question, réponse, points) in questions:
    print(question)
    rep = input("Votre réponse : ")
    if codeSoundex(rep) == codeSoundex(réponse):
        score += points

# calcul du score total possible par somme des points de toutes les questions
total = sum(p for _,_,p in questions)
print("Vous avez obtenu", score, "points sur un total possible de", total)



