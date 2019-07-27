from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('board.urls')),
    url(r'^board/', include('board.urls')),
    url(r'^login/', views.login, {'template_name': 'board/login_form.html'}, name='login'),
    url(r'^logout/', views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^oauth/', include('social.apps.django_app.urls', namespace='social')),

]
