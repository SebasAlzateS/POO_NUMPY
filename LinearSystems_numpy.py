'''
    SEBASTIÁN ALZATE SIERRA
    Trabajo #1 Programación Avanzada
    19/10/2023
'''

import numpy as np  

class SistemaLineal:
    def __init__(self, archivo):
        self.sistemas = self._leer_archivo(archivo)         # Inicializa la clase SistemaLineal con una lista de sistemas leída desde el archivo.

    def _leer_archivo(self, archivo):
        with open(archivo, 'r') as file:
            lineas = file.readlines()                       # Lee las líneas del archivo y las almacena en una lista llamada lineas.

        sistemas = []                                       # Inicializa una lista para almacenar los sistemas leídos del archivo.
        for i in range(0, len(lineas), 2):                  # Itera sobre las líneas en pasos de 2 para procesar las matrices A y los vectores B.
            coeficientes_a = list(map(int, lineas[i].strip().split(',')[1:]))    # Extrae los coeficientes de A de la línea i.
            orden = int(len(coeficientes_a) ** 0.5)         # Calcula el orden de la matriz A.
            a = np.array(coeficientes_a).reshape(orden, orden)                  # Convierte los coeficientes de A en una matriz y la reshape al tamaño adecuado.
            b = np.array(list(map(int, lineas[i + 1].strip().split(',')[1:])))  # Extrae los coeficientes de B de la siguiente línea.
            sistemas.append((a, b))                                             # Agrega el par (A, B) a la lista de sistemas.

        return sistemas                                                         # Devuelve la lista de sistemas leída desde el archivo.

    def mostrar_sistema(self, indice):
        A, b = self.sistemas[indice]                         # Obtiene la matriz A y el vector B del sistema en el índice dado.
        n = len(b)                                           # Obtiene el tamaño del vector B.
        for i in range(n):                                   # Itera sobre las ecuaciones del sistema.
            ecuacion = " + ".join([f"{A[i][j]}*x{j + 1}" for j in range(n)])  # Crea una cadena que representa la ecuación.
            print(f"{ecuacion} = {b[i]}")                    # Muestra la ecuación y su resultado.

    def mostrar_sistemas_disponibles(self):
        print("Sistemas disponibles para resolver:")  
        for i, sistema in enumerate(self.sistemas):         # Itera sobre los sistemas y sus índices.
            a_vector = np.array2string(sistema[0].reshape(-1), separator=',')  # Convierte la matriz A en una cadena y la muestra como un vector.
            b_vector = np.array2string(sistema[1], separator=',')              # Convierte el vector B en una cadena y la muestra.
            print(f"{i + 1}: A = {a_vector}, B = {b_vector}")                  # Muestra el índice, la matriz A y el vector B.

    def resolver_sistema(self, indice):
        A, b = self.sistemas[indice]                        # Obtiene la matriz A y el vector B del sistema en el índice dado.
        try:
            x = np.linalg.solve(A, b)                       # Resuelve el sistema de ecuaciones lineales Ax = b.
            return x.reshape(-1, 1)                         # Devuelve la solución como una matriz columna.
        except np.linalg.LinAlgError as e:                  # Captura un error si la matriz A es singular y no se puede resolver.
            print(f"Error: No se puede resolver el sistema. {e}")  # Muestra un mensaje de error.
            return None                                     # Devuelve None para indicar que no hay solución válida.

if __name__ == "__main__":
    archivo = 'matrices.txt'                                # Nombre del archivo que contiene los sistemas de ecuaciones.
    sistema = SistemaLineal(archivo) 

    while True: 
        print("\nSeleccione una opción:")
        print("1: Resolver un sistema")  
        print("2: Salir")  

        try:
            opcion = int(input("Ingrese el número de la opción que desea: "))  
            if opcion == 1:  
                while True:  
                    sistema.mostrar_sistemas_disponibles() 
                    try:
                        indice_sistema = int(input("Ingrese el número del sistema que desea resolver: ")) - 1  # Lee el índice del sistema.
                        if 0 <= indice_sistema < len(sistema.sistemas):                                        # Si el índice es válido,
                            solucion = sistema.resolver_sistema(indice_sistema)                                # Resuelve el sistema seleccionado.
                            if solucion is not None:                                                           # Si hay una solución válida, muestra la solución.
                                print("\nSistema de ecuaciones:")
                                sistema.mostrar_sistema(indice_sistema)                                        # Muestra el sistema de ecuaciones.
                                print("\nSolución del sistema:")
                                print(solucion)  
                            break  
                        else:  
                            print("Número de sistema no válido. Por favor, intente nuevamente.")
                    except ValueError:                  # Si se ingresa una entrada no válida, muestra un mensaje de error.
                        print("Entrada no válida. Por favor, ingrese un número.")
            elif opcion == 2:                            
                print("Saliendo del programa. ¡Hasta luego!")
                break                                   # Sale del bucle principal y finaliza el programa.
            else:                                       # Si se ingresa una opción inválida, muestra un mensaje de error.
                print("Opción no válida. Por favor, ingrese un número válido.")
        except ValueError:                              # Si se ingresa una entrada no válida , muestra un mensaje de error.
            print("Entrada no válida. Por favor, ingrese un número.")
