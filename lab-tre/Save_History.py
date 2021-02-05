import json
from tkinter import messagebox

class SaveHistory():
    def __init__(self):
        self.history = []
        self.json_path = 'history.json'
    def read_file(self):    
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f_obj:
                content = json.load(f_obj)
                self.history = content
                return self.history
        except FileNotFoundError:
            try:#om filen inte finns skapar den en lista
                self.history = []
                with open(self.json_path, 'w', encoding='utf-8') as f_obj:
                    json.dump(self.history, f_obj, ensure_ascii=False)
            except FileNotFoundError as ferr:
                messagebox.showerror((ferr)) 
    
    def save_histories(self, search_input):
        self.history.append(search_input)#Hämtar och lägger sök strängen i listan
        try:
            with open(self.json_path, 'w', encoding='utf-8') as f_obj:
                json.dump(self.history, f_obj, ensure_ascii=False)
        except FileNotFoundError as ferr:
            messagebox.showerror((ferr)) 
            