from flask_restplus import Namespace, fields


class HealthCheck:
    api = Namespace('healthcheck', description='sample using health check')
    healthCheck = api.model('healthcheck', {
        'username': fields.String(required=True, description='user username'),
        'description': fields.String(required=True, description='user description')
    })
