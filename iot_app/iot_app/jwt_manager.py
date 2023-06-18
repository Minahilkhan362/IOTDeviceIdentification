import jwt
import calendar
import time


class JWTManager:
    def __init__(self):
        self._key = 'super secret key'
        self._algorithm = 'HS256'

    def create_token(self, user_id):
        return jwt.encode({'id': user_id, 'timestamp': calendar.timegm(time.gmtime())}, self._key, algorithm=self._algorithm)

    def verify_token(self, token):
        try:
            payload = jwt.decode(
                token, self._key, algorithms=[self._algorithm])
            return payload['id']
        except Exception:
            pass
