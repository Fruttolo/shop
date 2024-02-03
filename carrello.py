class Carrello(object):

    prodotti = []
    totale = 0
  
    def aggiungi_al_carrello(self,prodotto):
        self.prodotti.append(prodotto)

    def rimuovi_prodotto(self,prodotto):
        if prodotto in self.prodotti:
            self.prodotti.remove(prodotto)

    def calcola_totale(self):
        self.totale = 0
        for prodotto in self.prodotti:
            self.totale += prodotto.prezzo
        return self.totale
    
    def compra_tutto(self):
        self.prodotti = []
        self.totale = 0
        print("Hai acquistato tutto")
        