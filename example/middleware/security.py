# import jwt
# import falcon

def _token_is_valid(self, token, account_id):
    return True  # Suuuuuure it's valid...


class SecurityMiddlware(object):

    def process_request(self, req, resp):
        """Process the request before routing it.

        Args:
            req: Request object that will eventually be
                routed to an on_* responder method.
            resp: Response object that will be routed to
                the on_* responder.
        """
        token = req.get_header('Authorization')
        account_id = req.get_header('Account-ID')

        challenges = ['Bearer']

        return

        # if token is None:
        #     description = ('Please provide an auth token as part of the request.')
        #     raise falcon.HTTPUnauthorized('Auth token required', description, challenges, href='http://docs.example.com/auth')
        #
        # if not self._token_is_valid(token, account_id):
        #     description = ('The provided auth token is not valid. '
        #                    'Please request a new token and try again.')
        #
        #     raise falcon.HTTPUnauthorized('Authentication required',
        #                                   description,
        #                                   challenges,
        #                                   href='http://docs.example.com/auth')

    def process_resource(self, req, resp, resource, params):
        """Process the request after routing.

        Note:
            This method is only called when the request matches
            a route to a resource.

        Args:
            req: Request object that will be passed to the
                routed responder.
            resp: Response object that will be passed to the
                responder.
            resource: Resource object to which the request was
                routed.
            params: A dict-like object representing any additional
                params derived from the route's URI template fields,
                that will be passed to the resource's responder
                method as keyword arguments.
        """
        pass

    def process_response(self, req, resp, resource):
        """Post-processing of the response (after routing).

        Args:
            req: Request object.
            resp: Response object.
            resource: Resource object to which the request was
                routed. May be None if no route was found
                for the request.
        """
        pass
