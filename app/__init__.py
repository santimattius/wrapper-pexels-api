from flask import Blueprint
from flask_restplus import Api

from .main.healthcheck.controller.health_check_controller import api as healthcheck_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Template: Rest API  using Flask',
          version='1.0',
          description='Rest API  using Flask with CI basic setup (Travis + Codecov)'
          )

api.add_namespace(healthcheck_ns, path='/test')
