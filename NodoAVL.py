import NodoAVL
import ArbolAVL


class NodoAVL:
  """
  Clase que representa los nodos del árbol e implementa diversos métodos para realizar recorridos, buscar datos y   
  mantener el factor de equilibrio.
  """

  def __init__(self,
               dato=None,
               lista: list = [],
               izq: NodoAVL = None,
               der: NodoAVL = None,
               padre: NodoAVL = None,
               f_eq: int = 0):
    """Constructor de la clase que inicializa las propiedades del objeto NodoAVL. """
    """Variables de instancia."""
    self.__dato = dato
    self.__lista = lista
    self.__izq = izq
    self.__der = der
    self.__padre = padre
    self.__f_eq = f_eq

  """Getters y setters para acceder y modoficar los atributos."""

  @property
  def dato(self):
    return self.__dato

  @dato.setter
  def dato(self, dato):
    self.__dato = dato

  @property
  def lista(self):
    return self.__lista

  @lista.setter
  def lista(self, lista):
    self.__lista = lista

  @property
  def izq(self):
    return self.__izq

  @izq.setter
  def izq(self, izq):
    self.__izq = izq

  @property
  def der(self):
    return self.__der

  @der.setter
  def der(self, der):
    self.__der = der

  @property
  def f_eq(self):
    return self.__f_eq

  @f_eq.setter
  def f_eq(self, f_eq):
    self.__f_eq = f_eq

  @property
  def padre(self):
    return self.__padre

  @padre.setter
  def padre(self, padre):
    self.__padre = padre

  @staticmethod
  def altura(nodo: NodoAVL = None) -> int:
    """Método estático que calcula la altura de un nodo mediante un enfoque recursivo."""
    if nodo is None:
      """Retorna '-1' si no se pasa ningún nodo. """
      return -1
    else:
      """Obtiene la altura máxima entre la altura del subárbol izquierdo y la del derecho del nodo y se le suma 
         '1' para incluir la altura del pripio nodo en el cálculo. """
      return 1 + max(NodoAVL.altura(nodo.izq), NodoAVL.altura(nodo.der))


  
  """ ------------------- Recorridos del árbol. ---------------------- """


  def inorden_descendente(self, arbol1: ArbolAVL, arbol2: ArbolAVL,
                          arbol3: ArbolAVL):
    """ Método que permite realizar un recorrido, visitando primero el subárbol derecho, después el nodo actual 
        y por último, el subárbol izquierdo. """
    """ Calcula la longitud máxima de las cadenas obtenidas en los recorridos de los árboles. """
    max_wd1 = len(max(arbol3.inorden1([]), key=len))
    max_wd2 = len(max(arbol2.inorden1([]), key=len))
    max_wd3 = len(max(arbol1.inorden1([]), key=len))
    """ Formato línea que se utilizará para imprimir los valores de los nodos en un formato tabular"""
    line = "{:<{}} | {:<{}} | {:<{}}"
                            
    """Se comprueba si el subárbol izquierdo es diferente de 'None' para llamarse recursivamente en el mismo 
       subárbol. """
    if self.izq != None:
      self.izq.inorden_descendente(arbol1, arbol2, arbol3)
    if self.lista == []:
      """Comprueba si la lista está vacía para imprimir una línea con info. del nodo actual y los datos 
         obtenidos de otros árboles (arbol2, arbol1). """

      print(
        line.format(self.dato, max_wd1, arbol2.buscarOtroArbol(self.dato),
                    max_wd2, arbol1.buscarOtroArbol(self.dato), max_wd3))
    else:
      """ Se itera sobre los elementos de la lista en orden inverso, esto es, desde el último hasta el primero. 
      """
      for i in reversed(range(len(self.lista))):
        """Imprime una línea formateada que contiene información del nodo actual, el elemento de la lista 'i' y 
           los datos obtenidos en los otros árboles. 
           Los otros valores se usan para alinear los datos en la línea.
        """
        print(
          line.format(self.dato, max_wd1, self.lista[i], max_wd2,
                      arbol1.buscarOtroArbol(self.lista[i]), max_wd3))
    """ Verifica si existe un subárbol derecho para realizarse un llamado recursivo. """
    if self.der != None:
      self.der.inorden_descendente(arbol1, arbol2, arbol3)

  
  
  def inorden_ascendente(self, arbol1: ArbolAVL, arbol2: ArbolAVL,
                         arbol3: ArbolAVL):
    """Metodo que permite realizar un recorrido, visitando primero el subárbol izquierdo, después el nodo 
       actual y por último, el subárbol derecho. """
    """ Calcula la longitud máxima de las cadenas obtenidas en los recorridos de los árboles. """
    max_wd1 = len(max(arbol3.inorden1([]), key=len))
    max_wd2 = len(max(arbol2.inorden1([]), key=len))
    max_wd3 = len(max(arbol1.inorden1([]), key=len))
    """ Formato línea que se utilizará para imprimir los valores de los nodos en un formato tabular"""
    line = "{:<{}} | {:<{}} | {:<{}}"
    """Se comprueba si el subárbol izquierdo es diferente de 'None' para llamarse recursivamente en el mismo 
       subárbol. """

    if self.der != None:
      self.der.inorden_ascendente(arbol1, arbol2, arbol3)
    if self.lista == []:
      """Comprueba si la lista está vacía para imprimir una línea con info. del nodo actual y los datos 
         obtenidos de otros árboles (arbol2, arbol1). """

      print(
        line.format(self.dato, max_wd1, arbol2.buscarOtroArbol(self.dato),
                    max_wd2, arbol1.buscarOtroArbol(self.dato), max_wd3))
    else:
      """ Se itera sobre los elementos de la lista en orden inverso, esto es, desde el último hasta el primero. 
      """
      for i in reversed(range(len(self.lista))):
        """Imprime una línea formateada que contiene información del nodo actual, el elemento de la lista 'i' y 
           los datos obtenidos en los otros árboles. 
           Los otros valores se usan para alinear los datos en la línea.
        """
        print(
          line.format(self.dato, max_wd1, self.lista[i], max_wd2,
                      arbol1.buscarOtroArbol(self.lista[i]), max_wd3))
      """ Verifica si existe un subárbol izquierdo para realizarse un llamado recursivo. """
    if self.izq != None:
      self.izq.inorden_ascendente(arbol1, arbol2, arbol3)


  
  def recorridoBusqueda(self, dato, bandera) -> str:
    """  Método para todos los nodos del arbol que permite encontrar el dato 'Nombre' """
    """Llama a la función que recorre la lista del nodo"""
    bandera = self.recorrer(dato)
    """Mientras no se encuentre el dato, se recorre el arbol en inorden"""
    if bandera != True:
      if self.izq != None:
        encontrado_izq = self.izq.recorridoBusqueda(dato, False)
        if encontrado_izq is not None:
          return encontrado_izq
      if self.der != None:
        encontrado_der = self.der.recorridoBusqueda(dato, False)
        if encontrado_der is not None:
          return encontrado_der
    else:
      """ Retorna el dato del nodo """
      return self.dato

  def recorrer(self, dato):
    """ Recorre los nombres de la listas del nodo actual """
    for i in range(len(self.lista)):
      if dato == self.lista[i]:
        """Valor para saber si el dato 'Nombre' se encontró en la lista del nodo"""
        return True
        """Valor de retorno en caso de que el dato 'Nombre' no se encuentre en la lista"""
    return False

  def inorden1(self, lista_nodos: list) -> list:
    """ Método que realiza un recorrido en inorden para guardar los elementos de cada nodo en una lista y esta 
        se retorna con los datos del árbol en inorden."""
    if self.izq != None:
      """ Se veridica si hay un subárbol izquierdo para llamarse recursivamente pasando 'lista_nodos' """
      self.izq.inorden1(lista_nodos)
    if self.lista == []:
      """ Se verfica si la lista asociada al nodo actual está vacía, para luego agregarlas a la lista en forma 
          de cadena. """
      lista_nodos.append(str(self.dato))
    else:
      """ La lista asociada al nodo no está vacía. """
      for i in self.lista:
        """ Se recorre la lista para agregar el elemento en forma de cadena. """
        lista_nodos.append(str(self.dato))
        """ Se verifica si existe un subárbol derecho para llamarse recursivamente pasando 'lista_nodos'. """
    if self.der != None:
      self.der.inorden1(lista_nodos)
    return lista_nodos
