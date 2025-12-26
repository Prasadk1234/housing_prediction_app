from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('',views.predict_view,name='predict'),
    # path('feedback/', views.feedback_view, name='feedback'),
    # path('create/', views.tweet_create, name='tweet_create'),
    # path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    # path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    # path('register/',views.register,name='register'),
    # path('search/', views.search, name='search'),
]
