from django.urls import path
from .views import StudentRecordAdd, AdminRecordAdd
urlpatterns = [
    path('', StudentRecordAdd, name='index'),
    path('admins/', AdminRecordAdd, name='admins'),
]