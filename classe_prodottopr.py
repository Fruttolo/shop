
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
    

    #def visualizza(self):
        #print("L'immagine del prodotto è:", self.immagine)
        #print("Il numero di serie del prodotto è:", self.numero_di_serie)
        #print("Il prezzo del prodotto è:", self.prezzo)
        #print("Il nome del prodotto è:", self.nome)
        #print("La quantità di prodotti è:", self.quantità)
        #print("Lo stock del prodotto è:",self.stock)
        #print("La descrizione del prodotto è:",self.descrizione)
        
    

    def riordino(self, quantità,stock):
        if int(quantità) < int(stock):
            self.quantità = str(int(quantità) + 10)


    def vendita(self,quantità,stock):
        if int(quantità) > int(stock):
            self.quantità = str(int(quantità) - 1)
            print("Hai venduto 1 articolo")
            self.riordino(quantità,stock)
        else:
            print("Esegui prima il riordino degli articoli")

