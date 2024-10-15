import pytest
from game.word_manager import WordManager

@pytest.fixture
def word_manager():
    return WordManager('words_medium.txt')

def testCargarPalabras(word_manager):
    assert len(word_manager.palabras_con_pistas) > 0
    
def testSeleccionarPalabras(word_manager):
    palabras = word_manager.seleccionar_todas_las_palabras()
    assert len(palabras) > 0
    for palabra in palabras:
        assert len(palabra) == 4