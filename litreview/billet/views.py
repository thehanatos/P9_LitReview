from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, Critic
from .forms import TicketForm, CriticForm, BilletForm

def create_ticket(request):
    if request.method == "POST":
        print(request.POST)
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('billet:list_tickets')
        else:
            print(form.errors)
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})

def create_critic(request, ticket_id=None):
    ticket = get_object_or_404(Ticket, id=ticket_id) if ticket_id else None
    if request.method == "POST":
        form = CriticForm(request.POST)
        if form.is_valid():
            critic = form.save(commit=False)
            critic.user = request.user
            critic.ticket = ticket
            critic.save()
            return redirect('list_critics')
    else:
        form = CriticForm()
    return render(request, 'billet/create_critic.html', {'form': form, 'ticket': ticket})

def create_billet(request):
    if request.method == "POST":
        form = BilletForm(request.POST)
        if form.is_valid():
            billet = form.save(user=request.user)
            return redirect('list_billets')
    else:
        form = BilletForm()
    return render(request, 'billet/create_billet.html', {'form': form})


def list_tickets(request):
    tickets = Ticket.objects.all().order_by('-date_creation')  # Affiche les tickets du plus récent au plus ancien
    print(tickets)
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

def list_critics(request):
    critics = Critic.objects.all().order_by('-date_creation')
    return render(request, 'billet/list_critics.html', {'critics': critics})

def list_billets(request):
    billets = Billet.objects.all()
    return render(request, 'billet/list_billets.html', {'billets': billets})

def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.user == ticket.user:
        ticket.delete()

    return redirect('billet:list_tickets')