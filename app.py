from flask import Flask, render_template, request
from model import Cliente
from pathlib import Path
from flask import abort

app = Flask(__name__)

Cliente.cargar_datos(str(Path('data') / 'clientes.csv'))





@app.route('/')
def index():
    # to dO: Cargar lista de clientes dende o modelo e pasala á vista clientes.html
    clientes = Cliente.todos()
    
    #Paginación.    
    PAGE_SIZE = 15  
    # Calcular la paginación
    _page = int(request.args.get('_page', 1))
    clientes = Cliente.todos()

    num_clientes = len(clientes)
    num_pages = (num_clientes + PAGE_SIZE - 1) // PAGE_SIZE
    clientes_paginados = clientes[(_page - 1) * PAGE_SIZE:_page * PAGE_SIZE]

    # Calcular las páginas para la paginación
    start_page = max(1, (_page - 1) // 3 * 3 + 1)
    end_page = min(num_pages, (_page - 1) // 3 * 3 + 4)
    pages = range(start_page, end_page)

# Renderizar la plantilla 'clientes.html' con los datos necesarios
    return render_template('clientes.html', clientes=clientes_paginados, pages=pages, _page=_page, num_pages=num_pages)
    

    

@app.route('/detalle_cliente/<int:id>')
def detalle_cliente(id):
    cliente = Cliente.buscar(id)  # Buscar el cliente según su ID
    
    if cliente is not None:
        return render_template('detalle_cliente.html', cliente=cliente)
    else:
        # Si no se encontró el cliente, puedes manejarlo de alguna manera, como redireccionar a una página de error o mostrar un mensaje.
        abort(404)


@app.route('/detalle_cliente', methods=['POST'])
def buscar_detalle_cliente():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        ciudad = request.form.get('ciudad')
        clientes = Cliente.filtrar(nombre = nombre, apellidos=apellido, ciudad=ciudad)
        if clientes:
            # Solo se mostrará el primer cliente que coincida con los criterios de búsqueda
            cliente = clientes[0]
            return render_template('detalle_cliente.html', cliente=cliente)
        else:
           abort(404)

    return render_template('buscar_cliente.html')



@app.errorhandler(404)
def pagina_no_encontrada(err):
    return render_template('404.html')





def main():
    app.run(debug=True)


