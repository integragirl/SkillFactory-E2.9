from django.urls import path
from sendmail.views import MailPostRead, MailPostCreate

app_name = 'sendmail'
urlpatterns = [
    path('',                    MailPostRead.as_view(),             name='list'),
    path('create/',             MailPostCreate.as_view(),           name='create'),
]