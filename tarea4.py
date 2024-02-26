import logging
import shutil

def configurar_logger():
    logging.basicConfig(
        filename='/home/joseluis/logs/espacio.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def analizar_espacio():
    espacio_total, espacio_usado, espacio_libre = shutil.disk_usage("/")
    porcentaje_usado = (espacio_usado / espacio_total) * 100

    if porcentaje_usado > 80:
        logging.error("El espacio es la particion raiz esta al {porcentaje_usado:.2f}%, es mayor que el 80%.")
    elif porcentaje_usado > 60:
        logging.warning(f"El espacio en la particion raiz esta al {porcentaje_usado:.2f}%, es mayor que el 60% pero menor que el 80%")
    else:
        logging.info(f"El espacio en la particion raiz esta al {porcentaje_usado:2f}%, es menor que el 60%.")

if __name__ == "__main__":
    configurar_logger()
    analizar_espacio()