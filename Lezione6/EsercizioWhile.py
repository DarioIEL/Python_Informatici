# Crea un programma che legge un numero inserito da un utente e stabilisce se questo numero è pari o dispari. Il programma si interrompe se l'utente inserisce il numero 0

# SOLUZIONE 1

# print("Esercizio Pari e Dispari. Ti verrà chiesto di inserire un numero. Se inserisci 0 terminari il programma")

# numero = int(input("Inserisci un numero"))

# while numero != 0:  # ! chiamato NOT logico serve a negare una condizione
#     if numero % 2 == 0:
#         print("Il numero è pari")
#     else:
#         print("Il numero è dispari")
#     numero = int(input("Inserisci un altro numero"))

# print("0 = sei uscito dal programma")

# SOLUZIONE 2
# numero = ""

# while numero != 0:
#     numero = int(input("Inserisci un numero (0 per uscire) "))
#     if numero == 0:
#         print("Hai scelto di uscire")
#     elif numero % 2 == 0:
#         print("Il numero è pari")
#     else:
#         print("Il numero è dispari")


#Crea un programma per indovinare un numero segreto. Fino a quando l'utente non inserisce il numero corretto composto da 3 cifre il programma continuerà a dirgli che non è possibile entrare. Ci sono un massimo di 4 tentativi
#Esempio numSegreto = 123
 
numeroSegreto = 123
numeroTentativi = 4

while numeroTentativi > 0:
    numeroUtente = int(input("Inserisci un numero segreto composto da 3 cifre \n"))
    
    numeroTentativi -= 1
    
    if(numeroUtente == numeroSegreto):
        print("Hai indovinato il numero segreto. Benvenuto !")
        # numeroTentativi = 0
        # oppure
        break #interrompe il ciclo
    elif (numeroUtente < 100 or numeroUtente > 999):
        print("Il numero deve essere composto da 3 cifre")
    elif numeroTentativi == 0:
        print("Hai esaurito i tentativi")
    else:
        print(f"numero errato! hai ancora {numeroTentativi} tentativi")
    