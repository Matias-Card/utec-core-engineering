# Python - Clases y modelo de objetos

## 0. Explorando objetos

Exploración de objetos de Python utilizando el intérprete interactivo (REPL). Creación de números, cadenas y listas. Uso de `type()`, `id()` y `dir()` para consultar sus clases, identidades y métodos. Pruebas de `upper()`, `replace()`, `==` e `is`.

## 1. Mi primer cuadrado

Creación de la clase `Square` sin atributos ni métodos, utilizando `pass`.

## 2. Cuadrado con tamaño

Definición de una clase `Square` con un atributo de instancia privado `__size`, cuyo valor se establece al crear el objeto mediante el constructor `__init__`, aplicando el principio de encapsulación en Python.

## 3. Validación de tamaño

Implementación de validaciones en la clase `Square` para asegurar que el atributo privado `__size` contenga un valor válido. El tamaño debe ser un número entero mayor o igual que cero. Si el valor no es un entero, se lanza una excepción `TypeError` con el mensaje `size must be an integer`. Si el valor es negativo, se lanza una excepción `ValueError` con el mensaje `size must be >= 0`. Se mantiene la encapsulación del atributo mediante el uso de `__size` y se establece `0` como valor predeterminado.

## 4. Área de un cuadrado

Implementación del método de instancia `area()` en la clase `Square`, que calcula y devuelve el área del cuadrado elevando al cuadrado la longitud de su atributo privado `__size`. Se conserva la encapsulación y las validaciones establecidas en el ejercicio anterior.


## 5. Acceder y actualizar un atributo privado

Implementación de un getter y un setter mediante los decoradores `@property` y `@size.setter` en la clase `Square`. El getter permite consultar el atributo privado `__size`, mientras que el setter permite modificarlo de forma controlada. Se mantienen las validaciones para asegurar que el tamaño sea un número entero mayor o igual que cero, lanzando `TypeError` o `ValueError` cuando corresponda. También se conserva el método `area()` para calcular el área utilizando el tamaño actualizado.


## 6. Imprimir un cuadrado

Implementación del método de instancia público `my_print()` en la clase `Square`, que imprime un cuadrado utilizando el carácter `#`. La cantidad de filas y columnas depende del valor del atributo privado `__size`. Si el tamaño es igual a cero, no se imprime ningún carácter. Se conservan los getters, setters, las validaciones y el método `area()` de los ejercicios anteriores.

