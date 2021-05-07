class Employee:
    def __init__(self, employee_id=0, employee_name='', supervisor_id=0, department_id=0):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.supervisor_id = supervisor_id
        self.department_id = department_id

    def json(self):
        return {
            'employeeId': self.employee_id,
            'employeeName': self.employee_name,
            'supervisorId': self.supervisor_id,
            'departmentId': self.department_id
        }

    @staticmethod
    def parse_json(json):
        employee = Employee()

        employee.employee_id = json['employeeId']
        employee.employee_name = json['employeeName']
        employee.supervisor_id = json['supervisorId']
        employee.department_id = json['departmentId']

        return employee
