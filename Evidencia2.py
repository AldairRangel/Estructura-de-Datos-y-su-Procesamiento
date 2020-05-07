'''Importación de librerías a utilizar'''
import pandas as pd
import time
import collections
import json

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
    print('5)Guardar archivos            6)Cargar archivos\n7)Salir')
    opcion = input()
    print('*' * 40)
    #Desarrollo del ingreso de alumnos, y asignación autómatica de claves
    if opcion == "1":
        while True:
            nombreAlumno = str(input('*Ingresa el nombre del alumno: '))
            print(f'*El nombre del alumno es {nombreAlumno}')
            claveAlumno = len(listaAlumnos.keys()) + 1
            print(f'*La clave del nuevo alumno es {claveAlumno}')
            print(f'*Se ha registrado al alumno {nombreAlumno} con clave {claveAlumno}')
            listaAlumnos[claveAlumno] = nombreAlumno
            alumno[claveAlumno] = [nombreAlumno]
            alumno.index = ['Alumno']
            decisionAlumno = input('Agregar otro alumno\n1) Si         2) No\n')
            print()
            if decisionAlumno == "1":
                pass
            else:
                break
    #Dar de altas las calificaciones en la materia que el usuario eliga del menu      
    elif opcion == "2":
        while True:
            print('Selecciona la materia:\n1)Programación                         2)Base de datos')
            print('3)Estadistica                          4)Macroeconomía')
            print('5)Creatividad                          6)Salir y guardar datos\n')
            materia = input()
            if materia == "1":
                for x in listaAlumnos:
                    nota = int(input(f"Introducir la calificación del alumno con clave {x}: "))
                    dicc_progra[x]= nota
                    if nota < 70:
                        lista_rep.append(x)
                a = dicc_progra.copy()
                print("Ha terminado de guardar las calificaciones, procederemos a darlas de alta.")
                print('*' * 40)
            elif materia == "2":
                for x in listaAlumnos:
                    nota = int(input(f"Introducir la calificación del alumno con clave {x}: "))
                    dicc_base[x]= nota
                    if nota < 70:
                        lista_rep.append(x)
                b = dicc_base.copy()
                print("Ha terminado de guardar las calificaciones, procederemos a darlas de alta.")
                print('*' * 40)
            elif materia == "3":
                for x in listaAlumnos:
                    nota = int(input(f"Introducir la calificación del alumno con clave {x}: "))
                    dicc_est[x]= nota
                    if nota < 70:
                        lista_rep.append(x)               
                c = dicc_est.copy()
                print("Ha terminado de guardar las calificaciones, procederemos a darlas de alta.")
                print('*' * 40)
            elif materia == "4":
                for x in listaAlumnos:
                    nota = int(input(f"Introducir la calificación del alumno con clave {x}: "))
                    dicc_macro[x]= nota
                    if nota < 70:
                        lista_rep.append(x)
                d = dicc_macro.copy()
                print("Ha terminado de guardar las calificaciones, procederemos a darlas de alta.")              
                print('*' * 40)
            elif materia == "5":
                for x in listaAlumnos:
                    nota = int(input(f"Introducir la calificación del alumno con clave {x}: "))
                    dicc_crea[x]= nota
                    if nota < 70:
                        lista_rep.append(x)       
                e = dicc_crea.copy()
                print("Ha terminado de guardar las calificaciones, procederemos a darlas de alta.")
                print('*' * 40)
            elif materia not in ["1","2","3","4","5","6"]:
                print("Esa opción no es válida")
                print("*" * 40)
            else:
                diccionario = {1:a,2:b,3:c,4:d,5:e}
                calificaciones = pd.DataFrame(diccionario)
                Alumnos = listaAlumnos.copy()               
                print(diccionario)
                print(calificaciones)
                print('*' * 40)
                break
    #Existiendo ya las calificaciones, procede a describir con ayuda de la estadistica como fueron las notas de cada materia
    elif opcion == "3":
        while True:
            print("Las estadisticas arrojadas según las materias, son las siguientes:")
            materia = calificaciones.describe()
            print(materia)
            m = materia
            print("*" * 40)
            print("Las estadisticas arrojadas por cada una de los alumnos, son las siguientes:")
            alumno =calificaciones.T.describe()
            print(alumno)
            a = alumno
            print("*" * 40)
            print("¿Desea guardar las estadisticas obtenidas en un archivo de texto plano?")
            print()
            decisionAlumnoTXT = input('Exportar a TXT:\n1) Si         2) No\n')
            if decisionAlumnoTXT == "1":
                txtFile=open('estadisticas.txt', 'w')
                txtFile.write(m.to_string() +'\n')
                txtFile.write(a.to_string())
                txtFile.close()
                print("Finalizamos.")
                break
            elif decisionAlumnoTXT not in ["1","2"]:
                print("Esa opción no es valida.")
                print("*" * 40)
            else:
                break
    #Muestra las claves de alumnos que tienen 2 o más materias reprobadas
    elif opcion == "4":
        while True:
            reprobados = collections.Counter(lista_rep)
            print("A continuación, les presentaremos las claves de los alumnos reprobados")
            print(reprobados)
            break    
    #Opción que nos permite salir del programa
    elif  opcion == "5":
        while True:
            opcion = input('Selecciona un tipo de archivo\n 1) CSV      2) JSON\n')
            if opcion == "1":
                alumno.to_csv(r'alumno.csv', index = True, header = True)
                print()
                calificaciones.to_csv(r'calificaciones.csv', index = True, header  = True)
                print('Espera mientras se guardan los archivos')
                time.sleep(2)
            else:
                with open("Alumnos.json", "w") as alumnosW:
                    json.dump(Alumnos,alumnosW)
                with open("calificaciones.json", "w") as cuentasW:
                    json.dump(diccionario, cuentasW)
            break
    elif opcion == "6":
        try:
            alumno = pd.read_csv('alumno.csv', index_col = 0)
            calificaciones = pd.read_csv('calificaciones.csv', index_col = 0)
            print('Alumnos')
            print(alumno.T)
            print("*" * 40)
            time.sleep(1)
            print()
            print('Calificaciones')
            print(calificaciones.T)
            time.sleep(1)
            print('*Archivos CSV cargados')
            print("*" * 40)
        except FileNotFoundError:
            print('*No se encontraron archivos csv')
            print("*" * 40)
        try:
            with open("calificaciones.json", "r") as cuentasR:
                diccionario = json.load(cuentasR)
                calificaciones = pd.DataFrame(diccionario)
            with open("Alumnos.json","r") as alumnosR:
                alumnos = json.load(alumnosR)
            print("*Archivo Json cargado: Calificaciones*")    
            print(diccionario)
            print("*" * 40)
            print("*Archivo Json cargado: Lista de Alumnos*")
            print(alumnos)
            print("*" * 40)
        except FileNotFoundError:
            print("*No se encontraron archivos json*")
    elif opcion not in ["1","2","3","4","5","6","7"]:
        print("Esta opción no es permitida")
        print("*" * 40)
    else:
        print('Adios')
        break        
