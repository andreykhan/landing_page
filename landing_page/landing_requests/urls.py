from django.urls import path

from .views import index, about, form_sent, create_request

app_name = 'landing_requests'

urlpatterns = [
    path('', index, name='main_page'),
    # path('offer/', CreateRequest.as_view(), name='offer_page'),
    path('offer/', create_request, name='offer_page'),
    path('about/', about, name='about_page'),
    path('form_sent/', form_sent, name='form_sent_page')
]
