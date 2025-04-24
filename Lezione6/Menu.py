
scelta = ''

while scelta != 'q':
    print("-----MENU-----")
    print("a) gioca")
    print("b) calcola")
    print("c) saluta")
    print("q) esci")
    print("--------------")
    
    scelta = str(input("Scegli una voce del menu \n"))

    if scelta == 'a':
        print("Hai scelto di giocare")
    elif scelta == 'b':
        print("Hai scelto di calcolare qualcosa")
    elif scelta == 'c':
        print("Hai scelto di salutare qualcuno")
    elif scelta == 'q':
        print("Ciao, sei uscito dal programma")
    else:
        print("Scelta non valida")