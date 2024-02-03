from classe_prodottopr import *
from carrello import *
import tkinter as tk
from PIL import ImageTk,Image

class Shop(object):

    def __init__(self,master):
        self.photo = []
        self.totale_carrello = 0
        self.master = master  #root
        self.master.title("Negozio")
        self.prodotti = []
        file = open("prodotti.txt","r")
        c = 0
        for riga in file:
            elementi = riga.split(",")
            image = Image.open(elementi[0])
            image = image.resize((50,50))
            self.photo.append(ImageTk.PhotoImage(image))
            self.prodotti.append(Prodotto(self.photo[c],elementi[1],elementi[2],elementi[3],elementi[4],elementi[5],elementi[6]))
            c = c + 1
        self.carrello = Carrello()
        self.visualizza_prodotti_frame = tk.Frame(self.master)
        self.visualizza_prodotti_frame.pack(padx = 10, pady = 10)
        self.visualizza_carrello_frame = tk.Frame(self.master)
        self.visualizza_carrello_frame.pack(padx = 10, pady = 10)
        self.visualizza_carrello()
        self.visualizza_prodotti()
        self.create_menu()
        self.mostra_prodotti()
    
    def visualizza_prodotti(self):
        for prodotto in self.prodotti:
            frame = tk.Frame(self.visualizza_prodotti_frame)
            frame.pack(fill=tk.X)
            frame2 = tk.Frame(frame)
            frame2.pack(fill=tk.X)
            image_label = tk.Label(frame2,image = prodotto.immagine)
            image_label.pack(side = tk.LEFT)
            label = tk.Label(frame2,text = f"{prodotto.nome} - € {prodotto.prezzo}")
            label.pack(side = tk.LEFT)
            button = tk.Button(frame2,text = "Aggiungi al carrello", command = lambda p = prodotto: self.aggiungi(p))
            button.pack(side = tk.RIGHT)
            self.label2 = tk.Label(frame,text = "Quantità:"+ prodotto.quantità + " Stock:"+ prodotto.stock + " Descrizione:"+ prodotto.descrizione + " Numero di serie:"+ prodotto.numero_di_serie)
            self.label2.pack(side = tk.LEFT)
            

    def visualizza_carrello(self):
        label = tk.Label(self.visualizza_carrello_frame)
        label.pack()
        self.lista_carrello = tk.Listbox(self.visualizza_carrello_frame,height = 15,width = 50)
        self.lista_carrello.pack()
        button = tk.Button(self.visualizza_carrello_frame, text = "Compra tutto",command = lambda: self.compra_tutto())
        button.pack()
        self.totale = tk.Label(self.visualizza_carrello_frame,text = "Totale: €" + str(self.totale_carrello))
        self.totale.pack()
        
    def aggiungi(self,p):
        self.carrello.aggiungi_al_carrello(p)
        self.aggiorna_carrello()

    def rimuovi(self,p):
        self.carrello.rimuovi_prodotto(p)
        self.aggiorna_carrello()
    
    def aggiorna_carrello(self):
        self.lista_carrello.delete(0,tk.END)
        for item in self.carrello.prodotti:
            self.lista_carrello.insert(tk.END,f"{item.nome} - € {item.prezzo}")

    def create_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu = menu)
        view = tk.Menu(menu,tearoff = False)
        menu.add_cascade(label = "visualizza",menu = view)
        view.add_command(label = "prodotti",command = self.mostra_prodotti)
        view.add_command(label = "carrello",command = self.mostra_carrello)

    def mostra_prodotti(self):
        self.visualizza_carrello_frame.pack_forget()
        self.visualizza_prodotti_frame.pack()
        #for prodotto in self.prodotti:
            #self.label2.config(text = "Quantità:"+ prodotto.quantità + " Stock:"+ prodotto.stock + " Descrizione:"+ prodotto.descrizione + " Numero di serie:"+ prodotto.numero_di_serie)
        #self.lista_carrello.config(text = "carrello")

    def mostra_carrello(self):
        self.totale_carrello = self.carrello.calcola_totale()
        self.visualizza_prodotti_frame.pack_forget()
        self.visualizza_carrello_frame.pack()
        self.totale.config(text = "Totale: €" + str(self.totale_carrello))

    def compra_tutto(self):
        self.carrello.compra_tutto()
        self.aggiorna_carrello()
        self.mostra_carrello()
        for prodotto in self.prodotti:
            print("Quantità:"+ prodotto.quantità + " Stock:"+ prodotto.stock + " Descrizione:"+ prodotto.descrizione + " Numero di serie:"+ prodotto.numero_di_serie)

        


root = tk.Tk()
app = Shop(root)
root.mainloop()