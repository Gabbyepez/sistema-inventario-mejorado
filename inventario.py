import os

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # ==============================
    # CARGAR INVENTARIO DESDE ARCHIVO
    # ==============================
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")
                    if len(datos) == 3:
                        nombre, cantidad, precio = datos
                        self.productos.append(
                            Producto(nombre, int(cantidad), float(precio))
                        )
            print("Inventario cargado correctamente.\n")

        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo.")
            open(self.archivo, "w").close()

        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")

        except Exception as e:
            print("Error al cargar archivo:", e)

    # ==============================
    # GUARDAR INVENTARIO EN ARCHIVO
    # ==============================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(str(producto) + "\n")
            print("Inventario guardado correctamente.\n")

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

        except Exception as e:
            print("Error al guardar archivo:", e)

    # ==============================
    # AÑADIR PRODUCTO
    # ==============================
    def añadir_producto(self, nombre, cantidad, precio):
        for producto in self.productos:
            if producto.nombre == nombre:
                print("El producto ya existe.")
                return

        nuevo = Producto(nombre, cantidad, precio)
        self.productos.append(nuevo)
        self.guardar_en_archivo()
        print("Producto añadido correctamente.\n")

    # ==============================
    # ACTUALIZAR PRODUCTO
    # ==============================
    def actualizar_producto(self, nombre, cantidad, precio):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.cantidad = cantidad
                producto.precio = precio
                self.guardar_en_archivo()
                print("Producto actualizado correctamente.\n")
                return

        print("Producto no encontrado.\n")

    # ==============================
    # ELIMINAR PRODUCTO
    # ==============================
    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.\n")
                return

        print("Producto no encontrado.\n")

    # ==============================
    # MOSTRAR INVENTARIO
    # ==============================
    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.\n")
            return

        print("\n--- INVENTARIO ACTUAL ---")
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}")
            print(f"Cantidad: {producto.cantidad}")
            print(f"Precio: ${producto.precio}")
            print("-------------------------")


# ==============================
# INTERFAZ DE USUARIO
# ==============================
def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.añadir_producto(nombre, cantidad, precio)

            elif opcion == "2":
                nombre = input("Nombre del producto a actualizar: ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(nombre, cantidad, precio)

            elif opcion == "3":
                nombre = input("Nombre del producto a eliminar: ")
                inventario.eliminar_producto(nombre)

            elif opcion == "4":
                inventario.mostrar_inventario()

            elif opcion == "5":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Error: Debe ingresar valores numéricos válidos para cantidad y precio.")

        except Exception as e:
            print("Ocurrió un error inesperado:", e)


if __name__ == "__main__":
    menu()