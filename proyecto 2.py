
class Categoriaprincipal:
    def __init__(self):
        self.Dic_categoria = {}
        self.cargar_categoria()

    def cargar_categoria(self):
        try:
            with open("categoria.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        Id_categoria, nombre = linea.split(":")
                        self.Dic_categoria[int(Id_categoria)] = {"Nombre": nombre}
            print("Categorías importadas desde categoria.txt")
        except FileNotFoundError:
            print("No existe el archivo categoria.txt, se creará uno nuevo al guardar.")


class Categoria_guardar:
    def __init__(self, categoria_manager):
        self.categoria_manager = categoria_manager

    def guardar_categoria(self):
        with open("categoria.txt", "w", encoding="utf-8") as archivo:
            for Id_categoria, datos in self.categoria_manager.Dic_categoria.items():
                archivo.write(f"{Id_categoria}:{datos['Nombre']}\n")


class Categoria_agregar:
    def __init__(self, categoria_manager, guardar_manager):
        self.categoria_manager = categoria_manager
        self.guardar_manager = guardar_manager

    def agregar_categoria(self, Id_cate, nombre):
        if Id_cate in self.categoria_manager.Dic_categoria:
            print("La categoría ya existe.")
        else:
            self.categoria_manager.Dic_categoria[Id_cate] = {"Nombre": nombre}
            self.guardar_manager.guardar_categoria()
            print(f"Categoría ID {Id_cate} agregada y guardada correctamente.")


class Categoria_mostrar:
    def __init__(self, categoria_manager):
        self.categoria_manager = categoria_manager

    def mostrar_categorias(self):
        if not self.categoria_manager.Dic_categoria:
            print("No hay categorías registradas.")
        else:
            print("\nCategorías registradas:")
            for Id_categoria, datos in self.categoria_manager.Dic_categoria.items():
                print(f"ID: {Id_categoria} - Nombre: {datos['Nombre']}")


class Categoria_eliminar:
    def __init__(self, categoria_manager, guardar_manager):
        self.categoria_manager = categoria_manager
        self.guardar_manager = guardar_manager

    def eliminar_categoria(self, Id_cate):
        if Id_cate in self.categoria_manager.Dic_categoria:
            eliminado = self.categoria_manager.Dic_categoria.pop(Id_cate)
            self.guardar_manager.guardar_categoria()
            print(f"Categoría eliminada: {eliminado['Nombre']}")
        else:
            print("La categoría no existe.")

class Producto:
    def __init__(self):
        self.Dic_producto = {}
        self.cargar_producto()

    def cargar_producto(self):

        try:
            with open("producto.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        Id_producto, nombre, id_categoria, total_compra, total_venta, stock = linea.split(":")
                        self.Dic_producto[int(Id_producto)] = {
                            "Nombre": nombre,
                            "Id_categoria": int(id_categoria),
                            "Total_compra": int(total_compra),
                            "Total_venta": int(total_venta),
                            "Stock": int(stock)
                        }
            print("Productos cargados desde producto.txt")
        except FileNotFoundError:
            print(" No existe producto.txt, se creará al guardar.")

    def guardar_producto(self):

        with open("producto.txt", "w", encoding="utf-8") as archivo:
            for Id_producto, datos in self.Dic_producto.items():
                archivo.write(
                    f"{Id_producto}:{datos['Nombre']}:{datos['Id_categoria']}:"
                    f"{datos['Total_compra']}:{datos['Total_venta']}:{datos['Stock']}\n"
                )

class Ing_producto:
    def __init__(self, producto_manager):
        self.producto_manager = producto_manager

    def ingreso_producto(self, Id_producto, nombre, id_categoria, total_compra, total_venta, stock):
        if Id_producto in self.producto_manager.Dic_producto:
            print(" El producto ya existe.")
        else:
            self.producto_manager.Dic_producto[Id_producto] = {
                "Nombre": nombre,
                "Id_categoria": id_categoria,
                "Total_compra": total_compra,
                "Total_venta": total_venta,
                "Stock": stock
            }
            self.producto_manager.guardar_producto()
            print(f" Producto ID {Id_producto} agregado y guardado.")

class Mostrar_producto:
    def __init__(self, producto_manager):
        self.producto_manager = producto_manager

    def mostrar_todos(self):
        if not self.producto_manager.Dic_producto:
            print(" No hay productos registrados.")
        else:
            print("\n Productos registrados:")
            for Id_producto, datos in self.producto_manager.Dic_producto.items():
                print(
                    f"ID: {Id_producto} | Nombre: {datos['Nombre']} | "
                    f"Categoría: {datos['Id_categoria']} | Total Compra: {datos['Total_compra']} | "
                    f"Total Venta: {datos['Total_venta']} | Stock: {datos['Stock']}"
                )
class Eliminar_producto:
    def __init__(self, producto_manager):
        self.producto_manager = producto_manager

    def eliminar(self, Id_producto):
        if Id_producto in self.producto_manager.Dic_producto:
            eliminado = self.producto_manager.Dic_producto.pop(Id_producto)
            self.producto_manager.guardar_producto()
            print(f" Producto eliminado: {eliminado['Nombre']}")
        else:
            print(" El producto no existe.")


class Buscar_producto:
    def __init__(self, producto_manager):
        self.producto_manager = producto_manager

    def buscar(self, Id_producto):
        if Id_producto in self.producto_manager.Dic_producto:
            datos = self.producto_manager.Dic_producto[Id_producto]
            print(
                f"ID: {Id_producto} | Nombre: {datos['Nombre']} | "
                f"Categoría: {datos['Id_categoria']} | Total Compra: {datos['Total_compra']} | "
                f"Total Venta: {datos['Total_venta']} | Stock: {datos['Stock']}"
            )
        else:
            print(" El producto no existe.")

class proveedor_principal:
    def __init__(self):
        self.Dic_proveedor = {}
        self.cargar_proveedor()

    def cargar_proveedor(self):

        try:
            with open("proveedor.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre,direccion,telefono,correo,empresa = linea.split(":")
                        self.Dic_proveedor[int(nit)] = {
                            "Nombre": nombre,
                            "direccion": (direccion),
                            "telefono": int(telefono),
                            "correo": (correo),
                            "empresa": (empresa)
                        }
            print("proveedor cargados desde proveedor.txt")
        except FileNotFoundError:
            print(" No existe proveedor.txt, se creará al guardar.")

    def guardar_proveedor(self):

        with open("proveedor.txt", "w", encoding="utf-8") as archivo:
            for nit, datos in self.Dic_proveedor.items():
                archivo.write(
                    f"{nit}:{datos['Nombre']}:{datos['direccion']}:"
                    f"{datos['Telefono']}:{datos['correo']}:{datos['empresa']}\n"
                )

class Ing_proveedor:
    def __init__(self, proveedor_manager):
        self.proveedor_manager = proveedor_manager

    def ingrese_proveedor(self, nit, nombre, direccion, telefono, correo, empresa):
        if nit in self.proveedor_manager.Dic_proveedor:
            print(" El proveedor  ya existe en sistema.")
        else:
            self.proveedor_manager.Dic_proveedor[nit] = {
                "Nombre": nombre,
                "direccion": direccion,
                "telefono": telefono,
                "correo": correo,
                "empresa": empresa
            }
            self.proveedor_manager.guardar_proveedor()
            print(f" proveedor Nit {nit} agregado y guardado.")

class Mostrar_proveedor:
    def __init__(self, proveedor_manager):
        self.proveedor_manager = proveedor_manager

    def mostrar_todos(self):
        if not self.proveedor_manager.Dic_proveedor:
            print(" No hay proveedor registrados.")
        else:
            print("\n Proveedor registrados:")
            for nit, datos in self.proveedor_manager.Dic_proveedor.items():
                print(
                    f"ID: {nit} | Nombre: {datos['Nombre']} | "
                    f"direccion: {datos['direccion']} | telefono: {datos['telefono']} | "
                    f"correo: {datos['correo']} | empresa: {datos['empresa']}"
                )
class Eliminar_proveedor:
    def __init__(self, proveedor_manager):
        self.proveedor_manager = proveedor_manager

    def eliminar(self, nit):
        if nit in self.proveedor_manager.Dic_proveedor:
            eliminado = self.proveedor_manager.Dic_proveedor.pop(nit)
            self.proveedor_manager.guardar_proveedor()
            print(f" proveedor eliminado: {eliminado['Nombre']}")
        else:
            print(" El proveedor no existe.")


class Buscar_preveedor:
    def __init__(self, proveedor_manager):
        self.proveedor_manager = proveedor_manager

    def buscar(self, nit):
        if nit in self.proveedor_manager.Dic_proveedor:
            datos = self.proveedor_manager.Dic_proveedor[nit]
            print(
                f"nit: {nit} | Nombre: {datos['Nombre']} | "
                f"direccion: {datos['direccion']} | telefono: {datos['telefono']} | "
                f"correo: {datos['correo']} | empresa: {datos['empresa']}"
            )
        else:
            print(" proveedor no existe.")


class cliente_principal:
    def __init__(self):
        self.Dic_cliente = {}
        self.cargar_cliente()

    def cargar_cliente(self):

        try:
            with open("cliente.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit_cliente, nombre,direccion,telefono,correo,= linea.split(":")
                        self.Dic_cliente[int(nit_cliente)] = {
                            "Nombre": nombre,
                            "direccion": (direccion),
                            "telefono": int(telefono),
                            "correo": (correo)
                        }
            print("cliente cargados desde proveedor.txt")
        except FileNotFoundError:
            print(" No existe cliente.txt, se creará al guardar.")

    def guardar_cliente(self):

        with open("cliente.txt", "w", encoding="utf-8") as archivo:
            for nit_cliente, datos in self.Dic_cliente.items():
                archivo.write(
                    f"{nit_cliente}:{datos['Nombre']}:{datos['direccion']}:"
                    f"{datos['Telefono']}:{datos['correo']}\n"
                )

class Ing_cliente:
    def __init__(self, cliente_manager):
        self.cliente_manager = cliente_manager

    def ingrese_cliente(self, nit_cliente, nombre, direccion, telefono, correo):
        if nit_cliente in self.cliente_manager.Dic_cliente:
            print(" cliente ya existe en sistema.")
        else:
            self.cliente_manager.Dic_cliente[nit_cliente] = {
                "Nombre": nombre,
                "direccion": direccion,
                "telefono": telefono,
                "correo": correo
            }
            self.cliente_manager.guardar_clienter()
            print(f" Nit cliente  {nit_cliente} agregado y guardado.")

class Mostrar_cliente:
    def __init__(self, cliente_manager):
        self.cliente_manager = cliente_manager

    def mostrar_todos(self):
        if not self.cliente_manager.Dic_cliente:
            print(" No hay cliente registrados.")
        else:
            print("\n cliente registrados:")
            for nit_cliente, datos in self.cliente_manager.Dic_cliente.items():
                print(
                    f"ID: {nit_cliente} | Nombre: {datos['Nombre']} | "
                    f"direccion: {datos['direccion']} | telefono: {datos['telefono']} | "
                    f"correo: {datos['correo']} "
                )
class Eliminar_cliente:
    def __init__(self, cliente_manager):
        self.cliente_manager = cliente_manager

    def eliminar(self, nit_cliente):
        if nit_cliente in self.cliente_manager.Dic_cliente:
            eliminado = self.cliente_manager.Dic_cliente.pop(nit_cliente)
            self.cliente_manager.guardar_cliente()
            print(f" cliente eliminado: {eliminado['Nombre']}")
        else:
            print(" El cliente no existe.")


class Buscar_cliente:
    def __init__(self, cliente_manager):
        self.cliente_manager = cliente_manager

    def buscar(self, nit_cliente):
        if nit_cliente in self.cliente_manager.Dic_cliente:
            datos = self.cliente_manager.Dic_proveedor[nit_cliente]
            print(
                f"nit: {nit_cliente} | Nombre: {datos['Nombre']} | "
                f"direccion: {datos['direccion']} | telefono: {datos['telefono']} | "
                f"correo: {datos['correo']}"
            )
        else:
            print(" cliente no existe.")

class venta_principal:
    def __init__(self):
        self.Dic_venta = {}
        self.cargar_venta()

    def cargar_venta(self):

        try:
            with open("venta.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_venta, fecha,id_empleado,nit_cliente,total,= linea.split(":")
                        self.Dic_venta[int(id_venta)] = {
                            "id venta": id_venta,
                            "fecha": fecha,
                            "Id empleado": int(id_empleado),
                            "Nit cliente": int(nit_cliente),
                            "total": int(total)
                        }
            print("venta cargada desde venta.txt")
        except FileNotFoundError:
            print(" No existe venta.txt, se creará al guardar.")

    def guardar_venta(self):

        with open("venta.txt", "w", encoding="utf-8") as archivo:
            for id_venta, datos in self.Dic_venta.items():
                archivo.write(
                    f"{id_venta}:{datos['fecha']}:{datos['id_empleado']}:"
                    f"{datos['nit_cliente']}:{datos['total']}\n"
                )

class Ing_venta:
    def __init__(self, venta_manager):
        self.venta_manager = venta_manager

    def ingrese_venta(self, id_venta, fecha, id_empleado, nit_cliente,total):
        if id_venta in self.venta_manager.Dic_venta:
            print(" cliente ya existe en sistema.")
        else:
            self.venta_manager.Dic_venta[id_venta] = {
                "fecha": fecha,
                "id empleado": id_empleado,
                "nit cliente": nit_cliente,
                "total": total
            }
            self.venta_manager.guardar_venta()
            print(f" Id venta  {id_venta} agregado y guardado.")

class Mostrar_venta:
    def __init__(self, venta_manager):
        self.venta_manager = venta_manager

    def mostrar_todos(self):
        if not self.venta_manager.Dic_venta:
            print(" No hay venta registrada.")
        else:
            print("\n venta registrados:")
            for id_venta, datos in self.venta_manager.Dic_venta.items():
                print(
                    f"ID: {id_venta} | fecha: {datos['fecha']} | "
                    f"id empleado: {datos['id_empleado']} | nit cliente: {datos['nit_cliente']} | "
                    f"total: {datos['total']} "
                )
class Eliminar_venta:
    def __init__(self, venta_manager):
        self.venta_manager = venta_manager

    def eliminar(self, id_venta):
        if id_venta in self.venta_manager.Dic_venta:
            eliminado = self.venta_manager.Dic_venta.pop(id_venta)
            self.venta_manager.guardar_cliente()
            print(f" venta eliminado: {eliminado['id_venta']}")
        else:
            print(" la venta no existe.")


class Buscar_venta:
    def __init__(self, venta_manager):
        self.venta_manager = venta_manager

    def buscar(self, id_venta):
        if id_venta in self.venta_manager.Dic_venta:
            datos = self.venta_manager.Dic_venta[id_venta]
            print(
                f"id venta: {id_venta} | fecha: {datos['fecha']} | "
                f"id empleado: {datos['id_empleado']} | nit cliente: {datos['nit_cliente']} | "
                f"total: {datos['total']}"
            )
        else:
            print(" venta no existe.")


class detalleventa_principal:
    def __init__(self):
        self.Dic_detalleventa = {}
        self.cargar_detalleventa()

    def cargar_detalleventa(self):

        try:
            with open("detalleventa.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_detalleventa, idventa,cantidad,id_producto,subtotal,stock,= linea.split(":")
                        self.Dic_detalleventa[int(id_detalleventa)] = {
                            "id venta": idventa,
                            "cantidad": cantidad,
                            "id producto": id_producto,
                            "subtotal": int(subtotal),
                            "stock": int(stock),

                        }
            print("detalle venta cargada desde detalleventa.txt")
        except FileNotFoundError:
            print(" No existe detalleventa.txt, se creará al guardar.")

    def guardar_detalleventa(self):

        with open("detalleventa.txt", "w", encoding="utf-8") as archivo:
            for id_detalleventa, datos in self.Dic_detalleventa.items():
                archivo.write(
                    f"{id_detalleventa}:{datos['idventa']}:{datos['cantidad']}:"
                    f"{datos['id producto']}:{datos['subtotal']}:{datos['stock']}\n"
                )

class Ing_detalleventa:
    def __init__(self, detalleventa_manager):
        self.detalleventa_manager = detalleventa_manager

    def ingresar(self, id_detalleventa, idventa, cantidad, id_producto, subtotal, stock):
        if id_detalleventa in self.detalleventa_manager.Dic_detalleventa:
            print("El detalle de venta ya existe en el sistema.")
        else:
            self.detalleventa_manager.Dic_detalleventa[id_detalleventa] = {
                "id venta": idventa,
                "cantidad": cantidad,
                "id producto": id_producto,
                "subtotal": subtotal,
                "stock": stock,
            }
            self.detalleventa_manager.guardar_detalleventa()
            print(f" Detalle de venta {id_detalleventa} agregado y guardado.")


class Mostrar_detalleventa:
    def __init__(self, detalleventa_manager):
        self.detalleventa_manager = detalleventa_manager

    def mostrar_todos(self):
        if not self.detalleventa_manager.Dic_detalleventa:
            print(" No hay detalles de venta registrados.")
        else:
            print("\n Detalles de venta registrados:")
            for id_detalleventa, datos in self.detalleventa_manager.Dic_detalleventa.items():
                print(
                    f"ID Detalle: {id_detalleventa} | ID Venta: {datos['id venta']} | "
                    f"Cantidad: {datos['cantidad']} | Producto: {datos['id producto']} | "
                    f"Subtotal: {datos['subtotal']} | Stock: {datos['stock']}")

class Eliminar_detalleventa:
    def __init__(self, detalleventa_manager):
        self.detalleventa_manager = detalleventa_manager

    def eliminar(self, id_detalleventa):
        if id_detalleventa in self.detalleventa_manager.Dic_detalleventa:
            eliminado = self.detalleventa_manager.Dic_detalleventa.pop(id_detalleventa)
            self.detalleventa_manager.guardar_detalleventa()
            print(f" Detalle de venta eliminado: {id_detalleventa} (Producto {eliminado['id producto']})")
        else:
            print(" El detalle de venta no existe.")


class Buscar_detalleventa:
    def __init__(self, detalleventa_manager):
        self.detalleventa_manager = detalleventa_manager

    def buscar(self, id_detalleventa):
        if id_detalleventa in self.detalleventa_manager.Dic_detalleventa:
            datos = self.detalleventa_manager.Dic_detalleventa[id_detalleventa]
            print(
                f" ID Detalle: {id_detalleventa} | ID Venta: {datos['id venta']} | "
                f"Cantidad: {datos['cantidad']} | Producto: {datos['id producto']} | "
                f"Subtotal: {datos['subtotal']} | Stock: {datos['stock']}"
            )
        else:
            print(" El detalle de venta no existe.")


class Compra_principal:
    def __init__(self):
        self.Dic_compra = {}
        self.cargar_compra()

    def cargar_compra(self):

        try:
            with open("compra.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_compra, fecha_ingreso,id_empleado,nit_proveedor,total,= linea.split(":")
                        self.Dic_compra[int(id_compra)] = {
                            "Fecha de ingreso": fecha_ingreso,
                            "id empleado": id_empleado,
                            "nit proveedor": nit_proveedor,
                            "total": int(total),

                        }
            print("compra cargada desde compra.txt")
        except FileNotFoundError:
            print(" No existe compra.txt, se creará al guardar.")

    def guardar_compra(self):

        with open("compra.txt", "w", encoding="utf-8") as archivo:
            for id_compra, datos in self.Dic_compra.items():
                archivo.write(
                    f"{id_compra}:{datos['fecha_ingreso']}:{datos['id empleado']}:"
                    f"{datos['nit']}:{datos['total']}\n"
                )

class Ing_compra:
    def __init__(self, compra_manager):
        self.compra_manager = compra_manager

    def ingresar(self, id_compra, fecha_ingreso, id_empleado, nit, total):
        if id_compra in self.compra_manager.Dic_compra:
            print("compra ya existe en el sistema.")
        else:
            self.compra_manager.Dic_compra[id_compra] = {
                "fecha de ingreso": fecha_ingreso,
                "id empleado": id_empleado,
                "nit proveedor": nit,
                "total": total,
            }
            self.compra_manager.guardar_compra()
            print(f" compra {id_compra} agregado y guardado.")


class Mostrar_compra:
    def __init__(self, compra_manager):
        self.compra_manager = compra_manager

    def mostrar_todos(self):
        if not self.compra_manager.Dic_compra:
            print(" No hay compra registradas.")
        else:
            print("\n compras registrados:")
            for id_compra, datos in self.compra_manager.Dic_compra.items():
                print(
                    f"ID compra: {id_compra} | fecha de ingreso : {datos['fecha_ingreso']} | "
                    f"id empleado: {datos['id_empleado']} | nit: {datos['nit']} | "
                    f"total: {datos['total']} ")

class Eliminar_compra:
    def __init__(self, compra_manager):
        self.compra_manager = compra_manager

    def eliminar(self, id_compra):
        if id_compra in self.compra_manager.Dic_compra:
            eliminado = self.compra_manager.Dic_compra.pop(id_compra)
            self.compra_manager.guardar_compra()
            print(f" Detalle de venta eliminado: {id_compra} (Producto {eliminado['id_compra']})")
        else:
            print(" compra no existe.")


class Buscar_compra:
    def __init__(self, compra_manager):
        self.compra_manager = compra_manager

    def buscar(self, id_compra):
        if id_compra in self.compra_manager.Dic_compra:
            datos = self.compra_manager.Dic_compra[id_compra]
            print(
                f" ID compra: {id_compra} | fecha ingreso: {datos['fecha_ingreso']} | "
                f"Id empleado: {datos['id_empleado']} | nit: {datos['nit']} | "
                f"total: {datos['total']} " )
        else:
            print(" compra no existe.")


class empleado_principal:
    def __init__(self):
        self.Dic_empleado = {}
        self.cargar_empleado()

    def cargar_empleado(self):

        try:
            with open("empleado.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        carnet, nombre,direccion,telefono,correo,= linea.split(":")
                        self.Dic_empleado[int(carnet)] = {
                            "Nombre": nombre,
                            "direccion": (direccion),
                            "telefono": int(telefono),
                            "correo": (correo)
                        }
            print("empleado cargados desde empleado.txt")
        except FileNotFoundError:
            print(" No existe empleado.txt, se creará al guardar.")

    def guardar_empleado(self):

        with open("empleado.txt", "w", encoding="utf-8") as archivo:
            for carnet, datos in self.Dic_empleado.items():
                archivo.write(
                    f"{carnet}:{datos['Nombre']}:{datos['direccion']}:"
                    f"{datos['Telefono']}:{datos['correo']}\n"
                )

class Ing_empleado:
    def __init__(self, empleado_manager):
        self.empleado_manager = empleado_manager

    def ingrese_empleado(self, carnet, nombre, direccion, telefono, correo):
        if carnet in self.empleado_manager.Dic_empleado:
            print(" empleado ya existe en sistema.")
        else:
            self.empleado_manager.Dic_empleado[carnet] = {
                "Nombre": nombre,
                "direccion": direccion,
                "telefono": telefono,
                "correo": correo
            }
            self.empleado_manager.guardar_empleado()
            print(f" carnet empleado  {carnet} agregado y guardado.")

class Mostrar_empleado:
    def __init__(self, empleado_manager):
        self.empleado_manager = empleado_manager

    def mostrar_todos(self):
        if not self.empleado_manager.Dic_empleado:
            print(" No hay empleado registrados.")
        else:
            print("\n empleado registrados:")
            for carnet, datos in self.empleado_manager.Dic_empleado.items():
                print(
                    f"ID: {carnet} | Nombre: {datos['Nombre']} | "
                    f"direccion: {datos['direccion']} | telefono: {datos['telefono']} | "
                    f"correo: {datos['correo']} "
                )
class Eliminar_empleado:
    def __init__(self, empleado_manager):
        self.empleado_manager = empleado_manager

    def eliminar(self, carnet):
        if carnet in self.empleado_manager.Dic_empleado:
            eliminado = self.empleado_manager.Dic_empleado.pop(carnet)
            self.empleado_manager.guardar_empleado()
            print(f" empleado eliminado: {eliminado['Nombre']}")
        else:
            print(" empleado no existe.")


class Buscar_empleado:
    def __init__(self, empleado_manager):
        self.empleado_manager = empleado_manager

    def buscar(self, carnet):
        if carnet in self.empleado_manager.Dic_empleado:
            datos = self.empleado_manager.Dic_empleado[carnet]
            print(
                f"nit: {carnet} | Nombre: {datos['Nombre']} | "
                f"direccion: {datos['direccion']} | telefono: {datos['telefono']} | "
                f"correo: {datos['correo']}"
            )
        else:
            print(" empleado no existe.")





class Compradetalle_principal:
    def __init__(self):
        self.Dic_compradetalle = {}
        self.cargar_compradetalle()

    def cargar_compradetalle(self):

        try:
            with open("compradetalle.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_decompra, id_venta,cantidad,id_producto,subtotal,fecha_caducidad,= linea.split(":")
                        self.Dic_compradetalle[int(id_decompra)] = {
                            "Id de venta": id_venta,
                            "cantidad": cantidad,
                            "id_producto": id_producto,
                            "subtotal": int(subtotal),
                            "fecha de caducidad":fecha_caducidad

                        }
            print("detallecompra cargada desde detallecompra.txt")
        except FileNotFoundError:
            print(" No existe detallecompra.txt, se creará al guardar.")

    def guardar_detallecompra(self):

        with open("detallecompra.txt", "w", encoding="utf-8") as archivo:
            for id_decompra, datos in self.Dic_compradetalle.items():
                archivo.write(
                    f"{id_decompra}:{datos['id_venta']}:{datos['cantidad']}:"
                    f"{datos['id_producto']}:{datos['subtotal']}:{datos['fecha_caducidad']}\n"
                )

class Ing_detallecompra:
    def __init__(self, detallecompra_manager):
        self.detallecompra_manager = detallecompra_manager

    def ingresar(self, id_decompra, idventa, cantidad, idproducto, subtotal,fecha_caducidad):
        if id_decompra in self.detallecompra_manager.Dic_compradetalle:
            print("compra ya existe en el sistema.")
        else:
            self.detallecompra_manager.Dic_compradetalle[id_decompra] = {
                "Id de venta": idventa,
                "cantidad": cantidad,
                "id_producto": idproducto,
                "subtotal": int(subtotal),
                "fecha de caducidad": fecha_caducidad
            }
            self.detallecompra_manager.guardar_compradetalle()
            print(f" compra {id_decompra} agregado y guardado.")


class Mostrar_compradetallle:
    def __init__(self, compradetalle_manager):
        self.compradetalle_manager = compradetalle_manager

    def mostrar_todos(self):
        if not self.compradetalle_manager.Dic_compradetalle:
            print(" No hay compra registradas.")
        else:
            print("\n compras registrados:")
            for id_decompra, datos in self.compradetalle_manager.Dic_compradetalle.items():
                print(
                    f"{id_decompra}:{datos['id_venta']}:{datos['cantidad']}:"
                    f"{datos['id_producto']}:{datos['subtotal']}:{datos['fecha_caducidad']}\n")

class Eliminar_compradetalle:
    def __init__(self, compradetalle_manager):
        self.compradetalle_manager = compradetalle_manager

    def eliminar(self, id_decompra):
        if id_decompra in self.compradetalle_manager.Dic_compradetalle:
            eliminado = self.compradetalle_manager.Dic_compradetalle.pop(id_decompra)
            self.compradetalle_manager.guardar_compradetalle()
            print(f" Detalle de venta eliminado: {id_decompra} (Producto {eliminado['id_decompra']})")
        else:
            print(" compra no existe.")


class Buscar_compradetalle:
    def __init__(self, compradetalle_manager):
        self.compradetalle_manager = compradetalle_manager

    def buscar(self, id_decompra):
        if id_decompra in self.compradetalle_manager.Dic_compradetalle:
            datos = self.compradetalle_manager.Dic_compradetalle[id_decompra]
            print(
                f"{id_decompra}:{datos['id_venta']}:{datos['cantidad']}:"
                f"{datos['id_producto']}:{datos['subtotal']}:{datos['fecha_caducidad']}\n")


        else:
            print(" compra no existe.")



class menus:
    def Menu_principal(self):
        print("==========MENU PRINCIPAL===========")
        print("1. Categoria ")
        print("2. productos")
        print("3. proveedor")
        print("4. cliente")
        print("5. ventas")
        print("6. detalle de ventas")
        print("7. compras")
        print("8. detalle de compra")
        print("9. empleado")
        print("10. salir")

    def Menu_categoria(self):
        print("=======CATEGORIA=======")
        print("1. ingrese categoria ")
        print("2. buscar categoria ")
        print("3. mostrar categoria")
        print("4. ordenar")
        print("5. eliminar categoria")
        print("6. salir")


    def menu_producto(self):
        print("=======MENU PRODUCTO=======")
        print("1. ingreso de producto ")
        print("2. buscar producto ")
        print("3. actualizar producto")
        print("4. mostrar producto")
        print("5. eliminar producto")
        print("6. salir")

    def menu_proveedor(self):
        print("=======MENU PROVEEDOR=======")
        print("1. ingreso de proveedor ")
        print("2. buscar ")
        print("3. mostrar")
        print("4. actualizar")
        print("5. eliminar ")
        print("6. salir")

    def menu_empleado(self):
        print("=======MENU EMPLEADO=======")
        print("1. ingreso de EMPLEADO ")
        print("2. buscar ")
        print("3. mostrar")
        print("4. actualizar")
        print("5. eliminar ")
        print("6. salir")

    def menu_cliente(self):
        print("=======MENU CLIENTE=======")
        print("1. ingreso de cliente ")
        print("2. buscar ")
        print("3. mostrar")
        print("4. actualizar")
        print("5. eliminar ")
        print("6. salir")

    def menu_venta(self):
        print("=======MENU VENTAS=======")
        print("1. ingrese venta ")
        print("2. buscar ")
        print("3. mostrar")
        print("4. actualizar")
        print("5. eliminar ")
        print("6. salir")


    def menu_detalleventa(self):
        print("=======MENU DETALLE VENTAS=======")
        print("1. ingrese venta ")
        print("2. buscar ")
        print("3. mostrar")
        print("4. actualizar")
        print("5. eliminar ")
        print("6. salir")


    def menu_compra(self):
        print("=======MENU COMPRAS=======")
        print("1. ingrese compra ")
        print("2. buscar ")
        print("3. mostrar")
        print("4. actualizar")
        print("5. eliminar ")
        print("6. salir")

    def menu_detallecompra(self):
        print("=======MENU  DETALLE COMPRAS=======")
        print("1. ingrese compra ")
        print("2. buscar ")
        print("3. mostrar")
        print("4. actualizar")
        print("5. eliminar ")
        print("6. salir")




def main():
    op=0


    menu=menus()

    while op!=10:
        menu.Menu_principal()

        try:
            op=int(input("ingrese una opcion a ejectura"))
            match op:
                case 1:
                    p=0

                    while p!=6:
                        menu.Menu_categoria()
                        categoria = Categoriaprincipal()
                        guardar = Categoria_guardar(categoria)
                        agregar = Categoria_agregar(categoria, guardar)
                        mostrar = Categoria_mostrar(categoria)
                        eliminar = Categoria_eliminar(categoria, guardar)
                        try:
                             p=int(input("ingrese una opcion a ejecturar"))
                             match p:
                                  case 1:
                                      categoria.cargar_categoria()
                                      try:
                                          id_cat = int(input("Ingrese ID de categoría: "))
                                          if id_cat not in categoria.Dic_categoria:
                                              nombre = input("Ingrese nombre de categoría: ")
                                              agregar.agregar_categoria(id_cat, nombre)
                                          else:
                                              print("La categoría ya existe")
                                      except ValueError:
                                           print("Ingrese un ID válido.")

                                  case 2:
                                         id_buscar = int(input("Ingrese ID de categoría a buscar: "))
                                         if id_buscar in categoria.Dic_categoria:
                                              print(f"Categoría encontrada: {categoria.Dic_categoria[id_buscar]['Nombre']}")
                                         else:
                                             print("Categoría no encontrada.")


                                  case 3:
                                      print("categorias ingresadas")
                                      print(mostrar.mostrar_categorias())
                                  case 4:
                                      pass
                                  case 5:
                                      try:
                                        id_del = int(input("Ingrese ID de categoría a eliminar: "))
                                        eliminar.eliminar_categoria(id_del)
                                      except ValueError:
                                          print("Ingrese un ID válido.")

                                  case 6:
                                      print("regresar a menu principal")
                                  case _:
                                      print("ingrese una opcion valida")

                        except ValueError:
                             print("ingrese un numero entero")

                case 2:
                    p = 0
                    productos = Producto()
                    ingreso = Ing_producto(productos)
                    mostrar_p = Mostrar_producto(productos)
                    eliminar_p = Eliminar_producto(productos)
                    buscar_p = Buscar_producto(productos)
                    categoria = Categoriaprincipal()
                    while p != 6:
                        menu.menu_producto()
                        try:

                            p = int(input("ingrese una opcion a ejecturar"))
                            match p:
                                case 1:
                                    productos.cargar_producto()
                                    try:
                                        id_producto = int(input("Ingrese ID de producto: "))
                                        if id_producto not in productos.Dic_producto:
                                            nombre = input("Ingrese nombre de producto: ")
                                            id_categoria = int(input("Ingrese Id de categoría: "))

                                            if id_categoria not in categoria.Dic_categoria:
                                                print(" La categoría no existe, regístrela primero.")
                                            else:
                                                total_compra = int(input("Ingrese precio de compra: "))
                                                total_venta = int(input("Ingrese precio de venta: "))
                                                stock = int(input("Ingrese stock: "))

                                                ingreso.ingreso_producto( id_producto, nombre, id_categoria,
                                                total_compra, total_venta, stock)
                                        else:
                                            print(" El producto ya existe en el sistema.")
                                    except ValueError:
                                        print(" Ingrese datos válidos.")

                                case 2:
                                    try:
                                       id_buscar = int(input("Ingrese ID de producto a buscar: "))
                                       buscar_p.buscar(id_buscar)
                                    except ValueError:
                                         print(" Ingrese un ID válido.")
                                case 3:
                                    print("Función actualizar producto pendiente.")
                                case 4:
                                         print( mostrar_p.mostrar_todos())

                                case 5:
                                    try:
                                      id_del = int(input("Ingrese ID de producto a eliminar: "))
                                      eliminar_p.eliminar(id_del)
                                    except ValueError:
                                      print("Ingrese un ID válido.")

                                case 6:
                                    print("regresar a menu principal")
                                case _:
                                    print("ingrese una opcion valida")

                        except ValueError:
                             print("ingrese un numero entero")

                case 3:
                    p = 0
                    while p != 6:
                        menu.menu_proveedor()
                        pro = proveedor_principal()
                        ingreso_prov = Ing_proveedor(pro)
                        mostrar_prov = Mostrar_proveedor(pro)
                        eliminar_prov = Eliminar_proveedor(pro)
                        buscar_prov = Buscar_preveedor(pro)

                        try:
                            p = int(input("ingrese una opcion a ejecturar"))
                            match p:
                                case 1:
                                     pro.cargar_proveedor()
                                     try:
                                         nit = int(input("Ingrese NIT del proveedor: "))
                                         if nit not in pro.Dic_proveedor:
                                             nombre = input("Ingrese nombre del proveedor: ")
                                             direccion = input("Ingrese dirección: ")
                                             telefono = int(input("Ingrese teléfono: "))
                                             correo = input("Ingrese correo: ")
                                             empresa = input("Ingrese empresa: ")

                                             ingreso_prov.ingrese_proveedor(nit, nombre, direccion, telefono, correo,
                                                                            empresa)
                                         else:
                                             print("El proveedor ya existe en el sistema.")
                                     except ValueError:
                                         print("Ingrese datos válidos.")

                                case 2:
                                     try:
                                        nit_buscar = int(input("Ingrese NIT del proveedor a buscar: "))
                                        buscar_prov.buscar(nit_buscar)
                                     except ValueError:
                                          print("Ingrese un NIT válido.")
                                case 3:
                                     mostrar_prov.mostrar_todos()
                                case 4:
                                    pass
                                case 5:
                                      try:
                                         nit_pro = int(input("Ingrese NIT del proveedor a eliminar: "))
                                         eliminar_prov.eliminar(nit_pro)
                                      except ValueError:
                                          print("Ingrese un NIT válido.")

                                case 6:
                                   print("regresar a menu principal")
                                case _:
                                  print("ingrese una opcion valida")

                        except ValueError:
                             print("ingrese un numero entero")
                case 4:
                    p=0
                    clie= cliente_principal()
                    ingreso_clie = Ing_cliente(clie)
                    mostrar_clie = Mostrar_cliente(clie)
                    eliminar_clie = Eliminar_cliente(clie)
                    buscar_clie = Buscar_cliente(clie)

                    while p != 6:
                        menu.menu_cliente()
                        try:
                            p = int(input("ingrese una opcion a ejecturar"))
                            match p:
                                case 1:
                                     clie.cargar_cliente()
                                     try:
                                       nit = int(input("Ingrese NIT del cliente: "))
                                       if nit not in clie.Dic_cliente:
                                          nombre = input("Ingrese nombre del proveedor: ")
                                          direccion = input("Ingrese dirección: ")
                                          telefono = int(input("Ingrese teléfono: "))
                                          correo = input("Ingrese correo: ")
                                          ingreso_clie.ingrese_cliente(nit, nombre, direccion, telefono, correo,)
                                       else:
                                           print("El cliente ya existe en el sistema.")
                                     except ValueError:
                                           print("Ingrese datos válidos.")


                                case 2:
                                    try:
                                        nit=int(input("ingrese nit de cliente a buscar "))
                                        if nit not in clie.Dic_cliente:
                                            print("cliente no aparece en sistema ")

                                        else:
                                            buscar_clie.buscar(nit)
                                    except ValueError:
                                        print("Ingrese un NIT válido.")



                                case 3:
                                    mostrar_clie.mostrar_todos()
                                case 4:
                                    pass
                                case 5:
                                      try:
                                          nit = int(input("ingrese nit de cliente a eliminar "))
                                          if nit not in clie.Dic_cliente:
                                             print("cliente no aparece en sistema ")

                                          else:
                                              eliminar_clie.eliminar(nit)

                                      except ValueError:
                                         print("Ingrese un NIT válido.")

                                case 6:
                                   print("regresar a menu principal")
                                case _:
                                  print("ingrese una opcion valida")

                        except ValueError:
                             print("ingrese un numero entero")

                case 5:
                    p = 0
                    venta = venta_principal()
                    ingreso_venta = Ing_venta(venta)
                    mostrar_venta = Mostrar_venta(venta)
                    eliminar_venta = Eliminar_venta(venta)
                    buscar_venta = Buscar_venta(venta)

                    while p != 6:
                        menu.menu_venta()
                        try:
                            p = int(input("Ingrese una opción a ejecutar: "))
                            match p:
                                case 1:
                                    venta.cargar_venta()
                                    try:
                                        id_venta = int(input("Ingrese ID de venta: "))
                                        if id_venta not in venta.Dic_venta:
                                            fecha = input("Ingrese fecha de la venta: ")
                                            id_empleado = int(input("Ingrese ID del empleado: "))
                                            nit_cliente = int(input("Ingrese NIT del cliente: "))
                                            total = int(input("Ingrese total de la venta: "))

                                            ingreso_venta.ingrese_venta(id_venta, fecha, id_empleado, nit_cliente,
                                                                        total)
                                        else:
                                            print("La venta ya existe en el sistema.")
                                    except ValueError:
                                        print("Ingrese datos válidos.")

                                case 2:
                                    try:
                                        id_buscar = int(input("Ingrese ID de venta a buscar: "))
                                        buscar_venta.buscar(id_buscar)
                                    except ValueError:
                                        print("Ingrese un ID válido.")

                                case 3:
                                    mostrar_venta.mostrar_todos()

                                case 4:
                                    print("Función actualizar venta pendiente.")

                                case 5:
                                    try:
                                        id_del = int(input("Ingrese ID de venta a eliminar: "))
                                        eliminar_venta.eliminar(id_del)
                                    except ValueError:
                                        print("Ingrese un ID válido.")

                                case 6:
                                    print("Regresando al menú principal...")
                                case _:
                                    print("Ingrese una opción válida.")
                        except ValueError:
                            print("Ingrese un número entero válido.")
                case 6:

                    p = 0
                    deventa = detalleventa_principal()
                    ingreso_deventa = Ing_detalleventa(deventa)
                    mostrar_deventa = Mostrar_detalleventa(deventa)
                    eliminar_deventa = Eliminar_detalleventa(deventa)
                    buscar_deventa = Buscar_detalleventa(deventa)

                    while p != 6:
                        menu.menu_detalleventa()
                        try:
                            p = int(input("Ingrese una opción a ejecutar: "))
                            match p:
                                case 1:
                                    deventa.cargar_detalleventa()
                                    try:
                                        id_detalle = int(input("Ingrese ID del detalle de venta: "))
                                        if id_detalle not in deventa.Dic_detalleventa:
                                            id_venta = int(input("Ingrese ID de la venta: "))
                                            id_producto = int(input("Ingrese ID del producto: "))
                                            cantidad = int(input("Ingrese cantidad: "))
                                            precio_unitario = float(input("Ingrese precio unitario: "))
                                            subtotal = cantidad * precio_unitario

                                            ingreso_deventa.ingresar( id_detalle, id_venta, id_producto, cantidad, precio_unitario, subtotal)
                                        else:
                                            print(" El detalle de venta ya existe en el sistema.")
                                    except ValueError:
                                        print(" Ingrese datos válidos.")

                                case 2:
                                    try:
                                        id_buscar = int(input("Ingrese ID de detalle venta a buscar: "))
                                        buscar_deventa.buscar(id_buscar)
                                    except ValueError:
                                        print("Ingrese un ID válido.")

                                case 3:
                                    mostrar_deventa.mostrar_todos()

                                case 4:
                                    print("Función actualizar detalle pendiente.")

                                case 5:
                                    try:
                                        id_del = int(input("Ingrese ID de detalle venta a eliminar: "))
                                        eliminar_deventa.eliminar(id_del)
                                    except ValueError:
                                        print("Ingrese un ID válido.")

                                case 6:
                                    print(" Regresando al menú principal...")
                                case _:
                                    print(" Ingrese una opción válida.")
                        except ValueError:
                            print("Ingrese un número entero válido.")


                case 7:
                    p = 0
                    import random
                    compra=Compra_principal ()
                    ingreso_compra = Ing_compra(compra)
                    mostrar_compra = Mostrar_compra(compra)
                    eliminar_compra = Eliminar_compra(compra)
                    buscar_compra = Buscar_compra(compra)
                    empleado= empleado_principal()
                    pro = proveedor_principal()

                    while p != 6:
                        menu.menu_compra()
                        try:
                            p = int(input("Ingrese una opción a ejecutar: "))
                            match p:
                                case 1:
                                    compra.cargar_compra()
                                    try:
                                        id_compra = random.randint (1,1000)
                                        fecha=input("ingrese fecha de ingreso")
                                        idempleado=int(input("ingrese Id de empleado"))
                                        if idempleado not in empleado.Dic_empleado:
                                            print("no tiene registrado empleados registre primero a empleado")
                                        else:
                                            nit=int(input("ingrese nit de proveedor"))
                                            if nit not in pro.Dic_proveedor:
                                                print("no tines proveedor registrado")
                                            else:
                                                total=int(input("ingrse total de compra"))
                                                print("compra registrado con exito")
                                                ingreso_compra.ingresar(id_compra, fecha, idempleado,nit, total)

                                    except ValueError:
                                        print(" Ingrese datos válidos.")

                                case 2:
                                    try:
                                        id_buscar = int(input("Ingrese ID de compra a buscar: "))
                                        buscar_compra.buscar(id_buscar)
                                    except ValueError:
                                        print("Ingrese un ID válido.")

                                case 3:
                                    mostrar_compra.mostrar_todos()

                                case 4:
                                    print(" Función actualizar compra pendiente.")

                                case 5:
                                    try:
                                        id_del = int(input("Ingrese ID de compra a eliminar: "))
                                        eliminar_compra.eliminar(id_del)
                                    except ValueError:
                                        print(" Ingrese un ID válido.")

                                case 6:
                                    print(" Regresando al menú principal...")
                                case _:
                                    print(" Ingrese una opción válida.")
                        except ValueError:
                            print("Ingrese un número entero válido.")


                case 8:
                    pass
                case 9:

                    p=0
                    empleado= empleado_principal()
                    ingreso_empleado = Ing_empleado(empleado)
                    mostrar_empleado = Mostrar_empleado(empleado)
                    eliminar_empleado = Eliminar_empleado(empleado)
                    buscar_empleado = Buscar_empleado(empleado)

                    while p != 6:
                        menu.menu_empleado()
                        try:
                            p = int(input("ingrese una opcion a ejecturar"))
                            match p:
                                case 1:
                                     empleado.cargar_empleado()
                                     try:
                                       carnet = int(input("Ingrese carnet del empleado: "))
                                       if carnet not in empleado.Dic_empleado:
                                          nombre = input("Ingrese nombre : ")
                                          direccion = input("Ingrese dirección: ")
                                          telefono = int(input("Ingrese teléfono: "))
                                          correo = input("Ingrese correo: ")
                                          ingreso_empleado.ingrese_empleado(carnet, nombre, direccion, telefono, correo,)
                                       else:
                                           print("El empleado ya existe en el sistema.")
                                     except ValueError:
                                           print("Ingrese datos válidos.")


                                case 2:
                                    try:
                                        carnet=int(input("ingrese carnet  a buscar "))
                                        if carnet not in empleado.Dic_empleado:
                                            print("empleado no aparece en sistema ")

                                        else:
                                            buscar_empleado.buscar(carnet)
                                    except ValueError:
                                        print("Ingrese un carnet válido.")



                                case 3:
                                    mostrar_empleado.mostrar_todos()
                                case 4:
                                    pass
                                case 5:
                                      try:
                                          carnet = int(input("ingrese carnet de empleadoa eliminar "))
                                          if carnet not in empleado.Dic_empleado:
                                             print("empleado no aparece en sistema ")

                                          else:
                                              eliminar_empleado.eliminar(carnet)

                                      except ValueError:
                                         print("Ingrese un carnet válido.")

                                case 6:
                                   print("regresar a menu principal")
                                case _:
                                  print("ingrese una opcion valida")

                        except ValueError:
                             print("ingrese un numero entero")


                case 10:
                    print("salir del programa ")
                case _:
                    print("ingrese una opcion valida")

        except ValueError:
            print("ingrese un numero entero")

main()