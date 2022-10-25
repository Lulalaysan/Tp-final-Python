from libro import Libros
class Catalogo:
    def __init__(self):
        l1 = Libros("IT","Stephen King")
        l2 = Libros("Las cuatro estaciones_del_amor","Gregoire Delacourt")
        l3 = Libros("Rebelion en la granja","George Orwell")
        l4 = Libros("Martin Fierro","Jose Hernandez")
        self.libros = [l1, l2, l3, l4]

    def nuevo_libro(self, titulo, autor=''):
        l = Libros(titulo, autor)
        self.libros.append(l)

    def buscar_id(self, id_libro):
           for a in self.libros:
            if a.id == id_libro:
                return a
           return None

    def mod_titulo_libro(self,id_libro, titulo):
        Libro = self.buscar_id(id_libro)
        if Libro :
            Libro.titulo=titulo
            return print("la modificacion se ha realizado exitosamente")
        
    def mod_autor_libro(self, id_libro, autor):
        Libro = self.buscar_id(id_libro)
        if Libro : 
            Libro.autor=autor
            return print("la modificacion se ha realizado exitosamente")
        
    def buscar(self, filtro):
      list = []
      for a in self.libros:
        if a.coincidir(filtro):
          list.append(a)
          return list
        else:
          return print("El filtro no coincide con ningun libro")
 
    def eli_libro_por_id(self, id_libro):
     Libro= self.buscar_id(id_libro)
     if Libro:
        self.libros.remove(Libro)
        return print("El libro se ha eliminado exitosamente")  
