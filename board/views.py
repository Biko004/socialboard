from django.shortcuts import render, redirect
from .models import Post, Comment
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm



@login_required
def index(request):
    posts = Post.objects.all()
    five = posts.order_by('-post_pub_date')[:5]
    return render(request, 'board/index.html', {'posts':five})


@csrf_exempt
def delete_post(request):
    post_id = request.POST.get("post_id")
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponse("success")


@csrf_exempt
def newpost(request):
    text = request.POST.get("text")
    title = request.POST.get("title")
    author = request.POST.get("author")
    post = Post.objects.create(post_title=title,post_pub_date=timezone.now(), post_author=author, post_desc=text)
    return render(request, 'board/post.html', {'post':post})

@csrf_exempt
def newcomment(request):
    post_id = int(request.POST.get("post"))
    commenttext = request.POST.get("text")
    commentauthor = request.POST.get("author")
    comment = Comment.objects.create(comment_text=commenttext, comment_author=commentauthor, post_id=post_id)
    return render(request, 'board/comment.html', {'comment':comment})

class UserFormView(View):
    form_class = UserForm
    template_name = 'board/registeration_form.html'

    #display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #clean (normlized) DATA
            username = form.cleaned_data['username']
            password2 = form.cleaned_data['password2']
            user.set_password(password2)
            user.save()

            #returns User objects if credentials are correct

            user = authenticate(username=username, password=password2)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    posts = Post.objects.all()
                    five = posts.order_by('-post_pub_date')[:5]
                    return render(request, 'board/index.html', {'posts':five})

        return render(request, self.template_name, {'form': form})

