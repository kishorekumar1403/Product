from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from .models import *
import jwt

# for Over all router authentication
class userTokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        try:
            print("user inside the authenticate")
            token = get_authorization_header(request).decode("utf-8").split()
            print(token)
            if len(token) == 2:
                de_value = jwt.decode(token[1], "login_key", algorithms=["HS256"])
                print(de_value)
                user_ = user.objects.filter(id=de_value["id"], gmail=de_value["gmail"])
                print("token ", de_value)
                if user_.exists():
                    return user_, de_value["gmail"]
                else:
                    raise AuthenticationFailed("Token authentication Failed")
            raise AuthenticationFailed("Token authentication Failed")
        # except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError): 
            # raise AuthenticationFailed("Token authentication Failed")
        except Exception:
            raise AuthenticationFailed("Token authentication Failed")