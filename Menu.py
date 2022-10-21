
from catalogo import Catalogo
import sys
class Menu:

    def __init__(self):
        self.catalogo = Catalogo()

    def mostrar_menu(self):
        print("""
Menú del anotador:
1. Mostrar todos los libros
2. Buscar libros
3. Agregar libro
4. Modificar libro
5. Eliminar libro
6. Salir
""")
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = int(input("Ingresar una opción: "))
            if opcion == 1:
                self.Mostrar_Libros()
            elif opcion == 2:
                self.Buscar_Libros()
            elif opcion == 3:
                self.agregar_libro()
            elif opcion == 4:
                self.modificar_libro()
            elif opcion == 5:
                self.eliminar_libro()
            elif opcion == 6:
                self.salir()
            else:
                print("No es una opcion valida")
    def Mostrar_Libros(self, libro=None):
        if libro is None:
            libro = self.catalogo.libros
        for n in libro:
            print(f"Libro nº: {n.id} - Titulo: {n.titulo} - Autor: {n.autor}")

    def Buscar_Libros(self):
    
       id = int(input("Ingresa una ID:"))
       filtro=input("Ingresar filtro de busqueda:")
       if id:
           libros = self.catalogo.buscar_id(id)
           if libros:
              self.Mostrar_Libros(libros)
       if filtro:
           libros = self.catalogo.buscar(filtro)
           if libros:
              self.Mostrar_Libros(libros)
    def agregar_libro(self):
     t= input("Ingresar titulo del libro:")
     a= input("ingresar nombre del autor:")
     self.catalogo.nuevo_libro(t, a)
    def eliminar_libro(self):
      ID=  int(input("Ingresa una ID:"))
      filtro=  input("Ingresa un filtro(Autor/Titulo):")
      if ID:
        self.catalogo.eli_libro_por_id(ID)
      if filtro:
        self.catalogo.eli_libro_por_filtro(filtro)
    def modificar_libro(self):
     Id = int(input("Ingresa una ID:"))
     titulo = input("Ingresa un titulo")
     autor = input ("Ingresa un autor")
     if titulo:
         self.catalogo.mod_titulo_libro(Id, titulo)
     if autor:
        self.catalogo.mod_autor_libro(Id, autor)
    def salir(self):
        print("Cerrando sistema...")
        sys.exit(0)

if __name__ == "__main__":
    Menu().ejecutar()

          
          




