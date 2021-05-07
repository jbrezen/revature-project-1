from daos.request_dao import RequestDAO
from models.request import Request
from util.db_connection import connection


class RequestDAOImpl(RequestDAO):
    def create_request(self, request):
        sql = "INSERT INTO requests VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) " \
              "RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (request.employee_id, request.event_date, request.event_location, request.event_description,
                             request.grade_format, request.event_type, request.justification, request.prj_reimbursement,
                             request.super_approval, request.head_approval, request.benco_approval, request.dept_id))

        connection.commit()
        rec = cursor.fetchone()

        new_request = Request(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5],
                              rec[6], rec[7], rec[8], rec[9], rec[10], rec[11], rec[12])
        return new_request

    def get_request(self, request_id):
        sql = "SELECT * FROM requests WHERE request_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [request_id])

        rec = cursor.fetchone()
        new_request = Request(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5],
                              rec[6], rec[7], rec[8], rec[9], rec[10], rec[11], rec[12])
        return new_request

    def all_requests(self):
        sql = "SELECT * FROM requests"

        cursor = connection.cursor()
        cursor.execute(sql)

        rec = cursor.fetchall()

        request_list = []
        for r in rec:
            record = Request(r[0], r[1], r[2], r[3], r[4], r[5],
                             r[6], r[7], r[8], r[9], r[10], r[11], r[12])
            request_list.append(record.json())

        return request_list

    def update_request(self, change):
        sql = "UPDATE requests SET employee_id=%s, event_date=%s, event_location=%s, event_description=%s, " \
              "grade_format=%s, event_type=%s, justification=%s, projected_reimbursement=%s, super_approval=%s, " \
              "head_approval=%s, benco_approval=%s, dept_id = %s WHERE request_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.employee_id, change.event_date, change.event_location, change.event_description,
                             change.grade_format, change.event_type, change.justification, change.prj_reimbursement,
                             change.super_approval, change.head_approval, change.benco_approval, change.dept_id,
                             change.request_id))
        connection.commit()

        rec = cursor.fetchone()
        new_request = Request(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5],
                              rec[6], rec[7], rec[8], rec[9], rec[10], rec[11], rec[12])
        return new_request

    def delete_request(self, request_id):
        sql = "DELETE FROM requests WHERE request_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [request_id])
        connection.commit()
        return ''
