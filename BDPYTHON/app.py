from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
app.secret_key = 'clave_secreta'

conexion = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='con_medico',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def usuarios():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM pacientes")
    datos = cursor.fetchall()
    cursor.close()
    return render_template('usuarios.html', usuarios=datos)

if __name__ == '__main__':
    app.run(debug=True)
