def saberPalindromo():
        nom = input('Ingrese una frase o una palabra para saber si es un palindromo: \n')
        sep = nom
        nom = nom.replace(' ', '').lower()
        if nom[0::] == nom[::-1]:
            print("'" + sep + "' " + 'Es un palindromo')
        else: 
            print("'" + sep + "' " + 'No es un palindromo')


if __name__ == '__main__':
    saberPalindromo()
