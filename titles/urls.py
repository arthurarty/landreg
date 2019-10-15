from django.urls import path
from titles import views

app_name = 'title'
urlpatterns = [
    path('create/', views.CreateTitleView.as_view(), name='create'),
]
