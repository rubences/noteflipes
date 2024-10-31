# noteflipes

Ejercicio 1 (1 punto) Tiempo estimado: 5 minutos. Responda a las cuestiones:


¿Qué es la encapsulación en la programación orientada a objetos? 
a) Es la capacidad de un objeto de tomar muchas formas. 
# b) Es el mecanismo que permite ocultar la información al exterior, controlando el acceso a los datos de un objeto.   

¿Qué es el polimorfismo en programación orientada a objetos?
# a) La capacidad de una función de tomar múltiples formas, permitiendo que diferentes clases respondan a la misma interfaz.
b) La capacidad de una clase de heredar métodos y propiedades de otra clase.

¿Cuál es el propósito de la función super() en una clase derivada?
# a) Llamar a un método de la clase base desde la clase derivada.
b) Definir un método estático en la clase derivada.

¿Qué es una excepción? 
a) Un error que ocurre durante la ejecución del programa. 
# b) Una situación anormal que puede ser manejada por el programa para evitar que se interrumpa su ejecución.

¿Qué significa sobrescribir un método heredado en una clase derivada?
# a) Definir un nuevo método en la clase derivada con el mismo nombre y parámetros que un método en la clase base, reemplazando su comportamiento.
b) Utilizar el método super() para llamar al método de la clase base desde la clase derivada.

Ejercicio 2  (1 punto) Tiempo estimado: 10 minutos. Desarrolla una función recursiva que calcule la suma de los dígitos de un número entero positivo dado. No se permite convertir el número a una cadena de caracteres para resolver el problema.	

Ejemplo de entrada y salida:
Entrada: 573
Salida: 15
(Explicación: 5+7+3=15)

Ejercicio 1 (1 punto) Tiempo estimado: 10 minutos. Dado del siguiente código	


Describa la utilidad de las funciones recursivas “funct1” y “funct2”.
Explicación
funct1: Calcula cuántas veces b cabe en a restando b repetidamente de a hasta que a sea menor que b. Imprime "value 0" cuando a < b y retorna 0, sumando 1 por cada llamada recursiva.
funct2: Resta b de a recursivamente hasta que a sea menor que b. Imprime el valor de a cuando a < b y retorna a.
Ambas funciones utilizan recursión para descomponer el problema en subproblemas más pequeños, pero funct1 cuenta las iteraciones mientras que funct2 simplemente retorna el valor final de a.
Responda el resultado que aparecerá por la línea de comandos:
Resultado 1:
Resultado 2:
Resultado 3:
Resultado 4:

Ejercicio 3 (1,5 puntos): 15 minutos. Determine el número de elementos examinados en el peor caso posible para la siguiente secuencia:

Para los siguientes métodos:
Búsqueda secuencial.
Búsqueda binaria.


La secuencia se descoloca. Indique la complejidad de los siguientes métodos para ordenar la siguiente secuencia, comentando brevemente el funcionamiento de cada uno:

Método de la burbuja.
Método de inserción.
Método de selección.
Quicksort, siempre se coge el primer número de cada división.

Ejercicio  ( 1,5 puntos): 20 minutos. 
Descripción: En este ejercicio, deberás demostrar tu comprensión de las estructuras de datos en Python, específicamente listas y diccionarios. Se te proporcionará una lista de estudiantes con sus respectivas calificaciones en diferentes asignaturas. Tu tarea será procesar esta información para obtener un resumen de las calificaciones.
Enunciado: Dada la siguiente lista de diccionarios, donde cada diccionario representa a un estudiante y sus calificaciones en varias asignaturas:
estudiantes = [
    {"nombre": "Ana", "matematicas": 85, "literatura": 78, "ciencias": 92},
    {"nombre": "Luis", "matematicas": 90, "literatura": 88, "ciencias": 95},
    {"nombre": "Marta", "matematicas": 76, "literatura": 85, "ciencias": 80},
    {"nombre": "Juan", "matematicas": 92, "literatura": 70, "ciencias": 85}
]
Parte Teórica:
Explica brevemente las diferencias entre una lista y un diccionario en Python.
¿Cuándo es más apropiado usar una lista y cuándo un diccionario?

Parte Práctica:
Escribe una función calcular_promedio_estudiantes(estudiantes) que reciba la lista de estudiantes y retorne una nueva lista de diccionarios, donde cada diccionario incluya el nombre del estudiante y su calificación promedio en todas las asignaturas.

Ejemplo de salida esperada:
promedios = calcular_promedio_estudiantes(estudiantes)
print(promedios)
# [{'nombre': 'Ana', 'promedio': 85.0}, {'nombre': 'Luis', 'promedio': 91.0}, {'nombre': 'Marta', 'promedio': 80.33}, {'nombre': 'Juan', 'promedio': 82.33}]

Ejercicio 4: Implementación de un Sistema de Gestión de Biblioteca en Python (4 puntos)
Tiempo estimado: 60 minutos

Descripción General: La Ciudadela es el centro de conocimiento y aprendizaje en el mundo de Poniente. En este ejercicio, tu objetivo es desarrollar un sistema de gestión para la Ciudadela utilizando Python. Este sistema deberá manejar aspectos como la catalogación de pergaminos y libros, préstamos y devoluciones, y la gestión de maestres y aprendices.
Especificaciones:
Clase Pergamino:
Atributos: Cada pergamino debe tener un título, autor (puede ser un maestre o una figura histórica), tipo (representado como una cadena de texto, por ejemplo, “HISTORIA”, “PROFECIA”, “GEOGRAFIA”, “BOTANICA”, etc.), y un estado que indique si está disponible o prestado. También puede incluir un atributo “Casa” que indique a qué casa nobiliaria pertenece la información (Stark, Lannister, Targaryen, etc.).
Constructor: Debe inicializar todos los atributos necesarios.
Métodos Setters y Getters: Implemente estos métodos según la necesidad.
Método is_available(self): Debe retornar un booleano indicando si el pergamino está disponible o no.
Clase Maestre:
Atributos: Cada maestre debe tener un nombre, un rango (Maestre, Archimaestre, Gran Maestre), y una lista de pergaminos que tiene prestados.
Constructor: Debe inicializar todos los atributos necesarios.
Métodos Setters y Getters: Implemente estos métodos según la necesidad.
Método tomar_prestado(self, pergamino): Este método permite al maestre tomar prestado un pergamino. Debe verificar si el pergamino está disponible y actualizar su estado y la lista de pergaminos del maestre.
Método devolver_pergamino(self, pergamino): Este método permite al maestre devolver un pergamino. Debe actualizar el estado del pergamino y la lista de pergaminos del maestre.

Ideas adicionales para extender el ejercicio:
Implementar una clase Aprendiz que herede de Maestre con atributos y métodos específicos.Implemente una clase Aprendiz que herede de la clase Maestre.
Los aprendices, además de los atributos y métodos heredados, deben tener un atributo mentor que referencie a un objeto de la clase Maestre.
Añade un método pedir_consejo(self) que actualice un contador del número de veces que se ha solicitado consejo al mentor, será un atributo..
Añadir un atributo “rareza” al pergamino (Común, Raro, Legendario) que influya en el tiempo de préstamo.
Implementar un sistema de búsqueda de pergaminos por título, autor o tipo.
Implementar un sistema de multas por retraso en la devolución de pergaminos.


Ejercicio 5: Implementación del Módulo Principal (1 puntos) Tiempo estimado: 10 minutos
Descripción General: Desarrolla un código de  prueba en Python que:
Cree una lista de pergaminos y maestres con datos de ejemplo.
Realice las siguientes acciones:
Liste todos los pergaminos disponibles.
Busque pergaminos por título, autor o tipo.
Haga que un maestre tome prestado un pergamino.
Haga que un maestre devuelva un pergamino.
Muestre la lista de pergaminos prestados a un maestre específico.
Nota: Utilice las clases de los Ejercicios 4 y 5 para implementar esta funcionalidad.
