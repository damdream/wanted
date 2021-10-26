import json

from django.http      import JsonResponse, request
from django.views     import View

from users.models     import User
from posts.models     import Post
from users.utils      import login_decorator

class PostingView(View):
    @login_decorator    
    def post(self,request):
        try:
            data = json.loads(request.body)

            if data["title"] == "" :
                return JsonResponse({"MESSAGE":"NULL_REVIEWS"}, status = 400)

            Post.objects.create( 
                user            = request.user,
                name            = data["name"],
                title           = data["title"],
                comment         = data["comment"],
            )

            return JsonResponse({"MESSAGE":"SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)    

    def get(self,request, post_id):
        posts = Post.objects.all()

        result = [
            {
                "user"            : post.user.id,
                "name"            : post.name ,
                "created_at"      : post.created_at,
                "title"           : post.title,
                "comment"         : post.comment,

            } for post in posts]

        return JsonResponse ({"result": result}, status = 200)

    @login_decorator
    def delete (self,request,post_id):

        if not Post.objects.filter(id=post_id, user = request.user).exists():
            return JsonResponse({"MESSAGE": "NO_REVIEWS"}, status = 400)

        Post.objects.filter(id=post_id).delete()

        return JsonResponse ({"MESSAGE" : "DELETE"}, status = 204)    

    @login_decorator
    def patch (self,request, post_id):
        try:
            data = json.loads(request.body)

            if not Post.objects.filter(id=post_id, user = request.user).exists():
              return JsonResponse({"MESSAGE": "NO_REVIEWS"}, status = 400)
    
            Post.objects.filter(id=post_id).update(title= data["title"], comment= data["comment"])
            return JsonResponse ({"MESSAGE" : "UPDATE"}, status = 200)

        except KeyError: 
            return JsonResponse ({"MESSAGE":"KEY_ERROR"},status = 400)