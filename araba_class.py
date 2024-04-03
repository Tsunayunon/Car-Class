class Araba:
    def __init__(self, marka,model,renk): #metod
        self.marka=marka
        self.model=model
        self.renk=renk

       
taksi=Araba("Mercedes","E200","Beyaz")
kamyon=Araba("Volvo","FH16","Kırmızı")    #nesneler
trakor=Araba("John Deere","8R","Yeşil")
print(taksi.marka)
print(kamyon.model)
print(trakor.renk)

        
        
