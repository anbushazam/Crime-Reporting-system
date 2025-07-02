import mysql

from PropertyUtil import get_property_string
import mysql.connector
class DB_connection:
    connection=None

    @staticmethod
    def get_connection():
        cred=get_property_string()

        if DB_connection.connection is None:
            DB_connection.connection = mysql.connector.connect(host=cred[0], user=cred[1], password=cred[2], database=cred[3])
        return DB_connection.connection

