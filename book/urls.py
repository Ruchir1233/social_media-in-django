from django.urls import path
from . import views
urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('',views.index,name='index'),
    path('signin',views.signin,name='signin'),
    path('search',views.search,name='search'),
    path('like-post',views.like_post,name='like_post'),
    path('logout',views.logout,name='logout'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('settings',views.settings,name='settings'),
    path('upload',views.upload,name="upload"),
    path('follow',views.follow,name="follow")
]