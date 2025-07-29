
class PrintFruits:
    def __init__(self):
        pass
    def ImprimeFruta(self,Fruta):
        Fruits_memo= {"Apple":self.ExemploFluxo,"Banana":self.ExemploFluxo,"Melon":self.ExWorkFlow}
        Fruits_memo.get(Fruta,self.Error)(Fruta)

    def ExWorkFlow(self,event):
        print(event)
        
    def Error(self,erro):
        print("Fruta não cadastrada: "+Error)

User = "Maca"
Fruit = PrintFruits()
Fruit.ImprimeFruta(User)
