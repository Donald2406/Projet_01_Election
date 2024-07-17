def candidats(nombre):
# Fonction pour ajputer les candidats
    pretendant = []
    for i in range(nombre):
        print('Ajoutez le candidat', i+1)
        name = input("Nom et prenom(s):  ")
        pretendant.append(name)
    return pretendant




print("Entrez le nombre de candidat")
nbre = int(input('_ '))
candidats = candidats(nbre)
