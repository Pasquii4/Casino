from re import I
import os
import sys
import random
import time 

def borrar_preguntas():
    for i in range(30):
        sys.stdout.write("\033[F")  # Mueve el cursor a la línea anterior
        sys.stdout.write("\033[K")  # Borra la línea

class Casino:

    def __init__(self):
        self.saldo = 1000.0  # Saldo

    def __init__(self, saldo_inicial=1000):
        self.saldo = saldo_inicial


    def coinflip(self):
        while True:
            borrar_preguntas()
            print("\033[1mCoin Flip\033[0m\n")
            print(f"Tu saldo actual es: ${self.saldo:.2f}")

            try:
                apuesta = float(input("Ingresa tu apuesta (o escribe 0 para salir): "))
                if apuesta == 0:
                    input("\nPulse Enter para salir. \n")
                    break
                if apuesta > self.saldo or apuesta <= 0:
                    input("\nLa apuesta no es válida. Asegúrate de que posea ese dinero. \n")
                    continue

                eleccion = input("Elige cara o cruz: ").strip().lower()
                if eleccion not in ["cara", "cruz"]:
                    input("\nElección no válida. Debes elegir 'cara' o 'cruz'. \n")
                    continue

                resultado = random.choice(["cara", "cruz"])
                print(f"\nResultado: {resultado}\n")

                if eleccion == resultado:
                    self.saldo += apuesta
                    input(f"\033[1m\n¡Ganaste!\n\033[0m Tu nuevo saldo es: ${self.saldo:.2f}\n")
                else:
                    self.saldo -= apuesta
                    input(f"\033[1m\nPerdiste...\n\033[0m Tu nuevo saldo es: ${self.saldo:.2f}\n")

                if self.saldo <= 0:
                    input("\n\033[1mSaldo insuficiente. Saliendo de Coin Flip...\033[0m\n")
                    break

            except ValueError:
                print("\nEntrada inválida. Ingresa un número válido.\n")

    def iniciar(self):
        while True:
            borrar_preguntas()
            print("\033[1mBienvenido al casino\033[0m\n")
            input("Pulse Enter Para Iniciar: ")
            self.coinflip()

casino = Casino()

casino.iniciar()