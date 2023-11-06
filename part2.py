#Enonse 1
# limit=12
# divizib_2=[]
# for i in range(limit+1):
#     if(i%2==0):
#         divizib_2.append(i)
# print(divizib_2)

#Enonse #2

# listePython = [1, 2, 3, 4, 5]
# listeChenn = [str(element) for element in listePython]
# print(listeChenn)

#Enonse #3
# listeMiniskil = ['bonjou', 'kijan ou ye', 'ou byen']
# listeMajiskil = [element.upper() for element in listeMiniskil]

# print(listeMajiskil)


# Enonse # 4

# liste = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# nouvoListe = [liste[i] for i in range(len(liste)) if i % 3 == 0]
# print(nouvoListe)

# Enoonse #5

# liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nouvoListe = [liste[i:i+3] for i in range(0, len(liste), 3)]
# print(nouvoListe)

# liste = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# nouvoListe = list(set(liste))
# print(nouvoListe)


# Enonse # 7

# lis1 = [1, 2, 3, 4, 5]
# lis2 = [3, 4, 5, 6, 7]
# nouvoListe =[]

# for i in lis1 :
#     if i in lis2:
#         nouvoListe.append(i)

# print(nouvoListe)

#enonse # 8

# lis1 = [1, 2, 3, 4, 5]
# lis2 = [3, 4, 5, 6, 7]
# nouvoListe = list(set(lis1) ^ set(lis2))

# print(nouvoListe)

#Enonse 9

diksyone = {'janvier': 31, 'fevriye': 28, 'mas': 31, 'avril': 30}

listkle = list(diksyone.keys())
listvale = list(diksyone.values())


print(listkle)
print(listvale)

