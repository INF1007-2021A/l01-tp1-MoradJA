
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = secondes//(3600*24*365)
    secondes = secondes%(3600*24*365)

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = secondes//(3600*24*7)
    secondes = secondes%(3600*24*7)

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = secondes//(3600*24)
    secondes = secondes%(3600*24)

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = secondes//3600
    secondes = secondes%3600

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = secondes//60
    secondes = secondes%60

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = secondes

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
