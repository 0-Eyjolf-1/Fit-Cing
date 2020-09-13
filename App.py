from flask import Flask

# Hacer el servidor
# Clase para obtener conexion u objeto a configurar
app = Flask(__name__)

#Retornamos algo en la pagina principal

@app.route('/')
def Index():
    return 'Hello World'

@app.route('/add_contact')
def add_contact():
    return 'add contact'    

if __name__ == '__main__':
    app.run(port = 3000, debug = True)



