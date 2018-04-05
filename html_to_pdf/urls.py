from django.urls import path, include
from django.views.generic import TemplateView
from .views import html_to_pdf

urlpatterns = [
    path('', TemplateView.as_view(template_name='html_to_pdf/home.html')),
    path('generate/', html_to_pdf, name='generate-pdf')
]
