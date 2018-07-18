import jwt
import datetime

"""
4.1.1.  "iss" (Issuer) Claim
4.1.2.  "sub" (Subject) Claim
4.1.3.  "aud" (Audience) Claim
4.1.4.  "exp" (Expiration Time) Claim
4.1.5.  "nbf" (Not Before) Claim
4.1.6.  "iat" (Issued At) Claim
4.1.7.  "jti" (JWT ID) Claim
"""


def generate_user_token(user):
    configuration = {'secret': "0000"}
    payload = {
        'user': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=600)
    }
    encoded = jwt.encode(payload=payload, key=configuration.secret)
    return encoded


def validate_user_token(token):
    return True
