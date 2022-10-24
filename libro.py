import datetime
ult_id = 0

class Libros:
     def __init__(self, tit, aut=''):
        self.titulo=tit
        self.autor=aut
        self.fecha_aniadida=datetime.date.today()
        global ult_id
        ult_id += 1
        self.id = ult_id

     def coincidir(self, filtro):

        if filtro in self.titulo or filtro in self.autor:
           return True 
        else:
           return False
     def coincidir_id(self, id):

        if id in self.id:
           return True 
        else:
           return False
