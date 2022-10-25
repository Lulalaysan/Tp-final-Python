from ctypes import LibraryLoader
from re import X
from catalogo import Catalogo
import tkinter
from tkinter import Place, ttk
from tkinter import messagebox
from Repositorio import repositorio
from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
from libro import Libros
class interfaz():
    def __init__(self):
        self.iniciar_catalogo()
        self.iniciar_interfaz()
        

    def iniciar_catalogo(self):  
        self.repositorio = repositorio()
        libros = self.repositorio.obtener_todo()
        self.catalogo = Catalogo(libros)
        
    def iniciar_interfaz(self):
        self.fachada_principal = tkinter.Tk()
        self.fachada_principal.title("Catalogo de Libros")
        self.fachada_principal.geometry('442x300')
        B_AgregarLibro=tkinter.Button(self.fachada_principal,text="Agregar libro ", 
                        command=self.nuevo_libro).grid(row=0, column=0)
        botoneliminar = tkinter.Button(self.fachada_principal,text="Eliminar libro ",
                        command=self.eliminar_libro).grid(row=0,column=2)
        botonmodificar = tkinter.Button(self.fachada_principal, text="Modificar Libro",
                        command=self.modificar_libro).grid(row=0 ,column=1)
        tkinter.Label(self.fachada_principal, text="Buscar:").grid(row=1,column=0)
        self.cajabuscar = tkinter.Entry(self.fachada_principal)
        self.cajabuscar.grid(row=1,column=1)
        tkinter.Label(self.fachada_principal, text="Cantidad de libros:" ).grid(row=11,column=1)
        tkinter.Label(self.fachada_principal, text=str(len(self.catalogo.libros))).grid(row=11,column=2)
        botonbuscar = tkinter.Button(self.fachada_principal,text="Buscar",
                        command=self.buscar).grid (row=1,column=2)
        self.treeview = ttk.Treeview(self.fachada_principal)
        self.treeview = ttk.Treeview(self.fachada_principal, columns=("titulo", "autor"))
        self.treeview.heading("#0", text="ID")
        self.treeview.column("#0", minwidth=0, width="40")
        self.treeview.heading("titulo", text="Titulo")
        self.treeview.heading("autor", text="Autor")
        self.treeview.grid(row=10, columnspan=3)
        self.escritura_tabla()
        botonsalir = tkinter.Button(self.fachada_principal, text = "Salir",
                command = self.salir).grid(row=11,column=0)
        self.cajabuscar.focus()
    def escritura_tabla(self, libros = None):
         for a in self.treeview.get_children():
            self.treeview.delete(a)
         if not libros:
            libros = self.catalogo.libros
         for libro in libros:
             item = self.treeview.insert("", tkinter.END, text=libro.id,
                              values=(libro.titulo, libro.autor), iid=libro.id) 
     
    def nuevo_libro(self):
        self.libroagg = tkinter.Toplevel(self.fachada_principal)
        self.libroagg.grab_set()
        tkinter.Label(self.libroagg,text="Libro: ").grid()
        self.titulo=tkinter.Entry(self.libroagg)
        self.titulo.grid(row=0,column=1,columnspan=2)
        self.titulo.focus()
        tkinter.Label(self.libroagg, text = "Autor: ").grid(row=1)
        self.autor = tkinter.Entry(self.libroagg)
        self.autor.grid(row=1, column=1, columnspan=2)
        botonOK = tkinter.Button(self.libroagg, text="Guardar",
                command=self.agregar_ok)
        self.libroagg.bind("<Return>", self.agregar_ok)
        botonOK.grid(row=2)
        botonCancelar = tkinter.Button(self.libroagg, text = "Cancelar",
                command = self.libroagg.destroy)
        botonCancelar.grid(row=2,column=2)

    def agregar_ok(self, event=None):
        libro = self.catalogo.nuevo_libro(self.titulo.get(), self.autor.get())
        self.libroagg.destroy()
        item = self.treeview.insert("", tkinter.END, text= libro.id, values=(libro.titulo, libro.autor))
       
    def modificar_libro(self):
       if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                    "Seleccione primero el libro a modificar")
            return False
       item = self.treeview.selection()        
       id = self.treeview.item(item)['text']

       print(id)
       libro = self.catalogo._buscar_id(id)
       self.libromod = tkinter.Toplevel(self.fachada_principal)
       self.libromod.grab_set()
       tkinter.Label(self.libromod, text = "Titulo: ").pack()
       self.titulo = tkinter.Entry(self.libromod)
       self.titulo.insert(0,libro.titulo)
       self.titulo.pack()
       self.titulo.focus()
       tkinter.Label(self.libromod, text = "Autor: ").pack()
       self.autor = tkinter.Entry(self.libromod)
       self.autor.insert(0,libro.autor)
       self.autor.pack()
       Bu_OK = tkinter.Button(self.libromod, text="Guardar",
                command=self.modificar_ok)
       self.libromod.bind("<Return>", self.modificar_ok)
       Bu_OK.pack()
       B_Cancelar = tkinter.Button(self.libromod, text = "Cancelar",
                                       command = self.libromod.destroy)
       B_Cancelar.pack()
    def modificar_ok(self, event=None):
        item = self.treeview.selection()        
        id = self.treeview.item(item)['text']
        print("Libro modificado ",id)
        self.catalogo.mod_titulo_libro(id, self.titulo.get())
        self.catalogo.mod_autor_libro(id, self.autor.get())
        self.treeview.set(self.treeview.selection()[0], column="titulo",
                          value = self.titulo.get())
        self.treeview.set(self.treeview.selection()[0], column="autor",
                          value = self.autor.get())
        self.libromod.destroy()
   
    def eliminar_libro(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                "Seleccione primero el libro a eliminar")
            return False
        else:
            resp = messagebox.askokcancel("Confirmar",
                "¿Está seguro de eliminar el libro?")
            if resp:
                id_lib = int(self.treeview.selection()[0])
                self.treeview.delete(self.treeview.selection()[0])
                self.catalogo.eli_libro_por_id(id_lib)
            else:
                return False

    def buscar(self):
        filtro = self.cajabuscar.get()
        libros = self.catalogo.buscar(filtro)
        if libros:
            self.escritura_tabla(libros)
        else:
            messagebox.showwarning("Sin resultados",
                                "Ningun libro  coincide con la búsqueda")       

    def salir(self):
        self.repositorio.guardar_todo(self.catalogo.libros)
        self.fachada_principal.destroy()

if __name__ == "__main__":
    Interfaz = interfaz()
    Interfaz.fachada_principal.mainloop()