import random
import time
from dict import thisdict

print ('Programme de traduction -- By ThR')

lge = int(input("Francais à Anglais (1) ou l'inverse (2): "))
nbre = int(input("Nombre de mots à traduire : "))
bot = random.choice(list(thisdict))
max = 0
lose = 0
s = 0
liste = []
vict = []

while lose < nbre :
    if lge == 1 :
        print (thisdict[bot])
        answer = str(input("Réponse : "))
        max = max + 1
        test = bot
        if answer == bot :
            print ('Bien joué')
            s = s+1
            vict.append(str(bot))
            thisdict.pop(test)
        else :
            choice = int(input('Voulez-vous rééssayer Oui (1) ou Non (2): '))
            if choice == 1 :
                second = str(input('Deuxième essai : '))
                if second == bot :
                    print ('Bien joué')
                    s = s+1
                    vict.append(str(bot))
                else :
                    print('Perdu, la réponse était ' + bot)
                    liste.append(str(bot))
                thisdict.pop(test)
            elif choice == 2 :
                print('Perdu, la réponse était ' + bot)
                liste.append(str(bot))
                thisdict.pop(test)
        if nbre > lose :
            print ('Score : ' + str(s) + '/' + str(max))
            time.sleep(2)
            lose = lose + 1
        else :
            lose = lose + 1
        bot = random.choice(list(thisdict))
    elif lge == 2 :
        print (bot)
        answer = str(input("Réponse : "))
        max = max + 1
        test = bot
        if answer == thisdict[bot] :
            print ('Bien joué')
            s = s+1
            vict.append(str(thisdict[bot]))
            thisdict.pop(test)
        else :
            choice = int(input('Voulez-vous rééssayer Oui (1) ou Non (2): '))
            if choice == 1 :
                second = str(input('Deuxième essai : '))
                if second == thisdict[bot] :
                    print ('Bien joué')
                    s = s+1
                    vict.append(str(thisdict[bot]))
                else :
                    liste.append(str(thisdict[bot]))
                    print('Perdu, la réponse était ' + thisdict[bot])
                thisdict.pop(test)
            elif choice == 2 :
                print('Perdu, la réponse était ' + thisdict[bot])
                liste.append(str(thisdict[bot]))
                thisdict.pop(test)
        if nbre > lose :
            print ('Score : ' + str(s) + '/' + str(max))
            time.sleep(2)
            lose = lose + 1
        else :
            lose = lose + 1
        bot = random.choice(list(thisdict))
    else :
        print ("Type de traduction incorrect")
print ('Voici la liste des mots incorrects : ')
for lettre in liste:
        print (lettre)
print ('Voici la liste des mots corrects : ')
for lettre in vict:
        print (lettre)