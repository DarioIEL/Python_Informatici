# Or Logico. In questo caso vale una condizione OPPURE l'altra affinche quella globale sia true

# Esami: l'esame viene superato se passi lo scritto oppure l'orale

esameScritto = False
esameOrale = True

# In questo caso il professore è buono
print("PROFESSORE BRAVO")
if esameScritto or esameOrale:
    print("Complimenti hai superato entrambi esami")
else:
    print("Mi spiace, non hai entrambi gli esami")


print("PROFESSORE CATTIVO") #ESPANDI con altri elif e gli and logici
if esameScritto and esameOrale:
    print("Complimenti hai superato l'esame")
else:
    print("Mi spiace non hai superato l'esame perché uno dei due è andato male")
