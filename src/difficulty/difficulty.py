class Difficulty:
    def __init__(self, nivel):
        self.nivel = nivel
    def obtener_archivo_por_dificultad(self):
        if self.nivel == 'fácil':
            return 'words_easy.txt'
        elif self.nivel == 'medio':
            return 'words_medium.txt'
        elif self.nivel == 'difícil':
            return 'words_hard.txt'
        else:
            raise ValueError(f"Nivel de dificultad desconocido: {self.nivel}")

