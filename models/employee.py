class Employee:
    def __init__(self, employee_id=0, employee_name='', supervisor_id=0, department_id=0, current_funds=0):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.supervisor_id = supervisor_id
        self.department_id = department_id
        self.current_funds = current_funds

    def json(self):
        return {
            'employeeId': self.employee_id,
            'employeeName': self.employee_name,
            'supervisorId': self.supervisor_id,
            'departmentId': self.department_id,
            'currentFunds': self.current_funds
        }

    @staticmethod
    def parse_json(json):
        employee = Employee()

        employee.employee_id = json['employeeId'] if 'employeeId' in json else 0
        employee.employee_name = json['employeeName']
        employee.supervisor_id = json['supervisorId']
        employee.department_id = json['departmentId']
        employee.current_funds = json['currentFunds']

        return employee
