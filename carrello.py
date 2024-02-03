class Carrello(object):
  
    #Costruttore dell'istanza
    def __init__(self):
        self.prodotti = []
        self.totale = 0
        
    #funzione che permette di aggiungere un prodotto al carrello
    def aggiungi_al_carrello(self,prodotto):
        self.prodotti.append(prodotto)

    #Funzione che permette di rimuovere un prodotto dal carrello
    def rimuovi_prodotto(self,prodotto):
        if prodotto in self.prodotti:
            self.prodotti.remove(prodotto)

    #Funzione che calcola il tolate dei prodotti nel carrello
    def calcola_totale(self):
        self.totale = 0
        for prodotto in self.prodotti:
            self.totale += int(prodotto.prezzo)
        return self.totale
    
    #Funzione che permette di comprare tutto quello che c'è nel carrello
    def compra_tutto(self):
        for prodotto in self.prodotti:
            prodotto.vendita(prodotto.quantità,prodotto.stock)
        self.prodotti = []
        self.totale = 0
        print("Hai acquistato tutto")
        