# 1. le varibili devono avere delle denominazioni "parlanti". Nel nome devo spiegarne il significato
# 2. non posso avere nomi con parole vietate: for, if, while, assert, true, false, ecc ecc ecc
# 3. le variabili sono dei contenitori di una informazione singola, indipendentemente dalla sua complessità

#PascalCase
#UPPERCASE
#kebab-case
#camelCase  OK
#questo_case   OK

#ASSEGNO UNA VARIABILE
#nomeVariabile = valore
mioNome = "Dario"
miaEta = 35
corsi = 2
studenti = 42


#RICHIAMO UNA VARIABILE
print(mioNome)

#Concateno più variabili all'interno del metodo print
print("Ciao", mioNome, "hai", miaEta, "anni. In questo momento insegno in", corsi, "corsi e ho un totale di", studenti, "studenti")


# Calcolo matematico
voto_scritto = 60
voto_orale = 85.5

media = (voto_orale + voto_scritto) / 2

print("La media del mio esame è ", round(media))





