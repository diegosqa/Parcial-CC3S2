Feature: Juego de Hangman

    Scenario: Adivinar letra correcta
        Given el juego a iniciado con la palabra "MESA"
        When adivino con la letra "A"
        Then deberia ver que la letra "A" esta en la palabra

    Scenario: Adivinar letra incorrecta
        Given el juego a iniciado con la palabra "MESA"
        When adivino con la letra "B"
        Then deberia ver que la letra "B" no esta en la palabra

    Scenario: Adivinar la palabra completa
        Given el juego a iniciado con la palabra "MESA"
        When adivino con la letra "M"
        And adivino con la letra "E"
        And adivino con la letra "S"
        And adivino con la letra "A"
        Then deberia ver que he adivinado la palabra "MESA"

    Scenario: Gastar todos los intentos y perder el juego
        Given el juego a iniciado con la palabra "SOL"
        When adivino con la letra "X"
        And adivino con la letra "Y"
        And adivino con la letra "Z"
        And adivino con la letra "D"
        And adivino con la letra "E"
        And adivino con la letra "C"
        Then deberia perder el juego