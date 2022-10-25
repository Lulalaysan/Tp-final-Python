from catalogo import Catalogo
from libro import Libros
import datetime
class repositorio:
    def __init__(self, archivo="libros.txt"):
        self.archivo = archivo
    
    def obtener_todo(self):
        libros=[]
        with open(self.archivo, 'r') as op:
             for Libro_texto in op:
                l = self.texto_a_libro(Libro_texto)
                libros.append(l)
        return libros
    def texto_a_libro(self, texto):
        texto = texto[:-1]
        libro_lista = texto.split(',')
        l = Libros(libro_lista[0], libro_lista[1])
        fecha = libro_lista[2].split('-')
        l.fecha_aniadida = datetime.date(int(fecha[0]),int(fecha[1]),int(fecha[2])) 
        return l
    def guardar_todo(self, libros):
        with open(self.archivo, 'w') as wr:
            for libro in libros:
                libro_texto = self.libro_a_texto(libro)
                wr.write(libro_texto)
        print("Guardado en "+ self.archivo) 
    def libro_a_texto(self,libro):
        fa = libro.fecha_aniadida
        fecha_en_texto = str(fa.year) + '-' + str(fa.month) + '-' + str(fa.day)
        return libro.titulo + ',' + libro.autor + ',' + fecha_en_texto + "\n"   
