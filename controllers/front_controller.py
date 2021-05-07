import logger
from controllers import request_controller, employee_controller, department_controller, login_controller


def route(app):
    request_controller.route(app)
    employee_controller.route(app)
    department_controller.route(app)
    login_controller.route(app)
    logger.log()