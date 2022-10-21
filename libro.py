import datetime
id=0

class Libros:
     def __init__(self, tit, aut=''):
        self.titulo=tit
        self.autor=aut
        self.fecha_aniadida=datetime.date.today()
        global id
        id+=1
        self.id=id

     def coincidir(self, filtro):

        if filtro in self.titulo or filtro in self.autor:
           return True 
        else:
           return False
