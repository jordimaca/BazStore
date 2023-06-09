import os
#Incluir el Framework Flask
from flask import Flask

#Importar la plantilla HTML. Para guardar datos desde el formulario importamos request y redirect

from flask import render_template, request,redirect, url_for,session

# Importar el enlace a base de datos con MySQL
from flaskext.mysql import MySQL

# Importar controlador del tiempo
from datetime import datetime

#Importar para obtener informacion de la imagen 
from flask import send_from_directory

import re
#Crear la aplicacion templates
app=Flask(__name__)

#crear llave secreta
app.secret_key="dicresoft"

# Crear conexión a la base de datos
mysql=MySQL(app)

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='bazstore'

# Agregar el valor para inicializar nuestra aplicación
mysql.init_app(app)

IMG_FOLDER = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER
#Colocar la palabra clave slash (/) con la cual se va a acceder a la url, para indicarle que cuando se le solicite buscar en esa ruta (diagonal /) va a mostrar un inicio.
@app.route('/')
#Crear una funcion con la palabra reservada def
def inicio():
    #Retornar la ubicacion del template que se desea mostrar
    return render_template('sitio/inicio.html')

#login y registro

@app.route('/login/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connect().cursor()
        cursor.execute('SELECT * FROM usuario WHERE nombre = %s AND contraseña = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['usuario']= username
            session['img']=cursor.execute('SELECT imagen FROM usuario WHERE nombre = %s AND contraseña = %s', (username, password,))
            return redirect('/')
        else:
            msg = 'contraseña/usuario incorrectos !'
   
    return render_template('sitio/login.html', msg=msg)


@app.route('/registro' ,methods =['GET', 'POST'])
def registro():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'telefono' in request.form :
        username = request.form['username']
        email = request.form['email']
        celular = request.form['telefono']
        password = request.form['password']
        imagen=os.path.join(app.config['UPLOAD_FOLDER'],'user-circle-icon.svg')
        #Abrir la conexion a la base de datos
        conexion=mysql.connect()
        #Se crea un cursor
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM usuario WHERE nombre = % s;', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'La cuenta ya existe.'
        else:
            sql ='INSERT INTO usuario VALUES (NULL, % s, % s, % s, % s, % s);'
            datos=(username, email, celular, password, imagen)
            cursor.execute(sql, datos)
            conexion.commit()
            return redirect('/login')
    elif request.method == 'POST':
        msg = 'Por favor, llene el formulario de forma correcta.'
    return render_template('sitio/registro.html', msg = msg)

#log out
@app.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('usuario',None)
    return redirect('/login')
#rutas principales

@app.route('/accesorios')
def accesorios():
    return render_template('sitio/categoria_accesorios.html')
@app.route('/hombre')
def hombre():
    return render_template('sitio/categoria_hombre.html')
@app.route('/mujer')
def mujer():
    return render_template('sitio/categoria_mujer.html')
@app.route('/nuevo')
def nuevo():
    return render_template('sitio/categoria_nuevo.html')

@app.route('/perfil')
def perfil():
    return render_template('usuario/perfil.html')
@app.route('/vendedor')
def vendedor():
    return render_template('usuario/vendedor.html')

#nesecita un arreglo para especificar el producto
@app.route('/articulo')
def articulo():
    return render_template('usuario/articulo.html')

#Subcategorias
@app.route('/accesorios/anillos')
def anillos():
    return render_template('sitio/subcategorias/accesorios_anillos.html')

@app.route('/mujer/blusas')
def blusas():
    return render_template('sitio/subcategorias/mujer_blusas.html')

@app.route('/accesorios/brazaletes')
def brazaletes():
    return render_template('sitio/subcategorias/accesorios_brazaletes.html')

@app.route('/accesorios/cadenas')
def cadenas():
    return render_template('sitio/subcategorias/accesorios_cadenas.html')

@app.route('/hombre/camisa')
def camisa():
    return render_template('sitio/subcategorias/hombre_camisa.html')

@app.route('/mujer/deportivo')
def deportivo():
    return render_template('sitio/subcategorias/mujer_deportivo.html')

@app.route('/hombre/deportivo')
def deportivoh():
    return render_template('sitio/subcategorias/hombre_deportivo.html')

@app.route('/mujer/jeans')
def jeans():
    return render_template('sitio/subcategorias/mujer_jeans.html')

@app.route('/hombre/jeans')
def jeansh():
    return render_template('sitio/subcategorias/hombre_jeans.html')

@app.route('/accesorios/otros')
def otros():
    return render_template('sitio/subcategorias/accesorios_otros.html')

@app.route('/accesorios/reloj')
def reloj():
    return render_template('sitio/subcategorias/accesorios_reloj.html')

@app.route('/hombre/tshirts')
def tshirts():
    return render_template('sitio/subcategorias/hombre_tshirts.html')

@app.route('/mujer/vestidos')
def vestidos():
    return render_template('sitio/subcategorias/mujer_vestidos.html')

@app.route('/mujer/zapatos')
def zapatos():
    return render_template('sitio/subcategorias/mujer_zapatos.html')

@app.route('/hombre/zapatos')
def zapatosh():
    return render_template('sitio/subcategorias/hombre_zapatos.html')

#Crear una ruta para mostrar la imagen 
@app.route('/images/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('templates/sitio/images'),imagen) #solucion rapida dejalo encima y veras la opcion


#Crear una instancia para poder ejecutar nuestra aplicacion
if __name__ == '__main__':
    #Se utiliza el modo debug para que se vean los cambios
    app.run(debug=True)