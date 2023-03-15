from django.urls  import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('show/',show,name='show'),
    path('show/delete/<id>',delete,name='show'),
    path('show/update/<id>',update,name='show'),
]
