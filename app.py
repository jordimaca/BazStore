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



#Crear la aplicaciontemplates
app=Flask(__name__)

# Crear conexión a la base de datos
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='bazstore'

# Agregar el valor para inicializar nuestra aplicación
mysql.init_app(app)

#Colocar la palabra clave slash (/) con la cual se va a acceder a la url, para indicarle que cuando se le solicite buscar en esa ruta (diagonal /) va a mostrar un inicio.
@app.route('/')
#Crear una funcion con la palabra reservada def
def inicio():
    #Retornar la ubicacion del template que se desea mostrar
    return render_template('sitio/inicio.html')

#login y registro

@app.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Pusiste mal la contraseña o el email. intenta nuevamente.'
        else:
            session['logged_in']= True
            return redirect('/')
    return render_template('sitio/login.html', error=error)

@app.route('/registro')
def registro():

    return render_template('sitio/registro.html')
#log out
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
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