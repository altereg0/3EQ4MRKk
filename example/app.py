import falcon

from example.db.manager import DBManager
from example.middleware.context import ContextMiddleware
from example.middleware.security import SecurityMiddlware
from example.resources import scores, message, index, employee, oauth
from falcon.testing import SimpleTestResource

class SinkAdapter(object):
    def __call__(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('web/public/index.html', 'r') as f:
            resp.body = f.read()


class SuccessAdapter(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('web/public/success.html', 'r') as f:
            resp.body = f.read()


class AlterRequest(falcon.Request):
    def __init__(self, env, options=None):
        super(AlterRequest, self).__init__(env, options)
        self.token = None


class AlterService(falcon.API):
    def __init__(self, cfg):
        super(AlterService, self).__init__(
            middleware=[ContextMiddleware(), SecurityMiddlware()],
            request_type=AlterRequest
        )

        self.cfg = cfg

        # Build an object to manage our db connections.
        mgr = DBManager(self.cfg.db.connection)
        mgr.setup()

        # Create our resources
        scores_res = scores.ScoresResource(mgr)

        # Build routes
        self.add_route('/scores', scores_res)

        # Alter routes
        self.add_route('/api', index.IndexResource(mgr))
        self.add_route('/api/index', index.IndexResource(mgr))
        self.add_route('/api/employees', employee.EmployeeCollectionResource(mgr))
        self.add_route('/api/employees/{id}', employee.EmployeeResource(mgr))

        self.add_route('/api/messages', message.MessageCollectionResource(mgr))
        self.add_route('/api/messages/{id}', message.MessageResource(mgr))

        self.add_route('/oauth', oauth.OAuthResource(mgr, cfg.social_config))
        self.add_route('/oauth/{provider}', oauth.CallbackResource(mgr, cfg.social_config))

        self.add_route('/auth/success', SuccessAdapter())

        self.add_route('/mock', SimpleTestResource(falcon.HTTP_200, json={"foo": "bar"}))

        sink = SinkAdapter()
        self.add_sink(sink, r'/')

    def start(self):
        """ A hook to when a Gunicorn worker calls run()."""
        pass

    def stop(self, signal):
        """ A hook to when a Gunicorn worker starts shutting down. """
        pass

### asd
