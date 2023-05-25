import csv

class Egresados:

  """
   Clase que proporciona un método para leer el .csv y extraer los elementos de una columna específica en forma de lista. 
  """
  
  def __init__(self):
    """
    Constructor de la clase Egresados. Crea una instancia de la clase sin             
    realizar alguna operación adicional.
    """
    pass

  def leerCSV(self, nombre_archivo, columna):
    """
    Método que permite leer el archivo CSV almacenado en nombre_archivo. Los elementos     de la columna se almacenan en una lista ('elementos') y esta se retorna.
    """
    """Lista vacía. """
    elementos = []
    with open(nombre_archivo, 'r', encoding='utf-8-sig',
              errors='replace') as archivo:
      """Crea un objeto reader para leer y procesar el contenido del archivo. """
      reader = csv.reader(archivo)
      """Omite el encabezado. """
      next(reader)
      for fila in reader:
        if fila:
          """Verifica que la fila no esté vacía. """
          valor = fila[columna]
          try:
            """Intenta convertir el valor a entero. """
            valor = int(valor)
            """Si no es posible, se deja el valor original. """
          except ValueError:
            pass
            """Agrega el elemento a la lista 'elementos'. """
          elementos.append(valor)
    return elementos
