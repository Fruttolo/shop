
class Prodotto(object):
    immagine = object()
    numero_di_serie = 0
    prezzo = 0
    nome = ""
    quantità = ""
    stock = 0
    descrizione = ""


    def __init__(self, immagine, numero_di_serie, prezzo, nome, quantità,stock,descrizione):
        self.immagine = immagine
        self.numero_di_serie = numero_di_serie
        self.prezzo = prezzo
        self.nome = nome
        self.quantità = quantità
        self.stock = stock
        self.descrizione = descrizione
    

    def modifica(self, numero_di_serie, prezzo, nome, quantità,stock,descrizione):
        if numero_di_serie != "":
            self.numero_di_serie = int(numero_di_serie)
        if prezzo != "":
            self.prezzo = int(prezzo)
        if nome != "":
            self.nome = nome
        if quantità !="" :
            self.quantità = int(quantità)
        if stock !="" :
            self.stock = int(stock)
        if descrizione != "":
            self.descrizione = descrizione
    
    

    def riordino(self, quantità,stock):
        if int(quantità) <= int(stock):
            self.quantità = str(int(quantità) + 9) #ne aggiungo 9 perchè 1 l'ho appena acquistato


    def vendita(self,quantità,stock):
        self.quantità = str(int(quantità) - 1)
        print("Hai venduto 1 articolo")
        if int(quantità) <= int(stock):
            self.riordino(quantità,stock)
            print("Ho eseguito il riordino degli articoli")

