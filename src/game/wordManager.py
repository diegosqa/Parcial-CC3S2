import random

class WordManager:
    def __init__(self, archivo):
        self.archivo = archivo
        self.pistas = self.cargarPalabras()
    
    def cargarPalabras(self):
        with open(self.archivo, 'r', encoding = 'utf-8') as f:
            palabras = f.readlines()
        return [linea.strip().split(',') for linea in palabras]
    
    def seleccionarPalabras(self):
        return random.sample(self.pistas, len(self.pistas))