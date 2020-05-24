import sys
import sqlite3
import pandas as pd
from sqlite3 import Error
import statistics


lista_promedios=[]

def desplegar_menu_principal():
    print("**********************")
    print("*** MENÚ PRINCIPAL ***")
    print("**********************")
    print("\n1) Agregar alumnos.")
    print("2) Agregar materias.")
    print("3) Calificar")
    print("4) Estadisticas.")
    print("5) Alumnos reprobados.")
    print("6) Promedios de menor a mayor")
    print('7) Salir')

        
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

def guardar_alumno(clave,nombre,periodo):
    try:
        with sqlite3.connect(nombreEvidencia +".db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("CREATE TABLE IF NOT EXISTS Alumno (Matricula INTEGER PRIMARY KEY, Nombre TEXT NOT NULL, Periodo TEXT NOT NULL);")
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
            EstMatTotalAl = m.describe()
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()
    
    decisionAlumnoTXT = input('¿Exportar a TXT?:\n1) Si         2) No\n')
    if decisionAlumnoTXT == "1":
        txtFile=open('EstMatAlumnos.txt', 'w')
        txtFile.write(EstMatTotalAl.to_string())
        txtFile.close()
        print("Finalizamos.")
    elif decisionAlumnoTXT not in ["1","2"]:
        print("Esa opción no es valida.")
        print("*" * 40)
        pass   
        
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
            EstMatxAlum = est_alumno.describe()
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()
    
    decisionAlumnoTXT = input('¿Exportar a TXT?:\n1) Si         2) No\n')
    if decisionAlumnoTXT == "1":
        txtFile=open('EstAlumSeleccionado.txt', 'w')
        txtFile.write(EstMatxAlum.to_string())
        txtFile.close()
        print("Finalizamos.")
    elif decisionAlumnoTXT not in ["1","2"]:
        print("Esa opción no es valida.")
        print("*" * 40)
        pass
        
def reprobados():
    try:
        with sqlite3.connect(nombreEvidencia +".db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT a.nombre FROM Alumno a INNER JOIN Calificaciones c ON a.matricula = c.matricula WHERE c.Calificacion < 70")
            alumnos = mi_cursor.fetchall()
            for alumno in alumnos:
                reprobados = alumnos.count(alumno)
                if reprobados > 1:
                    print(alumno)
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
            EstxMaterias = mat.describe()
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()
        
    decisionAlumnoTXT = input('¿Exportar a TXT?:\n1) Si         2) No\n')
    if decisionAlumnoTXT == "1":
        txtFile=open('estadisticasPorMaterias.txt', 'w')
        txtFile.write(EstxMaterias.to_string())
        txtFile.close()
        print("Finalizamos.")
    elif decisionAlumnoTXT not in ["1","2"]:
        print("Esa opción no es valida.")
        print("*" * 40)
        pass
        
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
            MatSel = Xmateria.describe()
            print()
            mi_cursor.execute("SELECT AVG(c.Calificacion),m.Nombre FROM Materias m INNER JOIN Calificaciones c on m.Clave = c.Clave_Materia WHERE m.Clave = :clave",valor)
            promedio = mi_cursor.fetchall()
            for x in promedio:
                lista_promedios.append(x)
            lista_promedios.sort()
    except Error as e:
        print (e)
        print("*" * 80)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        print("*" * 80)
    finally:
        conn.close()
        
    decisionAlumnoTXT = input('¿Exportar a TXT?:\n1) Si         2) No\n')
    if decisionAlumnoTXT == "1":
        txtFile=open('EstadisticaMateriaSeleccionada.txt', 'w')
        txtFile.write(MatSel.to_string())
        txtFile.close()
        print("Finalizamos.")
    elif decisionAlumnoTXT not in ["1","2"]:
        print("Esa opción no es valida.")
        print("*" * 40)
        pass
    
nombreEvidencia = input("¿Qué nombre tiene su base de datos? ")

ciclo_principal = True

while ciclo_principal:
    continuar = True
    desplegar_menu_principal()
    opcion = input("\n Indique su elección: ")
    if opcion == "1":
        periodo = input("Periodo en el que se estará trabajando: ")
        while continuar:
            print("* Favor de darnos la clave del alumno. *")
            claveA = int(input("Clave de alumno a agregar: "))
            nombreA = input("Nombre del alumno a agregar: ")
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
            matricula = int(input('* Favor de proporcionar la matricula *\n'))
            clave_materia = int(input('* Ingresa la clave de la materia *\n'))
            calificacion = int(input('* Ingresa la calificacion *\n'))
            asignar_calificaciones(matricula, clave_materia, calificacion)
            decisionCalif = input('Calificar a otro alumno\n 1)Si            2)No\n')
            print()
            if decisionCalif == "1":
                pass
            elif decisionCalif == "2":
                continuar = False
            else:
                print(f"Lo siento, la opción *{decisionCalif}* no es una opción válida")
                print()
    elif opcion == "4":#Consulta única a decision del usuario
        while continuar:
            print(f"Eliga la opcion de como quiere sus estadisticas")
            decisionEst =input('Elige el formato de estadisticas:\n 1)Alumno    2)Materia       3)Salir\n')
            print()
            if decisionEst == "1":
                si = True
                while si:
                    decisionAl =input('Selecciona una opción de como desplegar tus datos:1\n 1)Alumnos    2)Alumno    3)Salir\n')
                    if decisionAl == "1":
                        materiaXalumnos()
                        print()
                        alumnos = ()
                    elif decisionAl == "2":
                        clave = int(input("Introduce la matricula del alumno: "))
                        materiaXalumno(clave)
                        print()
                    elif decisionAl == "3":
                        si = False
                    else:
                        print (f"Lo siento, la opción *{decisionAl}* no es una opción válida")
            elif decisionEst == "2":
                decision = input('Selecciona si lo deseas por:\n1) Materia         2) Conjunto de materias\n')
                if decision == "1":
                    clave = int(input('Selecciona la clave de la materia \n'))
                    estXmateria(clave)
                    print()
                elif decision == "2":
                    estXmaterias()
                    print()
            elif decisionEst == "3":
                continuar = False
            else:
                print(f"Lo siento, la opción *{decisionEst}* no es una opción válida")
    elif opcion == "5":
        print("A continuación los alumnos que reprobaron dos o más materias")
        reprobados()
    elif opcion == "6":
        print('*PROMEDIO DE MENOR A MAYOR')
        print('Promedio/Materia')
        for i in lista_promedios:
            print(i)
    elif opcion == "7":
        ciclo_principal = False
    else:
        print(f"Lo siento, la opción *{opcion}* no es una opción válida")
        print("")
print("PROGRAMA FINALIZADO")
                    