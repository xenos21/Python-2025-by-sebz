num1 = float(input("Ingrese el primer numero"))
num2 = float(input("Ingrese el segundo numero"))

print(f"suma: {num1 + num2 }")
print(f"resta: {num1 - num2 }")
print(f"multiplicacion: {num1 * num2 }")
print(f"division: {num1 / num2 if num2 != 0 else 'No se puede dividir entre 0'}")
