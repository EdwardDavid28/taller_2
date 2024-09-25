#Ejercicio 1
nombre="Edward"
edad=18
comida_favorita="Arroz con Pollo"

print(f"Hola! Mi nombre es {nombre}. Yo tengo {edad} años, y mi"
      f" comida favorita es {comida_favorita}")

#Ejercicio 2
nombre1=input("ingrese su nombre: ")
print(f"Hola,{nombre1}! tu nombre tiene {len(nombre1.replace(" ",""))} letras,excluyendo los espacios.")

#Ejercicio 3
porcentajedecrecimiento=12.93720081
crecimientodeingresos=18.33206078
print(f"Las ventas de la empresa lactea aumentaron un {porcentajedecrecimiento:.2f}% y los ingresos crecieron un {crecimientodeingresos:.2f}%")

#Ejercicio 4
mensajesecreto="aS!Ir waQm VL!eDafrcnXin=gS .P,yytahgoln.!"
print(f"{mensajesecreto[3:]}")

#Ejercicio 5
texto='''El nombre "Python" viene dado por la aficion de Van Rossum al grupo Monty Python.'''
print(f"Numero de palabras en la frase: {len(texto.split(" "))}")

#Ejercicio 6
digite=input("Digite su nommbre: ")
print(digite.replace("a","e"))

#Ejercicio 7
sentencia="La historia del lenguaje de programacion Python"
print(' '.join(sentencia.split(' ')[::-1]))
