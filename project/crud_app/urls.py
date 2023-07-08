from django.urls import path
from .views import Email_view

urlpatterns = [
    path('email/', Email_view, name='email_url')
]