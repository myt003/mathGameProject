import myPythonFunctions

try:
    userName=input("Donner votre nom : ")
    ch=myPythonFunctions.getUserPoint(userName)
    userScore=int(ch)
    if(ch=='-1'):
     newUser=True
     userScore=0
    else:
      newUser=False    
    userChoice=0
    while(userChoice!='-1'):
        userScore+=myPythonFunctions.generateQuestion()
        rep=input('voulez-vous continuer(tapez -1 pour terminer ) :')
        userChoice=rep
    myPythonFunctions.updateUserPoints(newUser,userName,userScore)
except (ValueError):
   print("une erreur s'est produit")
