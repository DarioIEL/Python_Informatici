#  L' AND logico (&&) mi permette di unire più condizioni. Vuol dire che ho bisogno che entrambe le condizioni siano valide affinché tutta la condizione sia true

#Stefan compie 18 anni, da oggi può accedere al club dei programmatori ma deve avere un invito

etaStefan = 18
invito = True #invito è già un boolean. Non ho necessità di valutarlo

if etaStefan >= 18 and invito:
    print("Ciao Stefan, puoi far parte del club dei programmatori")
elif etaStefan < 18 and invito:
    print("Caro Stefan, non hai ancora compiuto 18 anni. Anche se hai l'invito non puoi entrare")
elif etaStefan >= 18 and not invito: #il not logico nega una condizione
    print("Caro Stefan, pur avendo 18 anni non puoi entrare poiché ti manca l'invito")
else:
    print("Mi spiace, non puoi far parte del club. Non hai 18 anni e non hai neppure un invito")

# Continua il codice chiedendo all'utente il suo nome, l'età e se possiede l'invito
