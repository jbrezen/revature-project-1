class JoinRequestDept:
    def __init__(self, request_id=0, employee_id=0, event_date=0, event_location='', event_description='',
                 grade_format='', event_type='', justification='', prj_reimbursement=0, super_approval=False,
                 head_approval=False, benco_approval=False, dept_id=0, dept_head=''):
        self.request_id = request_id
        self.employee_id = employee_id
        self.event_date = event_date
        self.event_location = event_location
        self.event_description = event_description
        self.grade_format = grade_format
        self.event_type = event_type
        self.justification = justification
        self.prj_reimbursement = prj_reimbursement
        self.super_approval = super_approval
        self.head_approval = head_approval
        self.benco_approval = benco_approval
        self.dept_id = dept_id
        self.dept_head = dept_head

    def json(self):
        return {
            'requestId': self.request_id,
            'employeeId': self.employee_id,
            'eventDate': self.event_date,
            'eventLocation': self.event_location,
            'eventDescription': self.event_description,
            'gradeFormat': self.grade_format,
            'eventType': self.event_type,
            'justification': self.justification,
            'projectedReimbursement': self.prj_reimbursement,
            'superApproval': self.super_approval,
            'headApproval': self.head_approval,
            'bencoApproval': self.benco_approval,
            'deptId': self.dept_id,
            'deptHead': self.dept_head,
        }

    @staticmethod
    def parse_json(json):
        new_join = JoinRequestDept()

        new_join.request_id = json['requestId'] if 'requestId' in json else 0
        new_join.employee_id = json['employeeId']
        new_join.event_date = json['eventDate']
        new_join.event_location = json['eventLocation']
        new_join.event_description = json['eventDescription']
        new_join.grade_format = json['gradeFormat']
        new_join.event_type = json['eventType']
        new_join.justification = json['justification']
        new_join.prj_reimbursement = json['projectedReimbursement']
        new_join.super_approval = json['superApproval']
        new_join.head_approval = json['headApproval']
        new_join.benco_approval = json['bencoApproval']
        new_join.dept_id = json['deptId']
        new_join.dept_head = json['deptHead']

        return new_join
