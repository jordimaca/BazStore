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
@app.route('/subcategorias/subcategoria_anillos.html')
def anillos():
    return render_template('sitio/subcategorias/subcategoria_anillos.html')

@app.route('/subcategorias/subcategoria_blusas.html')
def blusas():
    return render_template('sitio/subcategorias/subcategoria_blusas.html')

@app.route('/subcategorias/subcategoria_brazaletes.html')
def brazaletes():
    return render_template('sitio/subcategorias/subcategoria_brazaletes.html')

@app.route('/subcategorias/subcategoria_cadenas.html')
def cadenas():
    return render_template('sitio/subcategorias/subcategoria_cadenas.html')

@app.route('/subcategorias/subcategoria_camisa.html')
def camisa():
    return render_template('sitio/subcategorias/subcategoria_camisa.html')

@app.route('/subcategorias/subcategoria_deportivo.html')
def deportivo():
    return render_template('sitio/subcategorias/subcategoria_deportivo.html')

@app.route('/subcategorias/subcategoria_deportivoh.html')
def deportivoh():
    return render_template('sitio/subcategorias/subcategoria_deportivoh.html')

@app.route('/subcategorias/subcategoria_jeans.html')
def jeans():
    return render_template('sitio/subcategorias/subcategoria_jeans.html')

@app.route('/subcategorias/subcategoria_jeansh.html')
def jeansh():
    return render_template('sitio/subcategorias/subcategoria_jeansh.html')

@app.route('/subcategorias/subcategoria_otros.html')
def otros():
    return render_template('sitio/subcategorias/subcategoria_otros.html')

@app.route('/subcategorias/subcategoria_reloj.html')
def reloj():
    return render_template('sitio/subcategorias/subcategoria_reloj.html')

@app.route('/subcategorias/subcategoria_tshirts.html')
def tshirts():
    return render_template('sitio/subcategorias/subcategoria_tshirts.html')

@app.route('/subcategorias/subcategoria_vestidos.html')
def vestidos():
    return render_template('sitio/subcategorias/subcategoria_vestidos.html')

@app.route('/subcategorias/subcategoria_zapatos.html')
def zapatos():
    return render_template('sitio/subcategorias/subcategoria_zapatos.html')

@app.route('/subcategorias/subcategoria_zapatosh.html')
def zapatosh():
    return render_template('sitio/subcategorias/subcategoria_zapatosh.html')

#Crear una ruta para mostrar la imagen 
@app.route('/images/<imagen>')
def imagenes(imagen):
    print(imagen)
    return send_from_directory(os.path.join('templates/sitio/images'),imagen) #solucion rapida dejalo encima y veras la opcion
#Crear una instancia para poder ejecutar nuestra aplicacion
if __name__ == '__main__':
    #Se utiliza el modo debug para que se vean los cambios
    app.run(debug=True)