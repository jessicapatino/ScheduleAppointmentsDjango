from django.conf.urls import include
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from Appointments import settings
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_patients, name='list_patients'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('api-auth/', include('rest_framework.urls')),
    path('home_view/', views.home_view, name= 'photo'),
]
