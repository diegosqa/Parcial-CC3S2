import random

class GameState:
    def __init__(self, palabra, pistas):
        self.palabra = palabra
        self.pistas = pistas
        self.letras_adivinadas = set()
        self.letras_incorrectas = set()
        self.intentos_restantes = 6
        self.pistas_mostradas = 0
        self.ganado = False
        self.revelar_letras_iniciales()

    def revelar_letras_iniciales(self):
        if len(self.palabra) <= 4:
            letras_a_revelar = random.sample(self.palabra, k=1)
        else:
            letras_a_revelar = random.sample(self.palabra, k=min(3, len(self.palabra)))
        self.letras_adivinadas.update(letras_a_revelar)

    def mostrar_estado(self):
        return ' '.join([letra if letra in self.letras_adivinadas else '_' for letra in self.palabra])

    def adivinar_letra(self, letra):
        letra = letra.upper()

        if letra in self.letras_adivinadas or letra in self.letras_incorrectas:
            return f"Ya has adivinado la letra '{letra}'"

        if letra in self.palabra:
            self.letras_adivinadas.add(letra)
            if self.palabra_completa():
                self.ganado = True
            return f"\nCorrecto! La letra '{letra}' esta en la palabra"
        else:
            self.letras_incorrectas.add(letra)
            self.intentos_restantes -= 1
            self.mostrar_pista() 
            return f"La letra '{letra}' no esta en la palabra"

    def mostrar_pista(self):
        if self.pistas_mostradas < len(self.pistas):
            print(f"Pista {self.pistas_mostradas + 1}: {self.pistas[self.pistas_mostradas]}")
            self.pistas_mostradas += 1

    def palabra_completa(self):
        return all(letra in self.letras_adivinadas for letra in self.palabra)

    def juego_terminado(self):
        return self.ganado or self.intentos_restantes <= 0