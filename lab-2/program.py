import modules
import os

clear = lambda: os.system('cls')
def main():
    while True:
        clear()
        print('+---------(Labb  2)---------+')
        modules.homepage()
        print('|  Välj ett av alternativen |')
        modules.homepage()
        print('|    (1.Läs in text-fil.    |')
        print('|    (2.Visa data.          |')
        print('|    (3.Lägg till person.   |')
        print('|    (4.Ta bort person.     |')
        print('|    (5.Spara fil.          |')
        print('|    (6.Avsluta programmet. |')
        modules.homepage()
        print('|           -(☺)-           |')
        modules.homepage()
        print('+---------------------------+')
        meny_option = input('Välj ett av dem sex alternativen\n')
        meny_opt = meny_option
        if meny_opt == '1':
            modules.read_file_csv()
            clear()
        if meny_opt == '2':
            modules.show_json()
            clear()
        if meny_opt == '3':
            modules.add_person(modules.json_path)
            clear()
        if meny_opt == '4':
            modules.delete_person(modules.json_path)
            clear()
        if meny_opt == '5':
            modules.save_json()
            clear()
        elif meny_opt == '6':
            print('Programmet stängs av....')
            break
        else:
            print('Välj något av dem sex alternativen')
    
if __name__== "__main__":
    main()
