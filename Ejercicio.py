# Hacer el diagrama de flujo y el programa en python, que lea un capital c, 
# y que averigue e imprima en cuanto meses se  duplica, si lo colocamos a un interes 
# compuesto del 5 % mensual.

print("---------------------------------")
print("----------- Mes_duplicado--------")
print("---------------------------------")

capital = int(input("Valor de la capital inicial que desee invertir: "))
doble = capital * 2
meses = 0

while capital <= doble:
    capital = capital + (capital * 0.05)
    meses += 1

print("La cantidad de meses necesarios para duplicar el capital inicial es de " + str(meses) + " meses.")