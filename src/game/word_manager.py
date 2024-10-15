import random

class WordManager:
    def __init__(self, archivo):
        self.archivo = archivo
        self.palabras_con_pistas = self.cargar_palabras()
    
    def cargar_palabras(self):
        with open(self.archivo, 'r', encoding = 'utf-8') as f:
            palabras = f.readlines()
        return [linea.strip().split(',') for linea in palabras]
    
    def seleccionar_todas_las_palabras(self):
        return random.sample(self.palabras_con_pistas, len(self.palabras_con_pistas))