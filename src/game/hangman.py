from game.gamestate import GameState
from game.word_manager import WordManager
from difficulty.difficulty import Difficulty

class Hangman:

    def __init__(self):
        self.word_manager = None
        self.game_state = None
        self.difficulty = None
        self.jugadores = []
        self.puntos = {}
        self.turno = 0  

    def seleccionar_dificultad(self):
        print("Selecciona un nivel de dificultad:")
        print("1. Fácil (4-6 letras)")
        print("2. Medio (7-9 letras)")
        print("3. Difícil (10 letras o más)")

        nivel = input("Introduce el número de la dificultad: ")

        if nivel == '1':
            return 'fácil'
        elif nivel == '2':
            return 'medio'
        elif nivel == '3':
            return 'difícil'
        else:
            print("Opción inválida, empieza en nivel facil")
            return 'fácil'
    
    def iniciar_juego(self):
      
      
        nivel_dificultad = self.seleccionar_dificultad()
        self.difficulty = Difficulty(nivel_dificultad)

       
        archivo_palabras = self.difficulty.obtener_archivo_por_dificultad()

       
        self.word_manager = WordManager(archivo_palabras)

        
        for i in range(2):
            nombre = input(f"Introduce el nombre del Jugador {i+1}: ")
            self.jugadores.append(nombre)
            self.puntos[nombre] = 0

    def calcular_puntos(self, jugador, letras_adivinadas, errores):
      
        puntos_letras = len(letras_adivinadas)  
        penalizacion_errores = errores * 2 
        bonificacion_palabra = 5  

        return max(0, puntos_letras - penalizacion_errores + bonificacion_palabra)

    def jugar_turno(self, palabra, pistas):
        
        self.game_state = GameState(palabra, pistas)
        
        while not self.game_state.juego_terminado():
            jugador_actual = self.jugadores[self.turno]
            print(f"\nTurno de {jugador_actual}")
            print(f"\nPalabra: {self.game_state.mostrar_estado()}")
            print(f"Letras incorrectas: {', '.join(self.game_state.letras_incorrectas)}")
            print(f"Intentos restantes: {self.game_state.intentos_restantes}")
            
            letra = input(f"{jugador_actual}, adivina una letra: ").upper()

            
            if len(letra) != 1 or not letra.isalpha():
                print("Por favor, ingresa una única letra válida.")
                continue

           
            resultado = self.game_state.adivinar_letra(letra)
            print(resultado)

         
            if self.game_state.ganado:
                print(f"¡Felicidades {jugador_actual}! Adivinaste la palabra: {self.game_state.palabra}")
                puntos = self.calcular_puntos(jugador_actual, self.game_state.letras_adivinadas, len(self.game_state.letras_incorrectas))
                self.puntos[jugador_actual] += puntos
                print(f"{jugador_actual} ganó {puntos} puntos en esta palabra.")
                break  # Termina el turno porque la palabra fue adivinada
            else:
              
                self.turno = (self.turno + 1) % 2

    def jugar(self):
       
        self.iniciar_juego()

     
        palabras_y_pistas = self.word_manager.seleccionar_todas_las_palabras()

       
        for palabra, pista1, pista2, pista3 in palabras_y_pistas:
            print("\nNueva palabra para adivinar:")
            self.jugar_turno(palabra, [pista1, pista2, pista3])
            # Mostrar el puntaje actual después de cada palabra adivinada
            print(f"Puntaje actual: {self.jugadores[0]} - {self.puntos[self.jugadores[0]]} | {self.jugadores[1]} - {self.puntos[self.jugadores[1]]}")

      
        print("\nResultados finales:")
        print(f"Puntaje final de {self.jugadores[0]}: {self.puntos[self.jugadores[0]]}")
        print(f"Puntaje final de {self.jugadores[1]}: {self.puntos[self.jugadores[1]]}")

        if self.puntos[self.jugadores[0]] > self.puntos[self.jugadores[1]]:
            print(f"¡{self.jugadores[0]} gana!")
        elif self.puntos[self.jugadores[1]] > self.puntos[self.jugadores[0]]:
            print(f"¡{self.jugadores[1]} gana!")
        else:
            print("¡Es un empate!")

if __name__ == "__main__":
    juego = Hangman()
    juego.jugar()
