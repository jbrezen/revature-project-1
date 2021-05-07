from daos.employee_dao import EmployeeDAO
from models.employee import Employee
from util.db_connection import connection


class EmployeeDAOImpl(EmployeeDAO):
    def create_employee(self, employee):
        sql = "INSERT INTO employees VALUES (DEFAULT, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (employee.employee_name, employee.department_id, employee.supervisor_id))

        rec = cursor.fetchone()
        new_employee = Employee(rec[0], rec[1], rec[2], rec[3])
        return new_employee

    def get_employee(self, employee_id):
        sql = "SELECT * FROM employees WHERE employee_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        rec = cursor.fetchone()
        new_employee = Employee(rec[0], rec[1], rec[2], rec[3])
        return new_employee

    def all_employees(self):
        sql = "SELECT * FROM employees"

        cursor = connection.cursor()
        cursor.execute(sql)

        rec = cursor.fetchall()

        employee_list = []
        for r in rec:
            record = Employee(r[0], r[1], r[2], r[3])
            employee_list.append(record.json())

        return employee_list

    def update_employee(self, change):
        sql = "UPDATE employees SET employee_name=%s, supervisor_id=%s, department_id=%s WHERE employee_id=%s " \
              "RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.employee_name, change.supervisor_id, change.department_id, change.employee_id))
        connection.commit()

        rec = cursor.fetchone()
        new_employee = Employee(rec[0], rec[1], rec[2], rec[3])
        return new_employee

    def delete_employee(self, employee_id):
        sql = "DELETE FROM employees WHERE employee_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
        return ''
