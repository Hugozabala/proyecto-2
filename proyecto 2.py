
Dic_compras ={}
Dic_detalleventas={}
Dic_detallecompra={}
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
        if id_venta in self.cliente_manager.Dic_cliente:
            datos = self.venta_manager.Dic_venta[id_venta]
            print(
                f"id venta: {id_venta} | fecha: {datos['fecha']} | "
                f"id empleado: {datos['id_empleado']} | nit cliente: {datos['nit_cliente']} | "
                f"total: {datos['total']}"
            )
        else:
            print(" venta no existe.")



class detalle_ventas:
    def __init__(self,idv_detalles,idventas,idproducto,cantidad,subtotal,stock):
        self.idv_detalles=idv_detalles
        self.idventas=idventas
        self.idproducto=idproducto
        self.cantidad=cantidad
        self.subtotal=subtotal
        self.stock=stock

    def mostrar(self):
        print(f"\n Id detalle deventa: {self.idv_detalles}- Id venta: {self.idventas}- Id producto: {self.idproducto}- Cantidad: {self.cantidad}- subtotal: {self.subtotal}- Stock: {self.stock}")

class deta_ventas:
    def ventas_detalle(self):
        import random
        idv_detalle=random.randint(1 ,1000)
        try:
            idventa=int(input("ingrese Id de venta"))
            if idventa not in Dic_ventas:
                print("ID no aparece ingrese venta primero")
            else:
                Idproducto=int(input("ingrese Id de producto"))
                cantidad=int(input("ingrese cantidad de producto"))
                subtotal=cantidad
                stock1=0
                vetna=detalle_ventas(idv_detalle,idventa,Idproducto,cantidad,subtotal,stock1)
                Dic_detalleventas[idventa]=vetna


        except ValueError:
            print("ingrese un dato valido")

class compra:
    def __init__(self,idcompra,fecha_ingreso,id_empleado,nit_vededor,total):
        self.idcompra=idcompra
        self.fecha_ingreso=fecha_ingreso
        self.id_empleado=id_empleado
        self.nit_vendedor=nit_vededor
        self.total=total

    def mostrar_compra(self):
        print(f"\n Id compra: {self.idcompra}- Fecha de ingreso: {self.fecha_ingreso}- Id empleado: {self.id_empleado}- Nit vendedor: {self.nit_vendedor}- Total de compra:{self.total}")

class compra_ingreso:
    def compra(self):
        import random
        import datetime
        idcompra=random.randint(1,1000)
        fecha_ingresso=datetime.date.today()
        try:
            id_emp=int(input("ingrese Id de empleado"))
            if id_emp not in Dic_empleado:
                print("empleado no aparece en sistema necesitas registrar antes")

            else:
                nit_vendendor=int(input("Ingrese nit de proveedor "))
                if nit_vendendor not in Dic_proveedor:
                    print("no existe proveedor en sistema registre primero ")
                else:
                    total=0
                    compra1=compra(idcompra,fecha_ingresso,id_emp,nit_vendendor,total)
                    Dic_compras[idcompra]=compra1

        except ValueError:
            print("ingrse  una opcion valida")

class detalle_compra:
    def __init__(self,id_det_compra,id_venta,cantidad,idproducto,subtotal,fecha_caducidad):
        self.id_det_compra=id_det_compra
        self.id_venta=id_venta
        self.cantidad=cantidad
        self.idproducto=idproducto
        self.subtotal=subtotal
        self.fecha_caducidad=fecha_caducidad

    def mostar_det_compra(self):
        print(f"\n Id de compra {self.id_det_compra}- Id venta: {self.id_venta}- Cantidad: {self.cantidad}- Id producto: {self.idproducto}- Subtotal: {self.subtotal}- Fecha de Caducidad: {self.fecha_caducidad}  ")

class ver_detalle_compras:
    def ver_compra_detallle(self):
        import random
        Id_det_compra=random.randint (1,1000)
        try:
            idventa=int(input("ingrese Id de venta "))
            if idventa not in Dic_ventas:
                print("no aparece registrado el Id de venta verifique la informacion")

            else:
                cantidad=int(input("ingrese cantidad de producto "))
                idproducto=int(input("ingrese Id de producto"))
                if idproducto not in Dic_producto:
                    print("Producto no esta en inventario")

                else:
                    subtotal=cantidad
                    fecha=input("ingrese decha de caducidad")
                    detallec=detalle_compra(Id_det_compra,idventa,cantidad,idproducto,subtotal,fecha)
                    Dic_detalleventas[Id_det_compra]=detallec


        except ValueError:
            print("ingrese un dato correcto")




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
        print("9. ")
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
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    pass
                case 9:
                    pass
                case 10:
                    pass
                case _:
                    print("ingrese una opcion valida")

        except ValueError:
            print("ingrese un numero entero")

main()