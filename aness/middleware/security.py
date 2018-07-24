import jwt
import falcon
from datetime import datetime, timedelta


class SecurityMiddlware(object):
    """
    JWT attributes
    4.1.1.  "iss" (Issuer) Claim
    4.1.2.  "sub" (Subject) Claim
    4.1.3.  "aud" (Audience) Claim
    4.1.4.  "exp" (Expiration Time) Claim
    4.1.5.  "nbf" (Not Before) Claim
    4.1.6.  "iat" (Issued At) Claim
    4.1.7.  "jti" (JWT ID) Claim
    """

    def __init__(self):
        pass

    def setup_config(self, cfg):
        self.cfg = cfg

    def _verify_token(self, auth):
        """
        Verify req.auth data with JWT specification
        :param auth: req.auth value
        :return: bool - is valid token
        """
        if not auth:
            return False
        if not auth.startswith(self.cfg.token_prefix):
            return False
        _token = auth[len(self.cfg.token_prefix):].strip()
        try:
            payload = self._decode(_token)
            if not payload:
                return False
            else:
                self.token = _token
                return True
        except:
            pass
        return False

    def _make_token(self, user):
        if not user:
            return None
        # Return a ready-made token
        return self._encode(self._make_payload(user))

    def _make_payload(self, user, payload={}):
        # for key, value in user.items():
        #     if value:
        #         payload[key] = value
        payload.update({'user': user['data']['id']})
        # Add an expiry date in there
        expiry = timedelta(hours=self.cfg.token_expiry)
        payload['exp'] = datetime.utcnow() + expiry
        return payload

    def _encode(self, payload):
        return jwt.encode(payload, self.cfg.secret)

    def _decode(self, token, verify_expiration=True):
        try:
            # Try to decode the token - this blows up spectacularly if it fails
            leeway = timedelta(seconds=self.cfg.tokens_leeway)
            return jwt.decode(token, self.cfg.secret, leeway=leeway.total_seconds())
        except jwt.DecodeError:
            # The token was tampered with, corrupted or otherwise invalid
            return None
        except jwt.ExpiredSignature:
            # The token has already expired, and the leeway couldn't save it :(
            return None

    def process_request(self, req, resp):
        """Process the request before routing it.

        Args:
            req: Request object that will eventually be
                routed to an on_* responder method.
            resp: Response object that will be routed to
                the on_* responder.
        """
        account_id = req.get_header('Account-ID')

        _check = dict()

        if self._verify_token(req.auth):
            _check['valid'] = True
        else:
            _check['valid'] = False

        req.context.update(_check)

        challenges = ['Bearer realm="aness', 'error="invalid_token"', 'error_description="The access token expired"']

        # if token is None:
        #     description = ('Please provide an auth token as part of the request.')
        #     raise falcon.HTTPUnauthorized('Auth token required', description, challenges,
        #                                   href='http://docs.example.com/auth')
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
        # TODO: Поменять этот бред
        user = resp.context.get('user', None)
        if user:
            token = self._make_token(user).decode()
            resp.context.update({'token': token})
