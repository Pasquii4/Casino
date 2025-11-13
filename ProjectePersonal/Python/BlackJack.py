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
    def __init__(self, ):
        self.saldo   = 1000.00
        self.apuesta = 0

    
    def blackjack(self):
        import random

        valores_cartas = {str(i): i for i in range(2, 11)}
        valores_cartas.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})

        def valor_mano(mano):
            total = sum(valores_cartas[carta.split(' ')[0]] for carta in mano)
            ases = sum(1 for carta in mano if carta.startswith('A'))
            while total > 21 and ases:
                total -= 10
                ases -= 1
            return total

        def repartir_cartas(baraja):
            return [baraja.pop(), baraja.pop()]

        while True:
            borrar_preguntas()
            print("\033[1mBlackjack\033[0m\n")
            print("Menú\n")
            try:
                print("1. Empezar a jugar")
                print("2. Salir")
                eleccion = int(input(": "))
                if eleccion == 2:
                    input("\nPulse Enter para salir.\n")
                    break

                elif eleccion == 1:
                 try:
                    borrar_preguntas()
                    print("\033[1mBlackjack\033[0m\n")
                    print(f"Tu saldo actual es: ${self.saldo:.2f}")
                    apuesta = float(input("Ingresa tu apuesta: "))
                    if apuesta > self.saldo or apuesta <= 0:
                        input("\nLa apuesta no es válida. Asegúrate de que posea ese dinero.\n")
                        continue

                    # Crear y barajar la baraja
                    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
                    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
                    baraja = [f"{valor} de {palo}" for valor in valores for palo in palos]
                    random.shuffle(baraja)

                    jugador = repartir_cartas(baraja)
                    crupier = repartir_cartas(baraja)

                    print(f"\nCartas del jugador: {jugador} (Total: {valor_mano(jugador)})")
                    if valor_mano(jugador) == 21:
                        print("Blackjack! Ganaste!")
                        self.saldo += apuesta*1.5
                        input(f"Su nuevo saldo es ${self.saldo}")
                        continue
                    elif valor_mano(jugador) > 21:
                        print("Te pasaste de 21. Pierdes.")
                        self.saldo -= apuesta
                        input(f"Su nuevo saldo es ${self.saldo}")
                        continue

                    while True:
                        accion = input("\n¿Qué deseas hacer? (Pedir/Plantarse): ").strip().lower()
                        if accion == 'pedir':
                            jugador.append(baraja.pop())
                            print(f"Nuevas cartas: {jugador} (Total: {valor_mano(jugador)})")
                            if valor_mano(jugador) > 21:
                                print("Te pasaste de 21. Pierdes.")
                                self.saldo -= apuesta
                                input(f"Su nuevo saldo es ${self.saldo}")
                                break
                        elif accion == 'plantarse':
                            break
                        else:
                            print("Opción no válida. Por favor escribe 'Pedir' o 'Plantarse'.")

                    print(f"\nCartas del crupier: {crupier} (Total: {valor_mano(crupier)})")
                    while valor_mano(crupier) < 17:
                        crupier.append(baraja.pop())
                        print(f"Crupier toma una carta: {crupier} (Total: {valor_mano(crupier)})")

                    jugador_total = valor_mano(jugador)
                    crupier_total = valor_mano(crupier)

                    if crupier_total > 21 or jugador_total > crupier_total and valor_mano(jugador)<= 21:
                        print("\nGanaste!")
                        self.saldo += apuesta
                        input(f"Su nuevo saldo es ${self.saldo}")
                    elif jugador_total == crupier_total:
                        print("\nEmpate!")
                        input(f"Su nuevo saldo es ${self.saldo}")
                    elif jugador_total < crupier_total:
                        print("\nPierdes.")
                        self.saldo -= apuesta
                        input(f"Su nuevo saldo es ${self.saldo}")
                    

                    if self.saldo <= 0:
                        input("\n\033[1mSaldo insuficiente. Saliendo de Blackjack...\033[0m\n")
                        break
                 except ValueError:
                  print("\nEntrada inválida. Por favor, ingresa un número válido.")
                  
            except ValueError:
                print("\nEntrada inválida. Por favor, ingresa un número válido.")

    def iniciar(self):
        while True:
            borrar_preguntas()
            print("\033[1mBienvenido al casino\033[0m\n")
            input("Pulse Enter Para Iniciar: ")
            self.blackjack()

casino = Casino()

casino.iniciar()