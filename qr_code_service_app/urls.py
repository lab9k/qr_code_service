from django.urls import path
from qr_code_service_app.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
]
