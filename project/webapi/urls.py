from django.urls import path
from . import views

app_name = 'webapi'

urlpatterns = [
    path('api/profile/', views.ProfileListCreate.as_view(), name='list-create'),
]