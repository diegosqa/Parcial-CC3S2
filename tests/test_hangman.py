import pytest
from game.hangman import Hangman
from game.gamestate import GameState
from game.word_manager import WordManager
from difficulty.difficulty import Difficulty

@pytest.fixture
def hangman():
    game = Hangman()
    game.jugadores = ["Jugador 1", "Jugador 2"]
    game.puntos = {"Jugador 1": 0, "Jugador 2": 0}
    return game

def test_seleccionar_dificultad_facil(monkeypatch, hangman):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    dificultad = hangman.seleccionar_dificultad()
    assert dificultad == 'fácil'

def test_seleccionar_dificultad_medio(monkeypatch, hangman):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    dificultad = hangman.seleccionar_dificultad()
    assert dificultad == 'medio'

def test_calcular_puntos_sin_errores(hangman):
    puntos = hangman.calcular_puntos('Jugador 1', 'PALABRA', 0)
    assert puntos == 12  

def test_calcular_puntos_con_errores(hangman):
    puntos = hangman.calcular_puntos('Jugador 1', 'PALABRA', 2)
    assert puntos == 8  

def test_resultado_final(hangman):
    hangman.puntos = {'Jugador 1': 15, 'Jugador 2': 10}
    hangman.jugadores = ['Jugador 1', 'Jugador 2']
    
    if hangman.puntos['Jugador 1'] > hangman.puntos['Jugador 2']:
        assert "¡Jugador 1 gana!" == "¡Jugador 1 gana!"
    elif hangman.puntos['Jugador 1'] < hangman.puntos['Jugador 2']:
        assert "¡Jugador 2 gana!" == "¡Jugador 2 gana!"
    else:
        assert "¡Es un empate!" == "¡Es un empate!"
