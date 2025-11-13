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
        self.caballos = {
            1: ("Caballo 🐴1", 0.45, 3),  # Probabilidad de ganar y recompensa por victoria
            2: ("Caballo 🐴2", 0.5, 2.0),
            3: ("Caballo 🐴3", 0.40, 5.0),
            4: ("Caballo 🐴4", 0.35, 10.0)
        }
        self.cartones = []
        self.crupier_carton = []
        self.numero_actual = 0
        self.numeros_sacados = []
        self.linea_hecha = False

    def mostrar_saldo(self):
        return self.saldo  # Acceso al atributo saldo usando self.saldo


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
                    time.sleep(0.5)
                    print("\nGirando...")
                    time.sleep(1)
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
                    time.sleep(0.5)
                    print("\nGirando...")
                    time.sleep(1)
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
                    time.sleep(0.5)
                    print("\nGirando...")
                    time.sleep(1)
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
                    print("\n\033[1mSaldo insuficiente. Saliendo de Ruleta...\033[0m\n")
                    time.sleep(1)
                    break

            except ValueError:
                input("\nEntrada inválida. Ingresa un número válido.\n")

#BlackJack

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
                        break

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
                        print("\n\033[1mSaldo insuficiente. Saliendo de Blackjack...\033[0m\n")
                        time.sleep(1)
                        break
                 except ValueError:
                    print("\nEntrada inválida. Por favor, ingresa un número válido.")

            except ValueError:
                print("\nEntrada inválida. Por favor, ingresa un número válido.")


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
        self.saldo -= self.apuesta 
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
                self.saldo += self.apuesta * (multiplicador / 4)
                if  slot[0] == slot[1]:
                    return f"😊 ¡Dos iguales! {slot[0]} x{multiplicador} \nTu saldo ahora es: ${self.saldo}"
                elif slot[1] == slot[2]:
                    return f"😊 ¡Dos iguales! {slot[1]} x{multiplicador} \nTu saldo ahora es: ${self.saldo}"
                else:
                    return f"😊 ¡Dos iguales! {slot[0]} x{multiplicador} \nTu saldo ahora es: ${self.saldo}"
        else:
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
                print("\n\033[1mSaldo insuficiente. Saliendo de las Slots...\033[0m\n")
                time.sleep(1)
                break

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


#BINGO

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
    def ATM(self):
        try:
            borrar_preguntas()
            print("\033[1m¿Sin Dinero?\033[0m \n")
            ingreso = float(input("Cuanto dinero desea Depositar: "))
            self.saldo += ingreso
            borrar_preguntas()
            self.mostrar_saldo()
            input("Pulse Enter para volver al menú")
        except ValueError:
            input("Pulse Enter para volver al menu")
        


    def iniciar(self):
        while True:
            borrar_preguntas()
            print("\033[1mBienvenido al casino\033[0m\n")
            print("¡Seleccione la modalidad!\n")
            print("1. Coin flip")
            print("2. La Mil Colores(Ruleta)")
            print("3. Blacjack")
            print("4. ArruinaSueldos(Slots)")
            print("5. Carrera De caballos")
            print("6. Bingo")
            print("7. ATM")
            print("8. Salir")
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
            elif opcion=="7":
                self.ATM()
            elif opcion == "8":
                input("\nGracias por jugar. ¡Vuelve pronto!\n")
                break
            else:
                print("\nOpción no válida. Inténtalo de nuevo.\n")


casino = Casino()

casino.iniciar()
