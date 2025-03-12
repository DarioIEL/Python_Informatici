# Esempio di dichiarazione e uso variabili
print("Scrivi il tuo nome, caro utente!")

# Per poter acquisire qualcosa che digita l'utente utilizzo la funzione input()
# nomeUser = "Dario"
nomeUser = input() #argomento mancante

print("Benvenuto", nomeUser)

# Faccio la stessa cosa in modo più veloce passando come argomento all'input una frase
# funzione (argomento) --> tutto questo si chiama FIRMA del METODO
cognomeUser = input("Scrivi il tuo cognome..")
print("Il tuo cognome è", cognomeUser)


print("------------NUMERI------------")
# ATT: tutto ciò che recupero da un utente è considerato una string, un testo. Per poter fare un calcolo devo fare il TYPE CASTING, ovvero forzare quella variabile ad essere un numero e non una stringa

# int() trasforma l'argomento in un numero intero
num1 = int( input("Scrivi un numero ") )
num2 = int( input("Scrivi un altro numero "))
somma = num1 + num2
print("La somma vale: ", somma)


# esempio con int
num3 = int("3") #Type Casting
num4 = 6 #Number -> int 
somma2 = num3 + num4
print(somma2)

