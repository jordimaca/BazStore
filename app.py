#Incluir el Framework Flask
import os #quick f
from flask import Flask

#Importar la plantilla HTML. Para guardar datos desde el formulario importamos request y redirect
from flask import render_template, request, redirect

#
#Crear la aplicaciontemplates
app=Flask(__name__)

#Colocar la palabra clave slash (/) con la cual se va a acceder a la url, para indicarle que cuando se le solicite buscar en esa ruta (diagonal /) va a mostrar un inicio.
@app.route('/')
#Crear una funcion con la palabra reservada def
def inicio():
    #Retornar la ubicacion del template que se desea mostrar
    return render_template('sitio/inicio.html')


#INCLUIR LAS PAGINAS DEL ADMIN
#Indicar que se abra otra pagina dentro del sitio
@app.route('/admin/') #Para que al crear el enlace a admin/libros no se duplique el admin (admin/admin/libros), se agrega un slash (/) al final.
#Crear una funcion con la palabra reservada def
def admin_index():
    #Retornar la ubicacion del template que se desea mostrar
    return render_template('admin/index.html')

#Acceder al login
@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

#Enrutar el login al metodo POST
@app.route('/admin/login', methods=['POST'])
def admin_login_post():
    _usuario=request.form['txtUsuario']
    _password=request.form['txtPassword']
    print(_usuario)
    print(_password)

    if _usuario=='admin' and _password=='123':
        session['login'] = True
        session['usuario'] = 'Administrador'
        return redirect('/admin')
    return render_template("admin/login.html" , mensaje="Usuario o contraseña Invalido")

#Crear una instancia para poder ejecutar nuestra aplicacion
if __name__ == '__main__':
    #Se utiliza el modo debug para que se vean los cambios
    app.run(debug=True)