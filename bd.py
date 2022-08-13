import codecs
from config import *
import mysql.connector as database


class BDdatos():
    """
        Clase para la Base de Datos
    """
    def conectar(self):
        """
           Conectarme a la bd
        """
        db = None
        try:
            # obtener datos de autentificacion de la base de datos
            host = HOST
            user = USER
            clave = PASS
            base_datos = BD
            db = database.connect(database=base_datos, user=user, host=host, \
            password=clave)
        except Exception(e):
            print("error de coneccion", e)
        return db

    def consulta(self, tabla):
        """
            conectarme a la bd, para sacar los datos necesarios
        """
        db = self.conectar()
        cursor = db.cursor()
        sql = """SELECT * FROM  %s;""" % tabla
        cursor.execute(sql)
        datos = cursor.fetchall()
        db.close()
        return datos

    def agregar(self, datos):
        """
            conectarme a la bd, para ingresar los datos
        """
        db = self.conectar()
        cursor = db.cursor()
        sql = """INSERT INTO usuarios (cedula, nombre, apellido, telefono)
                VALUES ('%s', '%s', '%s', '%s');""" % (datos[0], datos[1], datos[2], datos[3])
        m = cursor.execute(sql)
        db.commit()
        db.close()

    def actualizar(self, datos, campo):
        """
            conectarme a la bd, para actualizar los datos
        """
        db = self.conectar()
        cursor = db.cursor()
        sql = """UPDATE usuarios SET %s = '%s'
                WHERE cedula = '%s';""" % (campo, datos[1], datos[0])
        m = cursor.execute(sql)
        db.commit()
        db.close()