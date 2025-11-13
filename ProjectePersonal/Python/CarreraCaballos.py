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
        self.caballos = {
            1: ("Caballo 🐴1", 0.45, 3),  # Probabilidad de ganar y recompensa por victoria
            2: ("Caballo 🐴2", 0.5, 2.0),
            3: ("Caballo 🐴3", 0.40, 5.0),
            4: ("Caballo 🐴4", 0.35, 10.0)
        }


    def mostrar_caballos(self):
        """Muestra los caballos junto con sus probabilidades de ganar y recompensas."""
        print("Los caballos son:")
        for num, caballo in self.caballos.items():
            print(f"{num}. {caballo[0]} (Probabilidad de ganar: {caballo[1]}, Recompensa: {caballo[2]}x)")

    def mostrar_saldo(self):
        """Muestra el saldo actual del jugador."""
        print(f"Saldo actual: ${self.saldo}")

    def apostar(self, cantidad):
        """Gestiona la apuesta del jugador."""
        if cantidad > self.saldo:
            print("Saldo insuficiente.")
            return False
        else:
            self.saldo -= cantidad
            return True

    def recibir_recompensa(self, recompensa):
        """Añade la recompensa al saldo del jugador."""
        self.saldo += recompensa

    def mover_caballo(self, caballo, posicion):
        """Muestra la posición del caballo en la pista."""
        print(f"{caballo}: {'-' * posicion}>")

    def correr_carrera(self):
        """Simula la carrera de caballos y devuelve el ganador."""
        posiciones = {caballo[0]: 0 for caballo in self.caballos.values()}
        meta = 50

        while max(posiciones.values()) < meta:
            for num, caballo in self.caballos.items():
                if random.random() < caballo[1]:
                    posiciones[caballo[0]] += 1
                self.mover_caballo(caballo[0], posiciones[caballo[0]])
            time.sleep(0.1)
            print("\n" * 20)
        
        ganador = max(posiciones, key=posiciones.get)
        return ganador

    def iniciar_carrera(self):
        bucle = True
        """Inicia la carrera de caballos y gestiona el proceso de apuestas."""
        while True:
            borrar_preguntas()
            print("¡Bienvenidos a la carrera de caballos del Casino! 🏇")
            self.mostrar_caballos()
            self.mostrar_saldo()
        
        # Selección del caballo y cantidad de la apuesta
        
            try:
                apuesta_num = float(str(input("¿A cuál caballo quieres apostar (Escribe '0' para salir)?: ")))
                if apuesta_num == 0:
                    input("Pulse Enter para salir ")
                    return

                if apuesta_num <= -1 or apuesta_num >= 5:
                    print("El Caballo no existe")
                    input("Pulse Enter para salir ")
                    break


                apuesta = self.caballos[apuesta_num]

                # Cantidad de la apuesta
                cantidad_apuesta = float(input("¿Cuánto quieres apostar?: "))
                if not self.apostar(cantidad_apuesta):
                    print("Apuesta no realizada por saldo insuficiente.")
                    continue

                print("La carrera está por comenzar...")
                time.sleep(1)
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                print("¡Goo!")
                time.sleep(0.5)

                # Ejecución de la carrera
                ganador = self.correr_carrera()

                print(f"¡El ganador es {ganador}!")
                if ganador == apuesta[0]:
                    recompensa = cantidad_apuesta * apuesta[2]
                    self.recibir_recompensa(recompensa)
                    input(f"¡Has ganado! Tu recompensa es {recompensa:.2f} euros.")
                else:
                    input("Lo siento, has perdido tu apuesta.")

                self.mostrar_saldo()

            except ValueError:
                print("Número de caballo no válido. Inténtalo de nuevo.")
                break


    def iniciar(self):
        while True:
            borrar_preguntas()
            print("\033[1mBienvenido al casino\033[0m\n")
            input("Pulse Enter Para Iniciar: ")
            self.iniciar_carrera()

casino = Casino()

casino.iniciar()