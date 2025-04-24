#Le liste (chiamati anche Array in altri linguaggi) servono a trattenere più informazioni
#Sono dei contenitori di elementi simili tra loro. Ovvero sono dei contenitori omogenei, vuol dire che il tipo di dato è sempre lo stesso. Tutte stringhe, tutti numeri, tutti boolean

#Sintassi: le parentesi [] identificano la lista
#0-based: cioè la conta parte da 0
#              0       1        2         3    --> indice
miaLista = ["mela", "pesca", "banana", "kiwi"]
print(miaLista)
print(miaLista[0])
print(miaLista[1])
print(miaLista[2])
print(miaLista[3])
print(len(miaLista)) # la lunghezza vale ovviamente 4

#Il ciclo for è adatto a stampare ogni singolo elemetno della lista
print("Stampo un elemento alla volta")
for frutto in miaLista:
    print(frutto)
    
# ESEMPIO, fornisco una lista di voti. Tutte le volte che insufficiente stampo un avviso 
voti = [100, 50, 25, 85, 20]

for voto in voti:
    if voto <= 50:
        print("Voto: ", voto, "attenzione sei sotto soglia di sufficienza")
    else:
        print("Voto: ", voto )
