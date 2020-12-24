# Correction de l'évaluation 1

## Partie 1

1. On construit un tableau des "questions", chaque question étant constitué de 
   - la question posée, 
   - la réponse attendue 
   - et le nombre de points attribués. 
   
   Ainsi chaque question sera représentée par un triplet de deux chaînes de caractères et d'un entier (str,str,int). Ce tableau est bien homogène et sera modifié par la suite (pour permettre le mélange par l'algorithme de Fisher-Yates) tandis que les questions sont immuables et hétérogènes (dû à l'inclusion des points) et doivent donc être représentées par un p-uplet. 
   
   Les opérations à effectuer (mélange, sélection d'une sous-liste, parcours dans l'ordre) sont particulièrement adaptées à un tableau.

2. Voir le code python de la [partie 1](partie1.py) ainsi que les modules [tableau](tableau.py) et [chaine](chaine.py) qui contiennent des fonctions utilitaires créées précédemment dans l'année (ou rajoutées à l'occasion comme la fonction `demanderEntierEntre()`). 

---

## Partie 2

3. On peut réaliser ce choix à l'aide des tableaux utilisés dans la partie 1 mais cela est assez peu pratique, impliquant un parcours complet de tableau pour retrouver les questions correspondant à chaque nombre de points. 

   Il est plus pragmatique et lisible de créer un dictionnaire lors de la lecture du fichier dont les clés seront le nombre de points par question possibles et la valeur associée est le tableau des questions rapportant ce nombre de point. Voir la [partie 2](partie2.py) pour la réalisation.

4. Notez que cette partie a été rédigée en supposant que l'utilisateur veut toujours pouvoir choisir le nombre de questions par points. 

   S'il souhaite pouvoir utiliser le mode de sélection de la partie 1 de temps en temps, il est préférable de garder une liste mère de toutes les questions également et de lui proposer l'alternative, voir la [partie 2bis](partie2bis.py) pour une implémentation (notez que les triplets représentant les questions sont partagés en mémoire entre la liste et le dictionnaire et que l'immuabilité des tuples en Python (et des str) garantit ici l'absence de bugs dus à ce partage). 

---

## Partie 3

5. On aura besoin d'un dictionnaire `sansAccent` dont les clés seront les lettres accentuées et les valeurs la version non-accentuée de la clé.

   On utilisera également un dictionnaire `soundexValeurs` pour sélectionner quel traitement effectuer pour chaque lettre lors de l'étape finale, avec comme clés les lettres majuscules et comme valeurs leur valeur numérique selon soundex, ainsi que 0 pour celles à supprimer. On reconstruira ainsi, caractère par caractère la version Soundex de la chaine (qu'on suppose constituée de majuscules sans accent à cette étape).

6. On notera que cette suppression des accents (et cédille) peut aussi être accompli par une utilisation adéquate d'Unicode en mettant d'abord sa chaîne en forme normale KD (qui décompose un caractère composé en la lettre de base et un caractère dit "combinant" représentant l'accent) puis en supprimant les caractères "combinants" (accents, cédilles, etc). 

   D'une façon plus basique, on peut remplacer chaque caractère par sa version non-accentuée si ce caractère est une clé de `sansAccent` (utilisation de l'opérateur `in` sur un dictionnaire) ou en la rajoutant à l'identique sinon. Voir `retirerAccent()` dans le module [chaine](chaine.py).

7. La fonction `enMajuscule()` n'a à se préoccuper que des lettres minuscules sans accent, il suffit donc de remplacer chacune de ces lettres par sa version majuscule en ajoutant la différence entre les codes ASCII du 'a' minuscule et du 'A' majuscule à leur code ASCII. Voir le module [chaine](chaine.py).

8. La fonction `retireDoublon()` examine chaque caractère excepté le premier et ne recopie ce caractère au bout de la sortie que s'il diffère du précédent. Voir le module [chaine](chaine.py).

9. Pour `codeSoundex()`, on met de côté la première lettre puis l'on examine chaque lettre restante et selon sa valeur associée dans `soundexValeurs`, on passe (valeur 0) ou on la remplace par sa valeur (transformée en chaine par `str()`). Enfin on renvoie ma concaténation de la première lettre mise de côté, et des trois premiers caractères de la version traduite (à laquelle on a ajouté `'000'` pour garantir qu'elle contienne bien trois caractères au moins). Voir le module [eval1](eval1.py) pour l'implémentation.

On peut alors reprendre la partie 2 en comparant la version Soundex des réponses données et attendues.

## Bonus

Il y a néanmoins un petit problème si vous exécutez ce code : si vous tombez sur la question « Quel est le nom de l'encodage qui utilise le code ASCII ? », la réponse « utf-8 » n'étant pas constituée entièrement de lettres sera mal traitée par votre fonction `codeSoundex()` : si vous avez négligé de vérifier qu'un caractère est bien une clé de votre dictionnaire avant de procéder, votre programme plantera tandis que si vous avez passé ces caractères sans modifications ou sans les recopier, la valeur renvoyée sera incorrecte (notez que le 8 dans utf-8 est important vu l'existence de utf-16 et utf-32).

Une solution propre à ce problème serait de découper le texte à traiter en parties constituées entièrement de lettres auxquelles on applique Soundex et d'autres symboles qu'on laisse passer à l'identique. C'est ce qui est fait dans la fonction `soundexParMot()` du module [eval1](eval1.py) et utilisé dans la [version finale du programme](partie3.py).