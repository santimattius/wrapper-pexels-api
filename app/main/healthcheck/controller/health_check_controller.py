from flask import request
from flask_restplus import Resource
from ..model.health_check_dto import HealthCheck

api = HealthCheck.api

@api.route('/healthcheck')
class HealthCheckController(Resource):

    @api.doc('health check')
    def get(self):
        response_object = {
            'status': 'success',
            'message': 'Successfully Health check'
        }
        return response_object, 200
