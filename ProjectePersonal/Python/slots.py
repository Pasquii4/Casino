
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

    def mostrar_slots(self, slot):
        borrar_preguntas()
        print(f"| {slot[0]} | {slot[1]} | {slot[2]} |")

    def girar_rodillos(self):
        simbolos = ["🍒", "🔔", "🍋", "🍉", "⭐", "💎", "7"]
        return [random.choice(simbolos) for _ in range(3)]  

    def obtener_multiplicador(self, simbolo):
        multiplicadores = {
            "🍒": 10,    
            "🔔": 10,   
            "🍋": 10,  
            "🍉": 10,    
            "⭐": 20,   
            "7" : 25,
            "💎": 30   
        }
        return multiplicadores.get(simbolo, 1)

    # Función para calcular el resultado
    def calcular_resultado(self, slot):
        if slot[0] == slot[1] == slot[2]:
            multiplicador = self.obtener_multiplicador(slot[0])
            self.saldo += self.apuesta * multiplicador 
            if  slot[0] == slot[1]:
                return f"🎉 ¡Ganaste! {slot[0]} x{multiplicador} \nTu saldo ahora es: ${self.saldo}"
            elif slot[1] == slot[2]:
                return f"🎉 ¡Ganaste! {slot[1]} x{multiplicador} \nTu saldo ahora es: ${self.saldo}"
            else:
                return f"🎉 ¡Ganaste! {slot[0]} x{multiplicador} \nTu saldo ahora es: ${self.saldo}"
        elif ((slot[0] == slot[1] and ("7" in slot[0] or "💎" in slot[0])) or (slot[0] == slot[2] and ("7" in slot[0] or "💎" in slot[0])) or (slot[1] == slot[2] and ("7" in slot[1] or "💎" in slot[1]))):
                multiplicador = self.obtener_multiplicador("7" if "7" in slot else "💎")
                self.saldo += self.apuesta * (multiplicador / 2)
                if  slot[0] == slot[1]:
                    return f"😊 ¡Dos iguales! {slot[0]} x{multiplicador} \nTu saldo ahora es: ${self.saldo}"
                elif slot[1] == slot[2]:
                    return f"😊 ¡Dos iguales! {slot[1]} x{multiplicador} \nTu saldo ahora es: ${self.saldo}"
                else:
                    return f"😊 ¡Dos iguales! {slot[0]} x{multiplicador} \nTu saldo ahora es: ${self.saldo}"
        else:
            self.saldo -= self.apuesta 
            return f"😢 No ganaste esta vez. ¡Intenta de nuevo! \nSu saldo ahora es: ${self.saldo}"

    # Juego slots
    def jugar_slots(self):
        borrar_preguntas()
        print("🎰 Bienvenido a la Máquina de Slots: La ArruinaSueldos 🎰")
        print(f"Tu saldo inicial es: ${self.saldo}")
        while True:
            jugar = input("\nPresiona 'Enter' para girar.\nEscribe 'salir' para terminar.\nEscribe 'apuesta' para editar tu apuesta.\n: ").strip().lower()
            if jugar == "salir":
                print(f"¡Gracias por jugar! Tu saldo final es: ${self.saldo}")
                break
            elif jugar == "apuesta":
                try:
                    nueva_apuesta = int(input("Introduce la cantidad que deseas apostar: "))
                    if nueva_apuesta > 0 and nueva_apuesta <= self.saldo:
                        self.apuesta = nueva_apuesta
                        print(f"Tu apuesta ahora es de: ${self.apuesta}")
                    else:
                        print("La apuesta debe ser positiva y no mayor que tu saldo.")
                except ValueError:
                    print("Por favor, introduce un número válido.")
                continue
            elif self.apuesta <= 0:
                print("Por favor, establece una apuesta antes de jugar.")
                continue

            slot = self.girar_rodillos()
            self.mostrar_slots(slot)
            resultado = self.calcular_resultado(slot)
            print(resultado)

            # Verificar si queda saldo
            if self.saldo <= 0:
                input("😢 Te has quedado sin saldo. ¡Gracias por jugar!")
                break

    def iniciar(self):
        while True:
            borrar_preguntas()
            print("\033[1mBienvenido al casino\033[0m\n")
            input("Pulse Enter Para Iniciar: ")
            self.jugar_slots()

casino = Casino()

casino.iniciar()