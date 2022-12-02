def calcularResultado(operacion):
	
	numero1 = int( input("\nDigite el nuemro 1: ") )
	numero2 = int( input("Digite el nuemro 2: ") )
	
	if operacion == 1:
		resultado = numero1 + numero2
	elif operacion == 2:
		resultado = numero1 - numero2
	elif operacion == 3:
		resultado = numero1 * numero2
	elif operacion == 4:
		resultado = numero1 / numero2

	return print("\nEl resultado es : " + str(resultado) + "\n")

opcion = 0

while( opcion !=5 ):
	
	print("=====================================")
	print("CALCULADORA V.1")
	print("=====================================")
	print("1. Sumar")
	print("2. Restar")
	print("3. Multiplicar")
	print("4. Dividir")
	print("5. Salir")
	print("=====================================")
	
	opcion = int(input("Seleccione una opción : "))

	if opcion == 1:
		print("=====================================")
		print("           OPERACIÓN SUMA            ")
		print("=====================================")
		calcularResultado(opcion)
	elif opcion == 2:
		print("=====================================")
		print("           OPERACIÓN RESTA           ")
		print("=====================================")
		calcularResultado(opcion)
	elif opcion == 3:
		print("=====================================")
		print("      OPERACIÓN MULTIPLICACIÓN       ")
		print("=====================================")
		calcularResultado(opcion)
	elif opcion == 4:
		print("=====================================")
		print("        OPERACIÓN DIVISIÓN           ")
		print("=====================================")
		calcularResultado(opcion)
	elif opcion == 5:
		print("Saliendo del programa...")
	else:
		print("La opción ingresada es invalida")