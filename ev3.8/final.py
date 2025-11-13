meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo",
         "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
         "Noviembre", "Diciembre")

numn_mes =int(input("Ingrese un numero del 1 al 12: "))

if 1 <= numn_mes <= 12:
    print("El mes correspondiente es {meses[num_mes - 1]}")
else:
    print("Numero invalido.")
