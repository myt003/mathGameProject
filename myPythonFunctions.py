import random
import os

def getUserPoint(nom):
    try:
        lst = []
        fichier = open('C:\\Users\\youss\\Desktop\\projet_python\\userScores.txt', 'r')
        for ligne in fichier:
            lst.append(ligne.strip().split(','))
        fichier.close()
        
        print(lst)

        for element in lst:
            if nom == element[0]:
                return element[1]

        return '-1'
    finally:
        fichier.close()

def updateUserPoints(newUser, userName, score):
    if newUser:
        fich = open('userScores.txt', 'a')
        fich.write(f"{userName},{score}\n")
        fich.close()
    else:
        fich = open('userScores.txt', 'r')
        lignes = fich.readlines()
        fich.close()

        tmp = open('userScores.tmp', 'w')
        ch = getUserPoint(userName)
        if ch != '-1':
            for line in lignes:
                if userName in line:
                    line = line.replace(ch, str(score))
                tmp.write(line)
        tmp.close()

        os.rename('userScores.tmp', 'userScores.txt')

def generateQuestion():
    operandlist = [random.randint(1, 9) for _ in range(5)]
    operatorDict = {1: '+', 2: '-', 3: '*', 4: '**'}
    operatorList = [operatorDict[random.randint(1, 4)] for _ in range(4)]

    for j in range(1, len(operatorList)):
        if operatorList[j-1] == '**' and operatorList[j] == '**':
            operatorList[j-1] = operatorDict[random.randint(1, 3)]

    questionString = ''.join(str(operandlist[i]) + operatorList[i] for i in range(4)) + str(operandlist[4])
    result = eval(questionString)
    questionString = questionString.replace('**', '^')

    print('la question: ' + questionString)
    score = 0

    while True:
        try:
            rep = float(input("reponse : "))

            if result == rep:
                print(1)
                score += 10
                print("votre score est :", score)
                return score
            else:
                print(0)
                print("la bonne reponse est :", result)
                print("votre score est :", score)
                return score
        except ValueError:
            print("Veuillez entrer un nombre valide.")
