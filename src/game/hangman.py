from game.gamestate import GameState
from game.word_manager import WordManager
from difficulty.difficulty import Difficulty

class Hangman:
    """Clase principal del juego de Ahorcado."""

    def __init__(self):
        self.word_manager = None
        self.game_state = None
        self.difficulty = None
        self.jugadores = []
        self.puntos = {}
        self.turno = 0  # Mantiene el turno del jugador actual


    def iniciar_juego(self):
        """Iniciar un nuevo juego."""
        # Seleccionar la dificultad
        nivel_dificultad = self.seleccionar_dificultad()
        self.difficulty = Difficulty(nivel_dificultad)

        # Obtener el archivo de palabras adecuado según la dificultad
        archivo_palabras = self.difficulty.obtener_archivo_por_dificultad()

        # Crear WordManager con el archivo correcto
        self.word_manager = WordManager(archivo_palabras)

        # Solicitar nombres de los jugadores
        for i in range(2):
            nombre = input(f"Introduce el nombre del Jugador {i+1}: ")
            self.jugadores.append(nombre)
            self.puntos[nombre] = 0

    def calcular_puntos(self, jugador, letras_adivinadas, errores):
        """Calcular los puntos del jugador basados en aciertos y errores."""
        puntos_letras = len(letras_adivinadas)  # Un punto por cada letra adivinada correctamente
        penalizacion_errores = errores * 2  # Restar 2 puntos por cada error
        bonificacion_palabra = 5  # Bonificación por completar la palabra

        return max(0, puntos_letras - penalizacion_errores + bonificacion_palabra)

    def jugar_turno(self, palabra, pistas):
        """El juego alterna entre los jugadores hasta que se adivina la palabra."""
        self.game_state = GameState(palabra, pistas)
        
        while not self.game_state.juego_terminado():
            jugador_actual = self.jugadores[self.turno]
            print(f"\nTurno de {jugador_actual}")
            print(f"\nPalabra: {self.game_state.mostrar_estado()}")
            print(f"Letras incorrectas: {', '.join(self.game_state.letras_incorrectas)}")
            print(f"Intentos restantes: {self.game_state.intentos_restantes}")
            
            letra = input(f"{jugador_actual}, adivina una letra: ").upper()

            # Validar entrada
            if len(letra) != 1 or not letra.isalpha():
                print("Por favor, ingresa una única letra válida.")
                continue

            # Intentar adivinar la letra
            resultado = self.game_state.adivinar_letra(letra)
            print(resultado)

            # Verificar si el jugador adivinó toda la palabra
            if self.game_state.ganado:
                print(f"¡Felicidades {jugador_actual}! Adivinaste la palabra: {self.game_state.palabra}")
                puntos = self.calcular_puntos(jugador_actual, self.game_state.letras_adivinadas, len(self.game_state.letras_incorrectas))
                self.puntos[jugador_actual] += puntos
                print(f"{jugador_actual} ganó {puntos} puntos en esta palabra.")
                break  # Termina el turno porque la palabra fue adivinada
            else:
                # Cambiar turno al otro jugador
                self.turno = (self.turno + 1) % 2

    def jugar(self):
        """Ciclo principal del juego."""
        self.iniciar_juego()

        # Obtener todas las palabras del archivo
        palabras_y_pistas = self.word_manager.seleccionar_todas_las_palabras()

        # Jugar con todas las palabras
        for palabra, pista1, pista2, pista3 in palabras_y_pistas:
            print("\nNueva palabra para adivinar:")
            self.jugar_turno(palabra, [pista1, pista2, pista3])
            # Mostrar el puntaje actual después de cada palabra adivinada
            print(f"Puntaje actual: {self.jugadores[0]} - {self.puntos[self.jugadores[0]]} | {self.jugadores[1]} - {self.puntos[self.jugadores[1]]}")

        # Determinar el ganador
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
