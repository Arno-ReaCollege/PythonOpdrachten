import tkinter as tk
from tkinter.ttk import Combobox
import random

#gooi een dobbelsteen (random nummer tussen 1-6)
def gooi():
    return random.randint(1,6)

#verwijder alle labels
def clear():
    for label in window.winfo_children():
        label.destroy()

def start():
    clear()
    # begroeting en start
    greeting = tk.Label(text="Hallo, dobbelaar\n\n Met hoeveel dobbelstenen wil je gooien?")
    greeting.pack()

    # vraag om aantal dobbelstenen
    mogelijk_aantal_dobbelstenen = [3,4,5]
    aantal = tk.IntVar()

    c_box = Combobox(window, values=(mogelijk_aantal_dobbelstenen), state='readonly')
    c_box.pack()

    c_box.bind('<<ComboboxSelected>>', get_aantal_dobbelstenen)

#start het dobbelen na input aantal dobbelstenen
def get_aantal_dobbelstenen(event):
        
    aantal = event.widget.get()
    clear()
    tekst = tk.Label(text='Je koos '+ aantal + ' dobbelstenen')
    tekst.pack()

    i = 1
    totaal = 0
    totaal_onder = 0
    count = 0
    
    while i <= int(aantal):
        ogen = gooi()
        #count als het aantal ogen 6 is
        if ogen == 6:
            count += 1
        totaal += ogen
        totaal_onder += 7 - ogen
        dobbel = tk.Label(text="\n\nDobbelsteen " + str(i) + " gooit " + str(ogen) + " ogen\nDe onderzijde telt " + str(7 - ogen) + " ogen")
        dobbel.pack()
        i += 1
        
        if i-1 == int(aantal):
            einde = tk.Label(text="\nHet totaal aantal gegooide ogen is " + str(totaal) +  "\nHet totaal ogen aan de onderzijde is " + str(totaal_onder) +"\n\nWil je nog een keer?")
            einde.pack()
            btn = tk.Button(text="opnieuw", command=start)
            btn.pack()


        if count > 2:
            hoera = tk.Label(text = "Hoera, je hebt geluk: je hebt minimaal drie x een zes gegooid!!")
            hoera.pack()
        

#maak een window
window = tk.Tk()
window.title("Dobbelsteen")
window.geometry("400x800")

start()
window.mainloop()