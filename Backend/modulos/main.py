from .menus import opcionesMenu1


def reiniciar():#funcion para poner a 0 los resultados almacenados en el fichero
    archivos = [
        "HumanoVSMinMax.txt",
        "HumanoVSAlfaBeta.txt"
    ]
    for archivo in archivos:
        with open(archivo,"w") as f:
            f.write(str(0) + "\n")
            f.write(str(0) + "\n")
            f.write(str(0) + "\n")



def main():
    reiniciar()
    opcionesMenu1()



if __name__ =="__main__":
    main()
