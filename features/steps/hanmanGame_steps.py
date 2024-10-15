from behave import given,when,then
from game.gamestate import GameState

@given('el juego a iniciado con la palabra "{palabra}"')
def step_iniciar_juego(context,palabra):
    context.game = GameState(palabra,["Pista_1", "Pista_2", "Pista_3"])

@when('adivino con la letra "{letra}"')
def step_adivinar_letra(context,letra):
    context.resultado = context.game.adivinar_letra(letra)

@then('deberia ver que la letra "{letra}" esta en la palabra')
def step_ver_letra_esta_en_palabra(context,letra):
    assert letra in context.game.letras_adivinadas
    assert context.resultado == f"\nCorrecto! La letra '{letra}' esta en la palabra"

@then('deberia ver que la letra "{letra}" no esta en la palabra')
def step_ver_letra_no_esta_en_palabra(context,letra):
    assert letra in context.game.letras_incorrectas
    assert context.resultado ==  f"La letra '{letra}' no esta en la palabra"

@then('deberia ver que he adivinado la palabra "{palabra}"')
def step_ver_he_adivinado_palabra(context,palabra):
    assert context.game.ganado is True
    assert context.game.palabra == palabra

@then('deberia perder el juego')
def step_perder_juego(context):
    assert context.game.intentos_restantes == 0
    assert context.game.ganado is False