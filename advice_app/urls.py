from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.home_view,name='home-view'),
    path('register/',views.register,name='register'),
    path('post/',views.post_question,name='post-question'),
    path('login/',LoginView.as_view(template_name='advice/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='advice/logout.html'),name='logout'),

]