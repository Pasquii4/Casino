
from re import I
import os
import sys
import random
import time 
from typing import Self

def borrar_preguntas():
    for i in range(30):
        sys.stdout.write("\033[F")  # Mueve el cursor a la línea anterior
        sys.stdout.write("\033[K")  # Borra la línea
class Casino:
    def __init__(self, ):
        self.saldo   = 1000.00
        self.apuesta = 0
        self.cartones = []
        self.crupier_carton = []
        self.numero_actual = 0
        self.numeros_sacados = []
        self.linea_hecha = False

    def mostrar_saldo(self):
        """Muestra el saldo actual del jugador."""
        print(f"Saldo actual: ${self.saldo:.2f} ")

    def comprar_carton(self):
        """Permite al jugador comprar un cartón de bingo."""
        costo_carton = 10
        if self.saldo >= costo_carton:
            self.saldo -= costo_carton
            carton = [random.sample(range(i, i+15), 5) for i in range(1, 76, 15)]
            self.cartones.append(carton)
            print("Has comprado un cartón:")
            self.mostrar_carton(carton)
        else:
            print("Saldo insuficiente para comprar un cartón.")

    def generar_carton_crupier(self):
        """Genera un cartón de bingo para el crupier."""
        carton = [random.sample(range(i, i+15), 5) for i in range(1, 76, 15)]
        self.crupier_carton = carton
        print("Cartón del crupier:")
        self.mostrar_carton(carton)

    def mostrar_carton(self, carton):
        """Muestra el cartón de bingo de forma legible."""
        for fila in carton:
            print("\t".join(map(str, fila)))

    def sacar_numero(self):
        """Saca un número aleatorio del bombo."""
        while True:
            numero = random.randint(1, 75)
            if numero not in self.numeros_sacados:
                self.numeros_sacados.append(numero)
                self.numero_actual = numero
                break
        print(f"Número sacado: {self.numero_actual}")
        self.marcar_cartones(numero)

    def marcar_cartones(self, numero):
        """Marca el número sacado en todos los cartones del jugador y del crupier."""
        for carton in self.cartones:
            for fila in carton:
                if numero in fila:
                    fila[fila.index(numero)] = "X"

        for fila in self.crupier_carton:
            if numero in fila:
                fila[fila.index(numero)] = "X"

    def verificar_linea(self, carton):
        """Verifica si algún cartón tiene una línea completa."""
        # Verificar filas
        for fila in carton:
            if all(x == "X" for x in fila):
                return True
        # Verificar columnas
        for i in range(5):
            if all(fila[i] == "X" for fila in carton):
                return True
        # Verificar diagonales
        if all(carton[i][i] == "X" for i in range(5)) or all(carton[i][4-i] == "X" for i in range(5)):
            return True
        return False

    def verificar_bingo(self, carton):
        """Verifica si algún cartón tiene bingo completo."""
        for fila in carton:
            if not all(x == "X" for x in fila):
                return False
        return True

    def mostrar_cartones(self):
        """Muestra todos los cartones del jugador y del crupier."""
        print("\nTus cartones:")
        for carton in self.cartones:
            self.mostrar_carton(carton)
            print()

        print("Cartón del crupier:")
        self.mostrar_carton(self.crupier_carton)
        print()

    def jugarbingo(self):
        """Método principal para iniciar el juego de Bingo."""
        print("¡Bienvenido al Bingo del Casino! 🎉")
        self.generar_carton_crupier()
        while True:
            self.mostrar_saldo()
            print("1. Comprar cartón (10 euros)")
            print("2. Sacar número (presiona Enter)")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.comprar_carton()
            elif opcion == "2" or opcion == "":
                if self.cartones:
                    self.sacar_numero()
                    self.mostrar_cartones()

                    # Verificar líneas
                    for carton in self.cartones:
                        if not self.linea_hecha and self.verificar_linea(carton):
                            self.linea_hecha = True
                            recompensa_linea = 50
                            self.saldo += recompensa_linea
                            print(f"¡Línea! Has ganado {recompensa_linea} euros.")
                    
                    if not self.linea_hecha and self.verificar_linea(self.crupier_carton):
                        self.linea_hecha = True
                        print("El crupier ha hecho una línea.")
                    
                    # Verificar bingo
                    for carton in self.cartones:
                        if self.verificar_bingo(carton):
                            recompensa_bingo = 100
                            self.saldo += recompensa_bingo
                            print(f"¡Bingo! Has ganado {recompensa_bingo} euros.")
                            self.cartones = []
                            self.numeros_sacados = []
                            self.linea_hecha = False

                    if self.verificar_bingo(self.crupier_carton):
                        print("El crupier ha ganado el Bingo. Has perdido.")
                        self.cartones = []
                        self.numeros_sacados = []
                        self.linea_hecha = False
                else:
                    print("Compra un cartón primero.")
            elif opcion == "3":
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")


    def iniciar(self):
        while True:
            borrar_preguntas()
            print("\033[1mBienvenido al casino\033[0m\n")
            print("¡Seleccione la modalidad!\n")
            print("1. Coin flip")
            print("2. Ruleta")
            print("3. Blacjack")
            print("4. ArruinaSueldos(Slots)")
            print("5. Carrera De caballos")
            print("6. Bingo")
            print("7. Salir")
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                self.coinflip()
            elif opcion == "2":
                self.ruleta()
            elif opcion == "3":
                self.blackjack()
            elif opcion == "4":
                self.jugar_slots()
            elif opcion == "5":
                self.iniciar_carrera()
            elif opcion =="6":
                self.jugarbingo()
            elif opcion == "7":
                input("\nGracias por jugar. ¡Vuelve pronto!\n")
                break
            else:
                print("\nOpción no válida. Inténtalo de nuevo.\n")


    def iniciar(self):
        while True:
            borrar_preguntas()
            print("\033[1mBienvenido al casino\033[0m\n")
            input("Pulse Enter Para Iniciar: ")
            self.jugarbingo()

casino = Casino()

casino.iniciar()