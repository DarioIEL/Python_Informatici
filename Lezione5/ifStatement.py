#If Statement serve ad operare delle scelte in base a delle condizioni
#SINTASSI
#if condizione:
#     esegui se condizione è true
#else:
#     esegui se condizione è false

x = 10
y = 8

if x == y:
    print("I due numeri sono uguali")
else:
    print("I due numeri sono diversi")


###############Leggi i due numeri inseriti dall'utente
num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

if num1 > num2:
    print("Il primo numero inserito è più grande")
elif num1 < num2:
    print("Il secondo numero inserito è più grande")
elif num1 == num2:
    print("I due numeri sono uguali")
else:
    print("Non posso interpretare i due numeri")




