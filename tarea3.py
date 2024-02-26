import os

def crear_carpetas_y_ficheros(ruta):
    for i in range(1,6):
        nombre_carpeta = os.path.join(ruta, f"folder{i}")
        os.makedirs(nombre_carpeta, exist_ok=True)

        for j in range(1, 11):
            nombre_fichero = f"fichero{j}.txt"
            contenido = f"Este es el contenido del fichero {j}"

            with open(os.path.join(nombre_carpeta, nombre_fichero), "w") as f:
                f.write(contenido)

if __name__ == "__main__":
    ruta_destino = "/home/joseluis/Escritorio/Python/Prueba_tarea3"
    crear_carpetas_y_ficheros(ruta_destino)
    print("Carpetas y ficheros creados exitosamente en", ruta_destino)