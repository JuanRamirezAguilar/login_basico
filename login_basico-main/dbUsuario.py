import mysql.connector
from conecta import DatabaseConnection  # Asegúrate de que esta importación sea correcta
from usuario import Usuario

class DBUsuario:
    def __init__(self) -> None:
        self.db_connection = DatabaseConnection()

    def authenticate_user(self, usuario: Usuario) -> bool:
        try:
            conn = self.db_connection.open()
            cursor = conn.cursor()

            # Consultar la base de datos para verificar el usuario
            query = "SELECT * FROM usuarios WHERE correo = %s AND contraseña = %s"
            cursor.execute(query, (usuario.get_correo(), usuario.get_password()))
            result = cursor.fetchone()

            if result:
                print("Autenticación exitosa.")
                return True
            else:
                print("Autenticación fallida: correo o contraseña incorrectos.")
                return False

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            self.db_connection.close()
