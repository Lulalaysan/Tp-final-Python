from libro import Libros
class Catalogo:
    def __init__(self, lista_de_libros = []):
        self.libros = lista_de_libros

    def nuevo_libro(self, titulo, autor=''):
        l = Libros(titulo, autor)
        self.libros.append(l)
        return l
    def _buscar_id(self, id_libro):
           for libro in self.libros:
            if str(libro.id) == str(id_libro):
                return libro
            return None

    def mod_titulo_libro(self,id_libro, titulo):
        Libro = self._buscar_id(id_libro)
        if Libro :
            Libro.titulo=titulo
            return print("la modificacion se ha realizado exitosamente")
        
    def mod_autor_libro(self, id_libro, autor):
        Libro = self._buscar_id(id_libro)
        if Libro : 
            Libro.autor=autor
            return print("la modificacion se ha realizado exitosamente")
        
    def buscar(self, filtro):
      return [ libro for libro in self.libros if libro.coincidir(filtro) ]
 
    def eli_libro_por_id(self, id_libro):
     Libro= self._buscar_id(id_libro)
     if Libro:
        self.libros.remove(Libro)
        return True
     return False
