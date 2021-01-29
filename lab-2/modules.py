import csv,json,os

json_path = 'labb-2personer.json'
csv_path = 'labb2-personer.csv'
json_new_path = 'modifierad-labb-2personer.json'
json_start_file ='labb-2personer.json'

def read_file_csv():
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for csv_row in csv_reader:
            print (csv_row)
        go_back()
         
def show_json():
    while True:    
        try:
            with open(json_path, "r", encoding="utf-8") as file:
                person = json.load(file)
                i = 0
                for list_person in person:
                    user = list_person["Användarnamn"]
                    f_name = list_person["Förnamn"]
                    l_name = list_person["Efternamn"]
                    e_mail = list_person["E-mail"]
                    print(f'Nr: {i} Användarnamn: {user} Förnamn: {f_name} Efternamn: {l_name} E-mail: {e_mail}')
                    i=i+1
                input('\nListan utskriven, tryck enter för att fortsätta.')
            break
        except FileNotFoundError:        
            try:
                data = [] 
                with open(csv_path, 'r', encoding='utf-8') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=';')
                    next(csv_reader)
                    for csv_row in csv_reader:
                        data.append({'Användarnamn': csv_row[0], 'Förnamn': csv_row[1], 'Efternamn': csv_row[2], 'E-mail': csv_row[3]})         
                with open (json_path, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file, indent=4, ensure_ascii=False)
            except FileNotFoundError:
                input('Finns ingen CSV fil')
                return
def add_person(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        return input('Det finns ingen sparad fil, tryck på val 2 i menyn för att skapa en fil.\nTryck enter för att gå tillbaka')
    print('Lägg till användare')
    user = input('Vad är ditt användarnamn: ')
    f_name = input('Vad är ditt förnamn: ')
    l_name = input('Vad är ditt efternamn: ')
    e_mail = input('Vad är din E-mail: ')
    data.append({'Användarnamn': (user), 'Förnamn': (f_name), 'Efternamn': (l_name), 'E-mail': (e_mail)})
    with open (json_new_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    save_file(json_new_path)
    print(f'Användarnamn: {user} Förnamn: {f_name} Efternamn: {l_name} E-mail: {e_mail} är sparad')
    go_back()

def save_file(json_modified_path):
    global json_path
    json_path = json_modified_path
    
def delete_person(json_path):
    data_append = []
    user_input = None
    print('Vill du verkligen ta bort någon skriv j för ja annars skriv n för nej för att gå tillbaka till menyn: ')
    while user_input not in ("j","n"):
        user_input = input()
        if user_input.lower() == "j":
            show_json()
            with open(json_path, 'r', encoding='utf-8') as file:
                person = json.load(file)
                data_length = len(person)-1 
            print('\nVem vill du ta bort ?')
            print(f'Skriv en siffra mellan 0-{data_length} för att ta bort den personen, tryck enter för att välja siffra.')
            erase_person = check_nums(data_length)
            i=0        
            for person_list in person:
                if i == int(erase_person):
                    pass
                    i=i+1
                else:
                    data_append.append(person_list)
                    i=i+1
            with open(json_new_path, 'w', encoding='utf-8') as file:
                json.dump(data_append, file, indent=4, ensure_ascii=False)
            save_file(json_new_path)
            input(f'Du tog bort Nr:{erase_person}, tryck enter för att gå tillbaka till menyn')
        elif user_input.lower() == 'n':
            return
        else:
            print("skriv j eller n, försök igen")

def save_json():
    if os.path.isfile(json_new_path) == True:
        user_input = None
        input('Är du säker på att du vill spara filen skriv j för ja eller n för nej: ')
        while user_input not in ("j","n"):
            user_input = input()
            if user_input.lower() == 'j':
                with open (json_new_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    input('Din fil är nu sparad')
                save_file(json_start_file)
                delete_file()
                with open(json_start_file, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
            elif user_input.lower() == 'n':
                return input('Tryck enter för att gå tillbaka till menyn')
            else:
                print("skriv j eller n, försök igen")
    else:
        return input('Finns ingen sparad fil\nTryck enter för att gå tillbaka till menyn')
     
def delete_file():
    os.remove(json_new_path)
    
def check_nums(max_value):
    while True:
        try:
            user_input = int(input())
            if user_input >= 0 and user_input <= max_value:
                return user_input
            else:
                print(f'Välj en siffra mellan 1 och {max_value}')
        except ValueError:
            print('Skriv ett heltal, tack')
def go_back():
    input('\nTryck på valfri enter för att komma tillbaka till menyn')
def homepage():
    print('|                           |')
