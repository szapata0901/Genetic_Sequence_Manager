
def encontrar(nombre_archivo,nombre):
    i=0
    linea = ""
    with open(nombre_archivo, "r") as archivo:  
        lista_archivo = archivo.readlines()
        while i < len(lista_archivo): 
            linea = lista_archivo[i] 
            if linea[1:-1] == nombre: 
                i=i+1 
                break 
            i=i+1
        linea = ""
        while i < len(lista_archivo) and lista_archivo[i][0] != ">" : 
            linea = linea + lista_archivo[i]                                                                                                                                                                                                
            i=i+1                                                                                                                                                                                                                       
        return linea 


def Ingresar(nombre_archivo, nombre, secuencia): 
    buscar_virus = encontrar(nombre_archivo, nombre) 
    if buscar_virus == "" : 
        with open(nombre_archivo, "a") as archivo:   
            archivo.write("\n") 
            archivo.write(">")
            archivo.write(nombre)
            archivo.write("\n")  
            archivo.write(secuencia)
    else:
        print("La secuencia",nombre,"ya está en la base de datos")
    

def Ingresar_por_archivo(nombre_archivo, nombre_fasta): 
    with open(nombre_fasta, "r") as archivo_nueva_sec:  
        lectura_archivo = archivo_nueva_sec.readlines() 
        primer_linea = lectura_archivo[0]
        nombre_virus = primer_linea[1:-1]
        buscar_virus = encontrar(nombre_archivo, nombre_virus) 
        i=1
        sec = "" 
        while i < len(lectura_archivo) and lectura_archivo[i][0] != ">" : 
            sec = sec + lectura_archivo[i]
            i=i+1    
        if buscar_virus == "" : 
            with open(nombre_archivo, "a") as archivo:
                archivo.write("\n")
                archivo.write(">")
                archivo.write(nombre_virus) 
                archivo.write("\n")
                archivo.write(sec)  
        else:
            print("La secuencia",nombre_virus,"ya está en la base de datos")
    

def eliminar(nombre_archivo, nombre):
    i=0
    linea = ""
    with open(nombre_archivo, "r") as archivo:     
        lista_archivo = archivo.readlines() 
        tam_lista = len(lista_archivo)  
        while i < len(lista_archivo): 
            linea = lista_archivo[i] 
            if linea[1:-1] == nombre: 
                lista_archivo.pop(i) 
                lista_archivo.pop(i) 
                break 
            i=i+1
        tam_list_despues = len(lista_archivo)         
    
        if tam_lista == tam_list_despues: 
            print("La secuencia del virus", nombre,"no se encuentra en la base de datos")
        else:
            with open(nombre_archivo, "w") as archivo:
                for linea2 in lista_archivo:
                    archivo.write(linea2)        
                print("La secuencia del virus",nombre,"ha sido borrada\n")


def compartir(nombre_archivo):
    nombre= input("¿Cómo quiere guardar el archivo?: ")
    with open(nombre,"w") as nombre, open(nombre_archivo, "r") as archivo:
        lista_archivo = archivo.readlines()
        for linea2 in lista_archivo: 
            nombre.write(linea2)


def comparar_secuencias (secuencia_inicial, secuencia_comparada):
    secuencia_inicial=list(secuencia_inicial)
    secuencia_comparada=list(secuencia_comparada)
    contador=0
    nucleotidos_iguales=0
    C,A,U,G,T = 0,0,0,0,0
    long_secuencia=len(secuencia_inicial) 
    while contador < long_secuencia: 
        base_i= secuencia_inicial[contador]
        base_c= secuencia_comparada[contador]
        if base_i== base_c:                
            if base_i == "C":
                C = C + 1
            elif base_i == "A":
                A = A + 1
            elif base_i == "U":
                U = U + 1
            elif base_i == "G":
                G = G + 1
            elif base_i == "T":
                T = T + 1
            nucleotidos_iguales= nucleotidos_iguales +1    
        else:
            nucleotidos_iguales= nucleotidos_iguales    
        contador= contador + 1
          
    porcentaje_similitud=int((nucleotidos_iguales/long_secuencia)*100)
    return porcentaje_similitud, C, A, U, G, T


def buscar_virus(nombre_archivo, nombre_virus):
    i=0
    linea = ""
    with open(nombre_archivo, "r") as archivo:    
        lista_archivo = archivo.readlines() 
        while i < len(lista_archivo):
            linea = lista_archivo[i]
            if linea[1:-1] == nombre_virus: 
                i=i+1
                break
            i=i+1
        return lista_archivo[i]


def cortar_secuencia(secuencia_1, n):
    tamaño_secuencia = len(secuencia_1)
    while tamaño_secuencia > n:
        secuencia_1.pop()
        tamaño_secuencia = len(secuencia_1)    
    return secuencia_1


def rellenar_secuencia(secuencia_1, n):
    tamaño_secuencia = len(secuencia_1)
    while tamaño_secuencia < n:
        secuencia_1.append("0")
        tamaño_secuencia = len(secuencia_1)
    return secuencia_1



def comparador():
    nombre_archivo = "secuencias.fasta" 
    original = input("Ingrese el nombre del virus a comparar: ")
    secuencia_o = list(buscar_virus(nombre_archivo, original)) 
    n = int(input("¿Con cuantos virus desea compararlo?: "))   
    secuencias = list(list())
    otro_virus = list()
    i=0
    while i < n:
        otro_virus.append(input("Ingrese el nombre de los otros virus: "))
        secuencias.append(list(buscar_virus(nombre_archivo, otro_virus[i]))) 
        i=i+1

    tamaño_o = len(secuencia_o)
    i=0
    while i < n:
        if len(secuencias[i]) > tamaño_o:
            secuencias[i] = cortar_secuencia(secuencias[i], tamaño_o)
        elif len(secuencias[i]) < tamaño_o:
            secuencias[i] = rellenar_secuencia(secuencias[i], tamaño_o)
        else:
            print("")
        i=i+1

    i=0
    while i < n:
        porcentaje_similitud, C,A,U,G,T= comparar_secuencias(secuencia_o, secuencias[i])
        print("Virus: {} vs Virus: {}".format(original, otro_virus[i] ))
        print("Porcentaje Similitud: {}% | C: {} | A: {} | U: {} | G: {} | T: {}".format(porcentaje_similitud, C,A,U,G,T))
        print("\n")
        i=i+1


def hallar_mutacion():
    nombre_virus = input("Ingrese el nombre del virus: ")
    mutacion = input("Ingrese la subsecuencia de mutación: ")
    nombre_archivo = "secuencias.fasta" 
    secuencia_virus = buscar_virus(nombre_archivo, nombre_virus)
    indice = secuencia_virus.find(mutacion) 
    if indice != -1:
        print("El virus {} si tiene la mutacion {} y esta ubicada desde el indice:  {}".format(nombre_virus,mutacion, indice))
    else:
        print("El virus {} no tiene la mutacion {}".format(nombre_virus,mutacion))


   
def menu():
    i=0
    while i < 100:
        print("\n")
        print("¿Qué tarea desea realizar?: \n")
        print("1) Encontrar secuencia")
        print("2) Ingresar una secuencia")
        print("3) Eliminar una secuencia")
        print("4) Compartir base de datos")    
        print("5) Comparar secuencias")
        print("6) Encontrar mutación\n")
    
        nombre_archivo = "secuencias.fasta" 
        pregunta = int(input("Ingrese un número: "))
        if pregunta == 1:
            nombre = input("\nNombre de la secuencia a encontrar: ")
            resultado = encontrar(nombre_archivo,nombre)
            if resultado == "":
                print("La secuencia asociada al virus",nombre,"no está en la lista")
            else:
                print("La secuencia del virus {} es {}".format(nombre,resultado))
        elif pregunta == 2:
            print("¿Como desea ingresar la nueva secuencia?: \n")
            print("1) Mediante teclado")
            print("2) Mediante archivo FASTA\n")
            opcion = int(input("Ingrese la opción: "))
            if opcion == 1:
                nombre = input("\nIngrese el nombre de la secuencia nueva: ")
                secuencia = input("Ingrese la secuencia nueva: ")
                ingresar_t=Ingresar(nombre_archivo, nombre, secuencia)
            elif opcion == 2:
                nombre_fasta = input("\nIngrese el nombre del archivo FASTA: ")
                ingresar_f=Ingresar_por_archivo(nombre_archivo, nombre_fasta)
            else:
                print("La opción ingresada es errónea")
        elif pregunta == 3:
            nombre = input("\nIngrese el nombre de la secuencia a eliminar: ")
            borrar= eliminar(nombre_archivo, nombre)
        elif pregunta == 4:
            compartir(nombre_archivo)
        elif pregunta == 5:
            comparar=comparador()    
        elif pregunta == 6:
            hallar=hallar_mutacion()
        else:
            print("La opción elegida no se encuentra en el menú")
    i=i+1        
menu()



