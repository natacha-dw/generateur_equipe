import random # ajout de module qui contient les fonctions qui permettent de choisir des joueurs au hasard dans une liste





joueurs = ["Rose", "Alexia", "Maria", "Thomas", "Yohann", "Guillaume"]

print("Bienvenue dans le génerateur d'equipe !") 

while True:

    random.shuffle(joueurs)

    equipe1 = joueurs[:len(joueurs)//3]

    print("Capitaine de l'equipe 1 : " + random.choice(equipe1)) 

    print("equipe 1:")

    for joueur in equipe1 :

       print(joueur) 


    equipe2 = joueurs[len(joueurs)//3 :(len(joueurs)//3)*2]
 
    print("\nCapitaine de l'equipe 2 : "   + random.choice (equipe2)) 

    print("equipe 2 :")
    for joueur in equipe2 :
        print(joueur) 


    equipe3 = joueurs[(len(joueurs)//3)*2:]
 
    print("\nCapitaine de l'equipe 3 : "   + random.choice (equipe3)) 

    print("equipe 3 :")
    for joueur in equipe3 :
        print(joueur)     

    reponse = input("Choisir de nouvelles équipes? \
                                Saisissez o ou n: " )  

    if reponse == "n":

        break                