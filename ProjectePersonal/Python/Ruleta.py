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
    
    def ruleta(self):
        while True:
            borrar_preguntas()

            try:
                borrar_preguntas()
                print("\033[1mRuleta\033[0m \n")
                print(f"Su saldo actual es: ${self.saldo}")
                apuesta = float(input("Ingresa tu apuesta (o escribe 0 para salir): "))
                if apuesta == 0:
                    input("\nPulse Enter para salir. \n")
                    break
                if apuesta > self.saldo or apuesta <= 0:
                    input("\nLa apuesta no es válida. Asegúrate de que posea ese dinero. \n")
                    continue

                print("Opciones de apuesta:")
                print("1. Número específico (0-36)")
                print("2. Color (Rojo/Negro)")
                print("3. Par o impar")
                tipo_apuesta = input("Elige el tipo de apuesta: ").strip()

                if tipo_apuesta == "1":
                    numero = input("Elige un número (0-36): ").strip()
                    if not numero.isdigit() or not (0 <= int(numero) <= 36):
                        input("\nNúmero no válido. Debes elegir un número entre 0 y 36.\n")
                        continue
                    resultado = random.randint(0, 36)
                    borrar_preguntas()
                    print(f"Su apuesta es ${apuesta} a {numero}")
                    print(f"\nLa ruleta cayó en el número {resultado}.\n")
                    if int(numero) == resultado:
                        self.saldo += apuesta * 35  # Paga 35:1
                        input(f"\033[1m\n¡Ganaste! \n\033[0mTu nuevo saldo es: ${self.saldo:.2f}\033[0m\n")
                    else:
                        self.saldo -= apuesta
                        input(f"\033[1m\nPerdiste...\n\033[0mTu nuevo saldo es: ${self.saldo:.2f}\n")

                elif tipo_apuesta == "2":
                    color = input("Elige un color (rojo/negro): ").strip().lower()
                    if color not in ["rojo", "negro"]:
                        input("\nColor no válido. Debes elegir 'rojo' o 'negro'.\n")
                        continue
                    resultado = random.choice(["rojo", "negro"])
                    borrar_preguntas()
                    print(f"Su apuesta es ${apuesta} a {color}")
                    print(f"\nLa ruleta cayó en el color {resultado}.\n")
                    if color == resultado:
                        self.saldo += apuesta
                        input(f"\033[1m\n¡Ganaste!\n\033[0mTu nuevo saldo es: ${self.saldo:.2f}\033[0m\n")
                    else:
                        self.saldo -= apuesta
                        input(f"\033[1m\nPerdiste... \n\033[0mTu nuevo saldo es: ${self.saldo:.2f}\033[0m\n")

                elif tipo_apuesta == "3":
                    paridad = input("Elige par o impar: ").strip().lower()
                    if paridad not in ["par", "impar"]:
                        input("\nOpción no válida. Debes elegir 'par' o 'impar'.\n")
                        continue
                    resultado = random.randint(0, 36)
                    borrar_preguntas()
                    print(f"Su apuesta es ${apuesta} a {paridad}")
                    print(f"\nLa ruleta cayó en el número {resultado}.\n")
                    if (resultado % 2 == 0 and paridad == "par") or (resultado % 2 != 0 and paridad == "impar"):
                        self.saldo += apuesta
                        input(f"\033[1m\n¡Ganaste!\n\033[0mTu nuevo saldo es: ${self.saldo:.2f}\033[0m\n")
                    else:
                        self.saldo -= apuesta
                        input(f"\033[1m\nPerdiste... \n\033[0mTu nuevo saldo es: ${self.saldo:.2f}\033[0m\n")

                else:
                    input("\nTipo de apuesta no válido. Inténtalo de nuevo.\n")

                if self.saldo <= 0:
                    input("\n\033[1mSaldo insuficiente. Saliendo de Ruleta...\033[0m\n")
                    break

            except ValueError:
                input("\nEntrada inválida. Ingresa un número válido.\n")
    def iniciar(self):
        while True:
            borrar_preguntas()
            print("\033[1mBienvenido al casino\033[0m\n")
            input("Pulse Enter Para Iniciar: ")
            self.ruleta()

casino = Casino()

casino.iniciar()