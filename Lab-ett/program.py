import modules
import os

clear = lambda: os.system('cls')
def main():
    while True:
        clear()
        print('---------(Labb 1)------------')
        print('|                           |')
        print('|  Välj ett av alternativen |')
        print('|                           |')
        print('|(1.Vilket nr tänker jag på.|')
        print('|(2.Skriv ut delbara heltal.|')
        print('|(3.  Avsluta programmet.   |')
        print('-----------------------------')
        meny_alternativ = input('Välj ett av dem tre alternativen\n')
        meny_val = int(meny_alternativ)
        if meny_val == 1:
            clear()
            modules.gissnings_game()
        elif meny_val == 2:
            clear()
            modules.delbara_heltal()
        elif meny_val == 3:
            print('Programmet stängs av....')
            break
        else:
            print('Du valde inget mellan 1-3, försök igen')
            
if __name__== "__main__":
    main()