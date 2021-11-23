#libraries
from flask import Flask, request, jsonify;
from flask_mysqldb import MySQL;
from flask_cors import CORS, cross_origin;

# initializations
app = Flask(__name__)
CORS(app)

#MYSQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'clinic_world'
mysql = MySQL(app)
#llave de encriptado
app.secret_key = "mysecretkey"


#PRINCIPAL
@cross_origin()
@app.route('/', methods=['GET'])
def index():
    return jsonify(
        {
            "Mensaje": "Bienvenido a Clinic World - Seccion de CITAS"
        })


# COMIENZO DE LA TABLA TIPO DE USUARIOS

#QUERY CONSULTAR TODOS
@cross_origin()
@app.route('/getAlltipo', methods=['GET'])
def getAlltipo():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tipo_usuarios')
    res = con.fetchall()
    #close connection
    con.close()
    #loop for scan data
    if(res):
        payload = []
        content = {}
        for result in res:
            content = {
                'idTipo_usuario': result[0],
                'nombre': result[1],
                'descripcion': result[2]
            }
            payload.append(content)
            content = {}
        return jsonify(payload)
    else:
        return jsonify('No hay Informacion Agregada Aun')


#QUERY CONSULTAR POR ID
@cross_origin()
@app.route('/getByIdtipo/<id>', methods=['GET'])
def getByIdtipo(id):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tipo_usuarios WHERE idTipo_usuario = %s', (id))
    res = con.fetchall()
    con.close()
    if(res):
        payload = []
        content = {}
        #apply the information
        content = {
            "Id": res[0][0],
            "Nombre": res[0][1],
            "Descripcion": res[0][2]
        }
        payload.append(content)
        content = {}
        return jsonify(payload)
    else:
        return jsonify('No hay Informacion Aun')


#QUERY DE INSERCION
@cross_origin()
@app.route('/addTipo', methods=['POST'])
def addTipo():
    #Analice the type of method to send information
    if (request.method == 'POST'):
        nombre = request.json['nombre'],
        descripcion = request.json['descripcion']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO tipo_usuarios(nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
        mysql.connection.commit()
        return jsonify({"Mensaje" : "Dato Insertado Correctamente"})



#QUERY DE ACTUALIZACION
@cross_origin()
@app.route('/updateTipo/<id>', methods=['PUT'])
def updateTipo(id):
    nombre = request.json['nombre'],
    descripcion = request.json['descripcion']
    con = mysql.connection.cursor()
    con.execute("""
        UPDATE tipo_usuarios
        SET nombre = %s,
            descripcion = %s
        WHERE idTipo_usuario = %s
    """, (nombre, descripcion, id))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})



#QUERY PARA ELIMINAR
@cross_origin()
@app.route('/deleteTipo/<id>', methods = ['DELETE'])
def deleteTipo(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tipo_Usuarios WHERE idTipo_usuario = %s', (id))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})




 # COMIENZO DE LA TABLA USUARIOS

# ruta para consultar todos los registros
@cross_origin()
@app.route('/getAllusuarios', methods=['GET'])
def getAllusuarios():
    con = mysql.connection.cursor()
    con.execute('select * from usuarios')
    res = con.fetchall()
    con.close()
    payload = []
    content = {}
    if (res):
     for result in res:
        content = {
           'idUsuario': result[0],
           'tipo_documento': result[1],
           'numero_documento': result[2],
           'edad': result[3],
           'nombre':result[4],
           'segundo_nombre':result[5],
           'apellido':result[6],
           'segundo_apellido':result[7],
           'direccion':result[8],
           'telefono':result[9],
           'idTipo_usuario':result[10],
           'correo':result[11],
           'usuario':result[12],
           'contraseña':result[13]
           }
        payload.append(content)
        content = {}
     return jsonify(payload)
    else:  return jsonify('No hay Informacion Agregada Aun')

# ruta para consultar por parametro
@cross_origin()
@app.route('/getByIdusuarios/<id>',methods=['GET'])
def getByIdusuarios(id):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM clientes WHERE idCliente = %s', (id))
    res = con.fetchall()
    con.close()
    payload = []
    content = {}
    content = {
    'idCliente': res[0][0],
    'tipo_documento': res[0][1],
    'numero_documento': res[0][2],
    'edad': res[0][3], 
    'nombre':res[0][4],
    'segundo_nombre':res[0][5],
    'apellido':res[0][6],
    'segundo_apellido':res[0][7],
    'direccion':res[0][8],
    'telefono':res[0][9],
    'correo':res[0][10]
    }
    payload.append(content)
    content = {}
    return jsonify(payload)


#### ruta para crear un registro########
@cross_origin()
@app.route('/addusuarios', methods=['POST'])
def addusuarios():
    if request.method == 'POST':
        tipo_documento = request.json['tipo_documento'] 
        numero_documento = request.json['numero_documento']        
        edad = request.json['edad']  
        nombre = request.json['nombre']
        segundo_nombre = request.json['segundo_nombre'] 
        apellido = request.json['apellido']
        segundo_apellido = request.json['segundo_apellido']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        correo = request.json['correo']
        tipo_usuario = request.json['idTipo_usuario']
        usuario = request.json['usuario']
        contraseña = request.json['contraseña']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO usuarios (tipo_documento, numero_documento, edad, nombre, segundo_nombre, apellido, segundo_apellido, direccion,telefono,correo, idTipo_usuario, usuario, contraseña) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (tipo_documento, numero_documento, edad,nombre,segundo_nombre,apellido,segundo_apellido,direccion,telefono,correo, tipo_usuario, usuario, contraseña))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})



######### ruta para actualizar################
@cross_origin()
@app.route('/updateUsuarios/<documento>', methods=['PUT'])
def updateUsuarios(documento):
        tipo_documento = request.json['tipo_documento'] 
        numero_documento = request.json['numero_documento']        
        edad = request.json['edad']  
        nombre = request.json['nombre']
        segundo_nombre = request.json['segundo_nombre'] 
        apellido = request.json['apellido']
        segundo_apellido = request.json['segundo_apellido']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        correo = request.json['correo']
        tipo_usuario = request.json['idTipo_usuario']
        usuario = request.json['usuario']
        contraseña = request.json['contraseña']
        con = mysql.connection.cursor()
        con.execute("""
            UPDATE usuarios
            SET tipo_documento = %s,
                numero_documento= %s,
                edad = %s,
                nombre = %s,
                segundo_nombre = %s,
                apellido = %s,
                segundo_apellido = %s,
                direccion = %s,
                correo = %s,
                telefono = %s,
                idTipo_usuario = %s,
                usuario = %s,
                contraseña = %s
            WHERE numero_documento = %s
        """, ( tipo_documento, numero_documento, edad, nombre, segundo_nombre, apellido, segundo_apellido, 
                direccion, correo, telefono, tipo_usuario, usuario, contraseña, documento))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro actualizado"})



######### ruta para eliminar################
@cross_origin()
@app.route('/deleteUsuarios/<documento>', methods = ['DELETE'])
def deleteUsuarios(documento):
    con = mysql.connection.cursor()
    con.execute("DELETE FROM usuarios WHERE numero_documento = %s" %documento)
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})

#COMIENZO DE LA TABLA CLIENTE

# ruta para consultar todos los registros
@cross_origin()
@app.route('/getAllcliente', methods=['GET'])
def getAllcliente():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM clientes')
    res = con.fetchall()
    con.close()
    payload = []
    content = {}
    if (res):
     for result in res:
       content = {
           'idCliente': result[0],
           'tipo_documento': result[1],
           'numero_documento': result[2],
           'edad': result[3],
           'nombre':result[4],
           'segundo_nombre':result[5],
           'apellido':result[6],
           'segundo_apellido':result[7],
           'direccion':result[8],
           'telefono':result[9],
           'correo':result[10]
           }
       payload.append(content)
       content = {}
     return jsonify(payload)
    else:
         return jsonify('No hay Informacion Agregada Aun')

# ruta para consultar por parametro
@cross_origin()
@app.route('/getByIdcliente/<documento>',methods=['GET'])
def getAllByIdcliente(documento):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM clientes WHERE numero_documento = %s', (documento))
    res = con.fetchall()
    con.close()
    payload = []
    content = {}
    content = {
    'idCliente': res[0][0],
    'tipo_documento': res[0][1],
    'numero_documento': res[0][2],
    'edad': res[0][3], 
    'nombre':res[0][4],
    'segundo_nombre':res[0][5],
    'apellido':res[0][6],
    'segundo_apellido':res[0][7],
    'direccion':res[0][8],
    'telefono':res[0][9],
    'correo':res[0][10]
    }
    payload.append(content)
    content = {}
    return jsonify(payload)


#### ruta para crear un registro########
@cross_origin()
@app.route('/addCLiente', methods=['POST'])
def addCliente():
    if request.method == 'POST':
        tipo_documento = request.json['tipo_documento'] 
        numero_documento = request.json['numero_documento']        
        edad = request.json['edad']  
        nombre = request.json['nombre']
        segundo_nombre = request.json['segundo_nombre'] 
        apellido = request.json['apellido']
        segundo_apellido = request.json['segundo_apellido']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        correo = request.json['correo']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO clientes (tipo_documento, numero_documento, edad, nombre, segundo_nombre, apellido, segundo_apellido, direccion,telefono,correo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (tipo_documento, numero_documento, edad,nombre,segundo_nombre,apellido,segundo_apellido,direccion,telefono,correo))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})



######### ruta para actualizar################
@cross_origin()
@app.route('/updateCliente/<documento>', methods=['PUT'])
def updateCliente(documento):
        print(request.json)
        tipo_documento = request.json['tipo_documento'] 
        numero_documento = request.json['numero_documento']        
        edad = request.json['edad']  
        nombre = request.json['nombre']
        segundo_nombre = request.json['segundo_nombre'] 
        apellido = request.json['apellido']
        segundo_apellido = request.json['segundo_apellido']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        correo = request.json['correo']
        con = mysql.connection.cursor()
        con.execute("""
            UPDATE clientes
            SET tipo_documento = %s,
                numero_documento= %s,
                edad = %s,
                nombre = %s,
                segundo_nombre = %s,
                apellido = %s,
                segundo_apellido = %s,
                direccion = %s,
                correo = %s,
                telefono = %s
            WHERE numero_documento = %s
        """, ( tipo_documento, numero_documento, edad, nombre, segundo_nombre, apellido, segundo_apellido, 
                direccion, correo, telefono, documento))
        mysql.connection.commit()
        return jsonify({"informacion":documento})






######### ruta para eliminar################
@cross_origin()
@app.route('/deleteCliente/<documento>', methods = ['DELETE'])
def deleteCliente(documento):
    print(type(documento))
    con = mysql.connection.cursor()
    con.execute("DELETE FROM clientes WHERE numero_documento = %s" %documento)
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


#COMIENZO DE LA TABLA ESPECIALIDAD

    #QUERY CONSULTAR TODOS 
@cross_origin()
@app.route('/getAllespecialidad', methods=['GET'])
def getAllespecialidad():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM especialidad')
    res = con.fetchall()
    #close connection
    con.close()
    #loop for scan data
    if(res):
        payload = []
        content = {}
        for result in res:
            content = {
                'idTipo_usuario': result[0],
                'nombre': result[1],
                'descripcion': result[2]
            }
            payload.append(content)
            content = {}
        return jsonify(payload)
    else:
        return jsonify('No hay Informacion Agregada Aun')


#QUERY CONSULTAR POR ID
@cross_origin()
@app.route('/getByIdespecialidad/<id>', methods=['GET'])
def getByIdespecialidad(id):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM especialidad WHERE idEspecialidad = %s', (id))
    res = con.fetchall()
    con.close()
    if(res):
        payload = []
        content = {}
        #apply the information
        content = {
            "Id": res[0][0],
            "Nombre": res[0][1],
            "Descripcion": res[0][2]
        }
        payload.append(content)
        content = {}
        return jsonify(payload)
    else:
        return jsonify('No hay Informacion Aun')


#QUERY DE INSERCION
@cross_origin()
@app.route('/addEspecialidad', methods=['POST'])
def addEspecialidad():
    #Analice the type of method to send information
    if (request.method == 'POST'):
        nombre = request.json['nombre'],
        descripcion = request.json['descripcion']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO especialidad(nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
        mysql.connection.commit()
        return jsonify({"Mensaje" : "Dato Insertado Correctamente"})



#QUERY DE ACTUALIZACION
@cross_origin()
@app.route('/updateEspelcialidad/<id>', methods=['PUT'])
def updateEspecialidad(id):
    nombre = request.json['nombre'],
    descripcion = request.json['descripcion']
    con = mysql.connection.cursor()
    con.execute("""
        UPDATE especialidad
        SET nombre = %s,
            descripcion = %s
        WHERE idEspecialidad = %s
    """, (nombre, descripcion, id))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})



#QUERY PARA ELIMINAR
@cross_origin()
@app.route('/deleteEspecialidad/<id>', methods = ['DELETE'])
def deleteEspecialidad(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM especialidad WHERE idEspecialidad = %s', (id))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


#COMIENZO DE LA TABLA ESPECIALIDADES DE MEDICOS

#QUERY CONSULTAR TODOS
@cross_origin()
@app.route('/getAllEsp_medico', methods=['GET'])
def getAllEsp_medico():
    con = mysql.connection.cursor()
    con.execute('SELECT idEspecialidad_medico, concat(usuarios.nombre, " ", usuarios.apellido) as usuario, especialidad.nombre as especialidad, fecha_creacion FROM especialidad_medico,' +
    'especialidad, usuarios WHERE especialidad_medico.idEspecialidad = especialidad.idEspecialidad ' + 
    'AND especialidad_medico.idUsuario = usuarios.idUsuario')
    res = con.fetchall()
    #close connection
    con.close()
    #loop for scan data
    if(res):
        payload = []
        content = {}
        for result in res:
            content = {
                'idEspecialidad_medico': result[0],
                'medico': result[1],
                'especialidad': result[2],
                'Fecha de creacion': result[3]
            }
            payload.append(content)
            content = {}
        return jsonify(payload)
    else:
        return jsonify('No hay Informacion Agregada Aun')


#QUERY CONSULTAR POR ID
@cross_origin()
@app.route('/getByIdEsp_medico/<id>', methods=['GET'])
def getByIdEsp_medico(id):
    con = mysql.connection.cursor()
    con.execute('SELECT idEspecialidad_medico, usuarios.nombre as usuario, especialidad.nombre as especialidad, fecha_creacion FROM especialidad_medico,' +
    'especialidad, usuarios WHERE especialidad_medico.idEspecialidad = especialidad.idEspecialidad ' + 
    'AND especialidad_medico.idUsuario = usuarios.idUsuario AND idEspecialidad_medico = %s', (id))
    res = con.fetchall()
    con.close()
    if(res):
        payload = []
        content = {}
        #apply the information
        content = {
            'idEspecialidad_medico': res[0][0],
            'Nombre Medico': res[0][1],
            'Nombre Especialidad': res[0][2],
            'Fecha de creacion': res[0][3]
        }
        payload.append(content)
        content = {}
        return jsonify(payload)
    else:
        return jsonify('No hay Informacion Aun')


#QUERY DE INSERCION
@cross_origin()
@app.route('/addEsp_medico', methods=['POST'])
def addEsp_medico():
    #Analice the type of method to send information
    if (request.method == 'POST'):
        idUsuario = request.json['idUsuario'],
        idEspecialidad = request.json['idEspecialidad'],
        fecha = request.json['fecha']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO especialidad_medico(idUsuario, idEspecialidad, fecha_creacion) VALUES (%s, %s, %s)", (idUsuario, idEspecialidad, fecha))
        mysql.connection.commit()
        return jsonify({"Mensaje" : "Dato Insertado Correctamente"})



#QUERY DE ACTUALIZACION
@cross_origin()
@app.route('/updateEsp_medico/<id>', methods=['PUT'])
def updateEsp_medico(id):
    idUsuario = request.json['idUsuario'],
    idEspecialidad = request.json['idEspecialidad']
    fecha = request.json['fecha']
    con = mysql.connection.cursor()
    con.execute("""
        UPDATE especialidad_medico
        SET idUsuario = %s,
            idEspecialidad = %s,
            fecha_creacion = %s
        WHERE idEspecialidad_medico = %s
    """, (idUsuario, idEspecialidad, fecha, id))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})



#QUERY PARA ELIMINAR
@cross_origin()
@app.route('/deleteEsp_medico/<id>', methods = ['DELETE'])
def deleteEsp_medico(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM especialidad_medico WHERE idEspecialidad_medico = %s', (id))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


    # COMIENZO DE LA TABLA CITAS (PRINCIPAL)


#QUERY CONSULTAR TODOS
@cross_origin()
@app.route('/getAllCitas', methods=['GET'])
def getAllCitas():
    con = mysql.connection.cursor()
    con.execute('SELECT citas.idCitas, concat(clientes.nombre, " " ,clientes.apellido) as cliente_nombre, concat(usuarios.nombre, " " ,usuarios.apellido) as medico_nombre, citas.fecha_hora, citas.idCliente, citas.idEspecialidad_medico, especialidad.nombre, citas.codigo_cita '
    +'FROM citas, usuarios, especialidad, clientes, especialidad_medico '
    +'WHERE citas.idCliente = clientes.idCliente AND citas.idEspecialidad_medico = especialidad_medico.idEspecialidad_medico AND especialidad_medico.idUsuario = usuarios.idUsuario '
    +'AND especialidad_medico.idEspecialidad = especialidad.idEspecialidad')
    res = con.fetchall()
    #close connection
    con.close()
    #loop for scan data
    if(res):
        payload = []
        content = {}
        for result in res:
            content = {
                'idCitas': result[0],
                'cliente': result[1],
                'medico': result[2],
                'fecha': result[3],
                'idCliente': result[4],
                'idEsp_Medico': result[5],
                'especialidad': result[6],
                'codigo': result[7]
            }
            payload.append(content)
            content = {}
        return jsonify(payload)
    else:
        return jsonify('No hay Informacion Agregada Aun')


#QUERY CONSULTAR POR ID
@cross_origin()
@app.route('/getByIdCitas/<id>', methods=['GET'])
def getByIdCitas(id):
    con = mysql.connection.cursor()
    con.execute('select * from citas where idCitas = %s', (id))
    res = con.fetchall()
    con.close()
    if(res):
        payload = []
        content = {}
        #apply the information
        content = {
            'idCitas': res[0][0],
            'idCliente': res[0][1],
            'fecha_hora': res[0][2],
            'idEspecialidad_medico': res[0][3]
        }
        payload.append(content)
        content = {}
        return jsonify(payload)
    else:
        return jsonify('No hay Informacion Aun')


#QUERY DE INSERCION
@cross_origin()
@app.route('/addCitas', methods=['POST'])
def addCitas():
    #Analice the type of method to send information
    if (request.method == 'POST'):
        idCliente = request.json['idCliente'],
        fecha_hora = request.json['fecha_hora'],
        idEspecialidad_medico = request.json['idEspecialidad_medico']
        con = mysql.connection.cursor()
        #CREAMOS ESTA CONSULTA PARA TRAER EL ULTIMO ID PARA LA LLAVE UNICA
        con.execute('SELECT CONCAT( "CIT", MAX(LAST_INSERT_ID(idCitas)) +1) FROM citas')
        res = con.fetchall()
        #INSERCION FINAL
        con.execute('INSERT INTO citas(idCliente, fecha_hora, idEspecialidad_medico, codigo_cita) VALUES(%s, %s, %s, %s);',
        (idCliente, fecha_hora, idEspecialidad_medico, res[0][0]) )
        mysql.connection.commit()
        return jsonify({"informacion" : "Dato Insertado Correctamente"})



#QUERY DE ACTUALIZACION
@cross_origin()
@app.route('/updateCitas/<codigo>', methods=['PUT'])
def updateCitas(codigo):
    print(codigo)
    idCliente = request.json['idCliente'],
    fecha_hora = request.json['fecha_hora']
    idEspecialidad_medico = request.json['idEspecialidad_medico']
    con = mysql.connection.cursor()
    con.execute("""
        UPDATE citas
        SET idCliente = %s,
            fecha_hora = %s,
            idEspecialidad_medico = %s
        WHERE codigo_cita = %s
    """, (idCliente, fecha_hora, idEspecialidad_medico, codigo))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})



#QUERY PARA ELIMINAR
@cross_origin()
@app.route('/deleteCitas/<codigo>', methods = ['DELETE'])
def deleteCitas(codigo):
    print('codigo es: ', codigo)
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM citas WHERE codigo_cita = '%s'" %codigo)
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


    

#iniciado de la app (Nota: ir al final ya que la lectura es de arriba a hacia abajo)
if __name__ == "__main__":
   app.run(port=3000, debug=True)
