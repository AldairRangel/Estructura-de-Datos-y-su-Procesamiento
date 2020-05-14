import sys
import sqlite3
import pandas as pd
from sqlite3 import Error

dicc= {}

def desplegar_menu_principal():
    print("**********************")
    print("*** MENÚ PRINCIPAL ***")
    print("**********************")
    print("\n1) Agregar un periodo.")
    print("2) Agregar una materia.")
    print("3) Agregar alumno.")
    print("4) Calificar")
    print("5) Estadisticas.")
    print("6) SALIR")

        
def guardar_materia(claveMat,nombreMat):
    try:
        with sqlite3.connect(nombreEvidencia +".db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS Materias (Clave INTEGER PRIMARY KEY, Nombre TEXT NOT NULL);")
            valores = {"claveM":claveMat, "nombreM":nombreMat}
            mi_cursor.execute("INSERT INTO Materias VALUES(:claveM,:nombreM)", valores)
            print("*** MATERIA AGREGADA EXITOSAMENTE ***")
            print("")
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()

def guardar_periodo(claveP,nombreP):
    try:
        with sqlite3.connect(nombreEvidencia +".db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS Periodo (Clave INTEGER PRIMARY KEY, Nombre TEXT NOT NULL);")
            valores = {"clave":claveP, "nombre":nombreP}
            mi_cursor.execute("INSERT INTO Periodo VALUES(:clave,:nombre)", valores)
            print("*** PERIODO AGREGADO EXITOSAMENTE ***")
            print("")
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()

def guardar_alumno(clave,nombre, periodo):
    try:
        with sqlite3.connect(nombreEvidencia +".db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS Alumno (Matricula INTEGER PRIMARY KEY, Nombre TEXT NOT NULL, Periodo INTEGER NOT NULL, FOREIGN KEY (Periodo) REFERENCES periodo(Clave));")
            valores = {"clave":clave, "nombre":nombre, "periodo":periodo}
            mi_cursor.execute("INSERT INTO Alumno VALUES(:clave,:nombre,:periodo)", valores)
            print("*** ALUMNO AGREGADO EXITOSAMENTE ***")
            print("")
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()
        
def asignar_calificaciones(matricula, clave_materia, calificacion):
    try:
        with sqlite3.connect(nombreEvidencia +".db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute('CREATE TABLE IF NOT EXISTS Calificaciones(Matricula INTEGER NOT NULL, Clave_materia INTEGER NOT NULL, Calificacion INTEGER NOT NULL,FOREIGN KEY(Matricula) REFERENCES Alumno(Clave), FOREIGN KEY(Clave_materia) REFERENCES Materias(Clave));')
            valores = {'matricula':matricula,'clave_materia':clave_materia,'calificacion':calificacion}
            mi_cursor.execute("INSERT INTO calificaciones VALUES(:matricula,:clave_materia,:calificacion)", valores)
            print('*** CALIFICACIONES AGREGADAS EXITOSAMENTE ***')
            print('')
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()
        
def materiaXalumnos():
    try:
        with sqlite3.connect(nombreEvidencia +".db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT a.Nombre,c.Calificacion FROM Alumno as a INNER JOIN Calificaciones as c on a.Matricula = c.Matricula")
            alumnos = mi_cursor.fetchall()
            print(alumnos)
            m = pd.DataFrame(alumnos)
            print(m.describe())
            print(m)
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()

def materiaXalumno(clave):
    try:
        with sqlite3.connect(nombreEvidencia +".db") as conn:
            mi_cursor = conn.cursor()
            valor = {'clave':clave}
            mi_cursor.execute("SELECT a.nombre,c.calificacion FROM Alumno a INNER JOIN Calificaciones c WHERE a.Matricula = c.Matricula AND c.Matricula = :clave",valor)
            alumnos = mi_cursor.fetchall()
            est_alumno = pd.DataFrame(alumnos)
            for alumno in alumnos:
                print(alumno)
            print(est_alumno.describe())
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()
        
def estXmaterias():
    try:
        with sqlite3.connect(nombreEvidencia +".db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT a.Nombre, m.Nombre,c.Calificacion FROM Materias m INNER JOIN Calificaciones c on m.Clave = c.Clave_Materia INNER JOIN Alumno a on c.Matricula = a.Matricula ORDER BY m.Nombre")
            materias = mi_cursor.fetchall()
            for materia in materias:
                print(materia)
            mat = pd.DataFrame(materias)
            print(mat.describe())
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()
        
def estXmateria(clave):
    try:
        with sqlite3.connect(nombreEvidencia +".db") as conn:
            mi_cursor = conn.cursor()
            valor = {'clave':clave}
            mi_cursor.execute("SELECT m.Nombre, a.Nombre, c.Calificacion FROM Materias m INNER JOIN Calificaciones c on m.Clave = c.Clave_Materia INNER JOIN Alumno a on c.Matricula = a.Matricula WHERE m.Clave = :clave",valor)
            materia_indv = mi_cursor.fetchall()
            for materia in materia_indv:
                print(materia)
            print()
            Xmateria = pd.DataFrame(materia_indv)
            print(Xmateria.describe())
            print()
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()
        
def estXperiodos():
    try:
        with sqlite3.connect(nombreEvidencia +".db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT p.Nombre,a.Nombre,c.Calificacion FROM Periodo p INNER JOIN Alumno a INNER JOIN Calificaciones c WHERE p.Clave = a.Periodo and a.Matricula = c.Matricula")
            periodo = mi_cursor.fetchall()
            for periodos in periodo:
                print(periodos)
            m = pd.DataFrame(periodo)
            print(m.describe())
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()

def estXperiodo(clave):
    try:
        with sqlite3.connect(nombreEvidencia + ".db") as conn:
            mi_cursor = conn.cursor()
            valor = {"clave":clave}
            mi_cursor.execute("SELECT p.Nombre, a.Nombre, c.Calificacion FROM periodo p INNER JOIN alumno a on p.Clave = a.Periodo INNER JOIN calificaciones c on a.Matricula = c.Matricula WHERE p.Clave =:clave",valor)
            periodo_indv = mi_cursor.fetchall()
            for periodo in periodo_indv:
                print(periodo)
            Xperiodo = pd.DataFrame(periodo_indv)
            print(Xperiodo.describe())
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()

nombreEvidencia = input("¿Qué nombre tiene su base de datos? ")

ciclo_principal = True

while ciclo_principal:
    continuar = True
    desplegar_menu_principal()
    opcion = input("\n Indique su elección: ")
    if opcion == "1":
        while continuar:
            print("* Favor de darnos la clave con la que se estarán manejando los periodos *")
            claveP = int(input("Clave del periodo a agregar: "))
            nombreP = input("Periodo a agregar, ej: 'Agosto-Diciembre 2020': ")
            guardar_periodo(claveP,nombreP)
            decisionP = input("Agregar otro periodo\n1)Si            2)No\n")
            print()
            if decisionP == "1":
                pass
            elif decisionP == "2":
                continuar = False
            else:
                print(f"Lo siento, la opción *{decisionP}* no es una opción válida")
                print()
        pass
    elif opcion == "2":#Alta Materia
        while continuar:
            print("* Favor de darnos la clave del materia. *")
            claveMat = int(input("Clave de materia a agregar: "))
            nombreMat = input("Nombre de la materia a agregar: ")
            guardar_materia(claveMat,nombreMat)
            decisionMat = input("Agregar otro materia\n1) Si         2) No\n")
            print()
            if decisionMat == "1":
                pass
            elif decisionMat == "2":
                continuar = False
            else:
                print(f"Lo siento, la opción *{decisionMat}* no es una opción válida")
                print("")  
        pass
    elif opcion == "3":
        while continuar:
            print("* Favor de darnos la clave del alumno. *")
            claveA = int(input("Clave de alumno a agregar: "))
            nombreA = input("Nombre del alumno a agregar: ")
            periodo = int(input("Clave del periodo en curso: "))
            guardar_alumno(claveA,nombreA, periodo)
            decisionAlumno = input("Agregar otro alumno\n1) Si         2) No\n")
            print()
            if decisionAlumno == "1":
                pass
            elif decisionAlumno == "2":
                continuar = False
            else:
                print(f"Lo siento, la opción *{decisionAlumno}* no es una opción válida")
                print("")
    elif opcion == "4":#Consulta única
        while continuar:
            matricula = int(input('* Favor de proporcionar la matricula *\n'))
            clave_materia = int(input('* Ingresa la clave de la materia *\n'))
            calificacion = int(input('* Ingresa la calificacion *\n'))
            asignar_calificaciones(matricula, clave_materia, calificacion)
            decisionCalif = int(input('Calificar a otro alumno\n 1)Si            2)No\n'))
            print()
            if decisionCalif == 1:
                pass
            elif decisionCalif == 2:
                continuar = False
            else:
                print(f"Lo siento, la opción *{decisionCalif}* no es una opción válida")
                print()
    elif opcion == "5":
        while continuar:
            print(f"Eliga la opcion de como quiere sus estadisticas")
            decisionEst =input('Elige el formato de estadisticas:\n 1)Alumno    2)Materia    3)Periodo     4)Salir\n')
            print()
            if decisionEst == "1":
                si = True
                while si:
                    decisionAl =input('Selecciona una opción de como desplegar tus datos:1\n 1)Alumnos    2)Alumno    3)Salir\n')
                    if decisionAl == "1":
                        materiaXalumnos()
                        print()
                    elif decisionAl == "2":
                        clave = int(input("Introduce la matricula del alumno: "))
                        materiaXalumno(clave)
                        print()
                    elif decisionAl == "3":
                        si = False
                    else:
                        print (f"Lo siento, la opción *{decisionAl}* no es una opción válida")
            elif decisionEst == "2":
                decision = int(input('Selecciona si lo deseas por:\n1) Materia         2) Conjunto de materias\n'))
                if decision == 1:
                    clave = int(input('Selecciona la clave de la materia \n'))
                    estXmateria(clave)
                    print()
                else:
                    estXmaterias()
                    print()
            elif decisionEst == "3":
                decision = int(input("Selecciona si desea por:\n1) Periodo           2) Conjunto de periodos\n"))
                print()
                if decision == 1:
                    clave = int(input('Ingresa la clave del periodo\n'))
                    print()
                    estXperiodo(clave)
                elif decision == 2:
                    estXperiodos()
                else:
                    print("Seleccione una opcion valida\n")
                print()
            elif decisionEst == "4":
                continuar = False
            else:
                print(f"Lo siento, la opción *{decisionEst}* no es una opción válida")
    elif opcion == "6":#Salir
        ciclo_principal = False
    else:
        print(f"Lo siento, la opción *{opcion}* no es una opción válida")
        print("")
print("PROGRAMA FINALIZADO")
