from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('', views.subscriptions_view, name='subscriptions_view'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
]
