import falcon

from aness.db.pw import PeeweeDBManager
from aness.middleware.context import ContextMiddleware
from aness.middleware.security import SecurityMiddlware
from aness.resources import message, index, user, oauth
from falcon.testing import SimpleTestResource


class SinkAdapter(object):
    def __call__(self, req, resp):
        resp.status = falcon.HTTP_404
        resp.content_type = falcon.MEDIA_JSON
        error = {'shit': 'happens'}
        # with open('web/public/index.html', 'r') as f:
        #     resp.body = f.read()
        resp.media = error


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

        # Patch callback url
        self.__patch_oauth_callback_url__()

        # Build an object to manage our db connections.
        dbmgr = PeeweeDBManager(self.cfg.db.pw.connection)
        dbmgr.setup()

        # Alter routes
        self.add_route('/api', index.IndexResource(dbmgr))
        self.add_route('/api/index', index.IndexResource(dbmgr))

        self.add_route('/api/users', user.UserCollectionResource(dbmgr))
        self.add_route('/api/users/{id}', user.UserResource(dbmgr))

        self.add_route('/api/messages', message.MessageCollectionResource(dbmgr))
        self.add_route('/api/messages/{id}', message.MessageResource(dbmgr))

        self.add_route('/api/oauth', oauth.OAuthResource(dbmgr, cfg.social_config))
        self.add_route('/api/oauth/{provider}', oauth.CallbackResource(dbmgr, cfg.social_config))

        self.add_route('/api/oauth/success', SuccessAdapter())

        self.add_route('/mock', SimpleTestResource(falcon.HTTP_200, json={"foo": "bar"}))

        sink = SinkAdapter()
        self.add_sink(sink, r'/')

    def start(self):
        """ A hook to when a Gunicorn worker calls run()."""
        pass

    def stop(self, signal):
        """ A hook to when a Gunicorn worker starts shutting down. """
        pass

    def __patch_oauth_callback_url__(self):
        for cfg in self.cfg.social_config.sites_list:
            cfg[3]['redirect_uri'] = '/api/'.join([self.cfg.social_config.base_url, cfg[3]['redirect_uri']])



### asd

class AlterDecoy():
    def _hmm(self):
        return 'fuuz'

    def hmm(self):
        if False:
            return self._hmm()
