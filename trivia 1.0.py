# Importar la funcion choice
from random import choice
# Pedir el nombre del usuario
nombre = str(input("nombre del jugador: "))
# categorias
categoria = ["ciencia","historia"]
# Preguntas por categoria con sus opciones de respuesta
preguntas_ciencia = [("¿que es la fotosintesis?\n a.Proceso mediante el cual la planta tomo el color verde\n b.Proceso mediante el cual la planta fabrica su propio alimento", "b"), ("¿Como se le llama al animal que come carne?\n a.Carnivoro\n b.Herviboro", "a"), ("¿que es la ausencia de todos los colores?\n a.El color blanco\n b.El color negro", "b"), ("¿Que es el H20?\n a.Es agua\n b.Es monoxido de carbono", "a"), ("¿Cual es el organo mas grande del cuerpo?\n a.Son los dientes\n b.Es la piel", "b"), ("¿Que es un mamifero?\n a.Un animal que pone huevos\n b.El animal que da de lactar", "b"), ("¿Cuales son los estados de la materia?\n a.solido, liquido, gaseoso\n b.agua, hielo, aire", "a"), ("La luna es...\n a.una roca\n b.un satelite","b"), ("¿de que fruta se obtiene el vino tradicionalmente?\n a.de la pera\n b.de la uva","b"), ("¿Como se llama el proceso mediente el cual el liquido pasa a estado solido?\n a.condensacion\n b.evaporacion", "a")]
preguntas_historia = [("¿En que año se inicio la primera guerra mundial\n a.1916\n b.1939", "a"), ("¿quien fundo KFC?\n a.Sanders Pete Harman\n b.Donald Trump", "a"), ("¿Cómo se llamaban los gobernantes del antiguo Egipto?\n a.rey\n b.faraon", "b"), ("¿Cuál de estos emperadores fue alumno del filósofo griego Aristóteles?\n a.Alejandro Magno\n b.Platon", "a"), (" Los samuráis eran:\n a.cocineros\n b.guerreros", "b"), ("¿Cuál idioma hablaban los aztecas?\n a.nahualt\n b.español", "a"), ("¿Cuál de estos libros fue escritos por William Shakespeare?\n a.la ilíada\n b.romeo y julieta", "b"), ("¿Cuándo comenzó la Revolución Francesa?\n a.5 mayo de 1789\n b.25 de abril de 1811", "a"), ("¿Cuándo fueron lanzadas las bombas atómicas de Hiroshima y Nagasaki?\n a.6 de agosto de 1945 - 9 de agosto de 1945\n b.9 de mayo de 1945 - 11 de abril de 1945", "a"), ("¿En que fecha cayo el muro de berlin?\n a.9 de noviembre de 1989\n b.18 de diciembre de 1979", "a")]
# variable para guardar el numero de respuestas correctas
respuestas_correctas = 0
# Escoger una categoria al azar, Choice para letras(cadenas de caracteres) y guardarlo en la variable para despues alternar la categoria
variable_categoria = (choice(categoria))

   # bucle for para imprimir las preguntas aleatoriamente
for m in range(20):
    # print Para saber la categoria
    print(variable_categoria)
    # If para preguntar imprimir las preguntas para la categoria ciencia
    if variable_categoria == "ciencia":
      
     # escoger pregunta aleatoria y guardarlo en la variable (arreglo)
     pregunta_ciencia_actual = (choice(preguntas_ciencia))
     #imprimir la pregunta aleatoria
     print(pregunta_ciencia_actual[0])
     # solicitar la respuesta al usuario
     respuesta_actual = str(input("indique su respuesta entre a y b: "))

     # comprobar si la respuesta es correcta
     if respuesta_actual == pregunta_ciencia_actual[1]:
       respuestas_correctas+=1
       print(f"felicidades por la respuesta correcta {nombre}")
     else:
       print("la respuesta es incorrecta")
       # remover la pregunta y respuesta ya utilizada opara que no se repita
     preguntas_ciencia.remove(pregunta_ciencia_actual)

    # If para imprimir las preguntas de la categoria historia 
    if variable_categoria == "historia":
      # escoger pregunta aleatoria
      pregunta_historia_actual = (choice(preguntas_historia))
      #imprimir la pregunta aleatoria
      print(pregunta_historia_actual[0])

      # solicitar la respuesta al usuario
      respuesta_actual = str(input("indique su respuesta entre a y b: "))
      if respuesta_actual == pregunta_historia_actual[1]:
        respuestas_correctas+=1
        print(f"felicidades por la respuesta correcta {nombre}")
      else:
        print("la respuesta es incorrecta")
      preguntas_historia.remove(pregunta_historia_actual)
      
   # Pregunta para saber si continuar en el juego o terminar
    i = int(input("¿quiere continuar? 1 para no. 0 para si: "))

    if i== 1:
     break
   # Para calternar entre ctegorias despues de cada pregunta
    if variable_categoria == categoria[0]:
      variable_categoria = categoria[1]
    else:
      variable_categoria = categoria[0]
      # para saber si el ususario tuvo todas las preguntas bien
if respuestas_correctas == 20:
    print(f"felicidades {nombre}, obtuviste una puntuacion perfecta")
   # Variable para salir del bucle while si se completan todas la preguntas
print(f"gracias por jugar {nombre}")