import math, csv, random
def asignar_sueldos(diccionario_trabajadores):
    for trabajador in diccionario_trabajadores:
        sueldo = random.randint(300000,2500000)
        trabajador['sueldo'] = sueldo
    return diccionario_trabajadores

def clasificar_sueldos(diccionario_trabajadores):
    try:
        cont1=0
        cont2=0
        cont3=0
        for trabajador in diccionario_trabajadores:
            if trabajador['sueldo'] < 800000:
                cont1+=1
        print(f"Sueldos menores a $800.000: TOTAL: {cont1}\n")
        for trabajador in diccionario_trabajadores:
            if trabajador['sueldo'] < 800000:
                print(f"Nombre empleado: {trabajador['nombre']} Sueldo: ${trabajador['sueldo']}\n")
                
        for trabajador in diccionario_trabajadores:
            if trabajador['sueldo'] > 800000 and trabajador['sueldo'] <2000000:
                cont2+=1
        print(f"Sueldos entre $800.000 y $2.000.000: TOTAL: {cont2}\n")
        for trabajador in diccionario_trabajadores:
            if trabajador['sueldo'] > 800000 and trabajador['sueldo'] <2000000:
                print(f"Nombre empleado: {trabajador['nombre']} Sueldo: ${trabajador['sueldo']}\n")
                
        for trabajador in diccionario_trabajadores:
            if trabajador['sueldo'] > 2000000:
                cont3+=1
        print(f"Sueldos mayores a $2000000: TOTAL: {cont3}\n")
        for trabajador in diccionario_trabajadores:
            if trabajador['sueldo'] > 2000000:
                print(f"Nombre empleado: {trabajador['nombre']} Sueldo: ${trabajador['sueldo']}\n")
    except KeyError:
        print("¡Aun no hay sueldos registrados!")

def ver_estadisticas(diccionario_trabajadores):
    try:
        sueldos=[]
        for trabajador in diccionario_trabajadores:
            sueldos.append(trabajador['sueldo'])
    except KeyError:
        print("¡No hay sueldos registrados!")
    else:
        sueldo_max=max(sueldos)
        sueldo_min=min(sueldos)
        sueldo_promedio = sum(sueldos) / len(sueldos)    
        sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))
        print(f"Sueldo mas alto: ${sueldo_max}")
        print(f"Sueldo mas bajo: ${sueldo_min}")
        print(f"Sueldo promedio: ${sueldo_promedio:.2f}")
        print(f"Media geometrica: ${sueldo_geom:.2f}")

def crear_reporte_sueldos(diccionario_trabajadores):
    try:
        campos = ['Nombre', 'Sueldo base', 'Descuento AFP', 'Descuento salud', 'Sueldo liquido']
        with open('Reporte_archivos.csv','w',newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for trabajador in diccionario_trabajadores:
                Sueldo_base = trabajador['sueldo']
                descuento_afp = Sueldo_base * 0.12
                descuento_salud = Sueldo_base * 0.07
                sueldo_liquido = Sueldo_base - descuento_afp - descuento_salud
                fila ={
                        'Nombre': trabajador['nombre'],
                        'Sueldo base': Sueldo_base,
                        'Descuento salud': descuento_salud,
                        'Descuento AFP': descuento_afp,
                        'Sueldo liquido': sueldo_liquido
                        }
                escritor.writerow(fila)
                print(f"Nombre empleado: {fila['Nombre']} Sueldo base: ${fila['Sueldo base']} Descuento salud: {fila['Descuento salud']:.2f} Descuento AFP: {fila['Descuento AFP']:.2f} Sueldo liquido: {fila['Sueldo liquido']:.2f}")
    except KeyError:
        print("¡Aun no hay sueldos regstrados!")
    
diccionario_trabajadores =[
    {'nombre':'Juan Pérez'},
    {'nombre': 'María García'},
    {'nombre': 'Carlos López'},
    {'nombre': 'Ana Martínez'},
    {'nombre': 'Pedro Rodríguez'},
    {'nombre': 'Laura Hernández'},
    {'nombre': 'Miguel Sánchez' },
    {'nombre': 'Isabel Gómez'},
    {'nombre': 'Francisco Díaz'},
    {'nombre': 'Elena Fernández'}
    ]

while True:
    print("1.- Asignar sueldos aleatorios\n2.- Clasificar sueldos\n3.- Ver estadísticas\n4.- Reporte de sueldos\n5.- Salir")
    op = input("Ingrese el numero de la accion que desea realizar: ")
    match op:
        case "1":
            diccionario_trabajadores= asignar_sueldos(diccionario_trabajadores)
        case "2":
            clasificar_sueldos(diccionario_trabajadores)
        case "3":
            ver_estadisticas(diccionario_trabajadores)
        case "4":
            crear_reporte_sueldos(diccionario_trabajadores)
        case "5":
            print("Finalizando programa...")
            print("Desarrollado por: Benjamin Castañeda")
            print("RUT: 21.499.102-0")
            break
        case default:
            print("Opcion no valida")