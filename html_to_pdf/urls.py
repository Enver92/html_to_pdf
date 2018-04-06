from django.urls import path, include
from django.views.generic import TemplateView
from .views import generate_pdf

urlpatterns = [
    path('', TemplateView.as_view(template_name='html_to_pdf/home.html'), name='home'),
    path('generate/', generate_pdf, name='generate-pdf')
]
