# Parcial-CC3S2

# Integracion de las Palabras
Se creo y implemento las palabras segun la dificultad elegida por el jugador 
con sus respectivas pistas de acuerdo al numero de intentos

- **Words Easy**  
Palabras comunes y faciles de adivinar, tales como:  
**`CASA`**  
`Pistas:`
  - Es un lugar donde vives.    
  - Tiene paredes y un techo.  
  - La mayoría de las personas duermen aquí.

- **Words Medium**  
Palabras no tan comunes pero aumenta la dificultad por la longitud.  
**`ESCUELA`**  
`Pistas:`  
  - Es un lugar de aprendizaje.  
  - Tiene aulas y maestros. 
  - Los estudiantes asisten aquí.

- **Words Hards**
Palabras raramente comunes, ademas de la complejidad de la longitud.  
**`UNIVERSIDAD`**  
`Pistas:`  
   - Es una institución educativa superior.  
   - Ofrece licenciaturas y posgrados.
   - Los estudiantes mayores asisten aquí.  
     
# Implementación de la clase Difficulty
La siguiente clase tiene un método `obtener_archivo_por_dificultad()`, el usuario al principio ingresa la dificultadad, entonces dependiendo de eso, el método devuelve el archivo txt correspondiente que tiene todas las palabras correspondientes a esa dificultad.  
  
![](img/DifficultyClass.png)  
  
# Implementación de la clase GameStates  
Esta clase tiene como objetivo gestionar el estado del juego controlando las letras que el jugador ha adivinado correctamente o incorrectamente, los intentos restantes (en un principio el jugador tiene 6 intentos para fallar), las pistas a mostrar y si el juego a terminado o no:  
  
+ Atributos:  

  `palabra`: almacena la palabra a adivinar  
  `pistas`: pistas asociadas a la palabra a adivinar(ver los txts)  
  `letras_adividadas`: Conjunto de las letras adivinadas correctamente  
  `letras_incorrectas`: Conjunto de las letras adivinadas incorrectamente  
  `intentos_restantes`: Intentos que tiene el jugador para fallar  
  `pistas_mostradas`: Número de pistas que se han mostrado  
  `ganado`: Variable booleana que indica si el jugador a adivinado toda la palabra completa  

![](img/gameState-atributos.png)  
    
+ Función `revelar_letras_iniciales()`:  

  Cuando el juego comienze, la palabra a adivianr no va a aparecer en blanco, es decir con letras vacías pues el jugador no tendría idea que palabra se trata, por eso se muestran unas cuantas palabras para que el jugagor pueda tener algo con que adivinar  

![](img/gameState-revelar_letras.png)  
  
+ Función `mostrar_estado()`:  
Aquí se devuelve el estado de la palabra, es decir se muestra que tanto a adivinado el jugador de la palabra, por ejemplo si la palabra es `PUERTA` y el jugador solo ha adivinado P,R,T entonces el estado de la palabra será P_ _ RT _.
  
![](img/gameState-mostrar-estado.png)  
  
    
+ Función `adivinar_letra()`:  
  Esta función responde a cada adivinanza que el jugador hace, si la letra ya ha sido adivina antes (correcta o incorrectamente) le da un respectivo mensaje. Pero si la letra es correcta es decir está en la palabra entonces se muestra un mensaje respectivo, sin embargo si no está en la palabra se muestra una pista y descontamos los intentos en 1.

![](img/gameState-adivinar_letra.png)  
    
+ Función `mostrar_pista()`:  
Esta función muestra la pista cada vez que el jugador ha fallado al momento de adivinar una palabra, además el numero de pistas mostradas se incremete para no repetir las mismas pistas  

![](img/gameState-mostrar-pista.png)  
  
+ Función `palabra_completa()`:  
Esta función verifica si el jugador ya ha adivinado todas las palabras, devolvéra True si eso es cierto, pero False si aun no ha terminado de adivinar toda la palabra   
  
![](img/gameState-palabra-completa.png)
  
+ Función `juego_terminado()`:  
Esta función verifica si el juego ya ha terminado, esto es si el jugador ya ha ganado el juego o si su numero de intentos se han acabado  
  
![](img/gameState-juego-terminado.png)