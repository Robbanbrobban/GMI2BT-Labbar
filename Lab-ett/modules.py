from random import randint


def gissnings_game():
    nummer = randint(0, 100)
    print('----------------------------')
    mitt_namn = input('Hej, vad heter du? ')
    print(f'Dåså, {mitt_namn} jag tänker på ett tal mellan 1 och 100.\nVilket? ')
    antal_gissningar = 0
    while True: 
        while True: 
            try:
                gissa = nummer_testaren()
                if gissa >= 1 and gissa <= 100:
                    break
                else:
                    print('Du skrev inte ett tal mellan 1 och 100, Försök igen')
            except ValueError:
                    print('Skriv ett tal')
                    continue                
        if gissa == nummer:
            antal_gissningar = str(antal_gissningar)
            print(f'Snyggt {mitt_namn}, du gissade rätt nummer som var {nummer} på {antal_gissningar} antal gissningar!')
            input(f'Om {mitt_namn} vill komma tillbaka till menyn tryck på valfri knapp')
            break
        elif gissa < nummer:
            print('Du gissade för lågt, försök igen')
            antal_gissningar += 1
        elif gissa > nummer:
            print('Du gissade för högt, försök igen')
            antal_gissningar += 1
                    
def delbara_heltal():
    summa = 0
    antal = 0
    print('Skriv första talet')
    x = nummer_testaren()
    print('Skriv andra talet')
    y = nummer_testaren()
    print('----------------------------')
    for tal in range(1, 1000):
        if tal % x == 0 and tal % y ==0:
            print(tal, end=" ")
            summa += tal
            antal += 1
    print(f'\nMedelvärdet: är {summa/antal}\nAntal tal: {antal}\nTryck på valfri knapp för att gå tillbaka till menyn\n')
    input()

    

def nummer_testaren():
    while True:
        try:
            nummer = int(input())
            break
        except ValueError:
            print('Oj något gick snett, försök igen med en siffra istället')
    return nummer
