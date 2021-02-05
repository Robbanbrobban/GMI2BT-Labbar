from tkinter.constants import BOTTOM, CENTER, END, LEFT, N, RIGHT, SINGLE, TOP
from typing import Sized
import requests, json,tkinter
from PIL import ImageTk ,Image
from io import BytesIO
from tkinter import BooleanVar, Canvas, Event, Listbox, PhotoImage, StringVar, Label,Entry,Button,Tk, Widget, messagebox
from Save_History import SaveHistory



class MovieSearchApp():   

    def __init__(self):
        self.app = self.create_app()
        # Här lägger vi till kontroller
        self.how_to_text = self.create_how_to_text()
        self.search_field = self.create_search_field()
        self.menu_label = self.create_menu_label()
        self.list_box = self.create_list_box()
        self.history = SaveHistory()
        self.show_history = self.create_show_history()
        self.history_label = self.create_history_lbl()
        # mainloop måste ligga sista annars fungerar inte kontrollerna i den
        self.app.mainloop()
        
    # appen
    def create_app(self):
        app= Tk() #appen
        app.title("                                                                                                                                                                    Movie Search App")  # sätter titel
        app.geometry('1200x800')  # sätter storleken på fönstret
        app.configure(background='gray')
        return app
    
    #Visar Texten för hur man gör
    def create_how_to_text(self):
        text_info = Label(self.app, text =" Hello movie entusiasts !☺\nWelcome to my Movie Search App")
        text_info.configure(background='gray')
        text_info.pack(side=TOP)
              
    #Skapar sökruta
    def create_search_field(self):
        search_field_label = Label(self.app, text="Type in the movie you want to search for.\nThen press enter :")
        search_field_label.pack()
        self.movie_text = StringVar()
        self.movie_entry = Entry(self.app, textvariable=self.movie_text)
        self.movie_entry.bind('<Return>', lambda event :self.search_movie(event, None, True))
        self.movie_entry.pack(side=TOP)
        return self.movie_entry
    # Söker filmer
    def search_movie(self, event, search_term, check_get):
        if check_get:#kollar om det är en entry get 
            search_term = self.movie_entry.get()
        self.movie_input = Label(self.app, width=20, text=self.movie_entry.get())
        response = requests.get("http://www.omdbapi.com/?&apikey=3971b343&s="+search_term)
        data = response.json()
        search_input = self.movie_entry.get()
        if data ['Response'] =='True':
            self.movie_list = data['Search']
            self.create_movie_menu() #tar dig vidare till att välja film
        else:
            messagebox.showerror('Error', 'Cannot find {}'.format(search_input))
        self.movie_entry.delete(0, 'end')
        self.history.read_file()
        self.history.save_histories(search_input)
        self.create_history_list()

    #Label ovanför listan så folk vet va dem ska göra    
    def create_menu_label(self):
        movie_menu_label = Label(self.app, text="Choose a movie in the list by clicking on it:")
        movie_menu_label.pack(side=TOP) 
    #skapar listan som kommer visa filmerna
    def create_list_box(self):
        self.choose_movie = Listbox(self.app, width=40, selectmode=SINGLE)
        self.choose_movie.pack(side=TOP)  
 
    # Visar filmerna som du sökt        
    def create_movie_menu(self):
        self.choose_movie.delete(0, END)
        for i in range(len(self.movie_list)):
            self.choose_movie.insert(END, self.movie_list[i]['Title'])
        self.choose_movie.bind('<<ListboxSelect>>', self.movie_picker)

    #Visar filmerna du sökt samt att du kan välja
    def movie_picker(self, event):
        listbox = event.widget
        index = int(listbox.curselection()[0])#tar ut indexet på den film jag klickar på
        movieid = self.movie_list[index]['imdbID']
        response = requests.get("http://www.omdbapi.com/?&apikey=3971b343&i=" + movieid)
        data = response.json()
        title = data['Title']
        year = data['Year']
        plot = data['Plot']
        try:
            self.show_info.pack_forget()#tar bort den tidigare labeln
        except AttributeError:
            print(AttributeError)
        #skriver ut info om filmen
        self.show_info = Label(self.app, text=f"Title: {title}\nYear: {year}\nPlot: {plot}")
        self.show_info.pack(side=LEFT)
        self.image = data['Poster']
        self.image_box = self.create_image_box()#för att öppna bilden
            
    #Visar filmens poster
    def create_image_box (self):
        try:
            self.lbl.pack_forget()
        except AttributeError:
            print(AttributeError)
        response = requests.get(self.image)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        image = ImageTk.PhotoImage(image=img)
        self.lbl = Label(self.app, image=image)
        self.lbl.image = image
        self.lbl.pack(side=RIGHT)
        
    #visar label för listan
    def create_history_lbl(self):
        history_lbl = Label(self.app, text="History searches, you can also scroll:")
        history_lbl.pack(side=BOTTOM)
         
    #skapar listan
    def create_show_history(self):
        self.lbx_history = Listbox(self.app, width=40, selectmode=SINGLE) #förkorta gärna långa
        self.lbx_history.pack(side=BOTTOM)
        
    #lägger in information om tidigare sökningar i en listbox
    def create_history_list(self):
        self.history.read_file()
        self.lbx_history.delete(0, END)# tar bort tidigare sökningar så den inte dubbleras
        for h in self.history.read_file():
            self.lbx_history.insert(END, h)
        self.lbx_history.bind('<<ListboxSelect>>', self.show_selected_history)
        
    #Hämtar sökningar        
    def show_selected_history(self,event):
        listbox = event.widget
        selection = listbox.curselection()
        try:
            selection_text = listbox.get(selection[0])# för att komma åt texten av ett av valda alternativen
            self.search_movie(event, selection_text, False)
        except IndexError as ferr:
            print(ferr)
    