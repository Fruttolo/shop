from tkinter import *
from tkinter import ttk
from classe_prodottopr import Prodotto
from PIL import ImageTk,Image
from carrello import Carrello


def selezione_opzione(event):
    for widget in frm.winfo_children():
            widget.destroy()
    if selezione.get() == "Visualizza prodotti":
        visualizza_prodotti()
    else:
        visualizza_carrello()


def visualizza_prodotti():
    r = 6
    p = 0
    for prodotto in prodotti:
        ttk.Label(frm,text = prodotto.nome).grid(column = 1,row = r - 6)
        ttk.Label(frm,text = prodotto.prezzo).grid(column = 1,row = r - 5)
        ttk.Label(frm,text = prodotto.quantità).grid(column = 1,row = r - 4)
        ttk.Label(frm,text = prodotto.stock).grid(column = 1,row = r - 3)
        ttk.Label(frm,text = prodotto.numero_di_serie).grid(column = 1,row = r - 2 )
        ttk.Label(frm,text = prodotto.descrizione).grid(column = 1,row = r - 1)
        ttk.Button(frm,text = "Aggiungi al carrello", command = lambda: carrello.aggiungi_al_carrello(prodotto)).grid(column = 2,row = r - 6) 
        #ttk.Label(frm,image = prodotto.immagine).grid(column = 0, row = r - 6)
        r = r + 6
        p = p + 1

def visualizza_carrello():
    r = 6
    p = 0
    for prodotto in carrello.prodotti:
        ttk.Label(frm,text = prodotto.nome).grid(column = 1,row = r - 6)
        ttk.Label(frm,text = prodotto.prezzo).grid(column = 1,row = r - 5)
        ttk.Label(frm,text = prodotto.quantità).grid(column = 1,row = r - 4)
        ttk.Label(frm,text = prodotto.stock).grid(column = 1,row = r - 3)
        ttk.Label(frm,text = prodotto.numero_di_serie).grid(column = 1,row = r - 2 )
        ttk.Label(frm,text = prodotto.descrizione).grid(column = 1,row = r - 1)
        #ttk.Label(frm,image = prodotto.immagine).grid(column = 0, row = r - 6)
        r = r + 6
        p = p + 1  



carrello = Carrello()
prodotti = []
photo = []
c = 0
file = open("prodotti.txt","r")
for riga in file:
    elementi = riga.split(",")
    #image = Image.open(elementi[0])
    #image = image.resize((50,50))
    #photo.append(ttk.PhotoImage(image))
    prodotti.append(Prodotto(elementi[0],elementi[1],elementi[2],elementi[3],elementi[4],elementi[5],elementi[6]))
    c = c + 1
    

root = Tk()
root.title("Shop")
main_frm = ttk.Frame(root)
frm = ttk.Frame(main_frm) 
frm.grid(column = 0,row = 1,pady=20)
main_frm.grid()
selezione = ttk.Combobox(main_frm,values=["Visualizza prodotti","Carrello"])
selezione.grid(column = 0,row = 0)
selezione.current(0)
visualizza_prodotti()
selezione.bind("<<ComboboxSelected>>",selezione_opzione)


root.mainloop()