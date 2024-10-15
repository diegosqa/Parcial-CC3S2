import pytest
from game.gamestate import GameState

@pytest.fixture
def gamestate():
    return GameState("PALABRA", ["Pista_1", "Pista_2", "Pista_3"])

def test_para_inicializacion(gamestate):
    assert gamestate.palabra == "PALABRA"
    assert gamestate.intentos_restantes == 6

def test_adivinar_letra_incorrecta(gamestate):
    resultado = gamestate.adivinar_letra("C")
    assert "C" in gamestate.letras_incorrectas
    assert gamestate.intentos_restantes == 5
    assert resultado == "La letra 'C' no esta en la palabra"

def test_palabra_completa(gamestate):
    for letra in "PALABRA":
        gamestate.adivinar_letra(letra)
    assert gamestate.ganado is True