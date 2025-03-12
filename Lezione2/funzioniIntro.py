# Funzioni Built-in: sono funzioni che appartengono al linguaggio stesso
print("Anche print è una funzione built-in")

print("Inserisci il tuo nome")
nome = input() #input() è una funzione built che mi permette di ricevere in input un valore e registrarlo in una variabile
print("Ciao", nome)

saldo = 400


print("Quanto desideri prelevare ?")
importo = int(input()) #sto forzando l'input ad essere un intero: CAST del dato

if importo > 500:
    print("Mi spiace, non puoi prelevare più di 500")
else:
    if importo > saldo:
        print("Mi spiace, non hai abbastanza soldi")
    else:
        saldo -= importo
        print("Il tuo saldo attuale è", saldo)


