# Con i loop ho la possibilità di ripetere dei blocchi di codice

# LOOP INDEFINITI: sono dei loop che potrebbero ciclare all'infinito

# SINTASSI: while condizioneTrue:
#           fai qualcosa()

#fin tanto che la condizione è true continua ad eseguire il codice

# ATTENZIONE: un loop del genere è un loop infinito 
# while True:
#     print("Ciao")

# While con variabile flag, counter esterno
numStop = 0

while numStop < 10:
    numStop += 1
    print("Adesso il numero vale: ", numStop)

# Esempio pratico

numMaggiore = -9999999999

numero = int(input("Inserisci un numero oppure digita -1 per fermare il loop \n"))

while numero != -1:

    if numero > numMaggiore:
        numMaggiore = numero
    
    numero = int(input("Inserisci un numero oppure digita -1 per fermare il loop \n"))

print("Il numero più grande è: ", numMaggiore)

