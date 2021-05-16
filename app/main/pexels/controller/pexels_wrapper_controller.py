import requests
from flask import request
from flask_restplus import Resource

from ..model.pexels_dto import Pexels

api = Pexels.api
_photo = Pexels.photo


@api.route('/pexels')
class PexelsWrapperController(Resource):

    @api.doc('pexels wrapper')
    @api.marshal_list_with(_photo)
    def get(self):

        size = request.args.get('size')
        resp = requests.get(
            'https://api.pexels.com/v1/search',
            params={
                'query': request.args.get('query'),
                'per_page': request.args.get('count'),
                'orientation': 'landscape'
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': request.headers.get('Authorization')
            })

        if resp.status_code == 200:
            json_response = resp.json()
            data = []
            for photo in json_response['photos']:
                data.append({
                    'id': photo['id'],
                    'author': photo['photographer'],
                    'width': photo['width'],
                    'height': photo['height'],
                    'url': photo['url'],
                    'download_url': photo['src'][size]
                })
            return data
        return {'error': 'code {}'.format(resp.status_code)}, resp.status_code
