import json
from tkinter import *
from operator import itemgetter
from tkinter import ttk
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

def update(data):
    tree.delete(*tree.get_children())
    for rij in data:
        tree.insert("", "end", values=(rij["name"], 'â‚¬' + str(rij["price"]), rij["genres"]))

def check(e):
    typed = e.widget.get()

    if typed == '':
        data = toppings
    else:
        data = []
        for item in toppings:
            if item['name'].lower()[0:len(typed)] == typed.lower():
                data.append(item)
    update(data)

def genre_selecteren(genre):
    data = []
    for item in toppings:
        if item['genres'] == genre:
            data.append(item)
    update(data)


root = tk.Tk()
root.title(('Steam'))
root.minsize(width=300, height=400)
root.resizable(width=0, height=0)
root.geometry('620x680')
myjsonfile = open('C:/Users/Moham/PycharmProjects/pythonProject1/steam.json', 'r')
jsondata = myjsonfile.read()
steambestand = json.loads(jsondata)
steambestand.sort(key=itemgetter("price"))
myjsonfile.close()
C = Canvas(bg="blue", height=250, width=300)
filename = PhotoImage(file = 'C:/Users/Moham/Documents/Opdrachten om in te leveren/steam foto.png')
background_label = Label(image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
root.iconbitmap('C:/Users/Moham/Documents/Opdrachten om in te leveren/steamicon.ico')

spel_zoeken = Label(root, text= "Zoek een spel", font = ("Helvetica", 15))
spel_zoeken.pack(pady =0, ipady =10, ipadx=10)

my_entry = Entry(root, font= ("Helvetica", 20))
my_entry.pack(pady= '20')

thema = ttk.Style()
thema.theme_use('clam')

tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings', height=5, selectmode = 'browse')
tree.place(x=30, y=95)

schuifbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
schuifbar.place(x=605, y=378, height=133)

tree.configure(yscrollcommand=schuifbar.set)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Spelnaam")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Prijs")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Genre")
tree.pack()

toppings = steambestand

update(toppings)

my_entry.bind("<KeyRelease>", check)

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Genres", menu=file_menu)

file_menu.add("command", label="Action", command=lambda: genre_selecteren('Action'))
file_menu.add("command", label="RPG", command=lambda: genre_selecteren('RPG'))
file_menu.add("command", label="Action;Free to Play", command=lambda: genre_selecteren('Action;Free to Play'))
file_menu.add("command", label="Early Access", command=lambda: genre_selecteren('Early Access'))
file_menu.add("command", label="Adventure", command=lambda: genre_selecteren('Adventure'))
file_menu.add("command", label="Racing", command=lambda: genre_selecteren('Racing'))
file_menu.add("command", label="Sports", command=lambda: genre_selecteren('Sports'))
file_menu.add("command", label="Strategy", command=lambda: genre_selecteren('Strategy'))

# statistiek functie
def graph():
    i = pd.read_json('C:/Users/Moham/PycharmProjects/pythonProject1/steam.json')
    plt.boxplot(i['price'])
    plt.show()

# prijs functie
def prijs():
    Button = Button(root, text="Prijzen", command=graph)
    Button.pack()

# statistiek knop
stat_menu = Menu(my_menu)
my_menu.add_cascade(label="Statistiek", menu=stat_menu)
stat_menu.add_command(label="Prijzen", command=prijs)

# account functie
def account():
    lbl_account = Label(root, text="Je bent online!").pack()
    lbl_account.pack()

# frame functie
def nieuw_frame():
    verstop_frame()
    new_frame.pack(fill='both', expand=1)
    my_label = Label(new_frame, text="Je bent online!").pack()

# frame verstoppen
def verstop_frame():
    new_frame.pack_forget()

# account knop
acc_menu = Menu(my_menu)
my_menu.add_cascade(label="Account", menu=acc_menu)
acc_menu.add_command(label='Welkom Team_6')
acc_menu.add_separator()
acc_menu.add_command(label="Overzicht", command=nieuw_frame)
acc_menu.add_separator()
acc_menu.add_command(label="Log uit", command=root.quit)

# frame maken
new_frame = Frame(root, width=400, height=400, bg='green')

root.mainloop()



