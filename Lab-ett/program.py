import modules

def main():
    print('-----------Labb 1-----------')
    print('----------------------------')
    print('Välj ett av alternativen')
    print('(1. Vilket nr tänker jag på.')
    print('(2. Skriv ut delbara heltal')
    print('----------------------------')
    meny_val = input()
    if meny_val == '1':
        modules.gissnings_game()
    elif meny_val == '2':
        modules.delbara_heltal()
    elif meny_val == '3':
        print('Programmet stängs av...')
        breakpoint()
    else:
        main()
if __name__== "__main__":
    main()