#Istanziare una variabile "saldo" = 10000 

#Chiedere all'utente quanto ha guadagnato questo mese (utilizza un valore con la virgola)
#Se l'utente ha guadagnato più di 1000 euro stampare: "Bravo, questo mese hai guadagnato bene". Calcolare il saldo su 10000 euro (guadagno 1500, incasso (10000 + 1500) = 10500)

#Se l'utente ha guadagnato meno di 1000 euro stampare: ("Mi spiace, questo mese hai guadagnato così così". Calcolare il saldo su 10000 euro)

#Se l'utente ha guadagnato 0 stampare: "Questo mese non hai guadagnato nulla". Calcolare il saldo

#Se l'utente è andato in perdita stampare: "Questo mese stai perdendo soldi". Calcolare il saldo


saldo = 10000
incasso = float(input("Quanto hai guadagnato questo mese ?")) #typecasting


if incasso < -500:
    print("Stai perdendo parecchio")
elif incasso < 0:
    print("Questo mese sei in perdita")
elif incasso == 0:
    print("Non hai guadagnato nulla")
elif incasso < 1000:
     print("Queste mese hai guadagnato così così")
else:
    print("Bravo questo mese hai guadagnato bene")

# saldo = saldo + incasso
saldo += incasso

print("Saldo attuale", saldo)

# if incasso >= 1000:
#     print("Bravo questo mese hai guadagnato bene")
# elif incasso == 0:
#     print("Non hai guadagnato nulla")
# elif incasso < 0:
#     print("Questo mese sei in perdita")
# else:
#     print("Queste mese hai guadagnato così così")

# totale = incasso + saldo

# print("Il tuo saldo corrisponde a ", totale)

