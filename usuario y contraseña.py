class contraseña():
  u = "usuario"
  contraseña = "caiz1234"

  intentos = 0
  max_intentos = 3

  while intentos < max_intentos:
         usu = input("Ingrese usuario: ")

         if usu != u:
             print("Usuario incorrecto, intente nuevamente.")
         else:
             co = input("Ingrese contraseña: ")
             if co !=contraseña:
                print("Contraseña incorrecta, intente nuevamente.")
             else:
                 print(" Hola mundo, acceso concedido.")
                 break

                 intentos += 1

  if intentos == max_intentos:
         print(" Has superado el  máximo de intentos. Acceso bloqueado.")