#!C:\Users\User\AppData\Local\Programs\Python\Python311\python.exe

# Copiar la carpeta del proyecto a xampp\htdocs.

# Modificar Apache Config (primera opción) y agregar:
# ScriptAlias /cgi-bin/ “C:/xampp/htdocs/<path_html>/cgi-bin/”
# <Directory “C:/xampp/htdocs/<path_html>/cgi-bin/”>
#    Options +ExecCGI
#    AddHandler cgi-script .cgi .py
# </Directory>

# En el navegador abrir http://localhost/<path>/index.html

#########################################

import sqlite3

import cgi

form = cgi.FieldStorage()
nombre = form.getvalue("nombre")
edad = form.getvalue("edad")
materia = form.getvalue("materia")
insertar = form.getvalue("insertar")

#########################################

def init_table():
    conn = sqlite3.connect("registro.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS estudiantes(nombre TEXT, edad NUMERIC, materia TEXT)")
    except sqlite3.OperationalError:
        print("No se pudo crear la tabla. Quizás ya existe.")
    finally:
        conn.commit()
        conn.close()

def ingresar():
    conn = sqlite3.connect("registro.sqlite")
    cursor = conn.cursor()    
    cursor.execute("INSERT INTO estudiantes (nombre, edad, materia) VALUES (?, ?, ?)", (nombre, edad, materia))
    conn.commit()
    conn.close()

def consultar():
    conn = sqlite3.connect("registro.sqlite")
    cursor = conn.cursor()
    try:
         cursor.execute("SELECT * FROM estudiantes")
         data = cursor.fetchall()
         return data
    except sqlite3.OperationalError:
         print("No se pudo llevar a cabo la consulta.")
    print(data)
    conn.close()

init_table()

if nombre and edad and materia:
    ingresar()

consultar()

#########################################

print("Content-type: text/html\n")
datos = consultar()

tabla_html = '<table>'
tabla_html += '<tr><th>Estudiante</th><th>Edad</th><th>Materia</th></tr>'

for fila in datos:
    tabla_html += '<tr>'
    for dato in fila:
        tabla_html += f'<td>{dato}</td>'
    tabla_html += '</tr>'
tabla_html += '</table>'

print(tabla_html)