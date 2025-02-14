app_name = 'billet'

from django.urls import path
from .views import create_ticket, create_critic, create_billet, list_tickets, list_critics, flux
from .views import list_billets, delete_ticket, edit_critic, delete_critic, edit_ticket, my_tickets_and_critics

urlpatterns = [
    path('ticket/new/', create_ticket, name='create_ticket'),
    path('critic/new/<int:ticket_id>/', create_critic, name='create_critic'),
    path('billet/new/', create_billet, name='create_billet'),
    path('tickets/', list_tickets, name='list_tickets'),
    path('critics/', list_critics, name='list_critics'),
    path('billets/', list_billets, name='list_billets'),
    path('ticket/delete/<int:ticket_id>/', delete_ticket, name='delete_ticket'),
    path("ticket/<int:ticket_id>/critic/", create_critic, name="create_critic"),
    path('critic/<int:critic_id>/edit/', edit_critic, name='edit_critic'),
    path('critic/<int:critic_id>/delete/', delete_critic, name='delete_critic'),
    path('ticket/<int:ticket_id>/edit/', edit_ticket, name='edit_ticket'), 
    path('mes-publications/', my_tickets_and_critics, name='my_tickets_and_critics'),
    path('flux/', flux, name='flux'),

]
