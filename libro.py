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

        return(filtro in self.titulo) or (filtro in self.autor)
                
