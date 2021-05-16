from flask_restplus import Namespace, fields


class Pexels:
    api = Namespace('wrapper', description='wrapper of pexels api')
    photo = api.model('photo', {
        'id': fields.String(required=True, description='photo identifier'),
        'author': fields.String(required=True, description='name of author'),
        'width': fields.Integer(required=True, description='photo wudth'),
        'height': fields.Integer(required=True, description='photo height'),
        'url': fields.String(required=True, description='online url'),
        'download_url': fields.String(required=True, description='download url'),
    })
