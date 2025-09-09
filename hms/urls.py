
from django.urls import path,include
from . import views as view

urlpatterns = [
    path('', view.testView.as_view(), name='test'),
    
]