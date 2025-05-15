import tkinter as tk
import math
from decimal import Decimal

def sluit():
    window.destroy()

def start():
    # begroeting en start
    greeting = tk.Label(frame,text="Hallo, muntmeester!!")
    greeting.grid(column=0, row=1, columnspan = 2, sticky='EW')

    vraag = tk.Label(frame,text="Om welk bedrag gaat het?")
    vraag.grid(column=0, row=2)
    # creer invoerveld
    entry = tk.Entry(frame)
    entry.grid(column=1, row=2)
    entry.bind("<Return>", bereken_munten)


    # zet om naar bedrag weergave
def to_geld(bedrag):
    x = int(bedrag)/100
    x = str('{0:.2f}'.format(x)).replace(".",",")
    return '\u20ac ' + x


    
#start het berekenen na input bedrag
def bereken_munten(event):
    # beschikbare munten op volgorde van groot naar klein
    euromunten = [200,100,50,20,10,5,1]

    # verwijder alle labels in frame1    
    for label in frame1.winfo_children():
        label.destroy()    

    #lees het invoerveld en zet om naar een bedrag als het een geldig bedrag is, anders geef tekst niet geldig
    try:
        bedrag = Decimal(event.widget.get().replace(",", "."))*100
    except:
        bedrag = 0    

    if bedrag <= 0:
        tekst = tk.Label(frame1, text='Dit is geen geldig geldbedrag, probeer opnieuw')
        tekst.pack()
        return        
    else:
        tekst = tk.Label(frame1, text='Het bedrag ' + to_geld(bedrag) + ' in minimaal aantal munten:')
        tekst.pack()

    count = 0
    rest = bedrag

    #bereken (van groot naar klein) hoeveel munten in het overige bedrag passen
    for munt in euromunten:
        aantal = math.floor(rest/munt)
        count += aantal
        rest = rest - (aantal * munt)
        if aantal != 0:
            t = tk.Label(frame1, text = str(aantal) + " x " + to_geld(munt))
            t.pack()
        if rest == 0:
            break
    
    result = tk.Label(frame1, text = "Het minimum aantal munten is dus " + str(count))
    result.pack()


#maak een window
window = tk.Tk()
window.title("Gepaste munten")
window.geometry("400x400")


#creeer bovenste frame met grid (blijft staan)
frame = tk.Frame()
frame.columnconfigure(0, weight=3)
frame.columnconfigure(1, weight=1)
frame.pack()

#creeer tweede frame (wordt gewist per berekening)
frame1 = tk.Frame()
frame1.pack()

btn = tk.Button(text="sluit app", command=sluit)
btn.pack(side=tk.BOTTOM)

start()
window.mainloop()