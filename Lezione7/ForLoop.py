# In precedenza con il while
# i = 0
# while i < 100:
#     print(i)
#     i += 1

# Con il ciclo for non sono nei cicli indefiniti ma sono nei cicli definiti
# Dobbiamo usare un metodo chiamato range(numero) il quale stabilisce il numero di cicli da effettuare

# i sta per indice e nel ciclo for viene automaticamente incrementata non ho bisogno di fare i+=1
for i in range(10): #ATT: il range(100) va da 0 a 99
    print(i)
    
for i in range(15, 20): #ATT: con range(15,20) ciclo da 15 a 19
    print("La i vale", i)
    
for i in range(5, 60, 3): #ATT: in questo caso il terzo parametro rappresenta l'incremento
    print("La i vale", i)


# Break e Continue
# break permette di interrompere un ciclo
# continue permette di saltare un ciclo, un giro 

#Esempio: dato un set di numeri da 1 a 10 interrompi il ciclo se incontri il numero 5
for x in range(1, 11):
    if x == 5:
        print("adesso vale 5 per cui interrompo il ciclo")
        break  #interrompe ed esce dal ciclo. Ricorda: posso usarlo anche nel while
    print("la x vale", x)

#Esempio: dato un set di numeri da 1 a 10 quando incontri il numero 5 salta quel ciclo
for x in range(1, 11):
    if x == 5:
        # print("Sto saltando il numero 5")
        continue
    print("La x vale", x)

