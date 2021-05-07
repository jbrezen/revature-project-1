from daos.department_dao import DepartmentDAO
from models.department import Department
from util.db_connection import connection


class DepartmentDAOImpl(DepartmentDAO):
    def create_department(self, department):
        sql = "INSERT INTO departments VALUES (DEFAULT, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (department.head_id, department.department_name))

        rec = cursor.fetchone()
        new_department = Department(rec[0], rec[1], rec[2])
        return new_department

    def get_department(self, department_id):
        sql = "SELECT * FROM departments WHERE department_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [department_id])

        rec = cursor.fetchone()
        new_department = Department(rec[0], rec[1], rec[2])
        return new_department

    def all_departments(self):
        sql = "SELECT * FROM departments"

        cursor = connection.cursor()
        cursor.execute(sql)

        rec = cursor.fetchall()

        dept_list = []
        for r in rec:
            record = Department(r[0], r[1], r[2])
            dept_list.append(record.json())

        return dept_list

    def update_department(self, change):
        sql = "UPDATE departments SET head_id=%s, department_name=%s WHERE department_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.head_id, change.department_name, change.department_id))
        connection.commit()

        rec = cursor.fetchone()
        new_department = Department(rec[0], rec[1], rec[2])
        return new_department

    def delete_department(self, department_id):
        sql = "DELETE FROM departments WHERE department_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [department_id])
        connection.commit()
        return ''
