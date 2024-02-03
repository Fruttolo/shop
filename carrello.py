class Carrello(object):

    prodotti = []
    totale = 0
  
    def aggiungi_al_carrello(self,prodotto):
        self.prodotti.append(prodotto)

    def rimuovi_prodotto(self,prodotto):
        if prodotto in self.prodotti:
            self.prodotti.remove(prodotto)
        