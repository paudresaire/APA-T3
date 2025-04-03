"""
Módulo de operaciones con vectores.

Autor: Pau
Descripción: Implementación de la clase Vector con operaciones básicas, incluyendo suma, resta,
multiplicación, producto escalar, y descomposición en componentes paralela y normal.
Incluye pruebas unitarias para validar las funciones implementadas.
"""

import unittest

class Vector:
    """
    Clase usada para trabajar con vectores sencillos.
    """
    def __init__(self, iterable):
        """
        Constructor de la clase Vector.
        
        Argumentos:
        iterable -- Un iterable con las componentes del vector.
        """
        self.vector = [valor for valor in iterable]

    def __repr__(self):
        """
        Representación oficial del vector para reconstrucción mediante corta-y-pega.
        """
        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación en formato de lista del vector.
        """
        return str(self.vector)

    def __getitem__(self, key):
        """
        Obtiene un elemento o una porción del vector.
        """
        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Asigna un valor a una componente o una porción del vector.
        """
        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """
        return len(self.vector)

    def __eq__(self, other):
        """
        Compara si dos vectores son iguales.
        """
        if isinstance(other, Vector):
            return self.vector == other.vector
        return False

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """
        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """
        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """
        return -(-self + other)

    def __rsub__(self, other):
        """
        Resta reflejada cuando el primer operando no es un Vector.
        """
        return -self + other
    
    def __mul__(self, other):
        """
        Producto de Hadamard o multiplicación por un escalar.
        """
        if isinstance(other, (int, float, complex)):
            return Vector(item * other for item in self)
        else:
            return Vector(uno * otro for uno, otro in zip(self, other))

    __rmul__ = __mul__

    def __matmul__(self, other):
        """
        Producto escalar entre dos vectores.
        """
        return sum(uno * otro for uno, otro in zip(self, other))

    __rmatmul__ = __matmul__
    
    def __floordiv__(self, other):
        """
        Devuelve la componente tangencial (paralela) de un vector respecto a otro.
        """
        factor = (self @ other) / (other @ other)
        return Vector(factor * item for item in other)
    
    __rfloordiv__ = __floordiv__
    
    def __mod__(self, other):
        """
        Devuelve la componente normal (perpendicular) de un vector respecto a otro.
        """
        return self - (self // other)
    
    __rmod__ = __mod__

class TestVectorOperations(unittest.TestCase):
    """
    Pruebas unitarias para la clase Vector.
    """
    def test_multiplication(self):
        """
        Comprueba la multiplicación de un vector por un escalar y el producto de Hadamard.
        """
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual(v1 * 2, Vector([2, 4, 6]))
        self.assertEqual(v1 * v2, Vector([4, 10, 18]))

    def test_dot_product(self):
        """
        Comprueba el producto escalar entre dos vectores.
        """
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual(v1 @ v2, 32)
    
    def test_parallel_perpendicular_components(self):
        """
        Comprueba la obtención de las componentes paralela y perpendicular de un vector respecto a otro.
        """
        v1 = Vector([2, 1, 2])
        v2 = Vector([0.5, 1, 0.5])
        self.assertEqual(v1 // v2, Vector([1.0, 2.0, 1.0]))
        self.assertEqual(v1 % v2, Vector([1.0, -1.0, 1.0]))

if __name__ == "__main__":
    unittest.main()