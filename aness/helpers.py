from functools import wraps
from falcon import HTTPForbidden

def token_required(func):
    @wraps(func)
    def f(*args, **kwargs):
        resource, req, resp = args
        # if not False:
        #     raise HTTPForbidden
        if not req.context['valid']:
            raise HTTPForbidden
        return func(*args, **kwargs)

    return f
