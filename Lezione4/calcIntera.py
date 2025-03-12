# Permetti all'utente di inserire 2 numeri interi e calcola il risultato delle seguenti operazioni
# + - * / **2

print("Calcolatrice per numeri interi")

num1 = int( input("Primo numero "))
num2 = int( input("Secondo numero "))

somma = num1 + num2
sottrazione = num1 - num2
moltiplicazione = num1 * num2
divisione = num1 / num2
potenza = num1 ** 2

print("La somma vale:", somma)
print("La sottrazione vale:", sottrazione)
print("La moltiplicazione vale:", moltiplicazione)
print("La divisione vale:", divisione)
print("La potenza di num1 vale:", potenza)