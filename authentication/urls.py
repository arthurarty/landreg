from django.urls import path
from authentication import views


urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
]
