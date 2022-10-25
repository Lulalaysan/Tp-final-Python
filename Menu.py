from catalogo import Catalogo
import sys
from Repositorio import repositorio
class Menu:

    def __init__(self):
        self.iniciar_repositorio()
    def iniciar_repositorio(self):
        self.repositorio = repositorio()
        libros = self.repositorio.obtener_todo()
        self.catalogo = Catalogo(libros)
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
        for l in libro:
            print(f"Libro nº:{l.id}, Titulo:{l.titulo}, Autor:{l.autor}")
    def Buscar_Libros_por_filtro(self):
     filtro=input("Ingresar un flitro(titulo/autor)")
     libros= self.catalogo.buscar(filtro)
     if libros:
                self.Mostrar_Libros(libros)
   
    def Buscar_Libros(self):
        self.Buscar_Libros_por_filtro()
    def agregar_libro(self):
      t= input("Ingresar titulo del libro:")
      a= input("Ingresar autor del libro:")
      self.catalogo.nuevo_libro(t,a)
      print("se ha añadido un libro al catalogo")

    def eliminar_libro(self):
       Id= int(input("Ingresar ID"))
       if Id:
        self.catalogo.eli_libro_por_id(Id)

    def modificar_libro(self):
     Id = int(input("Ingresa una ID:"))
     titulo = input("Ingresa un titulo")
     autor = input ("Ingresa un autor")
     if titulo:
         self.catalogo.mod_titulo_libro(Id, titulo)
     if autor:
        self.catalogo.mod_autor_libro(Id, autor)

    def salir(self):
        self.repositorio.guardar_todo(self.catalogo.libros)
        print("Cerrando sistema...")
        sys.exit(0)

if __name__ == "__main__":
    Menu().ejecutar()

                  