Dic_empleado={}
Dic_cliente={}
Dic_proveedor={}
Dic_compras ={}
Dic_ventas={}
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
    def guardar_categoria(self):

        with open("categoria.txt", "w", encoding="utf-8") as archivo:
            for Id_categoria, datos in self.Dic_categoria.items():
                archivo.write(f"{Id_categoria}:{datos['Nombre']}\n")

class Categoria_agregar:

    def agregar_categoria(self, Id_cate, nombre):

        if Id_cate in self.Dic_categoria:
            print("La categoría ya existe.")
        else:
            self.Dic_categoria[Id_cate] = {"Nombre": nombre}
            self.guardar_categoria()
            print(f"Categoría ID {Id_cate} agregada y guardada correctamente.")

class Catedoria_mostrar:
    def mostrar_categorias(self):

        if not self.Dic_categoria:
            print("No hay categorías registradas.")
        else:
            print("\nCategorías registradas:")
            for Id_categoria, datos in self.Dic_categoria.items():
                print(f"ID: {Id_categoria} - Nombre: {datos['Nombre']}")

class Categoria_eliminar:
    def eliminar_categoria(self, Id_cate):

        if Id_cate in self.Dic_categoria:
            eliminado = self.Dic_categoria.pop(Id_cate)
            self.guardar_categoria()
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

class empleado:
    def __init__(self,carnet,nombre_empleado,edad,direcion,telefono,correo,):
        self.carnet=carnet
        self.nombre_empleado=nombre_empleado
        self.edad=edad
        self.direccion=direcion
        self.telefono=telefono
        self.correo=correo

    def mostrar_Empleado(self):
        print(f"\n Numero de Carnet de trabajo:{self.carnet}-Nombre de empleado: {self.nombre_empleado,}-Edad: {self.edad}- direccion: {self.direccion}-Telefono: {self.telefono}-  Correo: {self.correo}")

class ingresar_empleado:
    def ingresa_emple(self):
        try:
            carnet=int(input("ingrese carnet de empleado"))
            if carnet not in Dic_empleado:
                nom=input("ingrese nombre")
                edad=int(input("ingrese edad"))
                dire=input("ingese direccion")
                tele=int(input("ingrese telefono: "))
                correo=input("ingrese correo")
                e=empleado(carnet,nom,edad,dire,tele,correo)
                Dic_empleado[carnet]=e
                print("empleado ingresdo con Exito")


            else:
                print("empleado ya existe en sistema ")

        except ValueError:
            print("ingrestes un dato no valido")
class buscar_empleado:
    def buscar_empleado(self):
        try:

            Id=int(input("Ingrese Id de empleado"))
            if Id not in Dic_empleado:
                print("el empleado no ha sido encontrado")
                return
            empleado=Dic_empleado[Id]
            print(f"empleado encontredo con exito")
            empleado.mostrar_Empleado()
        except ValueError:
            print("ingrese un dato correcto")

class mostrar_empleado:
    def mostrar_empleado(self):
        if not Dic_empleado:
            print("No hay empleado registrado")
        else:
            print("\n empleados registrados:")
            for emp in Dic_empleado.values():
                emp.mostrar_empleado()

class eliminar_empleado:
    def Eliminar_empleado(self):
        try:
            eliminar=int(input("ingrese ID de producto a eliminar"))
            if eliminar not in Dic_empleado:
                print("el producto que desea eliminar no existe en el inventario")
                return
            else:
                eliminar=Dic_empleado.pop(eliminar)
                print(f"producto eliminado {eliminar.nombre}")

        except ValueError:
             print("has ingresado un dato incorrecto")

class cliente:
    def __init__(self,nit,nombre_cliente,direcion,telefono,correo):
        self.nit=nit
        self.nombre_cliente=nombre_cliente
        self.direccion=direcion
        self.telefono=telefono
        self.correo=correo


    def mostrar_cliente(self):
        print(f"\n Numero de nit de cliente:{self.nit}-Nombre de cliente: {self.nombre_cliente,}-- direccion: {self.direccion}-Telefono: {self.telefono}- Correo: {self.correo}")
class ingresar_cliente:
    def ingresa_cliente(self):
        try:
            nit=int(input("ingrese nit de cliente"))
            if nit not in Dic_cliente:

                nom=input("ingrese nombre")
                dire=input("ingese direccion")
                tele=int(input("ingrese telefono: "))
                corr=input("ingrese correo")
                clie=cliente(nit,nom,dire,tele,corr)
                Dic_empleado[nit]=clie
                print("cliente ingresdo con Exito")
            else:
                print("cliente ya existe en sistema")

        except ValueError:
            print("ingrestes un dato no valido")

class mostrar_cliente:
    def mostrar_clie(self):
        if not Dic_cliente:
            print("No hay cliente registradas")
        else:
            print("\n clientes registrados:")
            for clie in categoria.Dic_categoria.values():
                clie.mostrar_cliente()

class eliminar_cliente:
    def eliminar_cliente(self):
        try:
            eliminar=int(input("ingrese nit  de cliente a eliminar"))
            if eliminar not in Dic_producto:
                print("el cliente que desa eliminar no existe")
                return
            else:
                eliminar=Dic_producto.pop(eliminar)
                print(f"producto eliminado {eliminar.nombre}")


        except ValueError:

            print("has ingresado un dato incorrecto")

class buscar_cliente:
    def buscar_cliente(self):
        try:

            nit=int(input("Ingrese nit de cliente"))
            if nit not in Dic_cliente:
                print(" cliente no ha sido encontrado")
                return
            cliente=Dic_empleado[nit]
            print(f"cliente encontredo con exito")
            cliente.mostrar_cliente()
        except ValueError:
            print("ingrese un dato correcto")

class Actualizar_pro:
    pass

class proeveedor:
    def __init__(self,nit,nombre_cliente,direcion,telefono,correo,empresa):
        self.nit=nit
        self.nombre_cliente=nombre_cliente
        self.direccion=direcion
        self.telefono=telefono
        self.correo=correo
        self.empresa=empresa


    def mostrar_proeveedor(self):
        print(f"\n Numero de nit de cliente:{self.nit}-Nombre de cliente: {self.nombre_cliente,}-- direccion: {self.direccion}-Telefono: {self.telefono}- Correo: {self.correo}- Empresa: {self.empresa}")
class ingre_proevedor:
    def ingresa_proeveedor(self):
        try:
            nit=int(input("ingrese nit de cliente"))
            if nit not in Dic_proveedor:

                nom=input("ingrese nombre")
                dire=input("ingese direccion")
                tele=int(input("ingrese telefono: "))
                corr=input("ingrese correo")
                emp=input("ingrese empresa o marca")
                vendedor=proeveedor(nit,nom,dire,tele,corr,emp)
                Dic_empleado[nit]=vendedor
                print("proveedor ingresdo con Exito")
            else:
                print("proveedor ya existe en sistema")

        except ValueError:
            print("ingrestes un dato no valido")

class mostrar_proveedor:
    def mostrar_prove(self):
        if not Dic_proveedor:
            print("No hay proveedor registrados")
        else:
            print("\n proveedor registrados:")
            for prov in Dic_proveedor.values():
                prov.mostrar_proveedor()

class eliminar_proveedor:
    def eliminar_prove(self):
        try:
            eliminar=int(input("ingrese nit  de proveedor a eliminar"))
            if eliminar not in Dic_proveedor:
                print("el proveedor que desa eliminar no existe")
                return
            else:
                eliminar=Dic_proveedor.pop(eliminar)
                print(f"proveedor eliminado {eliminar.nombre}")


        except ValueError:

            print("has ingresado un dato incorrecto")

class buscar_proveedor:
    def buscar_prove(self):
        try:

            nit=int(input("Ingrese nit de proveedor"))
            if nit not in Dic_proveedor:
                print(" proveedor no ha sido encontrado")
                return
            proveedor=Dic_proveedor[nit]
            print(f"proveedor encontredo con exito")
            proveedor.mostrar_proveedor()
        except ValueError:
            print("ingrese un dato correcto")

class actualizar_prov:
    pass

class ventas:
    def __init__(self,idventas,fecha,idempleado,nit_cliente,total):
        self.idventa=idventas
        self.fecha=fecha
        self.id_empleado=idempleado
        self.nit_cliente=nit_cliente
        self.total=total

    def mostrar(self):
        print(f"\n Id venta: {self.idventa}- fecha de venta: {self.fecha}- Id empleado: {self.id_empleado}- total: {self.total}")


class ingreso_ventas:
    def ingre_venta(self):
        import random
        import  datetime
        idventa= random.randint(1, 1000)
        fecha = datetime.date.today()
        try:
            idempleado=int(input("ingrse ID empleado"))
            if idempleado not in Dic_empleado:
                print("empleado no aparece en sistema registra primero a empleado")
            else:
                nitcliente=int(input("ingrese nit cliente"))
                if nitcliente not in Dic_cliente:
                    print("no aparece cliente en sistema agregue primero a cliente")
                else:
                    total=0
                    venta1=ventas(idventa,fecha,idempleado,nitcliente,total)
                    Dic_ventas[idventa]=venta1
                    print(" ")

        except ValueError:
            print("ingrese un dato valido")
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
        print("4. ordenar producto")
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
    categoria=Categoriaprincipal()

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
                        agregar =Categoria_agregar()
                        guardar=Categoria_guardar()
                        try:
                             p=int(input("ingrese una opcion a ejecturar"))
                             match p:
                                  case 1:
                                      categoria.cargar_categoria()
                                      try:

                                         id_cat = int(input("Ingrese ID de categoría: "))
                                         nombre = input("Ingrese nombre de categoría: ")
                                         agregar.agregar_categoria(id_cat, nombre)

                                      except ValueError:
                                          print("Ingrese un ID válido.")
                                          guardar.guardar_categoria()
                                          print("guardado con exito")

                                  case 2:
                                      pass

                                  case 3:
                                      pass

                                  case 4:
                                      pass
                                  case 5:
                                      pass

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
                    mostrar = Mostrar_producto(productos)
                    eliminar = Eliminar_producto(productos)
                    buscar = Buscar_producto(productos)

                    while p != 6:
                        menu.menu_producto()
                        try:

                            p = int(input("ingrese una opcion a ejecturar"))
                            match p:
                                case 1:
                                    productos.cargar_producto()
                                    try:
                                        id_producto = int(input("Ingrese ID de producto: "))
                                        nombre = input("Ingrese nombre de producto: ")
                                        id_categoria=int(input("ingrese Id de catedoria"))
                                        if id_categoria not in categoria.Dic_categoria.values:

                                            agregar.agregar_categoria(id_producto, nombre,id_categoria,)

                                    except ValueError:
                                        print("Ingrese un ID válido.")
                                        guardar.guardar_categoria()
                                        print("guardado con exito")

                                        ingreso.ingreso_producto()

                                case 2:
                                     mostrar.mostrar_todos()

                                case 3:
                                    eliminar.eliminar()

                                case 4:
                                    pass
                                case 5:
                                    buscar.buscar()

                                case 6:
                                    print("regresar a menu principal")
                                case _:
                                    print("ingrese una opcion valida")

                        except ValueError:
                             print("ingrese un numero entero")

                case 3:
                    p = 0

                    ingresar=ingre_proevedor()
                    buscar=buscar_proveedor()
                    mostrar=mostrar_proveedor()
                    actual=actualizar_prov()
                    eliminar=eliminar_proveedor()

                    while p != 6:
                        menu.menu_proveedor()
                        try:
                            p = int(input("ingrese una opcion a ejecturar"))
                            match p:
                                case 1:
                                    ingresar.ingresa_proeveedor()

                                case 2:
                                    buscar.buscar_prove()
                                case 3:
                                    mostrar.mostrar_prove()
                                case 4:
                                    pass
                                case 5:
                                    eliminar.eliminar_prove()

                                case 6:
                                   print("regresar a menu principal")
                                case _:
                                  print("ingrese una opcion valida")

                        except ValueError:
                             print("ingrese un numero entero")
                case 4:
                    p=0

                    ingresar=ingresar_cliente()
                    buscar=buscar_cliente()
                    mostrar=mostrar_cliente()
                    eliminar=eliminar_cliente()
                    while p != 6:
                        menu.menu_cliente()
                        try:
                            p = int(input("ingrese una opcion a ejecturar"))
                            match p:
                                case 1:
                                    ingresar.ingresa_cliente()

                                case 2:
                                    buscar.buscar_cliente()
                                case 3:
                                    mostrar.mostrar_clie()
                                case 4:
                                    pass
                                case 5:
                                    eliminar.eliminar_cliente()

                                case 6:
                                   print("regresar a menu principal")
                                case _:
                                  print("ingrese una opcion valida")

                        except ValueError:
                             print("ingrese un numero entero")

                case 5:
                    venta=ingreso_ventas()
                    venta.ingre_venta()
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