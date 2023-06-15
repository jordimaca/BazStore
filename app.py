#Incluir el Framework Flask
import os #quick f
from flask import Flask

#Importar la plantilla HTML. Para guardar datos desde el formulario importamos request y redirect
from flask import render_template, request, redirect

#Importar para obtener informacion de la imagen 
from flask import send_from_directory

#Crear la aplicaciontemplates
app=Flask(__name__)

#Colocar la palabra clave slash (/) con la cual se va a acceder a la url, para indicarle que cuando se le solicite buscar en esa ruta (diagonal /) va a mostrar un inicio.
@app.route('/')
#Crear una funcion con la palabra reservada def
def raiz():
    #Retornar la ubicacion del template que se desea mostrar
    return render_template('sitio/inicio.html')
#Funciones de navegacion
@app.route('/inicio.html')
def inicio():
    return render_template('sitio/inicio.html')

@app.route('/categoria_accesorios.html')
def accesorios():
    return render_template('sitio/categoria_accesorios.html')
@app.route('/categoria_hombre.html')
def hombre():
    return render_template('sitio/categoria_hombre.html')
@app.route('/categoria_mujer.html')
def mujer():
    return render_template('sitio/categoria_mujer.html')
@app.route('/categoria_nuevo.html')
def nuevo():
    return render_template('sitio/categoria_nuevo.html')

@app.route('/login.html')
def login():
    return render_template('sitio/login.html')
@app.route('/registro.html')
def registro():

    return render_template('sitio/registro.html')
@app.route('/perfil.html')
def perfil():
    return render_template('sitio/perfil.html')
@app.route('/vendedor.html')
def vendedor():
    return render_template('sitio/vendedor.html')

@app.route('/producto.html')
def producto():
    return render_template('sitio/producto.html')

    #Subcategorias
@app.route('/subcategorias/accesorios_anillos.html')
def anillos():
    return render_template('sitio/subcategorias/accesorios_anillos.html')

@app.route('/subcategorias/mujer_blusas.html')
def blusas():
    return render_template('sitio/subcategorias/mujer_blusas.html')

@app.route('/subcategorias/accesorios_brazaletes.html')
def brazaletes():
    return render_template('sitio/subcategorias/accesorios_brazaletes.html')

@app.route('/subcategorias/accesorios_cadenas.html')
def cadenas():
    return render_template('sitio/subcategorias/accesorios_cadenas.html')

@app.route('/subcategorias/hombre_camisa.html')
def camisa():
    return render_template('sitio/subcategorias/hombre_camisa.html')

@app.route('/subcategorias/mujer_deportivo.html')
def deportivo():
    return render_template('sitio/subcategorias/mujer_deportivo.html')

@app.route('/subcategorias/hombre_deportivo.html')
def deportivoh():
    return render_template('sitio/subcategorias/hombre_deportivo.html')

@app.route('/subcategorias/mujer_jeans.html')
def jeans():
    return render_template('sitio/subcategorias/mujer_jeans.html')

@app.route('/subcategorias/hombre_jeans.html')
def jeansh():
    return render_template('sitio/subcategorias/hombre_jeans.html')

@app.route('/subcategorias/accesorios_otros.html')
def otros():
    return render_template('sitio/subcategorias/accesorios_otros.html')

@app.route('/subcategorias/accesorios_reloj.html')
def reloj():
    return render_template('sitio/subcategorias/accesorios_reloj.html')

@app.route('/subcategorias/hombre_tshirts.html')
def tshirts():
    return render_template('sitio/subcategorias/hombre_tshirts.html')

@app.route('/subcategorias/mujer_vestidos.html')
def vestidos():
    return render_template('sitio/subcategorias/mujer_vestidos.html')

@app.route('/subcategorias/mujer_zapatos.html')
def zapatos():
    return render_template('sitio/subcategorias/mujer_zapatos.html')

@app.route('/subcategorias/hombre_zapatos.html')
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