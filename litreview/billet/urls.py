app_name = 'billet'

from django.urls import path
from .views import create_ticket, create_critic, create_billet, list_tickets, list_critics, list_billets, delete_ticket

urlpatterns = [
    path('ticket/new/', create_ticket, name='create_ticket'),
    path('critic/new/<int:ticket_id>/', create_critic, name='create_critic'),
    path('billet/new/', create_billet, name='create_billet'),
    path('tickets/', list_tickets, name='list_tickets'),
    path('critics/', list_critics, name='list_critics'),
    path('billets/', list_billets, name='list_billets'),
    path('ticket/delete/<int:ticket_id>/', delete_ticket, name='delete_ticket'),

]
