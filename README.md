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

**Explicación**
Función factorial.

*Hipótesis:*

La función factorial calcula el factorial de un número entero no negativo, utilizando un enfoque recursivo. El factorial de un número n, denotado como n!
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
