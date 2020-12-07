#!/usr/bin/python3
# -*- coding: utf-8 -*-
from eval1 import mélanger

# ouverture du fichier
fsource = open('quizz-diu-eil.txt','r')

# lecture des lignes dans une liste de
# p-uplets (question (str), réponse (str), points (int))
questions = []
for ligne in fsource:
    try:
        q, r, p = ligne.strip().split(';')
        questions.append((q,r,int(p)))
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

# calcul du score total possible par somme des points de toutes les questions
total = sum(p for _,_,p in questions)
print("Vous avez obtenu", score, "points sur un total possible de", total)



