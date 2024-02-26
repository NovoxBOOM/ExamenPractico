import psutil

def obtener_porcentaje_uso(particion):
	espacio = psutil.disk_usage(particion)
	porcentaje = espacio.percent
	return porcentaje

def main():
	particiones = ['/dev/sda1', '/dev/sda2', '/dev/sda3']

	for particion in particiones:
		porcentaje = obtener_porcentaje_uso(particion)
		print(f"{particion} {porcentaje:.1f}%")

if __name__ == "__main__":
	main()
