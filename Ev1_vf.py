'''Importación de librerías a utilizar'''
import pandas as pd
import time
import collections

'''Declaración de listas y diccionarios'''
listaAlumnos = {}
alumno = pd.DataFrame(listaAlumnos)

dicc_progra={}
dicc_base = {}
dicc_est = {}
dicc_macro = {}
dicc_crea={}
diccionario={}

a={}
b={}
c={}
d={}
e={}
lista_rep=[]

'''Inicio del código
Menu para seleccionar que hacer'''

while True:
    print('Selecciona una opcion:\n1)Ingresar alumno             2)Ingresar calificaciones')
    print('3)Mostrar estadísticas        4)Mostrar claves de alumnos reprobados')
    print('5)Salir')
    opcion = int(input())
    print('*' * 40)
    #Desarrollo del ingreso de alumnos, y asignación autómatica de claves
    if opcion == 1:
        while True:
            nombreAlumno = str(input('*Ingresa el nombre del alumno: '))
            print(f'*El nombre del alumno es {nombreAlumno}')
            claveAlumno = int(len(alumno.columns) + 1)
            print(f'*La clave del nuevo alumno es {claveAlumno}')
            print(f'*Se ha registrado al alumno {nombreAlumno} con clave {claveAlumno}')
            alumno[claveAlumno] = [nombreAlumno]
            decisionAlumno = int(input('Agregar otro alumno\n1) Si         2) No\n'))
            print()
            if decisionAlumno == 1:
                pass
            else:
                break
    #Dar de altas las calificaciones en la materia que el usuario eliga del menu      
    elif opcion == 2:
        while True:
            print('Selecciona la materia:\n1)Programación                         2)Base de datos')
            print('3)Estadistica                          4)Macroeconomía')
            print('5)Creatividad                          6)Salir y guardar datos\n')
            materia = int(input())
            if materia == 1:
                for x in alumno:
                    nota = int(input(f"Introducir la calificación del alumno con clave {x}: "))
                    dicc_progra[x]= nota
                    if nota < 70:
                        lista_rep.append(x)
                a = dicc_progra.copy()
                print("Ha terminado de guardar las calificaciones, procederemos a darlas de alta.")
                print('*' * 40)
            elif materia == 2:
                for x in alumno:
                    nota = int(input(f"Introducir la calificación del alumno con clave {x}: "))
                    dicc_base[x]= nota
                    if nota < 70:
                        lista_rep.append(x)
                b = dicc_base.copy()
                print("Ha terminado de guardar las calificaciones, procederemos a darlas de alta.")
                print('*' * 40)
            elif materia == 3:
                for x in alumno:
                    nota = int(input(f"Introducir la calificación del alumno con clave {x}: "))
                    dicc_est[x]= nota
                    if nota < 70:
                        lista_rep.append(x)               
                c = dicc_est.copy()
                print("Ha terminado de guardar las calificaciones, procederemos a darlas de alta.")
                print('*' * 40)
            elif materia == 4:
                for x in alumno:
                    nota = int(input(f"Introducir la calificación del alumno con clave {x}: "))
                    dicc_macro[x]= nota
                    if nota < 70:
                        lista_rep.append(x)
                d = dicc_macro.copy()
                print("Ha terminado de guardar las calificaciones, procederemos a darlas de alta.")              
                print('*' * 40)
            elif materia == 5:
                for x in alumno:
                    nota = int(input(f"Introducir la calificación del alumno con clave {x}: "))
                    dicc_crea[x]= nota
                    if nota < 70:
                        lista_rep.append(x)       
                e = dicc_crea.copy()
                print("Ha terminado de guardar las calificaciones, procederemos a darlas de alta.")
                print('*' * 40)
            elif materia == 6:
                diccionario = {1:a,2:b,3:c,4:d,5:e}
                calificaciones = pd.DataFrame(diccionario)
                print(diccionario)
                print(calificaciones)
                print('*' * 40)
                break
    #Existiendo ya las calificaciones, procede a describir con ayuda de la estadistica como fueron las notas de cada materia
    elif opcion == 3:
        print("Las estadisticas arrojadas según nuestra materia es lo siguiente:")
        print(calificaciones.describe())
    #Muestra las claves de alumnos que tienen 2 o más materias reprobadas
    elif opcion == 4:
        while True:
            reprobados = collections.Counter(lista_rep)
            print("A continuación, les presentaremos las claves de los alumnos reprobados")
            print(reprobados)
            break    
    #Opción que nos permite salir del programa
    else:
        print('Adios')
        break        
