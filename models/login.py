class Login:
    def __init__(self, login_id=0, employee_id=0, username='', password=''):
        self.login_id = login_id
        self.employee_id = employee_id
        self.username = username
        self.password = password

    def json(self):
        return {
            'loginId': self.login_id,
            'employeeId': self.employee_id,
            'username': self.username,
            'password': self.password
        }

    @staticmethod
    def parse_json(json):
        login = Login()
        login.login_id = json['loginId']
        login.employee_id = json['employeeId']
        login.username = json['username']
        login.password = json['password']
        return login
