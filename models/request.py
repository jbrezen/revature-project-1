class Request:
    def __init__(self, request_id=0, employee_id=0, event_date=0, event_location='', event_description='',
                 grade_format='', event_type='', justification='', prj_reimbursement=0, super_approval=False,
                 head_approval=False, benco_approval=False, dept_id=0):
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
            'deptId': self.dept_id
        }

    @staticmethod
    def parse_json(json):
        request = Request()

        request.request_id = json['requestId'] if 'requestId' in json else 0
        request.employee_id = json['employeeId']
        request.event_date = json['eventDate']
        request.event_location = json['eventLocation']
        request.event_description = json['eventDescription']
        request.grade_format = json['gradeFormat']
        request.event_type = json['eventType']
        request.justification = json['justification']
        request.prj_reimbursement = json['projectedReimbursement']
        request.super_approval = json['superApproval'] if 'superApproval' in json else False
        request.head_approval = json['headApproval'] if 'headApproval' in json else False
        request.benco_approval = json['bencoApproval'] if 'bencoApproval' in json else False
        request.dept_id = json['deptId']

        return request
