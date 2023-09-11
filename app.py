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

#IMG_FOLDER = os.path.join('images')

#app.config['UPLOAD_FOLDER'] = IMG_FOLDER
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
            cursor.execute('SELECT id_usuario FROM usuario WHERE nombre = %s', (username))
            session['id']=cursor.fetchone()
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
        imagen=os.path.join('user-icon.svg')
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
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Accesorio'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/categoria_accesorios.html',articulos=articulos)
@app.route('/hombre')
def hombre():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Hombre'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/categoria_hombre.html',articulos=articulos)
@app.route('/mujer')
def mujer():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Mujer'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/categoria_mujer.html',articulos=articulos)
@app.route('/nuevo')
def nuevo():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` ORDER BY imagen")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/categoria_nuevo.html',articulos=articulos)


#Subcategorias
# accesorios inicio
@app.route('/accesorios/anillos')
def anillos():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Accesorio' AND tipo='Anillos'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/accesorios_anillos.html',articulos=articulos)

@app.route('/accesorios/brazaletes')
def brazaletes():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Accesorio' AND tipo='Brazaletes'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/accesorios_brazaletes.html',articulos=articulos)

@app.route('/accesorios/cadenas')
def cadenas():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Accesorio' AND tipo='Cadenas'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/accesorios_cadenas.html',articulos=articulos)
@app.route('/accesorios/otros')
def otros():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Accesorio' AND tipo='Otros'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/accesorios_otros.html',articulos=articulos)

@app.route('/accesorios/reloj')
def reloj():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Accesorio' AND tipo='Reloj'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/accesorios_reloj.html',articulos=articulos)
# accesorios fin
# mujer inicio

@app.route('/mujer/blusas')
def blusas():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Mujer' AND tipo='Blusa'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/mujer_blusas.html',articulos=articulos)
@app.route('/mujer/deportivo')
def deportivo():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Mujer' AND tipo='Deportivo'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/mujer_deportivo.html',articulos=articulos)

@app.route('/mujer/pantalones')
def jeans():
     #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Mujer' AND tipo='Pantalon'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/mujer_jeans.html',articulos=articulos)

@app.route('/mujer/vestidos')
def vestidos():
     #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Mujer' AND tipo='Vestido'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/mujer_vestidos.html',articulos=articulos)

@app.route('/mujer/zapatos')
def zapatos():
     #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Mujer' AND tipo='Zapato'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/mujer_zapatos.html',articulos=articulos)
#mujer fin
#hombre inicio

@app.route('/hombre/camisa')
def camisa():
     #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Hombre' AND tipo='Camisa'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/hombre_camisa.html',articulos=articulos)



@app.route('/hombre/deportivo')
def deportivoh():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Hombre' AND tipo='Deportivo'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/hombre_deportivo.html',articulos=articulos)


@app.route('/hombre/pantalones')
def jeansh():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Hombre' AND tipo='Pantalon'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/hombre_jeans.html',articulos=articulos)

@app.route('/hombre/tshirts')
def tshirts():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Hombre' AND tipo='T-shirt'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/hombre_tshirts.html',articulos=articulos)


@app.route('/hombre/zapatos')
def zapatosh():
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE genero='Hombre' AND tipo='Zapato'")
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    return render_template('sitio/subcategorias/hombre_zapatos.html',articulos=articulos)
# hombre fin
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
    #print(articulos)
    return render_template('usuario/perfil.html',articulos=articulos)


#buscador 

@app.route('/buscador', methods=['GET', 'POST'])
def buscador():
    
    
    info = request.form['buscador']
    info=str(info)
    info='%'+info+'%'
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE nombre_articulo LIKE %s",(info))
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    
    return render_template('sitio/buscador.html',articulos=articulos)


@app.route('/perfil/publicarimg',methods =['POST'])
def publicarimg():
    _id=session['id']
    print(_id)

    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT imagen FROM `usuario` WHERE id_usuario=%s",(_id))
    articulo=cursor.fetchall()
    conexion.commit()
    print(articulo)

    # Verifica si la imagen existe antes de borrar
    if os.path.exists("templates/sitio/images/"+str(articulo[0][0])):
        #si la imagen exite le indicamos que elimine el registro
        os.unlink("templates/sitio/images/"+str(articulo[0][0]))

    
    adjunto = request.files['imagen']
    usuario=session['id']
    tiempo = datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')

    if adjunto.filename!='':
        adjuntonombre=horaActual+"_"+adjunto.filename
        adjunto.save("templates/sitio/images/"+adjuntonombre)

    #Abrir la conexion a la base de datos
    conexion=mysql.connect()
    #Se crea un cursor
    cursor = conexion.cursor()
    sql ='UPDATE usuario SET imagen=%s WHERE id_usuario=%s;'
    datos=(adjuntonombre,usuario)
    cursor.execute(sql, datos)
    conexion.commit()
    session.pop('img',None)
    cursor.execute('SELECT imagen FROM usuario WHERE id_usuario = %s ', (usuario))
    session['img']=cursor.fetchone()

    return redirect('/perfil')

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
    nuevoNombre = ""
    
    
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
    cursor.execute("SELECT imagen FROM `articulo` WHERE id_articulo=%s",(_id))
    articulo=cursor.fetchall()
    conexion.commit()
    print(articulo)

    # Verifica si la imagen existe antes de borrar
    if os.path.exists("templates/sitio/images/"+str(articulo[0][0])):
        #si la imagen exite le indicamos que elimine el registro
        os.unlink("templates/sitio/images/"+str(articulo[0][0]))

    # Borrar registro
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM `articulo` WHERE id_articulo=%s",(_id))
    conexion.commit()

    # Redireccionar a /perfil
    return redirect('/perfil')


#Borrar perfil
@app.route('/perfil/borrarperfil')
def borrar_perfil():
 
    usuario= session['id']
    # Borrar registro
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM articulo WHERE id_usuario=%s",(usuario))
    cursor.execute("DELETE FROM usuario WHERE id_usuario=%s",(usuario))
    conexion.commit()

    # Redireccionar a /perfil
    return redirect('/login/')


@app.route('/<id_usuario>')
def vendedor(id_usuario):
    if not 'login' in session:
        return redirect('/login')
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE id_usuario=%s",(id_usuario))
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    #Realizar una conexion de la bd creando la variable conexion
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `usuario` WHERE id_usuario=%s",(id_usuario))
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    usuario=cursor.fetchall()
    conexion.commit()
    print(usuario)
    
    
    
    return render_template('usuario/vendedor.html',articulos=articulos,usuario=usuario)
#Nesecita un arreglo para especificar el producto
@app.route('/<name>/<id_articulo>')
def articulo(name,id_articulo):
    if not 'login' in session:
        return redirect('/login')
    
    conexion=mysql.connect()
    #Reaizar una consulta
    cursor=conexion.cursor()
    #Ejecutar una consulta
    cursor.execute("Select * FROM `articulo` WHERE nombre_articulo = %s AND id_articulo = %s",(name,id_articulo))
    #Para mostrar creamos un variable, recuperamos todos los valores de la BD con Fetchall()
    articulos=cursor.fetchall()
    conexion.commit()
    #print(articulos)
    usuario=""
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
    app.run(debug=True, host = "localhost", port = 5000)

