import jwt

from django.http.response      import JsonResponse
from users.models              import User
from preonboarding.settings    import SECRET_KEY



def login_decorator(func): 
    def wrapper(self, request, *args, **kwargs) :
        try:
            token         = request.headers.get("Authorization", None)
            payload       = jwt.decode(token,SECRET_KEY, algorithms='HS256')
            request.user  = User.objects.get(id = payload["id"]) 
            return func(self, request, *args, **kwargs)   

        except jwt.exceptions.DecodeError:
            return JsonResponse({"MESSAGE" :"INVALID_TOKEN"}, status = 401)

        except User.DoesNotExist: 
            return JsonResponse({"MESSAGE": "INVALID_USER"}, status = 401) 

    return wrapper


def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token   = request.headers.get("Authorization")
            payload = jwt.decode(token, SECRET_KEY, algorithms = "HS256")

            if not User.objects.filter(id = payload.get("id")).exists() :
                return JsonResponse({"message" : "INVALID_MEMBER"}, status = 404)

            user         = User.objects.get(id = payload["id"])
            request.user = user

            return func(self, request, *args, **kwargs)
        
        except jwt.exceptions.DecodeError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 403)

    return wrapper
