# ALGORITMOS 2 Maria Muñoz
## Recursividad
**Código:**

def factorial(n):
    
    # Caso base: el factorial de 0 es 1
    if n == 0:
        return 1
    # Paso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

**Explicación función factorial.**

*Hipótesis:*

La función factorial calcula el factorial de un número entero no negativo, utilizando un enfoque recursivo. El factorial de un número n, denotado como
n!, es el producto de todos los números enteros positivos desde 1 hasta n.

*Entrada:*

n: Un entero no negativo, es el número del cual se calculará el factorial.

*Salida:*

Un entero que representa el factorial del numero ingresado.

*Precondición:*

n debe ser un número entero no negativo.

*Poscondición:*

El valor de retorno garantiza ser el factorial de n. Para n = 0, el factorial es definido como 1.

*Efecto:*

La función no modifica ninguna variable global ni altera ningún estado fuera de su ámbito. La función simplemente realiza cálculos y retorna un resultado.

## Ordenación

**Bubble Sort**

1- ¿Qué es?

Bubble sort es un método muy común para organizar listas.La idea es revisar la lista de inicio a fin, intercambiando elementos que están en el orden incorrecto, y repetir el proceso hasta que no se necesiten más cambios y la lista esté ordenada.

2- ¿Cómo funciona?

Empieza al principio de la lista y compara los dos primeros elementos. Si el primer elemento es mayor que el segundo, los intercambia (esto coloca el número más grande en la posición más alta de los dos). Esto se repite para cada par de elementos hasta el final de la lista.
Después de una pasada completa por la lista, el proceso se inicia de nuevo desde el principio. Con cada ciclo completo, el próximo número más grande queda en su posición correcta al final de la lista.
Si en una pasada completa no se hace ningún intercambio, significa que la lista ya está ordenada y el proceso puede terminar.

3- ¿Cuándo es útil usarlo?

Bubble Sort no es muy rápido con listas grandes o muy desordenadas. Sin embargo, es útil cuando la lista es pequeña o la lista está casi ordenada

4- Ejemplo Conceptual.

Números para ordenar: [34, 7, 23, 32, 5]

Pasada 1:

Compara 34 y 7, intercambia porque 34 es mayor que 7: [7, 34, 23, 32, 5]

Compara 34 y 23, intercambia porque 34 es mayor que 23: [7, 23, 34, 32, 5]

Compara 34 y 32, intercambia porque 34 es mayor que 32: [7, 23, 32, 34, 5]

Compara 34 y 5, intercambia porque 34 es mayor que 5: [7, 23, 32, 5, 34]

Ahora el número más grande (34) está al final y ya está en su lugar correcto. Se repite este proceso para todos los elementos hasta que la lista esté completamente ordenada.

Iteración 2:

Comparar 7 y 23: no intercambiar

Comparar 23 y 32: no intercambiar

Comparar 32 y 5: intercambiar (lista: [7, 23, 5, 32, 34])

Iteración 3:

Comparar 7 y 23: no intercambiar

Comparar 23 y 5: intercambiar (lista: [7, 5, 23, 32, 34])

Iteración 4:

Comparar 7 y 5: intercambiar (lista: [5, 7, 23, 32, 34])

Ahora la lista está ordenada: [5, 7, 23, 32, 34].














