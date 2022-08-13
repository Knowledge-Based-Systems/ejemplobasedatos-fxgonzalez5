from bd import *
import codecs

class Ejecutor:

    def select(self, tabla):
        base = BDdatos()
        print(base.consulta(tabla))

    def insert(self):
        base = BDdatos()
        cedula = input("Ingrese el número de cédula: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        telefono = input("Ingrese su número de telefono: ")
        base.agregar([cedula, nombre, apellido, telefono])

    def update(self):
        base = BDdatos()
        cedula = input("Ingrese el número de cédula: ")
        
        print("""¿Qué campo desea actualizar?
            1. Nombre
            2. Apellido
            3. Telefono
            4. Volver""")

        op = int(input("Seleccione una opción: "))

        if op == 1:
            nombre = input("Ingrese su nombre: ")
            base.actualizar([cedula, nombre], 'nombre')
        elif op == 2:
            apellido = input("Ingrese su apellido: ")
            base.actualizar([cedula, apellido], 'apellido')
        elif op == 3:
            telefono = input("Ingrese su número de telefono: ")
            base.actualizar([cedula, telefono], 'telefono')
        else:
            print()
            self.menu()

        
        

    def menu(self):
        print("""Menú
            1. Ver data de Usuarios
            2. Ingresar datos en Usuarios
            3. Actualizar datos de Usuarios
            4. Salir""")

        op = int(input("Seleccione una opción: "))

        if op == 1:
            self.select("usuarios")
            print()
            self.menu()
        elif op == 2:
            self.insert()
            print("Datos ingresados correctamente!\n")
            self.menu()
        elif op == 3:
            self.update()
            print("Datos actualizados correctamente!\n")
            self.menu()
        else:
            print("Gracias, vuelva pronto...")

if __name__ == '__main__':
    """
    """
    #
    objeto = Ejecutor()
    objeto.menu()
