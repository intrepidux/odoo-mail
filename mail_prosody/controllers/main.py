import logging
import json

from odoo import http
from odoo.http import Response, request


_logger = logging.getLogger(__name__)


# class Prosody(http.Controller):
#     @http.route('/api/auth/', methods=['POST'], type='json', auth='none', csrf=False)
#     def api_auth_user(self, **kwargs):
#         _logger.warning("Incoming data %s", kwargs)
#         # headers = {'Content-Type': 'application/json'}
#         # body = {'results': {'code': 200, 'message': 'OK'}}
#
#         res = request.session.authenticate('prosody', kwargs.get('username'), kwargs.get('password'))
#         # print(res)
#         return request.env['ir.http'].session_info()

        # return Response(json.dumps(body), headers=headers)
