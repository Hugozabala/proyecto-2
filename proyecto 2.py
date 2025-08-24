Dic_producto={}
Dic_empleado={}
Dic_cliente={}
Dic_vendedor={}
Dic_categoria={}
Dic_compras ={}
Dic_ventas={}

class categoria:
    def __init__(self,Id_categoria,nombre):
        self.Id_categoria=Id_categoria
        self.nombre=nombre
    def mostrar_categoria(self):
        print(f"\n ID categoria: {self.Id_categoria}- nombre: {self.nombre}")
class ingresar_categoria:
    def ing_categoria(self):
        try:
            id=int(input("ingrese Id de categoria"))
            if id not in Dic_categoria:
                nom=input("ingrese nombre de categoria")
                cate=categoria(id,nom)
                Dic_categoria[id]=cate
                print("ingresado con exito")
            else:
                print("categoria existente")

        except ValueError:
            print("ingrese un dato valido")

class mostrar_categoria:
    def mostrar(self):
        if not Dic_categoria:
            print("No hay categorías registradas")
        else:
            print("\n Categorías registradas:")
            for cat in Dic_categoria.values():
                cat.mostrar_categoria()

class eliminar_categoria:
    def eli_categoria(self):
        try:
            eliminar=int(input("ingrese Id de categoria a eliminar"))
            if eliminar not in Dic_categoria:
                print("categoria no aparece en sistema")

            else:
                eliminar=Dic_categoria.pop(eliminar)
                print(f"categoria eliminado{ eliminar.nombre}")
        except ValueError:
            print("ingrese un dato valido")


class producto:
     def __init__(self, Idproducto,nombre,Id_categoria,precio,total_compra=0,total_venta=0,stock=0):
         self.Idproducto=Idproducto
         self.nombre=nombre
         self.precio=precio
         self.Id_categoria=Id_categoria
         self.total_compra=total_compra
         self.total_venta=total_venta
         self.stock=stock


     def mostrar(self):
         print(f"\n Id de producto: {self.Idproducto}- Nombre de producto{self.nombre}- Precio: {self.precio}-totalcompra: {self.total_compra}- total_venta: {self.total_venta}- stock: {self.stock} ")
class Ing_producto:
    def Ingreso_producto(self):
        try:
            idpro=int(input("ingrese ID de producto"))
            if idpro not in Dic_producto:
                print("el producto ya existe en el inventario")
                return

            nom=input("ingrese nombre de producto")
            pre=float(input("ingrese precio de producto"))
        except ValueError:
            print("has ingresado un doto incorrecto")

        p=producto(idpro,nom,pre)
        Dic_producto[idpro]=p

class eliminar_pro:
    def Eliminar_producto(self):
        try:
            eliminar=int(input("ingrese ID de producto a eliminar"))
            if eliminar not in Dic_producto:
                print("el producto que desea eliminar no existe en el inventario")
                return
            else:
                eliminar=Dic_producto.pop(eliminar)
                print(f"producto eliminado {eliminar.nombre}")


        except ValueError:

            print("has ingresado un dato incorrecto")

class Actualizar_pro:
    def actualizar(self):
        try:
            id=int(input("ingrese el codigo del producto"))
            if id not in Dic_producto:
                print("producto a actualizar no existe")
                return

            producto = Dic_producto[id]
            print("mostrar producto a actualizar")
            producto.mostrar()

            try:
                nuevo_precio=float(input("ingrese nuevo precio de producto"))
                nuevo_stock=int(input(" ingrese cantidad de producto nuevo "))
                if nuevo_precio.strip() != "":
                    nuevo_precio = float(nuevo_precio)
                    if nuevo_precio > 0:
                        producto.precio = nuevo_precio
                    else:
                        print("Precio inválido, no se actualizó.")

                if nuevo_stock.strip() != "":
                    nuevo_stock = int(nuevo_stock)
                    if nuevo_stock >= 0:
                        producto.stock = nuevo_stock
                    else:
                        print("Stock inválido, no se actualizó.")

                print("\nProducto actualizado con éxito:")
                producto.Mostrar()

            except ValueError:
                print("has ingresado un dato no valido")

        except ValueError:
            print("has ingresado un dato incorrecto")


class buscar_pro:
    def buscar_pro(self):
        try:
            id=int(input("ingrese ID de producto"))
            if id not in Dic_producto:
                print("no existe producto en inventario ")
                return
            producto=Dic_producto[id]
            print("producto encontrado ")
            producto.mostrar()


        except   ValueError:
            print("has ingresado un dato no valido")

class ordenar_pro:

        def quicksort(self, lista):
            if len(lista) <= 1:
                return lista
            pivote = lista[0]

            menores = [x for x in lista[1:] if x < pivote]
            iguales = [x for x in lista if x == pivote]
            mayores = [x for x in lista[1:] if x > pivote]

            return self.quicksort(menores) + iguales + self.quicksort(mayores)

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
    def __init__(self,nit,nombre_cliente,direcion,telefono):
        self.nit=nit
        self.nombre_cliente=nombre_cliente
        self.direccion=direcion
        self.telefono=telefono


    def mostrar_cliente(self):
        print(f"\n Numero de nit de cliente:{self.nit}-Nombre de cliente: {self.nombre_cliente,}-- direccion: {self.direccion}-Telefono: {self.telefono}")

class ingresar_cliente:
    def ingresa_cliente(self):
        try:
            nit=int(input("ingrese nit de cliente"))
            nom=input("ingrese nombre")
            dire=input("ingese direccion")
            tele=int(input("ingrese telefono: "))
            c=cliente(nit,nom,dire,tele)
            Dic_empleado[nit]=c
            print("cliente ingresdo con Exito")

        except ValueError:
            print("ingrestes un dato no valido")

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

class menus:
    def Menu_principal(self):
        print("==========MENU PRINCIPAL===========")
        print("1. Categoria ")
        print("2. ")
        print("3. ")
        print("4. ")
        print("5. ")
        print("6. ")
        print("7. ")
        print("8. ")
        print("9. ")
        print("10. ")

    def Menu_categoria(self):
        print("=======CATEGORIA=======")
        print("1. ingrese categoria ")
        print("2. buscar categoria ")
        print("3. mostrar categoria")
        print("4. eliminar categoria")
        print("5. salir")


    def Sun_menu_pro(self):
        print("=======SUB MENU=======")
        print("1. ingreso de producto ")
        print("2. buscar producto ")
        print("3. actualizar producto")
        print("4. ordenar producto")
        print("5. eliminar producto")
        print("6. salir")
def main():
    op=0
    menu=menus()
    menu.Menu_principal()


    while op!=10:
        try:
            op=int(input("ingrese una opcion a ejectura"))
            match op:
                case 1:
                    p=0
                    menu.Menu_categoria()
                    categoria_ing = ingresar_categoria()
                    cat_eliminar =eliminar_categoria()
                    c=categoria()

                    while p!=6:
                        try:
                             p=int(input("ingrese una opcion a ejecturar"))
                             match p:
                                  case 1:
                                      categoria_ing.ing_categoria()

                                  case 2:
                                      pass

                                  case 3:
                                      c.mostrar_categoria()
                                  case 4:
                                      pass
                                  case 5:
                                       cat_eliminar.eli_categoria()
                                  case 6:
                                      print("regresar a menu principal")
                                  case _:
                                      print("ingrese una opcion valida")

                        except ValueError:
                             print("ingrese un numero entero")

                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
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