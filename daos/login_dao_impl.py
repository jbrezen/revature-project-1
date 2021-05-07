from daos.login_dao import LoginDAO
from models.login import Login
from util.db_connection import connection


class LoginDAOImpl(LoginDAO):
    def create_login(self, login):
        sql = "INSERT INTO login_info VALUES (DEFAULT, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (login.employee_id, login.username, login.password))

        rec = cursor.fetchone()
        new_login = Login(rec[0], rec[1], rec[2], rec[3])
        return new_login

    def get_login(self, login_id):
        sql = "SELECT * FROM login_info WHERE login_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [login_id])

        rec = cursor.fetchone()
        new_login = Login(rec[0], rec[1], rec[2], rec[3])
        return new_login

    def all_logins(self):
        sql = "SELECT * FROM login_info"

        cursor = connection.cursor()
        cursor.execute(sql)

        rec = cursor.fetchall()

        dept_list = []
        for r in rec:
            record = Login(r[0], r[1], r[2], r[3])
            dept_list.append(record.json())

        return dept_list

    def update_login(self, change):
        sql = "UPDATE login_info SET employee_id=%s, username=%s, password=%s WHERE login_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.employee_id, change.username, change.password, change.login_id))
        connection.commit()

        rec = cursor.fetchone()
        new_login = Login(rec[0], rec[1], rec[2], rec[3])
        return new_login

    def delete_login(self, login_id):
        sql = "DELETE FROM login_info WHERE login_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [login_id])
        connection.commit()
        return ''
