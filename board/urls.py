from django.conf.urls import url

from . import views

urlpatterns = [


url(r'^$', views.index, name='index'),
url(r'^register/$', views.UserFormView.as_view(), name='register'),
url(r'^[0-9]+$', views.delete_post, name='delete post'),
url(r'^comment/[0-9]+$', views.delete_comment, name='delete comment'),
url(r'^newpost$', views.newpost, name='new post'),
url(r'^newcomment$', views.newcomment, name='new comment')
]