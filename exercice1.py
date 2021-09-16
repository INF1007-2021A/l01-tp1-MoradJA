def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat


    def fizzBuzz(n):
        if n % 3 == 0:
            return print('fizz')
        if n % 5 == 0:
            return print('Buzz')
        if n % 3 == 0 and n % 5 == 0:
            return print('fizzBuzz')
        else:
            print(n)

    resultat = print(fizzBuzz(n))
    return resultat


if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))




