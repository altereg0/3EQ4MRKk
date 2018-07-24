import falcon
import uuid
from string import Template

SUCCESS_TPL = '<!DOCTYPE html><html><head><script type="text/javascript">window._token="$token"; window.close();</script></head><body></body></html>'


def set_context(req, resp):
    if not req.context.get('request_id'):
        req.context['request_id'] = str(uuid.uuid4())

    resp.set_header('request-id', req.context['request_id'])


class ContextMiddleware(object):
    def process_request(self, req, resp):
        set_context(req, resp)

    def process_response(self, req, resp, resource):
        """Post-processing of the response (after routing).

        Args:
            req: Request object.
            resp: Response object.
            resource: Resource object to which the request was
                routed. May be None if no route was found
                for the request.
        """
        user = resp.context.get('user', None)
        if user:
            token = resp.context.get('token', 'FAIL')
            resp.status = falcon.HTTP_OK
            resp.content_type = falcon.MEDIA_HTML
            resp.body = Template(SUCCESS_TPL).substitute(token=token)
