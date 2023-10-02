import os
import random

class Juego:
    def __init__(self, filas, columnas, inicio, fin, mapa):
        self.filas = filas
        self.columnas = columnas
        self.inicio = inicio
        self.fin = fin
        self.mapa = mapa

    def mostrar_mapa(self):
        for fila in self.mapa:
            print(" ".join(fila))

    def evaluar(self, x, y):
        if x < 0 or x >= self.filas or y < 0 or y >= self.columnas:
            return "Coordenadas fuera del rango."
        elif (x, y) == self.fin:
            return "¡Ganaste!"
        elif self.mapa[x][y] == "X":
            return "¡Boom! Explotó una bomba."
        else:
            return "No hay bomba en esta posición. ¡Continúa!"

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa, inicio, fin = self.leer_mapa_aleatorio(path_a_mapas)
        filas = len(mapa)
        columnas = len(mapa[0])
        super().__init__(filas, columnas, inicio, fin, mapa)

    def leer_mapa_aleatorio(self, path_a_mapas):
        nombres_archivos = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(nombres_archivos)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, "r") as archivo_mapa:
            lineas = archivo_mapa.readlines()
            dimensiones = lineas[0].strip().split()
            filas, columnas = map(int, dimensiones)
            mapa = [line.strip() for line in lineas[1:]]
            inicio = tuple(map(int, mapa[0].split()))
            fin = tuple(map(int, mapa[1].split()))
            mapa = mapa[2:]
            return mapa, inicio, fin

if __name__ == "__main__":
    # Ejemplo de uso:
    path_a_mapas = "directorio_de_mapas"
    juego = JuegoArchivo(path_a_mapas)
    juego.mostrar_mapa()

    while True:
        x = int(input("Ingresa la fila: "))
        y = int(input("Ingresa la columna: "))
        resultado = juego.evaluar(x, y)
        print(resultado)
        if resultado != "No hay bomba en esta posición. ¡Continúa!":
            break
