import os
#Incluir el Framework Flask
from flask import Flask

#Importar la plantilla HTML. Para guardar datos desde el formulario importamos request y redirect

from flask import render_template, request,redirect,session

# Importar el enlace a base de datos con MySQL
from flaskext.mysql import MySQL

# Importar controlador del tiempo
from datetime import datetime

#Importar para obtener informacion de la imagen 
from flask import send_from_directory

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
            session['login'] = True
            session['usuario']= username
            #cursor.execute('SELECT id_usuario FROM usuario WHERE nombre = %s AND contraseña = %s', (username, password,))
            session['id']=cursor.execute('SELECT id_usuario FROM usuario WHERE nombre = %s AND contraseña = %s', (username, password,))
            cursor.execute('SELECT imagen FROM usuario WHERE nombre = %s ', (username))
            session['img']=cursor.fetchone()
            return redirect('/')
        else:
            msg = 'Contraseña o usuario incorrectos'
   
    return render_template('sitio/login.html', msg=msg)

#hacer la confirmacion de la contraseña
@app.route('/registro' ,methods =['GET', 'POST'])
def registro():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'telefono' in request.form and (request.form['password2'] == request.form['password']):
        #almacenar en formulario en variables
        username = request.form['username']
        email = request.form['email']
        celular = request.form['telefono']
        password = request.form['password']
        imagen=os.path.join(app.config['UPLOAD_FOLDER'],'user-icon.svg')
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
        msg = 'Vuelva a confirmar la contraseña.'
    return render_template('sitio/registro.html', msg = msg)

#log out
@app.route('/logout')
def logout():
    session.pop('login',None)
    session.pop('usuario',None)
    session.pop('id',None)
    session.pop('img',None)
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


#Subcategorias
@app.route('/accesorios/anillos')
def anillos():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/accesorios_anillos.html')

@app.route('/mujer/blusas')
def blusas():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/mujer_blusas.html')

@app.route('/accesorios/brazaletes')
def brazaletes():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/accesorios_brazaletes.html')

@app.route('/accesorios/cadenas')
def cadenas():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/accesorios_cadenas.html')

@app.route('/hombre/camisa')
def camisa():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/hombre_camisa.html')

@app.route('/mujer/deportivo')
def deportivo():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/mujer_deportivo.html')

@app.route('/hombre/deportivo')
def deportivoh():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/hombre_deportivo.html')

@app.route('/mujer/jeans')
def jeans():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/mujer_jeans.html')

@app.route('/hombre/jeans')
def jeansh():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/hombre_jeans.html')

@app.route('/accesorios/otros')
def otros():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/accesorios_otros.html')

@app.route('/accesorios/reloj')
def reloj():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/accesorios_reloj.html')

@app.route('/hombre/tshirts')
def tshirts():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/hombre_tshirts.html')

@app.route('/mujer/vestidos')
def vestidos():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/mujer_vestidos.html')

@app.route('/mujer/zapatos')
def zapatos():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/mujer_zapatos.html')

@app.route('/hombre/zapatos')
def zapatosh():
    if not 'login' in session:
        return redirect('/login')
    return render_template('sitio/subcategorias/hombre_zapatos.html')

#usuario

@app.route('/perfil',methods =['GET', 'POST'])
def perfil():
    if not 'login' in session:
        return redirect('/login')
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo`")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    print(articulos)
    return render_template('usuario/perfil.html',articulos=articulos)


@app.route('/perfil/publicar',methods =['POST'])
def publicar():
    #almacenar en formulario en variables
    nombre = request.form['nombre']
    precio = request.form['precio']
    adjunto = request.files['adjunto']
    talla = request.form['talla']
    ubicacion=request.form['ubicacion']
    condicion=request.form['condicion']
    tipo=request.form['tipo']
    subtipo=request.form['subtipo']
    descripcion=request.form['com']
    usuario=session['id']
    tiempo = datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')
    
    #Adjuntar Archivo 
    if adjunto.filename!='':
        nuevoNombre=horaActual+"_"+adjunto.filename
        adjunto.save("templates/sitio/images/"+nuevoNombre)

    #Abrir la conexion a la base de datos
    conexion=mysql.connect()
    #Se crea un cursor
    cursor = conexion.cursor()
    sql ='INSERT INTO articulo VALUES (NULL,%s, % s, % s, % s, % s, % s,% s,% s,% s,% s);'
    datos=(usuario,nombre,nuevoNombre , precio,subtipo, talla, ubicacion,condicion,descripcion,tipo)
    cursor.execute(sql, datos)
    conexion.commit()

    return redirect('/perfil')

#Borrar articulo
@app.route('/perfil/borrar', methods=['POST'])
def borrar_articulo():
 
    _id=request.form['txtID']
    print(_id)

    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `articulo` WHERE id_articulo=%s",(_id))
    articulo=cursor.fetchall()
    conexion.commit()
    print(articulo)

    # Verifica si la imagen existe antes de borrar
    if os.path.exists("templates/sitio/img"+str(articulo[0][0])):
        #si la imagen exite le indicamos que elimine el registro
        os.unlink("templates/sitio/img"+str(articulo[0][0]))

    # Borrar registro
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM `articulo` WHERE id_articulo=%s",(_id))
    conexion.commit()

    # Redireccionar a /admin/libros
    return redirect('/perfil')







@app.route('/vendedor')
def vendedor():
    if not 'login' in session:
        return redirect('/login')
    return render_template('usuario/vendedor.html')
#Nesecita un arreglo para especificar el producto
@app.route('/<name>')
def articulo(name):
    if not 'login' in session:
        return redirect('/login')
    
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE nombre_articulo = %s",name)
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    print(articulos)
    for articulo in articulos:
        cursor.execute("Select * FROM `usuario` WHERE id_usuario = %s",articulo[1])
        #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
        usuario=cursor.fetchall()
        conexion.commit()
        print(usuario)

    return render_template('usuario/articulo.html', articulos=articulos, usuario=usuario)

#Crear una ruta para mostrar la imagen 
@app.route('/images/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('templates/sitio/images'),imagen)

#Crear una instancia para poder ejecutar nuestra aplicacion
if __name__ == '__main__':
    #Se utiliza el modo debug para que se vean los cambios
    app.run(debug=True)

