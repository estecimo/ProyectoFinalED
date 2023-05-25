from ArbolAVL import ArbolAVL
from Egresados import Egresados
import os
import traceback

arbol_enfoque = None
arbol_enfnom = None


def clear():
  """ Método que permite limpiar la pantalla de la consola. """
  os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
  """ Clase principal que permite ejecutar el programa. """

  while True:
    try:
      """ Interfaz basica
          Menu principal    """
      clear()
      print("Menu")
      print("Arbol de enfoque: ", arbol_enfnom)
      print(
        "\n1. Crear arboles.\n2. Cambiar arbol de enfoque.\n3. Listar.\n4. Búsqueda.\n5. Búsqueda avanzada.\n6. Salir."
      )
      """ Solicitud de entrada al usuario """
      ch = input()
      """ -------------- Opción 1: creación de árboles ------------- """
      if ch == "1":
        """ Ruta de acceso al archivo que contiene los datos. """
        ruta_archivo = "Egresados.csv"
        """Instancia de la clase 'Egresados'.  """
        
        Egresados_inst = Egresados()
        """ Llamada al método 'leerCSV' para leer las columnas del archivo .csv y asignar valores a las variables.  """
        nombres = Egresados_inst.leerCSV(ruta_archivo, 0)
        profesion = Egresados_inst.leerCSV(ruta_archivo, 1)
        calificacion = Egresados_inst.leerCSV(ruta_archivo, 2)
        """ Instancia de la clase 'ArbolAVL' asignada a una variable.  """
        arbolNombres = ArbolAVL(nombres[0])
        """ Lista que contiene el primer nombre de la lista 'nombres', parámetro usado en el constructor de la clase 'ArbolAVL'. """
        listaProfesion = [nombres[0]]
        """ Creación del árbol de profesiones """
        arbolProfesion = ArbolAVL(profesion[0], listaProfesion)
        """ Lista que contiene el primer nombre de la lista 'nombres'. """
        listaCalificacion = [nombres[0]]
        """ Creación del árbol de calificaciones. """
        arbolCalificacion = ArbolAVL(calificacion[0], listaCalificacion)
        """ Iterar sobre los elementos a partir del segundo elemento. """
        for elemento in nombres[1:]:
          """ Para cada elemento se llama al método 'insertar' del 'arbolNombres'. """
          arbolNombres.insertar(elemento)

        i = 0
        """ Se itera sobre la lista 'profesion' a partir del segundo elemento """
        for elemento in profesion[1:]:
          i = i + 1
          """ Se crea una nueva lista que contiene el nombre correspondiente a la posición [i]. """
          listaProfesion = [nombres[i]]
          """ Llamada al método 'insertar' del 'arbolProfesion'. """
          arbolProfesion.insertar(elemento, listaProfesion)

        i = 0
        """Se itera sobre la lista 'calificacion' a partir del segundo elemento. """
        for elemento in calificacion[1:]:
          i = i + 1
          """ Se crea una nueva lista que contiene el nombre correspondiente a la posición [i]. """
          listaCalificacion = [nombres[i]]
          """ Llamada al método 'insertar' del 'arbolCalificacion'. """
          arbolCalificacion.insertar(elemento, listaCalificacion)
        """ Se crea un diccionario 'arboles' que contiene tres claves con valor. Almacena los árboles relacionados con los dos 
            enfoques inicializados al principio de la clase 'main' """
        arboles = {
          "Nombres": arbolNombres,
          "Profesiones": arbolProfesion,
          "Promedios": arbolCalificacion
        }
        arbol_enfoque = arbolNombres
        arbol_enfnom = "Nombres"
        """ Obtiene una lista de los árboles diferentes al árbol actual de enfoque (Nombres). """
        other_trees = [
          value for value in arboles.values() if value != arbol_enfoque
        ]
        other_names = [key for key in arboles.keys() if key != arbol_enfnom]

        input(
          "\nArboles creados con éxito!!\nPresione cualquier tecla para continuar..."
        )
        clear()
        """ ------ Opción 2: cambiar árbol de enfoque --------- """
      elif ch == "2":
        clear()
        print("---Cambiar arbol de enfoque---\nArbol de enfoque: ",
              arbol_enfnom, "\n\n1.", other_names[0], "\n2.", other_names[1],
              "\n3. Regresar")
        ch2 = input("\n")
        """ Opciones para cambiar el árbol de enfoque. """
        if ch2 == "1":
          arbol_enfoque = other_trees[0]
          arbol_enfnom = other_names[0]

          clear()

        elif ch2 == "2":
          arbol_enfoque = other_trees[1]
          arbol_enfnom = other_names[1]
          clear()

        elif ch2 == "3":
          clear()
          """ Mensaje por si no se selecciona un número del 1-3. """
        else:
          raise ValueError("Ingrese un valor valido")
          """ Después de realizar el cambio en el árbol de enfo """
        other_trees = [
          value for value in arboles.values() if value != arbol_enfoque
        ]
        other_names = [key for key in arboles.keys() if key != arbol_enfnom]
        """------ Opción 3: selección de listado de árbol -------------"""
      elif ch == "3":

        while True:
          clear()
          print("---Listar---\nArbol de enfoque: ", arbol_enfnom)
          """ Opciones para enlistar los árboles de nombres y profesiones. """
          if arbol_enfoque is not arbolCalificacion:
            ch3 = input(
              "\nSeleccione el orden a enlistar:\n1. Ascendente\n2. Descendente\n3. Regresar\n\n"
            )

          else:
            ch3 = input(
              "\nSeleccione el orden a enlistar:\n1. Descendente\n2. Ascendente\n3. Regresar\n\n"
            )

          if ch3 == "1":
            arbol_enfoque.ascendente(other_trees[1], other_trees[0],
                                     arbol_enfoque)
            input("\nPresione cualquier tecla para continuar...")

          elif ch3 == "2":
            arbol_enfoque.descendente(other_trees[1], other_trees[0],
                                      arbol_enfoque)
            input("\nPresione cualquier tecla para continuar...")

          elif ch3 == "3":
            clear()
            break

          else:
            raise ValueError("Ingrese un valor valido")
            """ -------  Opción 4: búsqueda en árboles ------"""
      elif ch == "4":
        while True:
          clear()
          print("---Busqueda---\nArbol de enfoque:", arbol_enfnom,
                "\n\n1. Ingresar dato a buscar.\n2. Regresar")
          ch4 = input("\n")

          if ch4 == "1":
            clear()
            buscame = input("Ingrese el dato a buscar:\n")
            try:
              buscame = int(buscame)
              if arbol_enfoque is arbolNombres or arbol_enfoque is arbolProfesion:
                print("Dato inválido")
                input("\nPresione cualquier tecla para continuar...")
                break
            except ValueError:
              if arbol_enfoque is arbolCalificacion:
                print("Dato inválido")
                input("\nPresione cualquier tecla para continuar...")
                break

            encontrado = arbol_enfoque.buscar(arbol_enfoque.raiz, buscame)

            if encontrado is None: print('No se encontró')
            else:
              max_wd1 = 45
              max_wd2 = 15
              line = "{:<{}} | {:<{}} | {:<{}}"
              print('\nLocalizado: \n')
              if arbol_enfoque == arbolNombres:
                print(
                  line.format("Nombre:", max_wd1, "Profesion:", max_wd1,
                              "Calificacion:", max_wd2))
                print(
                  line.format(
                    encontrado.dato, max_wd1,
                    arbolProfesion.buscarOtroArbol(encontrado.dato), max_wd1,
                    arbolCalificacion.buscarOtroArbol(encontrado.dato),
                    max_wd2))
              elif arbol_enfoque == arbolProfesion:
                print(
                  line.format("Profesion:", max_wd1, "Nombre:", max_wd1,
                              "Calificacion:", max_wd2))
                for i in range(len(encontrado.lista)):
                  print(
                    line.format(
                      encontrado.dato, max_wd1, encontrado.lista[i], max_wd1,
                      arbolCalificacion.buscarOtroArbol(encontrado.lista[i]),
                      max_wd2))
              else:
                print(
                  line.format("Calificacion:", max_wd2, "Nombre:", max_wd1,
                              "Profesion:", max_wd1))
                for i in range(len(encontrado.lista)):
                  print(
                    line.format(
                      encontrado.dato, max_wd2, encontrado.lista[i], max_wd1,
                      arbolProfesion.buscarOtroArbol(encontrado.lista[i]),
                      max_wd1))

            input("\nPresione cualquier tecla para continuar...")

          elif ch4 == "2":
            clear()
            break
            """ ----- Opción 5: búsqueda en árboles con AND -----"""
      elif ch == "5":
        while True:
          clear()
          print("---Busqueda avanzada---", "\n\n1. Nombre y profesion",
                "\n2. Nombre y Calificacion", "\n3. Profesiones y Nombres",
                "\n4. Profesiones y Calificaciones", "\n5. Regresar")

          ch5 = input("\n")
          """ Buscar por nombre y profesión  """
          if ch5 == "1":
            clear()
            dato1 = input("Ingrese el nombre a buscar:\n")
            dato2 = input("Ingrese la profesión a buscar:\n")

            retorno = arbolNombres.busqueda_avanzada(
              arbolNombres.buscar(arbolNombres.raiz, dato1),
              arbolProfesion.buscar(arbolProfesion.raiz, dato2))

            if retorno is None: print('No se encontró')
            else:
              max_wd1 = 45
              max_wd2 = 15
              line = "{:<{}} | {:<{}} | {:<{}}"
              print('\nLocalizado: \n')
              print(
                line.format("Nombre:", max_wd1, "Profesion:", max_wd1,
                            "Calificacion:", max_wd2))
              print(
                line.format(retorno[0], max_wd1, retorno[1], max_wd1,
                            arbolCalificacion.buscarOtroArbol(dato1), max_wd2))

            input("\nPresione cualquier tecla para continuar...")
            """----- Opción 2: buscar por nombre y promedio -----"""
          elif ch5 == "2":
            clear()
            dato1 = input("Ingrese el nombre a buscar:\n")
            dato2 = input("Ingrese el promedio a buscar:\n")

            try:
              dato2 = int(dato2)
            except ValueError:
              print("Dato inválido, coloque correctamente el promedio")
              input("\nPresione cualquier tecla para continuar...")
              break

            retorno = arbolNombres.busqueda_avanzada(
              arbolNombres.buscar(arbolNombres.raiz, dato1),
              arbolCalificacion.buscar(arbolCalificacion.raiz, dato2))

            if retorno is None: print('No se encontró')
            else:
              max_wd1 = 45
              max_wd2 = 15
              line = "{:<{}} | {:<{}} | {:<{}}"
              print('\nLocalizado: \n')
              print(
                line.format("Nombre:", max_wd1, "Calificacion:", max_wd2,
                            "Profesion:", max_wd1))
              print(
                line.format(retorno[0], max_wd1, retorno[1], max_wd2,
                            arbolProfesion.buscarOtroArbol(dato1), max_wd1))

            input("\nPresione cualquier tecla para continuar...")
            """ ------- Opción 3: buscar por profesión y nombre. ----------- """

          elif ch5 == "3":
            clear()
            dato1 = input("Ingrese la profesion a buscar:\n")
            dato2 = input("Ingrese el nombre a buscar:\n")

            retorno = arbolProfesion.busqueda_avanzada(
              arbolNombres.buscar(arbolNombres.raiz, dato2),
              arbolProfesion.buscar(arbolProfesion.raiz, dato1))

            if retorno is None: print('No se encontró')
            else:
              max_wd1 = 45
              max_wd2 = 15
              line = "{:<{}} | {:<{}} | {:<{}}"
              print('\nLocalizado: \n')
              print(
                line.format("Profesion:", max_wd1, "Nombre:", max_wd1,
                            "Calificacion:", max_wd2))
              print(
                line.format(retorno[1], max_wd1, retorno[0], max_wd1,
                            arbolCalificacion.buscarOtroArbol(dato2), max_wd2))

            input("\nPresione cualquier tecla para continuar...")
            """ -------- Opción 4: buscar por profesión y nombre -------- """
          elif ch5 == "4":

            clear()
            dato1 = input("Ingrese la profesión a buscar:\n")
            dato2 = input("Ingrese el promedio a buscar:\n")

            try:
              dato2 = int(dato2)
            except ValueError:
              print("Dato inválido, coloque correctamente el promedio")
              input("\nPresione cualquier tecla para contiuar...")
              break

            retorno = arbolProfesion.busqueda_avanzadaPro(
              arbolProfesion.buscar(arbolProfesion.raiz, dato1),
              arbolCalificacion.buscar(arbolCalificacion.raiz, dato2))

            if retorno == [] or retorno == None: print('No se encontró')
            else:
              max_wd1 = 45
              max_wd2 = 15
              line = "{:<{}} | {:<{}} | {:<{}}"
              print('\nLocalizado: \n')
              print(
                line.format("Profesion", max_wd1, "Calificacion:", max_wd2,
                            "Nombre:", max_wd1))
              """ Se itera sobre los elementos de la lista 'retorno' y se imprime cada elemento. """
              for i in (range(len(retorno))):
                aux = retorno[i]
                print(
                  line.format(aux[1], max_wd1, aux[2], max_wd2, aux[0],
                              max_wd1))

            input("\nPresione cualquier tecla para continuar...")
          elif ch5 == "5":
            clear()
            break

          else:
            raise ValueError("Ingrese un valor valido")
          """ ------- Opción 6: salir del programa ------- """
      elif ch == "6":
        input("Presione cualquier tecla para salir...")
        clear()
        break
        """ En caso de no ingresar un número del 1-5 o ingresar una letra"""
      else:
        raise ValueError("Seleccione una opción váida")
        """ --------- Mensajes a posibles errores en la ejecución --------"""

    except NameError:
      clear()
      print("ERROR: No se encuentra el arbol, seleccione Crear arboles")
      traceback.print_exc()
      input("Presione cualquier tecla para continuar...")
      clear()
      continue

    except ValueError as e1:
      clear()
      print("ERROR: ", e1)
      input("Presione cualquier tecla para continuar...")
      clear()

    except AttributeError:
      clear()
      print("Object has no attribute, seleccione Crear arboles")
      traceback.print_exc()
      input("Presione cualquier tecla para continuar...")
      clear()
