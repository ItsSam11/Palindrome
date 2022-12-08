def saberPalindromo():
        nom = input('Ingrese una frase o una palabra para saber si es un palindromo: \n')
        nom = nom.replace(' ', '').lower()
        if nom[0::] == nom[::-1]:
            print("'" + nom + "' " + 'Es un palindromo')
        else: 
            print("'" + nom + "' " + 'No es un palindromo')


if __name__ == '__main__':
    saberPalindromo()