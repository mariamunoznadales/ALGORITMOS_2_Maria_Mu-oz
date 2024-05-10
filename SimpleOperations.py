import functools
""" 
Se crea una instancia de SimpleOperations
operations = SimpleOperations()

Se configuran funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
twenty_percent_discount 
vat_tax

Se usan las funciones preconfiguradas.
"""

class SimpleOperations:
    def apply_discount(self, price, discount):
        """
        Método para aplicar un descuento al precio dado.
        """
        discounted_price = price * (1 - discount)
        return discounted_price

    def calculate_tax(self, price, tax_rate):
        """
        Método para calcular el precio con impuestos.
        """
        price_with_tax = price * (1 + tax_rate)
        return price_with_tax

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
descuento_veinte = functools.partial(operations.apply_discount, discount=0.20)
vat_tax = functools.partial(operations.calculate_tax, tax_rate=0.21)  

# Usar las funciones preconfiguradas.
precio = 100

# Aplicar un descuento del 20%
precio_final_descuento_20 = descuento_veinte(precio)
print("Precio final con descuento del 20%:", precio_final_descuento_20)

# Calcular el precio con una tasa de impuesto del 21%
precio_final_impuesto_21 = vat_tax(precio)
print("Precio final con impuesto del 21%:", precio_final_impuesto_21)
