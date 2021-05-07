class Department:
    def __init__(self, department_id=0, head_id=0, department_name=''):
        self.department_id = department_id
        self.head_id = head_id
        self.department_name = department_name

    def json(self):
        return {
            'departmentId': self.department_id,
            'headId': self.head_id,
            'departmentName': self.department_name
        }

    @staticmethod
    def parse_json(json):
        dept = Department()

        dept.department_id = json['departmentId']
        dept.head_id = json['headId']
        dept.department_name = json['departmentName']

        return dept
