from NodoAVL import NodoAVL
import ArbolAVL


class ArbolAVL:
  """
   Clase que implementa un árbol AVL con métodos para inserción, búsqueda y rotaciones necesarias para mantener 
   el factor de equilibrio en el árbol. 
  """

  def __init__(self, dato=None, lista: list = []) -> None:
    """ Constructor de la clase. """
    self.__raiz = NodoAVL(dato=dato, lista=lista)

  @property
  def raiz(self):
    return self.__raiz

  @raiz.setter
  def raiz(self, dato):
    self.__raiz = dato

  def descendente(self, arbol1: ArbolAVL, arbol2: ArbolAVL, arbol3: ArbolAVL):
    """ Recorre el árbol en orden descendiente y toma tres parámetros. """
    if self.raiz is not None:
      """ Se verifica que la raíz no sea nula para llamar al método 'inorden_descendiente' implementado en     
          NodoAVL. 
      """
      self.raiz.inorden_descendente(arbol1, arbol2, arbol3)

  def inorden1(self, lista_nodos: list) -> list:
    """ Método que realiza el recorrido del árbol en inorden mediante una llamada recursiva. """
    if self.raiz is not None:
      return self.raiz.inorden1(lista_nodos)

  def preorden(self):
    """ Método que realiza el recorrido del árbol en preorden, visitando el nodo, subárbol izquierdo y derecho.       """
    if self.raiz is not None:
      self.raiz.preorden()

  def ascendente(self, arbol1: ArbolAVL, arbol2: ArbolAVL, arbol3: ArbolAVL):
    """ Método que realiza el recorrido del árbol en inorden ascendente, visitando el subárbol izquierdo, el nodo y el subárbol 
        derecho. """
    if self.raiz is not None:
      self.raiz.inorden_ascendente(arbol1, arbol2, arbol3)

  """ ------------------   Rotaciones   ------------------------"""

  def __rotacion_ii(self, nodo: NodoAVL):
    """ Método que realiza la rotación izquierda - izquierda. """
    """ .. Establecer los apuntadores.."""
    padre = nodo.padre
    """ Nodo"""
    p = nodo
    """ Nodo 1"""
    q = p.izq
    """ Hijo derecho de Nodo1"""
    b = q.der
    """ Ajustar hijos: al padre de Nodo se le coloca como hijo a Nodo1 en el lugar correspondiente. """
    if padre is not None:
      if padre.der == p:
        padre.der = q
      else:
        padre.izq = q
    else:
      self.raiz = q
    """ Reconstruir el arbol. """
    p.izq = b
    q.der = p
    """ Reasignar padres"""
    p.padre = q
    if b is not None:
      b.padre = p
    q.padre = padre
    """ Establecer el factor de equilibrio"""
    p.f_eq = 0
    q.f_eq = 0

  def __rotacion_dd(self, nodo: NodoAVL):
    """ Método que realiza la rotación derecha - derecha. """
    """ ..Establecer los apuntadores.."""
    padre = nodo.padre
    """ Nodo """
    p = nodo
    """ Nodo1 """
    q = p.der
    """ Hijo izquierdo de Nodo1 """
    b = q.izq
    """Ajustar hijos: al padre de Nodo se le coloca como hijo a Nodo1 en el lugar correspondiente. """
    if padre is not None:
      if padre.izq == p:
        padre.izq = q
      else:
        padre.der = q
    else:
      self.raiz = q
    """ Reconstruir el arbol. """
    p.der = b
    q.izq = p
    """ Reasignar padres. """
    p.padre = q
    if b is not None:
      b.padre = p
    q.padre = padre
    """ Establecer el factor de equilibrio. """
    p.f_eq = 0
    q.f_eq = 0

  def __rotacion_id(self, nodo: NodoAVL):
    """ Método que realiza la rotación izquierda - derecha. """
    """ ..Establecer los apuntadores.."""
    padre = nodo.padre
    """ Nodo """
    p = nodo
    """ Nodo1 """
    q = p.izq
    """ Nodo2 """
    r = q.der
    b = r.izq
    c = r.der

    if padre is not None:
      if padre.der == p:
        padre.der = r
      else:
        padre.izq = r
    else:
      self.raiz = r
    """ Reconstrucción del árbol"""
    """ Colocar el hijo izquierdo de Nodo2 como hijo derecho de Nodo1"""
    q.der = b
    """ Colocar el hijo derecho de Nodo2 como hijo izquierdo de Nodo"""
    p.izq = c
    """ Colocar a Nodo1 y Nodo2 como hijos izquierdo y derecho de Nodo"""
    r.izq = q
    r.der = p
    """ Reasignación de padres"""
    r.padre = padre
    p.padre = r
    q.padre = r
    if b is not None:
      b.padre = q
    if c is not None:
      c.padre = p
    """ Ajusta los valores de los factores de equilibrio"""
    """Nodo2"""
    if r.f_eq == -1:
      """Nodo"""
      p.f_eq = 0
      """Nodo1"""
      q.f_eq = 1

    elif r.f_eq == 0:
      """Nodo"""
      p.f_eq = 0
      """Nodo1"""
      q.f_eq = 0

    elif r.f_eq == 1:
      """Nodo"""
      p.f_eq = -1
      """Nodo1"""
      q.f_eq = 0

    r.f_eq = 0

  def __rotacion_di(self, nodo):
    """ Método que realiza la rotación derecha - izquierda. """
    """..Establecer los apuntadores.."""
    padre = nodo.padre
    """ Nodo"""
    p = nodo
    """ Nodo1"""
    q = p.der
    """ Nodo2"""
    r = q.izq
    b = r.der
    c = r.izq

    if padre is not None:
      if padre.izq == p:
        padre.izq = r
      else:
        padre.der = r
    else:
      self.raiz = r
    """ Reconstrucción del árbol"""
    """ Colocar el hijo derecho de Nodo2 como hijo izquierdo de Nodo1"""
    q.izq = b
    """ Colocar el hijo izquierdo de Nodo2 como hijo derecho de Nodo"""
    p.der = c
    """ Colocar a Nodo1 y Nodo2 como hijos izquierdo y derecho de Nodo"""
    r.der = q
    r.izq = p
    """ Reasignación de padres"""
    r.padre = padre
    p.padre = r
    q.padre = r
    if b is not None:
      b.padre = q
    if c is not None:
      c.padre = p
    """ Ajusta los valores de los factores de equilibrio"""
    """ Nodo2 """
    if r.f_eq == -1:
      """ Nodo """
      p.f_eq = 0
      """ Nodo1 """
      q.f_eq = 1

    elif r.f_eq == 0:
      """ Nodo """
      p.f_eq = 0
      """ Nodo1 """
      q.f_eq = 0

    elif r.f_eq == 1:
      """ Nodo """
      p.f_eq = -1
      """ Nodo1 """
      q.f_eq = 0
    r.f_eq = 0

  def __balancear(self, nodo: NodoAVL):
    """ Método que permite balancear el árbol determinando la rotación a usar a través del factor de equlibrio actual del nodo. """

    fe_actual = nodo.f_eq

    if fe_actual == 2:
      """ Determinar la rotación"""
      fe_hijo_der = nodo.der.f_eq
      if fe_hijo_der == 0:
        pass
      elif fe_hijo_der == 1:
        self.__rotacion_dd(nodo)
        print("Aplicando rotación DD...")
      elif fe_hijo_der == -1:
        self.__rotacion_di(nodo)
        print("Aplicando rotación DI...")
    else:
      fe_hijo_izq = nodo.izq.f_eq
      if fe_hijo_izq == 0:
        pass
      elif fe_hijo_izq == -1:
        self.__rotacion_ii(nodo)
        print("Aplicando rotación II...")
      elif fe_hijo_izq == 1:
        self.__rotacion_id(nodo)
        print("Aplicando rotación ID...")

  def __recalcular_fe(self, nodo: NodoAVL):
    """ Método que permite recalcular el factor de equilibrio después de aplicar las rotaciones correspondientes. """

    if nodo is not None:
      """ Si el nodo no es nulo, procede a calcular su altura mediante el método altura implementado en la clase 'NodoAVL'. """
      nodo.f_eq = NodoAVL.altura(nodo.der) - NodoAVL.altura(nodo.izq)
      if abs(nodo.f_eq) == 2:
        """ Si el valor absoluto del nodo == 2, se llama al método 'balancear'. """
        self.__balancear(nodo)
      else:
        """ Si el valor absoluto del nodo !== 2, se llama recursivamente el método 'recalcular_fe'. """
        self.__recalcular_fe(nodo.padre)

  def __inserta_ordenado(self, nodo: NodoAVL, dato, lista: list = []):
    """ Método privado que permite insertar de manera ordenada un nuevo nodo """

    n = nodo.dato
    """ El dato a insertar se compara con el dato del nodo actual.  """
    if dato == nodo.dato:
      """ Se almacena en la lista, esto permite múltiples elementos con el mismo valor en el árbol AVL. """
      nodo.lista = nodo.lista + lista

    if dato < n:
      if nodo.izq is None:
        """ Si ambas condiciones se cumplen, el dato se asigna como hijo izquierdo del nodo actual y se reclacula su factor de                  equilibrio y realizar el balanceo si es necesario.  """
        nodo.izq = NodoAVL(dato, lista, None, None, nodo)
        self.__recalcular_fe(nodo)
      else:
        """ Si el hijo izquierdo del nodo actual no está vacío, se llama recursivamente al método actual para encontrar el lugar 
            correcto (en el subárbol izquierdo) para insertar el dato. """
        self.__inserta_ordenado(nodo.izq, dato, lista)
    elif dato > n:
      if nodo.der is None:
        """ Si ambas condiciones se cumplen, el dato se inserta como hijo derecho del nodo actual y se recalcula su factor de                   equilibrio. """
        nodo.der = NodoAVL(dato, lista, None, None, nodo)
        self.__recalcular_fe(nodo)
      else:
        """ Si el hijo derecho del nodo actual no está vacío, se llama recursivamente al método actual para encontrar el lugar (en              el subárbol derecho) en donde se debe insertar el dato.  """
        self.__inserta_ordenado(nodo.der, dato, lista)

  def insertar(self, dato, lista: list = []):
    """ Método público que llama al método privado 'inserta_ordenado' pasando como parámetros el dato y una lista.  """
    self.__inserta_ordenado(self.raiz, dato, lista)

  """ ---------  Métodos de búsqueda ----------  """

  def buscar(self, nodo: NodoAVL, dato):
    """
    Método que recibe un nodo (la raíz del árbol), recorre el árbol a partir de ese nodo y retorna el nodo en donde se encuentra el 
    dato a buscar.
    """

    if dato < nodo.dato:
      if nodo.izq is None:
        return None
      else:
        return self.buscar(nodo.izq, dato)
    elif dato > nodo.dato:
      if nodo.der is None:
        return None
      else:
        return self.buscar(nodo.der, dato)
    else:
      return nodo

  """  -------  Método de búsqueda para operación AND -------  """
  """ Método para caso: Nombre y (Profesión o Promedio). """

  def busqueda_avanzada(self, nodo1: NodoAVL, nodo2: NodoAVL) -> list:
    """
      Método que recibe los nodos de los datos que se necesita buscar y retorna una lista con los datos de nodo1.dato y nodo2.dato.  """
    retorno = []
    if nodo1 is None or nodo2 is None:
      """ Los datos de nodo1 y nodo2 son None, retorna None. """
      return None
    else:
      """ Los datos de nodo1 y nodo2 son diferentes de None. """
      for i in range(len(nodo2.lista)):
        """ Itera a través de los elementos de la lista nodo2.lista y compara cada uno con el valor de nodo1.dato """
        """ Busca el nombre en la lista de nodo2 """
        if nodo1.dato == nodo2.lista[i]:
          """Retorna una lista con nombre y su respectiva profesión o promedio"""
          retorno = [nodo1.dato, nodo2.dato]
    return retorno
    """--------- Método de búsqueda para caso específico: "Profesión y Promedio"---------"""

  def busqueda_avanzadaPro(self, nodo1: NodoAVL, nodo2: NodoAVL) -> list:
    """
    Método que recibe como parámetros 2 nodos, los cuales son proporcionados por el método
    buscar en el main, retorna una lista con todos los datos que coincidan con el mismo nombre.
    """
    retorno = []
    if nodo1 is None or nodo2 is None:
      return None
    else:
      """ Itera sobre los elementos de la lista 'nodo1.lista'. """
      for i in range(len(nodo1.lista)):
        """ Itera sobre los elementos de la lista 'nodo2.lista'. """
        for j in range(len(nodo2.lista)):
          """ Compara para encontrar los nombres que coinciden en ambas listas. """
          if nodo2.lista[j] == nodo1.lista[i]:
            retorno.append([nodo1.lista[i], nodo1.dato, nodo2.dato])
            """ Retorna una lista con todos los datos"""
      return retorno

  def buscarOtroArbol(self, dato):
    """ Método que permite buscar en el árbol que contiene el dato que se necesita """
    if self.raiz is not None:
      """ Manda el dato 'Nombre'. """
      encontrado = self.raiz.recorridoBusqueda(dato, False)
      """ Retorna el dato faltante """
      return encontrado
